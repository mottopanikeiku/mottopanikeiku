I’m turning language models into superforecasters, and alongside that I build RL environments and evals and write CUDA, Triton and CPU kernels that make inference faster. There’s a longer list of what I’ve made on [alpcetin.com](https://alpcetin.com).

<a href="https://mottopanikeiku.github.io/lockstep/"><img src="https://raw.githubusercontent.com/mottopanikeiku/lockstep/main/docs/demo.gif" width="720" alt="lockstep playing back a dot product kernel, where the warp timeline fills in while the reduction switches off more lanes of each warp every round"></a>

**[lockstep](https://mottopanikeiku.github.io/lockstep/)** is a browser game for learning CUDA in which you write a kernel and a simulated GPU runs it warp by warp, so you can watch divergent branches, scattered loads and bank conflicts cost you cycles and get caught the moment you write a race. Its twenty levels start with a one-line map and end with flash attention, and the starter and reference kernels for all of them compile unchanged with nvcc.

**[doomformer](https://github.com/mottopanikeiku/doomformer)** compiles integer neural networks into DOOM maps, where voodoo dolls do the arithmetic. In the [DrawPad map](https://github.com/mottopanikeiku/doomformer/releases/download/v0.7.2/drawpad.wad) you draw a digit on the floor in GZDoom and 1,355 voodoo dolls in the same map read it with an MNIST network, while the [museum map](https://github.com/mottopanikeiku/doomformer/releases/download/v0.7.1/museum.wad) lets you rewire a smaller network as it runs.

**[abacus](https://github.com/mottopanikeiku/abacus)** is a CPU inference engine for Qwen3 in about 1,400 lines of C, built one measured commit at a time from a naive float loop, checked against transformers at every step, and explained commit by commit in a [walkthrough](https://mottopanikeiku.github.io/abacus/). With 4 threads on GitHub’s Neoverse-N2 runner it decodes 1.16× and prefills 1.25× as fast as llama.cpp Q8_0, while on x86 runners it prefills about 10% faster and roughly ties on decode, and on an M1 it still trails llama.cpp at 0.64× on prefill.

**[rigcheck](https://github.com/mottopanikeiku/rigcheck)** tests a local coding setup (model, engine and agent) the way the agent uses it. It sends llama.cpp or Ollama the real system prompts and tool schemas of OpenCode, Codex CLI and Qwen Code, checks every tool call that comes back, and times each turn with error bars.

**[weeble](https://github.com/mottopanikeiku/weeble)** is a set of walking robots trained with RL that you can [shove around in your browser](https://mottopanikeiku.github.io/weeble/), where MuJoCo runs as WebAssembly.

**[temperament](https://github.com/mottopanikeiku/temperament)** measures what FP8 attention does to accuracy on an H100. With FlashAttention-3’s FP8 kernel, Qwen2.5-7B-Instruct loses 17 points on HellaSwag in batch scoring, and subtracting the mean key before quantizing wins all of them back.

**[quartet](https://github.com/mottopanikeiku/quartet)** is a Triton matmul autotuner, measured against `torch.matmul` on 96 LLM-shaped workloads on a T4, an A10, an L4 and an H100.

#### Evals

- [rayleigh](https://github.com/mottopanikeiku/rayleigh): how many benchmark questions it takes to tell two LLMs apart, with a [calculator](https://mottopanikeiku.github.io/rayleigh/)
- [mendel](https://github.com/mottopanikeiku/mendel): the same question for RL training seeds
- [tithe](https://github.com/mottopanikeiku/tithe): base vs instruct calibration on TruthfulQA, which reverses when you change the prompt and the scored text
- [verge-lab](https://github.com/mottopanikeiku/verge-lab): Pareto selection of DPO preference pairs, tested against the obvious baseline on nine adapters without either one coming out clearly ahead, with a demo where you can [browse the real pairs](https://mottopanikeiku.github.io/verge-lab/) and see which ones each selector kept

#### RL

- [coldstart](https://github.com/mottopanikeiku/coldstart): times small RL runs from Python launch to a passing fixed-seed evaluation on CartPole and Acrobot
- [quantile-cycles](https://github.com/mottopanikeiku/quantile-cycles): a one-state MDP where quantile Bellman control cycles instead of converging, with the two-quantile case proved in Lean

#### Also

[contrapunctus](https://mottopanikeiku.github.io/contrapunctus/), an illustrated atlas of 80 classical composers · [bitbound](https://mottopanikeiku.github.io/bitbound-quantization-quest/), a pixel-art RPG about quantization · [exit-protocol](https://github.com/mottopanikeiku/exit-protocol), a three-lane browser runner · [terrasim](https://mottopanikeiku.github.io/terrasim/), a browser terrarium

Over 80 of my pull requests have been merged upstream, including fixes for a Dynamo equality bug in [PyTorch](https://github.com/pytorch/pytorch/pull/202136), beam search ignoring generation-config EOS tokens in [vLLM](https://github.com/vllm-project/vllm/pull/62072), Hugging Face streaming state that was lost between a checkpoint restore and the next read in [torchtitan](https://github.com/pytorch/torchtitan/pull/5501), and hard-negative mining that picked the anchor itself in [sentence-transformers](https://github.com/huggingface/sentence-transformers/pull/4267).
