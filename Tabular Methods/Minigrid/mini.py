from gym_minigrid.wrappers import *
import numpy as np
import matplotlib.pyplot as plt

env = gym.make('MiniGrid-FourRooms-v0')
#env = FullyObsWrapper(env)
env = ImgObsWrapper(env)
env.reset()
esp = 0.6
actions = 3
Q = np.zeros((env.height, env.width, 4, actions))
print(env.max_steps)
E = np.zeros((env.height, env.width, 4, actions))
#Q = np.random.rand(env.height, env.width, 4, actions)
aspace = np.argmax(Q, 3)
policy = np.zeros((env.height, env.width, 4, actions))
policy += esp/actions


for i in range(Q.shape[0]):
	for j in range(Q.shape[1]):
		policy[i, j, aspace[i, j]] += 1-esp


'''for i in range(20):
	pos, dire = env.agent_pos, env.agent_dir
	action = aspace[pos[0]-1][pos[1]-1]
	env.step(action)
	env.render()'''

y_ep = []
x_ep = []
reward_ep = []
def nstate(action):
	obs, reward, terminal, emp = env.step(action)
	if prev_action!=2:
		return env.step(2)
	return(obs, reward, terminal, emp)

for episode in range(200):
	print(episode)
	env.reset()
	terminal = False
	prev_pos, prev_dire = env.agent_pos, env.agent_dir
	aspace = np.argmax(Q, 3)
	prev_action = aspace[prev_pos[1]][prev_pos[0]][prev_dire]
	#n_obs, n_reward, terminal, emp = env.step(action)
	esp = 0.6
	E = np.zeros((env.height, env.width, 4, actions))

	while terminal==False:
		obs, reward, terminal, emp = env.step(prev_action)
		#obs, reward, terminal, emp = env.step(prev_action)
		#if prev_action!=2:
		#	obs, reward, terminal, emp = env.step(2)
		E[prev_pos[1], prev_pos[0], prev_dire, prev_action] += 1
		if terminal == False:
			reward = -1
		pos, dire = env.agent_pos, env.agent_dir
		aspace = np.argmax(Q, 3)
		action = aspace[pos[1]][pos[0]][dire]
		Gexp = Q[pos[1], pos[0], dire, action]
		#Gexp = 0
		#for i in range(actions):
		#	Gexp += Q[pos[1], pos[0], dire, i] * policy[pos[1], pos[0], dire, i]
		Gexp = reward + 0.9*Gexp
		Gexp = Gexp - Q[prev_pos[1], prev_pos[0], prev_dire, prev_action]


		#Q[prev_pos[1], prev_pos[0], prev_dire, prev_action] += 0.2*(reward+0.9*Gexp - Q[prev_pos[1], prev_pos[0], prev_dire, prev_action])
		Q = Q + 0.2*Gexp*E
		E= 0.9*0.9*E

		policy = np.zeros((env.height, env.width, 4, actions))
		policy += esp/actions
		aspace = np.argmax(Q, 3)
		policy[prev_pos[1], prev_pos[0], prev_dire, aspace[prev_pos[1], prev_pos[0]]] += 1-esp

		prev_pos = pos
		prev_dire = dire
		prev_action = action
		esp = esp/(1.001)
		'''for i in range(Q.shape[0]):
			for j in range(Q.shape[1]):
				policy[i, j, aspace[i, j]] += 1-esp'''
		if episode%50==0:
			env.render()
	reward_ep.append(reward)
	x_ep.append(env.step_count)
	y_ep.append(episode)

plt.subplot(1,2,1)
plt.plot(y_ep, reward_ep)
plt.xlabel('Episode')
plt.ylabel('Cummulative Reward')
plt.subplot(1,2,2)
plt.plot(y_ep, x_ep)
plt.xlabel('Episode')
plt.ylabel('Time Steps')
plt.show()

# env.reset()

# for i in range(50):
# 	pos, dire = env.agent_pos, env.agent_dir
# 	aspace = np.argmax(Q, 3)
# 	action = aspace[pos[1]][pos[0]][dire]
# 	env.step(action)
# 	#env.step(action)
# 	env.render()

# env.close()
