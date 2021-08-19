# Deep Deterministic Policy Gradient using PyTorch
## Overview
This is a simple PyTorch implementation of [DDPG](https://arxiv.org/abs/1509.02971). This repo is not aim at reproducing the performace in the original paper, but to show the basic logics of how to do forward as well as backward in ode network.

## Run
**Algorithm tested on [LunarLanderContinuous-v2](https://gym.openai.com/envs/LunarLanderContinuous-v2/) env -**
![Lunar Lander](https://github.com/M-NEXT/RL_repository/blob/main/Deep%20Reinforcement%20Learning/DDPG/images/lunarlander.png)

**Algorithm tested on [Pendulum-v0](https://gym.openai.com/envs/Pendulum-v0/) env -**
![Pendulum](https://github.com/M-NEXT/RL_repository/blob/main/Deep%20Reinforcement%20Learning/DDPG/images/pendulum.png)

Note : These are the results of when the agent is on training mode. So there maybe noise present for exploration. For testing make the noise term zero.

## Dependencies
* Python
* PyTorch
* OpenAI Gym

## To Do
1. Extend this idea to solve mujoco environments.
2. Come with some Novel Idea using this algorithm.
