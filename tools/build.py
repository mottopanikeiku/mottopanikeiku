# /// script
# requires-python = ">=3.11"
# dependencies = ["uharfbuzz>=0.39", "fonttools>=4.50", "pillow>=10"]
# ///
"""Draw the profile header and project cards into assets/.

Run with `uv run tools/build.py`. Numbers come from the personal site's data
extracts at a pinned commit; each extract records the project commit it was
read from. The font is Source Serif 4 (SIL OFL) at a pinned Google Fonts commit.
"""
from __future__ import annotations

import base64
import json
import math
import tempfile
import urllib.request
from pathlib import Path

from svgtext import Canvas, Face

ROOT = Path(__file__).resolve().parent.parent
ASSETS = ROOT / "assets"
SITE_DATA = "https://raw.githubusercontent.com/mottopanikeiku/mottopanikeiku.github.io/{commit}/data/{name}.json"
SITE_COMMIT = "3f242b0a0c0009a711afdadc91b9679338cc296e"
FONT_URL = ("https://github.com/google/fonts/raw/08dc85da6bca7ae308a6f1d38d0b137465646071/"
            "ofl/sourceserif4/SourceSerif4%5Bopsz,wght%5D.ttf")

THEMES = {
    "light": dict(paper="#f6f4ef", ink="#1c1b18", muted="#69655d", accent="#9a3b22", rule="#dcd8ce", signal="#c8331e"),
    "dark": dict(paper="#151412", ink="#e8e5de", muted="#9d988e", accent="#e08f72", rule="#2f2d29", signal="#e2553d"),
}


def fetch(url: str) -> bytes:
    with urllib.request.urlopen(url, timeout=60) as response:
        return response.read()


def site_data(name: str) -> dict:
    return json.loads(fetch(SITE_DATA.format(commit=SITE_COMMIT, name=name)))


font_path = Path(tempfile.gettempdir()) / "SourceSerif4-08dc85d.ttf"
if not font_path.exists():
    font_path.write_bytes(fetch(FONT_URL))
display = Face("d", str(font_path), wght=400, opsz=60)
text = Face("t", str(font_path), wght=400, opsz=20)
label_face = Face("l", str(font_path), wght=600, opsz=12)
small = Face("s", str(font_path), wght=400, opsz=12)


def tml_mark(c: Canvas, x: float, y: float, size: float, ink: str, signal: str) -> None:
    """The Tenth Man Labs mark: nine dots and the tenth."""
    s = size / 78
    body = "".join(f'<circle cx="{cx}" cy="{cy}" r="7.5"/>' for cx in (7.5, 28.5, 49.5) for cy in (28.5, 49.5, 70.5))
    c.raw(f'<g transform="translate({x} {y}) scale({s:.4f})" fill="{ink}">{body}'
          f'<circle cx="70.5" cy="7.5" r="7.5" fill="{signal}"/></g>')


def dot_field(c: Canvas, p: dict, x0: float, y0: float, cols: int, rows: int, pitch: float, r: float,
              odd: tuple[int, int]) -> None:
    """A field of dots that fades in from the left; one dot disagrees."""
    dots = []
    for j in range(rows):
        for i in range(cols):
            if (i, j) == odd:
                continue
            wave = 0.5 + 0.5 * math.sin(i * 0.55 + j * 0.9)
            opacity = 0.10 + 0.55 * (i / (cols - 1)) * (0.6 + 0.4 * wave)
            dots.append(f'<circle cx="{x0 + i * pitch:.1f}" cy="{y0 + j * pitch:.1f}" r="{r}" opacity="{opacity:.2f}"/>')
    c.raw(f'<g fill="{p["ink"]}">{"".join(dots)}</g>')
    c.raw(f'<circle cx="{x0 + odd[0] * pitch:.1f}" cy="{y0 + odd[1] * pitch:.1f}" r="{r}" fill="{p["signal"]}"/>')


def header(p: dict) -> str:
    w, h = 1000, 260
    c = Canvas(w, h, "Alp Cetin. GPU systems, evaluation and reinforcement learning. Building Tenth Man Labs.")
    c.raw(f'<rect x="0.5" y="0.5" width="{w - 1}" height="{h - 1}" rx="14" fill="{p["paper"]}" stroke="{p["rule"]}"/>')
    c.text(display, "Alp Cetin", 56, 122, 74, p["ink"])
    c.text(text, "GPU systems, evaluation and reinforcement learning.", 56, 166, 23, p["muted"])
    tml_mark(c, 56, 192, 19, p["ink"], p["signal"])
    c.text(text, "Building Tenth Man Labs", 87, 209, 19, p["ink"])
    dot_field(c, p, 640, 58, 12, 6, 26, 5.2, odd=(10, 1))
    return c.svg()


