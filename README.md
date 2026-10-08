I’m building [Tenth Man Labs](https://tenthmanlabs.com). We put probabilities on geopolitical events, with the sources behind each number and a dated record of how it moved.

My background is GPU systems. Lately most of my work is evaluation and reinforcement learning.

**Start here**

- [attention-numerics](https://github.com/mottopanikeiku/attention-numerics): when rotating queries and keys before FP8 rounding makes attention worse. With the real FlashAttention-3 FP8 kernel on an H100, rotation cuts Qwen2.5-7B’s HellaSwag accuracy from 80.9% to 45.5%; centering the keys first removes every measured loss of two points or more across eight models. [Interactive explanation](https://mottopanikeiku.github.io/attention-numerics/).
- [eval-power](https://github.com/mottopanikeiku/eval-power): how many benchmark items it takes to tell two LLMs apart, and how often a small pilot gets that number wrong. In a live test on six small models, plans committed before collecting fresh answers detected 23 of 27 differences. [Calculator](https://mottopanikeiku.github.io/eval-power/).
- [seed-power](https://github.com/mottopanikeiku/seed-power): the same question for RL seeds. On more than 77,000 fresh training runs, studies planned from small pilots for 80% power detected the difference 56% of the time with linear policies and 45% with neural PPO.
- [cpu-decode](https://github.com/mottopanikeiku/cpu-decode): a from-scratch C++ int8 decoder for Qwen2.5-0.5B. At short context it reaches 83% of the laptop's memory-read ceiling and, at its best thread count, beats llama.cpp; at long context llama.cpp is clearly faster.
- [control-clock](https://github.com/mottopanikeiku/control-clock): seconds from a fresh Python process to a policy that passes CartPole or Acrobot. Random search over linear policies beat every PPO on CartPole; tuned PPO won Acrobot; a cloud GPU was slower once startup counted.
- [alignmenttax](https://github.com/mottopanikeiku/alignmenttax): does instruction tuning trade calibration for truthfulness? Across nine base/instruct pairs up to 32B, it depends on the scoring: on a binary TruthfulQA format six pairs gained accuracy but lost calibration; on standard MC1 four improved both and none showed that tradeoff.
- [quantile-cycles](https://github.com/mottopanikeiku/quantile-cycles): a counterexample in distributional RL, checked in exact rational arithmetic and in Lean.
- [verge-lab](https://github.com/mottopanikeiku/verge-lab): picking preference pairs from multi-aspect judge scores, and abstaining when the aspects disagree. Neither agreement with human preferences nor DPO training on the selected pairs beat a simple score-gap rule.
- [branchpilot](https://github.com/mottopanikeiku/branchpilot): a learned stopping rule for self-consistency sampling. Simple agreement rules won on GSM8K and on a MATH-500 holdout.
- [faultline](https://github.com/mottopanikeiku/faultline): recurrent PPO agents that have to run a cheap test before an expensive repair. Across 375 seeds per curriculum, training only on ambiguous faults beat random sampling by 10 points but lost to a difficulty curriculum by 6.
- [heliostune](https://github.com/mottopanikeiku/heliostune): Triton autotuning across four NVIDIA GPUs. Tuning data from other GPUs didn’t help; on the H100 the limit was the kernel set, and adding split-K and persistent kernels won 9 of 96 workloads against torch.matmul, up from none.

Merged fixes in PyTorch, Ray, Sentence Transformers, SGLang, and Celery. More at [mottopanikeiku.github.io](https://mottopanikeiku.github.io).
