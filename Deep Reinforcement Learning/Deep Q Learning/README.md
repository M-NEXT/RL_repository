# Deep Q Network
## What is DQN ?
* The DQN ([Deep Q-Network](https://arxiv.org/abs/1312.5602)) algorithm was developed by DeepMind in 2015. 
* It was able to solve a wide range of Atari games (some to superhuman level) by combining reinforcement learning and deep neural networks at scale. 
* The algorithm was developed by enhancing a classic RL algorithm called Q-Learning with deep neural networks and a technique called experience replay.

## Implementing Deep Q-Learning in Python using PyTorch& OpenAI Gym
[CartPole](https://gym.openai.com/envs/CartPole-v0/) is one of the simplest environments in the OpenAI gym (a game simulator). The goal of CartPole is to balance a pole that’s connected with one joint on top of a moving cart. The system is controlled by applying a force of +1 or -1 to the cart. The pendulum starts upright, and the goal is to prevent it from falling over. A reward of +1 is provided for every timestep that the pole remains upright. The episode ends when the pole is more than 15 degrees from vertical, or the cart moves more than 2.4 units from the center.

## Result
DQN on cartpole environment - 
![Cartpole](https://github.com/M-NEXT/RL_repository/blob/main/Deep%20Reinforcement%20Learning/Deep%20Q%20Learning/images/cartpole.png)
