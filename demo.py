import gym 

def main():
	env = gym.make('MountainCar-v0')

	for episode in range(100):
		env.reset()

		while True:
			env.render()

			action = env.action_space.sample()
			env.step(action)

if __name__ == '__main__':
	main()