# Cards: 460 × 304, a label, a title, two lines of text and a 404 × 130 figure.
W, H, PAD = 460, 304, 28
FIG_Y, FIG_H = 150, 130
FIG_W = W - 2 * PAD


def caption(c: Canvas, p: dict, s: str, x: float, y: float, anchor: str = "start", fill: str | None = None) -> float:
    return c.text(small, s, x, y, 11, fill or p["muted"], anchor=anchor)


def attention(c: Canvas, p: dict) -> None:
    qwen7 = next(r for r in site_data("attention-accuracy")["rows"] if r["key"] == "qwen7")
    base = qwen7["bf16_accuracy"]["hellaswag"]
    acc = lambda variant: base + qwen7["variants"][variant]["tasks"]["hellaswag"]["delta"]
    spec = [("BF16", base, p["ink"], p["ink"]), ("FP8", acc("tile"), p["muted"], p["muted"]),
            ("FP8, Q/K rotated", acc("rotate"), p["signal"], p["ink"]),
            ("FP8, rotated, keys centered", acc("rotate_smooth_k"), p["ink"], p["ink"])]
    caption(c, p, "Qwen2.5-7B HellaSwag accuracy · FlashAttention-3 FP8 on one H100", PAD, FIG_Y + 10)
    bx0, bx1 = PAD + 158, PAD + FIG_W - 42
    sx = lambda v: bx0 + (bx1 - bx0) * v
    c.raw(f'<line x1="{sx(base):.1f}" y1="{FIG_Y + 22}" x2="{sx(base):.1f}" y2="{FIG_Y + 122}" stroke="{p["muted"]}" '
          f'stroke-dasharray="2 3" opacity="0.7"/>')
    for i, (name, value, bar, label) in enumerate(spec):
        y = FIG_Y + 34 + i * 24
        caption(c, p, name, bx0 - 10, y + 4, anchor="end", fill=label)
        c.raw(f'<rect x="{bx0}" y="{y - 6}" width="{sx(value) - bx0:.1f}" height="12" rx="2" fill="{bar}"/>')
        caption(c, p, f"{value * 100:.1f}%", sx(value) + 6, y + 4, fill=p["ink"])


def eval_power(c: Canvas, p: dict) -> None:
    detection = site_data("eval-prospective")["detection"]
    hit, n = detection["detected"], detection["tested"]
    width = c.text(display, f"{hit} of {n}", PAD, FIG_Y + 34, 34, p["ink"])
    caption(c, p, "planned comparisons found", PAD + width + 12, FIG_Y + 20)
    caption(c, p, "the difference they were sized for", PAD + width + 12, FIG_Y + 34)
    pitch, dots = FIG_W / n, []
    for i in range(n):
        cx = PAD + pitch * (i + 0.5)
        dots.append(f'<circle cx="{cx:.1f}" cy="{FIG_Y + 70}" r="5.4" fill="{p["accent"]}"/>' if i < hit else
                    f'<circle cx="{cx:.1f}" cy="{FIG_Y + 70}" r="4.6" fill="none" stroke="{p["muted"]}" stroke-width="1.4"/>')
    c.raw("".join(dots))
    caption(c, p, "Six open models on GSM8K and ARC. Sample sizes were fixed", PAD, FIG_Y + 104)
    caption(c, p, "from a pilot before any fresh answers were collected.", PAD, FIG_Y + 119)


