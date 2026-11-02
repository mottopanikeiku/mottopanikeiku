I’m turning language models into superforecasters. I also build RL environments and evals, and I write CUDA, Triton and CPU kernels to make inference faster. More at [alpcetin.com](https://alpcetin.com).

<a href="https://mottopanikeiku.github.io/lockstep/"><img src="https://raw.githubusercontent.com/mottopanikeiku/lockstep/main/docs/screenshot.png" width="720" alt="lockstep: the dot product level mid-run, with three of every four lanes masked off by a branch and the shared array's reads marked"></a>

**[lockstep](https://mottopanikeiku.github.io/lockstep/)** is a browser game for learning CUDA. You write a kernel and a simulated GPU runs it warp by warp, so you can watch divergent branches, scattered loads and bank conflicts cost you cycles, and get caught when you write a race. Twenty levels, from a one-line map to flash attention.

**[doomformer](https://github.com/mottopanikeiku/doomformer)** compiles integer neural networks into DOOM maps, where voodoo dolls do the arithmetic. Draw a digit on the floor and the dolls classify it, or load the [museum map](https://github.com/mottopanikeiku/doomformer/releases/download/v0.7.1/museum.wad) in GZDoom and rewire its network while it runs.

**[abacus](https://github.com/mottopanikeiku/abacus)** is a CPU inference engine for Qwen3, written in C. It starts as a naive float loop, and each commit after that is one optimization, timed against llama.cpp. On a Graviton4 it ends up tied with llama.cpp Q8_0 on decode and 1.5–1.7× faster on prefill.

**[rigcheck](https://github.com/mottopanikeiku/rigcheck)** tests a local coding setup (model, engine and agent) the way the agent uses it. It sends llama.cpp or Ollama the real system prompts and tool schemas of OpenCode, Codex CLI and Qwen Code, checks every tool call that comes back, and times each turn with error bars.

**[weeble](https://github.com/mottopanikeiku/weeble)** is a set of walking robots trained with RL that you can [shove around in your browser](https://mottopanikeiku.github.io/weeble/), where MuJoCo runs as WebAssembly.

**[temperament](https://github.com/mottopanikeiku/temperament)** measures FP8 attention on an H100. With FlashAttention-3’s FP8 kernel, Qwen2.5-7B-Instruct loses 17 points on HellaSwag in batch scoring; subtracting the mean key gets them back.

**[quartet](https://github.com/mottopanikeiku/quartet)** is a Triton matmul autotuner, measured against `torch.matmul` on 96 LLM-shaped workloads on a T4, an A10, an L4 and an H100.

#### Evals

- [rayleigh](https://github.com/mottopanikeiku/rayleigh): how many benchmark questions it takes to tell two LLMs apart, with a [calculator](https://mottopanikeiku.github.io/rayleigh/)
- [mendel](https://github.com/mottopanikeiku/mendel): the same question for RL training seeds
- [tithe](https://github.com/mottopanikeiku/tithe): base vs instruct calibration on TruthfulQA, which reverses when you change the prompt and the scored text
- [verge-lab](https://github.com/mottopanikeiku/verge-lab): Pareto selection of DPO preference pairs against the obvious baseline, on nine adapters; no clear winner. You can [browse the real pairs](https://mottopanikeiku.github.io/verge-lab/)

#### RL

- [coldstart](https://github.com/mottopanikeiku/coldstart): times small RL runs from Python launch to a passing fixed-seed evaluation on CartPole and Acrobot
- [quantile-cycles](https://github.com/mottopanikeiku/quantile-cycles): a one-state MDP where quantile Bellman control cycles instead of converging, with the two-quantile case proved in Lean

#### Also

[contrapunctus](https://mottopanikeiku.github.io/contrapunctus/), an illustrated atlas of 80 classical composers · [bitbound](https://mottopanikeiku.github.io/bitbound-quantization-quest/), a pixel-art RPG about quantization · [exit-protocol](https://github.com/mottopanikeiku/exit-protocol), a three-lane browser runner · [terrasim](https://mottopanikeiku.github.io/terrasim/), a browser terrarium

Over 80 of my pull requests have been merged upstream. A few: a Dynamo equality bug in [PyTorch](https://github.com/pytorch/pytorch/pull/202136), beam search ignoring generation-config EOS tokens in [vLLM](https://github.com/vllm-project/vllm/pull/62072), Hugging Face streaming state lost between a checkpoint restore and the next read in [torchtitan](https://github.com/pytorch/torchtitan/pull/5501), and hard-negative mining that picked the anchor itself in [sentence-transformers](https://github.com/huggingface/sentence-transformers/pull/4267).
