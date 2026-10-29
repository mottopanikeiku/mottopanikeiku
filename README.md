i'm turning language models into superforecasters. on the side i work on evals, rl and inference; these are the questions i've been testing.

each result links to committed evidence. more experiments and write-ups at [alpcetin.com](https://alpcetin.com/).

### evals

- [tithe](https://github.com/mottopanikeiku/tithe) — does instruction tuning trade calibration for truthfulness? [on the same 779 questions with shared prompts, 95% intervals resolve ece worsening in 8 of 9 label-scored pairs and none of the full-string-scored pairs](https://github.com/mottopanikeiku/tithe/blob/8c3e4e50bd6f94a6f574a466466934acc8499e9f/README.md?plain=1#L3). [write-up](https://mottopanikeiku.github.io/projects/alignmenttax/)
  <details><summary>details</summary>

  it depends on how i score the answer: on [the same 779 questions and answers, instruction tuning worsens ece in 8 of 9 pairs when i score the a/b label, but improves it in 6 and worsens it in none when i score the two answers as full strings (shared prompts, 95% intervals)](https://github.com/mottopanikeiku/tithe/blob/8c3e4e50bd6f94a6f574a466466934acc8499e9f/README.md?plain=1#L3). the prompts and scored text still differ, so this doesn't show what causes the flip.

  </details>
- [rayleigh](https://github.com/mottopanikeiku/rayleigh) — how many questions separate two models? [in simulation, planning from a 128-item pilot's observed gap reached 15–68% power instead of 80%](https://github.com/mottopanikeiku/rayleigh/blob/400e91a7ef4fda4c9cf1a5f4b7138e05b9151986/README.md?plain=1#L9). [calculator](https://mottopanikeiku.github.io/rayleigh/)
  <details><summary>details</summary>

  in simulations where i know the truth, [planning from a 128-item pilot's observed gap reached 15–68% power instead of 80%, while a 95% upper bound on the discordance rate reached 84–95% at 1.2–2.4 times the median plug-in budget](https://github.com/mottopanikeiku/rayleigh/blob/400e91a7ef4fda4c9cf1a5f4b7138e05b9151986/README.md?plain=1#L9). on fresh items, [23 of 27 planned comparisons between six small models detected a difference, 17 after holm over all 30 planned](https://github.com/mottopanikeiku/rayleigh/blob/400e91a7ef4fda4c9cf1a5f4b7138e05b9151986/README.md?plain=1#L29-L35) (nominal tests, mostly large gaps).

  </details>
- [mendel](https://github.com/mottopanikeiku/mendel) — how many training seeds are enough? [in simulation, a fixed-effect plan with a variance allowance kept power at 79.3–83.3% for an 80% target](https://github.com/mottopanikeiku/mendel/blob/b47b3a67291441839f73830448bedfc5ec362042/README.md?plain=1#L5). [write-up](https://mottopanikeiku.github.io/projects/seed-power/)
  <details><summary>details</summary>

  in a known-truth simulation, [fixing the effect in advance and allowing for noise in the pilot variance kept power at 79.3–83.3% for an 80% target, while planning from the pilot's observed gap gave 36.3–80.5%](https://github.com/mottopanikeiku/mendel/blob/b47b3a67291441839f73830448bedfc5ec362042/README.md?plain=1#L5). my fresh-seed ppo plans used the observed gap and [detected 139/307 differences](https://github.com/mottopanikeiku/mendel/blob/b47b3a67291441839f73830448bedfc5ec362042/results/neural/summary.json#L1-L19) (detection frequency, not power), and [cartpole's same-variant null controls rejected 5/36](https://github.com/mottopanikeiku/mendel/blob/b47b3a67291441839f73830448bedfc5ec362042/README.md?plain=1#L31-L33), which my diagnostics could not explain.

  </details>

### rl and environments

- [weeble](https://github.com/mottopanikeiku/weeble) — does shove training help a robot stay up? [go1's 50%-survival impulse improves by 8.8 N·s](https://github.com/mottopanikeiku/weeble/blob/463c6c1c0b83f3dfcf21371cebbb083853050598/results/report/ablation.csv), and [a robustness atlas tests the 12 released policies over 21,600 episodes](https://github.com/mottopanikeiku/weeble/blob/463c6c1c0b83f3dfcf21371cebbb083853050598/README.md?plain=1#L6-L16), all in simulation. [demo](https://mottopanikeiku.github.io/weeble/)
  <details><summary>details</summary>

  [go1's 50%-survival impulse improves by 8.8 N·s with three seeds per arm](https://github.com/mottopanikeiku/weeble/blob/463c6c1c0b83f3dfcf21371cebbb083853050598/results/report/ablation.csv). in [a robustness atlas of 21,600 episodes over the 12 released policies, every dog seed stayed up in at least 90% of episodes carrying 40% of its body mass, but none did with 40 ms of sensor delay](https://github.com/mottopanikeiku/weeble/blob/463c6c1c0b83f3dfcf21371cebbb083853050598/README.md?plain=1#L6-L16). it's all simulation, not hardware, and ci rebuilds the report and atlas byte for byte on pull requests.

  </details>
- [coldstart](https://github.com/mottopanikeiku/coldstart) — how soon can a cold process produce a policy? [ars qualifies cartpole in 1.08 s median](https://github.com/mottopanikeiku/coldstart/blob/d1886ebcec04f4facef65a5bb799486ab0dfb218/README.md?plain=1#L50) on my laptop, including imports and evaluation. [write-up](https://mottopanikeiku.github.io/projects/control-clock/)
  <details><summary>details</summary>

  [ars qualifies cartpole in 1.08 s median](https://github.com/mottopanikeiku/coldstart/blob/d1886ebcec04f4facef65a5bb799486ab0dfb218/README.md?plain=1#L50) on my laptop, including imports and evaluation (reused eval seeds). i wrote [a c environment batch that matches gymnasium's resets bit for bit on 1,010,006 seeds per task and steps cartpole environments 7.7–13× faster than my numpy batch](https://github.com/mottopanikeiku/coldstart/blob/d1886ebcec04f4facef65a5bb799486ab0dfb218/README.md?plain=1#L70), but [the environment is only 22–27% of an ars or cem run, so even a free environment would cut a run by at most about a quarter](https://github.com/mottopanikeiku/coldstart/blob/d1886ebcec04f4facef65a5bb799486ab0dfb218/README.md?plain=1#L71). i have not timed the c batch inside qualification.

  </details>

### inference and kernels

- [quartet](https://github.com/mottopanikeiku/quartet) — is the tuner limited by its kernel bank? [even the best action in my original h100 archive takes 1.608–1.609× torch's latency](https://github.com/mottopanikeiku/quartet/blob/74ac20cd5aacf5966b3b9e4f1d302c7ae5ba5fdd/README.md?plain=1#L45). [write-up](https://mottopanikeiku.github.io/projects/heliostune/)
  <details><summary>details</summary>

  in my original h100 archive, [the earlier-bank choice adds at most 0.14% geometric-mean latency over the later bank's in-sample best action, and even that best action's latency is 1.608–1.609× torch's](https://github.com/mottopanikeiku/quartet/blob/74ac20cd5aacf5966b3b9e4f1d302c7ae5ba5fdd/README.md?plain=1#L45). [the new triton actions reduce geometric-mean latency by 27.0% versus the old bank, but still take 1.174× torch's time](https://github.com/mottopanikeiku/quartet/blob/74ac20cd5aacf5966b3b9e4f1d302c7ae5ba5fdd/README.md?plain=1#L15-L21). these are descriptive medians from one h100 collection; the same collector now runs on any cuda gpu under its own run id, so i can repeat it.

  </details>
- [temperament](https://github.com/mottopanikeiku/temperament) — can rotation hurt fp8 attention? [paired against plain fp8, rotation costs qwen2.5-7b-instruct 18.20 points on hellaswag but gains 5.10 on mmlu](https://github.com/mottopanikeiku/temperament/blob/289c4f055878cedcee7c7bbe437754379cb5b93a/README.md?plain=1#L11). [write-up](https://mottopanikeiku.github.io/projects/attention-numerics/)
  <details><summary>details</summary>

  paired on the same items, [rotating queries and keys costs qwen2.5-7b-instruct 18.20 points on hellaswag against plain fp8 but gains 5.10 on mmlu, and adding rotation to already-centered keys changes hellaswag by +0.20 points (95% interval −0.25 to +0.65)](https://github.com/mottopanikeiku/temperament/blob/289c4f055878cedcee7c7bbe437754379cb5b93a/README.md?plain=1#L11). this is h100 batch scoring, with exploratory intervals and no multiple-comparison correction.

  </details>
- [abacus](https://github.com/mottopanikeiku/abacus) — how fast can my own cpu decoder run qwen2.5-0.5b-instruct? [it reaches 1.090–1.531× llama.cpp q8_0's paired throughput in all six pre-specified cells](https://github.com/mottopanikeiku/abacus/blob/b7dfceee8b85b0ae20c81c23c2d8522b7046eed6/README.md?plain=1#L4) on one cloud host, not my laptop. [write-up](https://mottopanikeiku.github.io/projects/cpu-decode/)
  <details><summary>details</summary>

  [it beat llama.cpp q8_0 in all six pre-specified cells, at 1.090–1.531× paired throughput](https://github.com/mottopanikeiku/abacus/blob/b7dfceee8b85b0ae20c81c23c2d8522b7046eed6/README.md?plain=1#L4), on one virtual cloud host with cpu binding, not my laptop. i also made generation stop at end of turn, specialized the batched kernels (speed not measured), added a one-command `make demo` and an offline corpus step, and [checked the shipped weights on six authored prompts: they pick the unquantized model's top token at 462 of 476 positions](https://github.com/mottopanikeiku/abacus/blob/b7dfceee8b85b0ae20c81c23c2d8522b7046eed6/docs/MEASUREMENTS.md?plain=1#L116) (agreement, not task accuracy).

  </details>
- [doomformer](https://github.com/mottopanikeiku/doomformer) — can a doom map do neural arithmetic? [fuzzing compared 1,987,632 values with no integer-reference mismatch](https://github.com/mottopanikeiku/doomformer/blob/eacf6c6b0a2d649604b95300add8833d31153a33/README.md?plain=1#L124-L126) (testing, not a proof), and [the museum map lets you rewire one weight inside a running level](https://github.com/mottopanikeiku/doomformer/blob/eacf6c6b0a2d649604b95300add8833d31153a33/README.md?plain=1#L86-L98). [films](https://mottopanikeiku.github.io/doomformer/)
  <details><summary>details</summary>

  [fuzzing 15,000 nets at the range limits compared 1,987,632 values with no integer-reference mismatch](https://github.com/mottopanikeiku/doomformer/blob/eacf6c6b0a2d649604b95300add8833d31153a33/README.md?plain=1#L124-L126), and readback is now guarded, so a dropped page can't pass with stale values (testing, not a compiler proof). in [the museum map, 136 voodoo dolls run a small hand-written network that reads a digit from floor pads, and rewiring one weight inside the running level turns a 7 into a 1, with all 148 values exact](https://github.com/mottopanikeiku/doomformer/blob/eacf6c6b0a2d649604b95300add8833d31153a33/README.md?plain=1#L86-L98); ci builds [the wad](https://github.com/mottopanikeiku/doomformer/blob/eacf6c6b0a2d649604b95300add8833d31153a33/docs/museum.md?plain=1#L81-L84) so you can download it and play without python (so far i've run it only in vizdoom).

  </details>

### upstream

over [80 merged pull requests](https://github.com/search?q=is%3Apr+is%3Amerged+author%3Amottopanikeiku+-user%3Amottopanikeiku&type=pullrequests), including [vllm beam search](https://github.com/vllm-project/vllm/pull/62072), [cupy chirp](https://github.com/cupy/cupy/pull/10146), [sglang docs](https://github.com/sgl-project/sglang/pull/32172), [torchtitan streaming state](https://github.com/pytorch/torchtitan/pull/5501) and [sentence-transformers hard negatives](https://github.com/huggingface/sentence-transformers/pull/4267). my [pytorch dynamo fix](https://github.com/pytorch/pytorch/pull/196711) also [landed on main](https://github.com/pytorch/pytorch/commit/41d1dafad77d67ebbdcfcbb7228a7b179308ce45).
