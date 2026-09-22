from environment import *
from agent import *
import csv
env = BaseEnvironment()
agent = Agent(env.moves)

state = env.reset()
total_reward = None
done = False
episode_rewards = []
episode_steps = []
episode_wins = []

for episode in range(100):

    state = env.reset()

    total_reward = 0
    steps = 0
    max_steps = 100

    while not done and steps < max_steps:

        action = agent.choose_action(state)

        state, reward, done = env.step(action)

        total_reward += reward
        steps += 1

    win = env.state[3] <= 0

    episode_rewards.append(total_reward)
    episode_steps.append(steps)
    episode_wins.append(win)
    with open("results\first_results.csv", 'w', newline='') as myfile:
     wr = csv.writer(myfile, quoting=csv.QUOTE_ALL)
     wr.writerow(episode_steps)
     wr.writerow(episode_wins)