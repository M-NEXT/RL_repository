import gym
import math
import random
import numpy as np
import matplotlib
import matplotlib.pyplot as plt
import torch
import torch.nn as nn
import torch.optim as optim
import torch.nn.functional as F
import Agents

env = gym.make('Pendulum-v0')
env.reset()

#############
capacity = 1000000
batch_size = 64
tau = 0.001
num_actions = env.action_space.shape[0]
input_dims = env.observation_space.shape[0]
episodes = 1000
lr_actor = 0.0001
lr_critic = 0.001
gamma = 0.99
#reward_track = []
device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
print('Number or actions : ', num_actions)
print('Action space : ', env.action_space)
print('Observation space : ', env.observation_space)

##############
agent = Agents.Agent(input_dims, num_actions, lr_actor, lr_critic, gamma, tau, batch_size, capacity, device)

##############
reward_track = []
best_score = -100000
for episode in range(episodes):
    print('Episode : ', episode, end='\t')
    score = 0
    terminal = False
    state = env.reset()
    while not terminal:
        # rate = memory.get_epsilon()
        # #print(rate)
        # eps_track.append(rate)
        action = agent.select_action(state, device)
        #action = action.cpu().detach().numpy().reshape(-1,)
        #print(action)
        next_state, reward, terminal, emp = env.step(action)
        if terminal:
            done = 0
        else:
            done = 1
        #state = state.reshape(-1,1)
        #next_state = next_state.reshape(-1,)
        #action = torch.tensor(action, dtype=torch.float32)
        #print(state.shape, next_state.shape)
        agent.memory.store(state, action, reward, next_state, terminal)
        state = next_state
        score += reward

        agent.learn(device)
        state = next_state
    
    #if score>best_score:
    #	agent.save_model('/home/tanmayp/Desktop/RL/DDPG/saved_model')
    print('score : ', score.item())
    reward_track.append(score.item())
