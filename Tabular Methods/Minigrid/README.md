## Minigrid environment
Minigrid is a easy to use, lightweight and fast environment to perform reinforcement learning algorithms. The code has very few dependencies, making it less likely to break or fail to install. It loads no external sprites/textures, and it can run at up to 5000 FPS on a Core i7 laptop, which means you can run your experiments faster.

**Requirements:**
* Python 3.5+
* OpenAI Gym
* Numpy
* Matplotlib

Note: To implement Q learning algorithms we have to fix the goal and the agent position. CHange it according to the environment which you are using

## Run

**Fourrooms environment**

With normal Temporal Difference algorithm - 

![normal fourromms](https://github.com/M-NEXT/RL_repository/blob/main/Tabular%20Methods/Minigrid/images/4roomsenv.png)

With Eligibility Traces(backward view) algorithm -

![backwardview](https://github.com/M-NEXT/RL_repository/blob/main/Tabular%20Methods/Minigrid/images/4roomswithbackwardview.png)

## Simulation
The first image consists of agent with random policy as you can see its exploring the environment. The second image is an agent with optimal policy which is leanred from 100 episodes. The agent directly moves to its target location.

![episode1](https://github.com/M-NEXT/RL_repository/blob/main/Tabular%20Methods/Minigrid/images/ep0.gif) ![episode100](https://github.com/M-NEXT/RL_repository/blob/main/Tabular%20Methods/Minigrid/images/ep100.gif)

