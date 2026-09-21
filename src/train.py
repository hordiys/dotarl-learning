from environment import *
from agent import *
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

    done = False
    total_reward = 0
    steps = 0

    while not done:

        action = agent.choose_action(state)

        state, reward, done = env.step(action)

        total_reward += reward
        steps += 1

    win = env.state[3] <= 0

    episode_rewards.append(total_reward)
    episode_steps.append(steps)
    episode_wins.append(win)