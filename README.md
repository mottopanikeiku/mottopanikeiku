i work on evals, rl and inference. these are the questions i've been testing in my side projects.

each result links to committed evidence. more experiments and write-ups at [alpcetin.com](https://alpcetin.com/).

### evals

- [tithe](https://github.com/mottopanikeiku/tithe) — does instruction tuning trade calibration for truthfulness? [6/9 binary pairs show a resolved tradeoff; none on standard mc1](https://github.com/mottopanikeiku/tithe/blob/d6d02e4ab2b6ebce5962772344d5f6adcf77c233/results/day_scale/analysis/summary.json#L1678-L1735) (different protocols, not a causal comparison). [write-up](https://mottopanikeiku.github.io/projects/alignmenttax/)
- [rayleigh](https://github.com/mottopanikeiku/rayleigh) — how many questions separate two models? [23/27 pilot-planned comparisons detect differences on fresh items](https://github.com/mottopanikeiku/rayleigh/blob/b10608765eb1ffa08c3f10020ccb1fd0f6cd9ce4/results/prospective/summary.json#L1828-L1845) (nominal tests, not measured power). [calculator](https://mottopanikeiku.github.io/rayleigh/)
- [mendel](https://github.com/mottopanikeiku/mendel) — how many training seeds are enough? [plans targeting 80% modeled power yield 139/307 fresh-seed ppo detections](https://github.com/mottopanikeiku/mendel/blob/a2ea67e91122590ade88fb2830ad34861ba4ec91/results/neural/summary.json#L1-L19) (detection frequency, not true power). [write-up](https://mottopanikeiku.github.io/projects/seed-power/)

### rl and environments

- [weeble](https://github.com/mottopanikeiku/weeble) — does shove training help a robot stay up? [go1's 50%-survival impulse improves by 8.8 N·s](https://github.com/mottopanikeiku/weeble/blob/ac15a37fe6035690348e20b83ca925e6feb9da93/results/report/ablation.csv), with three seeds per arm in simulation, not hardware. [demo](https://mottopanikeiku.github.io/weeble/)
- [coldstart](https://github.com/mottopanikeiku/coldstart) — how soon can a cold process produce a policy? [ars qualifies cartpole in 1.08 s median](https://github.com/mottopanikeiku/coldstart/blob/6b25a16a8423ab4a47bf54b0abde121a5528c012/README.md#original-laptop-results) on my laptop, including imports and evaluation (reused eval seeds). [write-up](https://mottopanikeiku.github.io/projects/control-clock/)

### inference and kernels

- [quartet](https://github.com/mottopanikeiku/quartet) — is the tuner limited by its kernel bank? [new triton actions cut geometric-mean latency 27% vs my old bank; still 1.17× torch](https://github.com/mottopanikeiku/quartet/blob/b4f3edf88973c9113b8ce1656c3796ecb7cd3ebd/results/action-expansion-summary.json#L1107-L1142) on one h100 (descriptive medians). [write-up](https://mottopanikeiku.github.io/projects/heliostune/)
- [temperament](https://github.com/mottopanikeiku/temperament) — can rotation hurt fp8 attention? [qwen2.5-7b hellaswag: 63.70% plain → 45.50% rotated → 81.05% rotated with centered keys](https://github.com/mottopanikeiku/temperament/blob/d4b4ad73a36a780ad0dd4f1980d5f5c0b1f50b24/results/accuracy/summary.json#L1058-L1137) (h100 batch scoring, not streaming). [write-up](https://mottopanikeiku.github.io/projects/attention-numerics/)
- [abacus](https://github.com/mottopanikeiku/abacus) — how far can a laptop decoder go? [qwen2.5-0.5b at 69.03 tokens/s, two threads, context 128](https://github.com/mottopanikeiku/abacus/blob/d2cb629bea01915140a996f6a83b4aacd1fb0165/results/tables.md#L3-L11), with int8 weights and fp32 arithmetic. [write-up](https://mottopanikeiku.github.io/projects/cpu-decode/)
- [doomformer](https://github.com/mottopanikeiku/doomformer) — can a doom map do neural arithmetic? [bounded mlp fuzzing compared 1,987,632 values with no integer-reference mismatch](https://github.com/mottopanikeiku/doomformer/blob/20f6dcd7065c8279f5dbc1339a8f3d1b1689927b/docs/verification.md#L224-L256) (testing, not a compiler proof). [films](https://mottopanikeiku.github.io/doomformer/)

### upstream

over [80 merged pull requests](https://github.com/search?q=is%3Apr+is%3Amerged+author%3Amottopanikeiku+-user%3Amottopanikeiku&type=pullrequests), including [vllm beam search](https://github.com/vllm-project/vllm/pull/62072), [cupy chirp](https://github.com/cupy/cupy/pull/10146), [sglang docs](https://github.com/sgl-project/sglang/pull/32172), [torchtitan streaming state](https://github.com/pytorch/torchtitan/pull/5501) and [sentence-transformers hard negatives](https://github.com/huggingface/sentence-transformers/pull/4267). my [pytorch dynamo fix](https://github.com/pytorch/pytorch/pull/196711) also [landed on main](https://github.com/pytorch/pytorch/commit/41d1dafad77d67ebbdcfcbb7228a7b179308ce45).
