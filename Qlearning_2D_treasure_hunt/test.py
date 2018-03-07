from maze_env import Maze
from RL_brain import QLearningTable


def update():
	for episode in range(100):
		# initial
		observation = env.reset()

		while True:
			# fresh env
			env.render()

			# RL choose action
			action = RL.choose_action(str(observation))

			# RL take action
			observation_, reward, done = env.step(action)

			# RL learn
			RL.learn(str(observation), action, reward, str(observation_))

			# update observation
			observation = observation_

			# break while done
			if done: break

	# end of game
	print('Game Over')
	env.destroy()

if __name__ == '__main__':
	env = Maze();
	RL = QLearningTable(actions=list(range(env.n_actions)))

	env.after(100, update)
	env.mainloop()
