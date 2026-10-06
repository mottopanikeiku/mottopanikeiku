I’m building [Tenth Man Labs](https://tenthmanlabs.com). We put probabilities on geopolitical events, with the sources behind each number and a dated record of how it moved.

My background is GPU systems. Lately most of my work is evaluation and reinforcement learning.

**Start here**

- [eval-power](https://github.com/mottopanikeiku/eval-power): how many benchmark items it takes to tell two LLMs apart, and how often a small pilot gets that number wrong.
- [control-clock](https://github.com/mottopanikeiku/control-clock): seconds from a fresh Python process to a policy that passes CartPole or Acrobot on a laptop CPU. Random search over linear policies beat every PPO on CartPole; tuned PPO won Acrobot.
- [cpu-decode](https://github.com/mottopanikeiku/cpu-decode): a from-scratch C++ int8 decoder for Qwen2.5-0.5B. At short context it reaches 83% of the laptop's memory-read ceiling and, at its best thread count, beats llama.cpp; at long context llama.cpp is clearly faster.
- [attention-numerics](https://github.com/mottopanikeiku/attention-numerics): rounding error in BF16 and FP8 attention, emulated against a float64 reference. Rotating inputs before FP8 rounding can make error much worse when keys share a common component.
- [quantile-cycles](https://github.com/mottopanikeiku/quantile-cycles): a counterexample in distributional RL, checked in exact rational arithmetic.
- [verge-lab](https://github.com/mottopanikeiku/verge-lab): picking preference pairs from multi-aspect judge scores, and abstaining when the aspects disagree.
- [branchpilot](https://github.com/mottopanikeiku/branchpilot): a learned stopping rule for self-consistency sampling. A simple agreement rule won on GSM8K.
- [faultline](https://github.com/mottopanikeiku/faultline): recurrent PPO agents that have to run a cheap test before an expensive repair. The curriculum effect I was testing for didn’t hold up across seeds.
- [heliostune](https://github.com/mottopanikeiku/heliostune): Triton autotuning across four NVIDIA GPUs. Tuning data from other GPUs didn’t help, and torch.matmul beat every tuned kernel.

Merged fixes in Ray, Sentence Transformers, SGLang, and Celery. More at [mottopanikeiku.github.io](https://mottopanikeiku.github.io).
