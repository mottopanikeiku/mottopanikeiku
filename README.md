I’m turning language models into superforecasters. I also build RL environments and evals, and I write CUDA, Triton and CPU kernels to make inference faster. More at [alpcetin.com](https://alpcetin.com).

**[doomformer](https://github.com/mottopanikeiku/doomformer)** compiles neural networks into DOOM maps, where voodoo dolls do the arithmetic. On the 10,000 MNIST test digits the level reads 97.2% correctly, and every value read back from the game matches NumPy. You can [download the museum map](https://github.com/mottopanikeiku/doomformer/releases/download/v0.7.1/museum.wad) and rewire its network while it runs in GZDoom.

**[weeble](https://github.com/mottopanikeiku/weeble)** is a set of walking robots you can [shove around in your browser](https://mottopanikeiku.github.io/weeble/). I trained the Go1 and G1 policies with RL on a single GPU (the dog took 14 minutes and 24 cents) and stress-tested them over 21,600 episodes.

**[abacus](https://github.com/mottopanikeiku/abacus)** is an LLM decoder I wrote from scratch in C++. Its int8 VNNI kernels run Qwen2.5-0.5B at 1.1–1.5× the speed of llama.cpp Q8_0 on a Zen 4 server.

**[temperament](https://github.com/mottopanikeiku/temperament)** measures FP8 attention on an H100. With FlashAttention-3, Qwen2.5-7B drops from 80.9% to 63.7% on HellaSwag, and rotating queries and keys first takes it down to 45.5%. Subtracting the mean key brings it back to 81.0%.

**[quartet](https://github.com/mottopanikeiku/quartet)** is a Triton matmul autotuner, measured against `torch.matmul` on 96 LLM-shaped workloads across T4, A10, L4 and H100. It lands within 3% of torch on A10 and L4. On H100, ten new kernel configurations cut its latency by 27%, to 1.17× torch’s.

#### Evals

- **[tithe](https://github.com/mottopanikeiku/tithe)**: are instruction-tuned models worse calibrated than their base models? On the same 779 TruthfulQA questions, they are in 8 of 9 pairs when you score the A/B label, and they’re better in 6 when you score the full answers.
- **[rayleigh](https://github.com/mottopanikeiku/rayleigh)**: how many benchmark questions it takes to tell two LLMs apart. In simulation, planning from a 128-question pilot’s observed gap gave 15–68% power instead of 80%. There’s a [calculator](https://mottopanikeiku.github.io/rayleigh/).
- **[mendel](https://github.com/mottopanikeiku/mendel)**: the same question for RL training seeds. In simulation, fixing the effect size up front and allowing for noise in the pilot’s variance kept power at 79–83%.

#### RL

- **[coldstart](https://github.com/mottopanikeiku/coldstart)**: on my laptop, random search gets a passing CartPole policy about a second after Python starts. PPO takes 4–6 seconds.
- **[quantile-cycles](https://github.com/mottopanikeiku/quantile-cycles)**: quantile Bellman control can cycle instead of converging, even with one state. The K=2 case is proved in Lean.

#### Also

[contrapunctus](https://mottopanikeiku.github.io/contrapunctus/), an illustrated atlas of 80 classical composers · [bitbound](https://mottopanikeiku.github.io/bitbound-quantization-quest/), a pixel-art RPG that teaches quantization · [terrasim](https://mottopanikeiku.github.io/terrasim/), a browser terrarium

I’ve merged 80+ pull requests into PyTorch, vLLM, SGLang, CuPy, torchtitan, sentence-transformers and others.
