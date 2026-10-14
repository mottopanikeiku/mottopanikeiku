"""Shape text with HarfBuzz and emit it as SVG glyph outlines.

README images load as <img>, so they cannot fetch web fonts. Outlining the
text keeps the typography identical everywhere; each glyph is defined once
in <defs> and placed with <use>.
"""
from __future__ import annotations

from dataclasses import dataclass, field

import uharfbuzz as hb
from fontTools.pens.svgPathPen import SVGPathPen
from fontTools.ttLib import TTFont


class _RoundPen(SVGPathPen):
    def __init__(self, glyphset=None):
        super().__init__(glyphset, ntos=lambda v: str(round(v)))


@dataclass
class Face:
    key: str
    path: str
    wght: float
    opsz: float
    _hb: hb.Font = field(init=False, repr=False)
    _upm: int = field(init=False)
    _gs: object = field(init=False, repr=False)

    def __post_init__(self) -> None:
        blob = hb.Blob.from_file_path(self.path)
        face = hb.Face(blob)
        self._hb = hb.Font(face)
        self._hb.set_variations({"wght": self.wght, "opsz": self.opsz})
        self._upm = face.upem
        tt = TTFont(self.path)
        self._gs = tt.getGlyphSet(location={"wght": self.wght, "opsz": self.opsz})
        self._names = tt.getGlyphOrder()

    @property
    def upm(self) -> int:
        return self._upm

    def shape(self, text: str, features: dict | None = None):
        buf = hb.Buffer()
        buf.add_str(text)
        buf.guess_segment_properties()
        hb.shape(self._hb, buf, features or {"kern": True, "liga": True})
        return [(i.codepoint, p.x_advance, p.x_offset, p.y_offset) for i, p in zip(buf.glyph_infos, buf.glyph_positions)]

    def outline(self, gid: int) -> str:
        pen = _RoundPen(self._gs)
        self._gs[self._names[gid]].draw(pen)
        return pen.getCommands()


class Canvas:
    """Collects glyph definitions and drawing fragments for one SVG."""

    def __init__(self, width: int, height: int, title: str):
        self.w, self.h, self.title = width, height, title
        self.defs: dict[str, str] = {}
        self.body: list[str] = []

    def width_of(self, face: Face, text: str, size: float, tracking: float = 0.0) -> float:
        k = size / face.upm
        adv = sum(a for _, a, _, _ in face.shape(text))
        return adv * k + tracking * size * max(len(text) - 1, 0)

    def text(self, face: Face, text: str, x: float, y: float, size: float, fill: str,
             anchor: str = "start", tracking: float = 0.0, opacity: float | None = None) -> float:
        """Draw `text` with its baseline at y. Returns the advance width in px."""
        k = size / face.upm
        glyphs = face.shape(text)
        width = self.width_of(face, text, size, tracking)
        if anchor == "end":
            x -= width
        elif anchor == "middle":
            x -= width / 2
        uses, pen_x = [], 0.0
        track_units = tracking * size / k
        for gid, adv, xo, yo in glyphs:
            gkey = f"{face.key}{gid}"
            if gkey not in self.defs:
                d = face.outline(gid)
                self.defs[gkey] = f'<path id="{gkey}" d="{d}"/>' if d else ""
            if self.defs[gkey]:
                yattr = f' y="{round(yo)}"' if yo else ""
                uses.append(f'<use href="#{gkey}" x="{round(pen_x + xo)}"{yattr}/>')
            pen_x += adv + track_units
        op = f' opacity="{opacity}"' if opacity is not None else ""
        self.body.append(
            f'<g fill="{fill}"{op} transform="translate({x:.1f} {y:.1f}) scale({k:.5f} {-k:.5f})">{"".join(uses)}</g>'
        )
        return width

    def wrap(self, face: Face, text: str, size: float, max_width: float) -> list[str]:
        words, lines, cur = text.split(), [], ""
        for w in words:
            trial = f"{cur} {w}".strip()
            if cur and self.width_of(face, trial, size) > max_width:
                lines.append(cur)
                cur = w
            else:
                cur = trial
        if cur:
            lines.append(cur)
        return lines

    def raw(self, fragment: str) -> None:
        self.body.append(fragment)

    def svg(self) -> str:
        defs = "".join(v for v in self.defs.values() if v)
        return (
            f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {self.w} {self.h}" '
            f'width="{self.w}" height="{self.h}" role="img" aria-label="{_esc(self.title)}">'
            f"<title>{_esc(self.title)}</title><defs>{defs}</defs>{''.join(self.body)}</svg>\n"
        )


def _esc(s: str) -> str:
    return s.replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;").replace('"', "&quot;")
