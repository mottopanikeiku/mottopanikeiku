I’m building [Tenth Man Labs](https://tenthmanlabs.com). We put probabilities on geopolitical events, with the sources behind each number and a dated record of how it moved.

My background is GPU systems. Lately most of my work is evaluation and reinforcement learning.

**Start here**

- [eval-power](https://github.com/mottopanikeiku/eval-power): how many benchmark items it takes to tell two LLMs apart, and how often a small pilot gets that number wrong.
- [quantile-cycles](https://github.com/mottopanikeiku/quantile-cycles): a counterexample in distributional RL, checked in exact rational arithmetic.
- [faultline](https://github.com/mottopanikeiku/faultline): recurrent PPO agents that have to run a cheap test before an expensive repair. The curriculum effect I was testing for didn’t hold up across seeds.
- [branchpilot](https://github.com/mottopanikeiku/branchpilot): a learned stopping rule for self-consistency sampling. A simple agreement rule won on GSM8K.
- [verge-lab](https://github.com/mottopanikeiku/verge-lab): picking preference pairs from multi-aspect judge scores, and abstaining when the aspects disagree.
- [heliostune](https://github.com/mottopanikeiku/heliostune): Triton autotuning across four NVIDIA GPUs. Tuning data from other GPUs didn’t help, and torch.matmul beat every tuned kernel.

Merged fixes in Ray, Sentence Transformers, and SGLang. More at [mottopanikeiku.github.io](https://mottopanikeiku.github.io).
