I’m building [Tenth Man Labs](https://tenthmanlabs.com). We put probabilities on geopolitical events, with the sources behind each number and a dated record of how it moved.

My background is GPU systems. Lately most of my work is evaluation and reinforcement learning.

**Start here**

- [quantile-cycles](https://github.com/mottopanikeiku/quantile-cycles): a counterexample in distributional RL, checked in exact rational arithmetic.
- [faultline](https://github.com/mottopanikeiku/faultline): recurrent PPO agents that have to run a cheap test before an expensive repair. The curriculum effect I was testing for didn’t hold up across seeds.
- [branchpilot](https://github.com/mottopanikeiku/branchpilot): a learned stopping rule for self-consistency sampling. Simpler rules won on GSM8K.
- [heliostune](https://github.com/mottopanikeiku/heliostune): Triton autotuning across four NVIDIA GPUs. Transferring a model learned on cheaper GPUs didn’t help.

Merged fixes in Ray, Sentence Transformers, and SGLang. More at [mottopanikeiku.github.io](https://mottopanikeiku.github.io).
