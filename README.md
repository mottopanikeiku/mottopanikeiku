I’m turning language models into superforecasters. I also build RL environments and evals, and I write CUDA, Triton and CPU kernels to make inference faster. More at [alpcetin.com](https://alpcetin.com).

**[doomformer](https://github.com/mottopanikeiku/doomformer)** compiles neural networks into DOOM maps, where voodoo dolls do the arithmetic. Split across four maps, an MNIST network reads 97.2% of the 10,000 test digits, and every value read back from the maps matches NumPy’s integer network. The [museum map](https://github.com/mottopanikeiku/doomformer/releases/download/v0.7.1/museum.wad) runs a small network by itself in GZDoom, and you can rewire it while it plays.

**[abacus](https://github.com/mottopanikeiku/abacus)** is a CPU inference engine for Qwen3 in about 1,000 lines of C. It starts as a naive float loop, and each commit after that is one optimization, timed against llama.cpp. On a Graviton4 it ends up tied with llama.cpp Q8_0 on decode and 1.5–1.7× faster on prefill.

**[rigcheck](https://github.com/mottopanikeiku/rigcheck)** tests a local coding setup (model, engine and agent) the way the agent uses it. It sends llama.cpp or Ollama the real system prompts and tool schemas of OpenCode, Codex CLI and Qwen Code, checks every tool call that comes back, and times each turn with error bars.

**[weeble](https://github.com/mottopanikeiku/weeble)** is a set of walking robots I trained with RL. You can [shove them around in your browser](https://mottopanikeiku.github.io/weeble/), where MuJoCo runs as WebAssembly. The dog’s policy trained in about 13 minutes on one L4.

**[temperament](https://github.com/mottopanikeiku/temperament)**: with FlashAttention-3’s FP8 attention, Qwen2.5-7B-Instruct drops from 81% to 64% on HellaSwag. Subtracting the mean key, which leaves exact attention unchanged, brings it back to 81%.

**[quartet](https://github.com/mottopanikeiku/quartet)** is a Triton matmul autotuner, measured against `torch.matmul` on 96 LLM-shaped workloads on four GPUs. On the H100, ten new kernel configurations took it from 1.61× torch’s latency to 1.17×.

#### Evals

- [rayleigh](https://github.com/mottopanikeiku/rayleigh): how many benchmark questions it takes to tell two LLMs apart, with a [calculator](https://mottopanikeiku.github.io/rayleigh/)
- [mendel](https://github.com/mottopanikeiku/mendel): the same question for RL training seeds
- [tithe](https://github.com/mottopanikeiku/tithe): on TruthfulQA, instruct models look worse calibrated than their base models in 8 of 9 pairs if you score the A/B label, and better in 6 of 9 if you score the full answer
- [verge-lab](https://github.com/mottopanikeiku/verge-lab): Pareto selection of DPO preference pairs against the obvious baseline, on nine adapters; no clear difference

#### RL

- [coldstart](https://github.com/mottopanikeiku/coldstart): a stopwatch for small RL runs that starts before Python does; on my laptop random search solves CartPole about a second after launch
- [quantile-cycles](https://github.com/mottopanikeiku/quantile-cycles): a one-state MDP where quantile Bellman control never converges, with the smallest case proved in Lean

#### Also

[contrapunctus](https://mottopanikeiku.github.io/contrapunctus/), an illustrated atlas of 80 classical composers · [bitbound](https://mottopanikeiku.github.io/bitbound-quantization-quest/), a pixel-art RPG about quantization · [terrasim](https://mottopanikeiku.github.io/terrasim/), a browser terrarium

I’ve had over 80 pull requests merged into PyTorch, vLLM, SGLang, torchtitan, sentence-transformers, tensordict, timm and others.