def cpu_decode(c: Canvas, p: dict) -> None:
    pts = sorted((q for q in site_data("cpu-decode")["points"] if q["context"] == 128), key=lambda q: q["threads"])
    px0, px1 = PAD + 26, PAD + FIG_W - 52
    py0, py1 = FIG_Y + 38, FIG_Y + FIG_H - 20
    xs = [px0 + (px1 - px0) * i / (len(pts) - 1) for i in range(len(pts))]
    sy = lambda v: py1 - (py1 - py0) * v / 90
    best = max(pts, key=lambda q: q["engine"])
    caption(c, p, f"tokens/s, 128-token context, laptop CPU · peak {best['percent_of_ceiling']:.0f}% of the read ceiling",
            PAD, FIG_Y + 6)
    lx, ly = PAD, FIG_Y + 24
    for color, dash, dot, name in ((p["signal"], "", True, "this decoder"), (p["muted"], "", False, "llama.cpp Q8_0"),
                                   (p["muted"], "3 3", False, "estimated read ceiling")):
        da = f' stroke-dasharray="{dash}"' if dash else ""
        c.raw(f'<line x1="{lx}" y1="{ly - 4}" x2="{lx + 18}" y2="{ly - 4}" stroke="{color}" stroke-width="2"{da}/>')
        if dot:
            c.raw(f'<circle cx="{lx + 9}" cy="{ly - 4}" r="2.6" fill="{color}"/>')
        lx += 24 + caption(c, p, name, lx + 24, ly, fill=p["ink"] if dot else None) + 18
    for v in (0, 40, 80):
        c.raw(f'<line x1="{px0}" y1="{sy(v):.1f}" x2="{px1}" y2="{sy(v):.1f}" stroke="{p["rule"]}"/>')
        caption(c, p, str(v), px0 - 8, sy(v) + 4, anchor="end")
    for x, q in zip(xs, pts):
        caption(c, p, str(q["threads"]), x, py1 + 15, anchor="middle")
    caption(c, p, "threads", px1 + 12, py1 + 15)
    for key, color, width, dash in (("ceiling", p["muted"], 1.2, "3 3"), ("llama", p["muted"], 1.6, ""),
                                    ("engine", p["signal"], 2.2, "")):
        d = " ".join(f"{'M' if i == 0 else 'L'}{x:.1f} {sy(q[key]):.1f}" for i, (x, q) in enumerate(zip(xs, pts)))
        da = f' stroke-dasharray="{dash}"' if dash else ""
        c.raw(f'<path d="{d}" fill="none" stroke="{color}" stroke-width="{width}" stroke-linejoin="round"{da}/>')
    c.raw("".join(f'<circle cx="{x:.1f}" cy="{sy(q["engine"]):.1f}" r="3" fill="{p["signal"]}"/>' for x, q in zip(xs, pts)))


def quantile_cycles(c: Canvas, p: dict) -> None:
    caption(c, p, "greedy action under exact quantile-projected Bellman iteration", PAD, FIG_Y + 10)
    top, bot, lx = FIG_Y + 40, FIG_Y + 88, PAD + 70
    caption(c, p, "optimal", lx - 10, top + 4, anchor="end", fill=p["ink"])
    caption(c, p, "worse", lx - 10, bot + 4, anchor="end", fill=p["ink"])
    steps = 14
    step_w = (FIG_W - 96) / steps
    for v in (top, bot):
        c.raw(f'<line x1="{lx}" y1="{v}" x2="{PAD + FIG_W}" y2="{v}" stroke="{p["rule"]}"/>')
    d, dots = [], []
    for i in range(steps):
        y = top if i % 2 == 0 else bot
        d.append(f"{'M' if i == 0 else 'L'}{lx + i * step_w:.1f} {y} L{lx + (i + 1) * step_w:.1f} {y}")
        dots.append(f'<circle cx="{lx + (i + 0.5) * step_w:.1f}" cy="{y}" r="3" '
                    f'fill="{p["signal"] if y == bot else p["accent"]}"/>')
    c.raw(f'<path d="{" ".join(d)}" fill="none" stroke="{p["accent"]}" stroke-width="2" stroke-linejoin="round"/>')
    c.raw("".join(dots))
    end = lx + steps * step_w
    c.raw("".join(f'<circle cx="{end + 7 + k * 7:.1f}" cy="{(top + bot) / 2}" r="1.6" fill="{p["muted"]}"/>' for k in range(3)))
    caption(c, p, "No fixed point. The smallest rational cycle is checked in Lean.", PAD, FIG_Y + 122)


