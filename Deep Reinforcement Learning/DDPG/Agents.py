import ReplayBuffer as rb
import Networks as networks
import Noise
import numpy as np
import torch

class Agent():
    def __init__(self, input_dims, num_actions, lr_actor, lr_critic, gamma, tau, batch_size, capacity, device):
        self.num_actions = num_actions
        self.input_dims = input_dims
        self.lr_actor = lr_actor
        self.lr_critic = lr_critic
        self.gamma = gamma
        self.tau = tau
        #self.device = device
        self.memory = rb.ReplayMemory(capacity, num_actions, batch_size, input_dims)
        self.critic = networks.Critic(input_dims, num_actions, lr_critic).to(device)
        self.critic_target = networks.Critic(input_dims, num_actions, lr_critic).to(device)
        self.actor = networks.Actor(input_dims, num_actions, lr_actor).to(device)
        self.actor_target = networks.Actor(input_dims, num_actions, lr_actor).to(device)
        self.noise = Noise.OUActionNoise(mu=np.zeros(num_actions))#.to(device)
        

    def select_action(self, obs, device):
        obs = torch.tensor([obs], dtype=torch.float32).to(device)
        mu = self.actor.forward(obs)
        mu = mu + torch.tensor(self.noise(), dtype=torch.float32).to(device)
        return mu

    def get_tensors(self, batch, device):
        states = torch.tensor(batch[0]).to(device)
        actions = torch.tensor(batch[1], dtype=torch.float32).to(device)
        rewards = torch.tensor(batch[2]).to(device)
        next_states = torch.tensor(batch[3]).to(device)
        dones = torch.tensor(batch[4]).to(device)
        #print(type(actions))
        return states, actions, rewards, next_states, dones


    def learn(self, device):
        if self.memory.can_provide_batch():
            batch = self.memory.give_batch()
            states, actions, rewards, next_states, dones = self.get_tensors(batch, device)
            #print(type(actions))
            next_actions = self.actor_target.forward(next_states)
            next_q_value = self.critic_target.forward(next_states, next_actions)
            current_q_value = self.critic_target.forward(states, actions)

            next_q_value[dones] = 0
            next_q_value = next_q_value.reshape(-1,)
            #rewards = rewards.reshape(-1,)
            #current_q_value.reshape(-1,)
            calc_q_value = rewards + self.gamma * next_q_value
            calc_q_value = calc_q_value.reshape(-1,1).detach()
            #print(next_q_value.shape, rewards.shape)

            self.critic.optimizer.zero_grad()
            critic_loss = self.critic.loss(calc_q_value, current_q_value)
            critic_loss.backward()
            self.critic.optimizer.step()

            self.actor.optimizer.zero_grad()
            self.critic.eval()
            #self.actor.eval()
            temp_actions = self.actor.forward(states)
            #self.actor.train()
            actor_loss = -1 * self.critic.forward(states, temp_actions)
            actor_loss = torch.mean(actor_loss)
            actor_loss.backward()
            self.actor.optimizer.step()
            self.critic.train()

            self.update_target_networks(self.tau)

    def update_target_networks(self, tau):
        actor_params = dict(self.actor.named_parameters())
        actor_target_params = dict(self.actor_target.named_parameters())
        critic_params = dict(self.critic.named_parameters())
        critic_target_params = dict(self.critic_target.named_parameters())

        for name in actor_params:
            actor_params[name] = tau*actor_params[name].clone() + (1-tau)*actor_target_params[name].clone()

        for name in critic_params:
            critic_params[name] = tau*critic_params[name].clone() + (1-tau)*critic_target_params[name].clone()

        self.actor_target.load_state_dict(actor_params)
        self.critic_target.load_state_dict(critic_params)
