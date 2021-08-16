import gym
import math
import random
import numpy as np
import matplotlib
import matplotlib.pyplot as plt
#matplotlib.use('TkAgg')
import torch
import torch.nn as nn
import torch.optim as optim
import torch.nn.functional as F

class Actor(nn.Module):
    def __init__(self, input_dims, num_actions, lr):
        super().__init__()
        self.fc1 = nn.Linear(in_features=input_dims, out_features=512)  #
        self.fc2 = nn.Linear(in_features=512, out_features=256)
        self.fc3 = nn.Linear(in_features=256, out_features=num_actions)
        self.optimizer = optim.Adam(self.parameters(), lr=lr)
        #self.loss = nn.MSELoss()
        
    def forward(self, t):
        t = self.fc1(t)
        t = F.relu(t)
        t = self.fc2(t)
        t = F.relu(t)
        t = self.fc3(t)
        #t = F.relu(t)
        t = torch.tanh(t)
        return t


class Critic(nn.Module):
    def __init__(self, input_dims, num_actions, lr):
        super().__init__()

        self.V_fc1 = nn.Linear(in_features=input_dims, out_features=512)  #
        self.V_fc2 = nn.Linear(in_features=512, out_features=256)
        #self.V_fc3 = nn.Linear(in_features=256, out_features=128)
        self.A_fc1 = nn.Linear(in_features=num_actions, out_features=256)
        self.AV_fc = nn.Linear(in_features=256, out_features=1)

        self.optimizer = optim.Adam(self.parameters(), lr=lr)
        self.loss = nn.MSELoss()


        
    def forward(self, t, a):
        t = self.V_fc1(t)
        t = F.relu(t)
        state_value = self.V_fc2(t)
        #t = F.relu(t)
        #state_value = self.V_fc3(t)

        #print(a, type(a))

        action_value = self.A_fc1(a)
        state_action_value = F.relu(torch.add(state_value, action_value))
        state_action_value = self.AV_fc(state_action_value)

        return state_action_value
