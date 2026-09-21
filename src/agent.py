import random
class Agent:
    def __init__(self, moves):
        self.moves = moves

    def choose_action(self, state):
        action = random.choice(self.moves)
        return action
    