def alignmenttax(c: Canvas, p: dict) -> None:
    rows = site_data("alignmenttax")["rows"]
    style = {"truth_gain_ece_worse": ("fill", p["signal"]), "truth_and_calibration_improve": ("fill", p["ink"]),
             "truth_and_calibration_worsen": ("fill", p["muted"]), "uncertain": ("ring", p["muted"])}

    def mark(cx: float, cy: float, kind: str, color: str, r: float) -> None:
        c.raw(f'<circle cx="{cx}" cy="{cy}" r="{r}" fill="{color}"/>' if kind == "fill" else
              f'<circle cx="{cx}" cy="{cy}" r="{r - 0.8}" fill="none" stroke="{color}" stroke-width="1.3"/>')

    caption(c, p, f"{len(rows)} base → instruct pairs, 0.5B to 32B, one dot each", PAD, FIG_Y + 10)
    for j, (key, name) in enumerate((("binary", "binary TruthfulQA"), ("standard", "standard MC1"))):
        y = FIG_Y + 36 + j * 28
        caption(c, p, name, PAD + 110, y + 4, anchor="end", fill=p["ink"])
        for i, row in enumerate(rows):
            mark(PAD + 126 + i * 25, y, *style[row[key]["classification"]], 6.5)
    legend = [("truth_gain_ece_worse", "more accurate, worse calibrated"), ("truth_and_calibration_improve", "both better"),
              ("truth_and_calibration_worsen", "both worse"), ("uncertain", "unclear")]
    lx, ly = PAD, FIG_Y + 104
    for idx, (key, s) in enumerate(legend):
        if idx == 2:
            lx, ly = PAD, ly + 16
        mark(lx + 4, ly - 4, *style[key], 4)
        lx += 29 + caption(c, p, s, lx + 13, ly)


def bitbound(c: Canvas, p: dict) -> None:
    image = base64.b64encode((ASSETS / "src" / "bitbound-title.webp").read_bytes()).decode()
    c.raw(f'<clipPath id="shot"><rect x="{PAD}" y="{FIG_Y}" width="{FIG_W}" height="{FIG_H}" rx="6"/></clipPath>')
    c.raw(f'<image x="{PAD}" y="{FIG_Y}" width="{FIG_W}" height="{FIG_H}" clip-path="url(#shot)" '
          f'preserveAspectRatio="xMidYMid slice" href="data:image/webp;base64,{image}"/>')
    c.raw(f'<rect x="{PAD + 0.5}" y="{FIG_Y + 0.5}" width="{FIG_W - 1}" height="{FIG_H - 1}" rx="6" fill="none" '
          f'stroke="{p["rule"]}"/>')


CARDS = [
    ("attention-numerics", "FP8 attention", "attention-numerics",
     "Rotating queries and keys before FP8 rounding doubled Qwen2.5-7B’s accuracy loss. Centering the keys removed it.",
     attention),
    ("eval-power", "Evaluation", "eval-power",
     "How many benchmark items it takes to tell two LLMs apart, and how often a small pilot gets that number wrong.",
     eval_power),
    ("cpu-decode", "CPU inference", "cpu-decode",
     "A from-scratch C++ int8 decoder for Qwen2.5-0.5B, measured against memory bandwidth and llama.cpp.",
     cpu_decode),
    ("quantile-cycles", "RL theory", "quantile-cycles",
     "Greedy control with quantile-projected Bellman updates can alternate forever between the best action and a worse one.",
     quantile_cycles),
    ("alignmenttax", "Calibration", "alignmenttax",
     "Does instruction tuning trade calibration for truthfulness? Across nine base/instruct pairs, it depends on the scoring.",
     alignmenttax),
    ("bitbound", "Browser game", "Bitbound",
     "A pixel-art RPG where quantization grids power the spells and puzzles. It plays in the browser.",
     bitbound),
]


def card(p: dict, label: str, title: str, body: str, figure) -> str:
    c = Canvas(W, H, f"{title}: {body}")
    c.raw(f'<rect x="0.5" y="0.5" width="{W - 1}" height="{H - 1}" rx="12" fill="{p["paper"]}" stroke="{p["rule"]}"/>')
    c.text(label_face, label.upper(), PAD, 40, 10.5, p["muted"], tracking=0.14)
    c.text(display, title, PAD, 76, 28, p["ink"])
    lines = c.wrap(text, body, 15, FIG_W)
    if len(lines) > 2:
        raise ValueError(f"{title}: card text needs {len(lines)} lines; shorten it to two")
    for i, line in enumerate(lines):
        c.text(text, line, PAD, 104 + i * 21, 15, p["muted"])
    figure(c, p)
    return c.svg()


def main() -> None:
    ASSETS.mkdir(exist_ok=True)
    for theme, p in THEMES.items():
        (ASSETS / f"header-{theme}.svg").write_text(header(p))
        for slug, label, title, body, figure in CARDS:
            (ASSETS / f"{slug}-{theme}.svg").write_text(card(p, label, title, body, figure))
    for path in sorted(ASSETS.glob("*.svg")):
        print(f"{path.name:32s} {path.stat().st_size / 1024:5.1f} KB")


if __name__ == "__main__":
    main()
