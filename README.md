I’m building [Tenth Man Labs](https://tenthmanlabs.com). We put probabilities on geopolitical events, with the sources behind each number and a dated record of how it moved.

My background is GPU systems. Lately most of my work is evaluation and reinforcement learning.

**Start here**

- [attention-numerics](https://github.com/mottopanikeiku/attention-numerics): when rotating queries and keys before FP8 rounding makes attention worse. On a real FlashAttention-3 FP8 kernel on an H100, rotation multiplies Qwen2.5-1.5B’s teacher-forced perplexity by 12.6; centering the keys first brings it back to 1.004×. A rounding-noise model fixed in advance ranks the harmed heads with AUC 0.96. [Interactive explanation](https://mottopanikeiku.github.io/attention-numerics/).
- [eval-power](https://github.com/mottopanikeiku/eval-power): how many benchmark items it takes to tell two LLMs apart, and how often a small pilot gets that number wrong. [Calculator](https://mottopanikeiku.github.io/eval-power/).
- [seed-power](https://github.com/mottopanikeiku/seed-power): the same question for RL seeds. On 11,440 fresh training runs, studies planned from small pilots for 80% power detected the difference only 56% of the time.
- [cpu-decode](https://github.com/mottopanikeiku/cpu-decode): a from-scratch C++ int8 decoder for Qwen2.5-0.5B. At short context it reaches 83% of the laptop's memory-read ceiling and, at its best thread count, beats llama.cpp; at long context llama.cpp is clearly faster.
- [control-clock](https://github.com/mottopanikeiku/control-clock): seconds from a fresh Python process to a policy that passes CartPole or Acrobot. Random search over linear policies beat every PPO on CartPole; tuned PPO won Acrobot; a cloud GPU was slower once startup counted.
- [alignmenttax](https://github.com/mottopanikeiku/alignmenttax): does instruction tuning trade calibration for truthfulness? In seven base/instruct pairs, calibration got worse in six, but only four gained accuracy in exchange.
- [quantile-cycles](https://github.com/mottopanikeiku/quantile-cycles): a counterexample in distributional RL, checked in exact rational arithmetic and in Lean.
- [verge-lab](https://github.com/mottopanikeiku/verge-lab): picking preference pairs from multi-aspect judge scores, and abstaining when the aspects disagree. Against human preferences it did no better than a simple score-gap rule.
- [branchpilot](https://github.com/mottopanikeiku/branchpilot): a learned stopping rule for self-consistency sampling. Simple agreement rules won on GSM8K and on a MATH-500 holdout.
- [faultline](https://github.com/mottopanikeiku/faultline): recurrent PPO agents that have to run a cheap test before an expensive repair. The curriculum effect I was testing for didn’t hold up across seeds.
- [heliostune](https://github.com/mottopanikeiku/heliostune): Triton autotuning across four NVIDIA GPUs. Tuning data from other GPUs didn’t help, and on the H100 torch.matmul beat all 36 tuned configurations on every workload.

Merged fixes in PyTorch, Ray, Sentence Transformers, SGLang, and Celery. More at [mottopanikeiku.github.io](https://mottopanikeiku.github.io).
