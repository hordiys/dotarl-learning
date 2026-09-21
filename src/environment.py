class BaseEnvironment : 
    def __init__(self):
        self.state = [0, 800, 5, 100]
        self.agent_damage = 60
        self.moves = ["Move_forward", "Attack", "Move_backward"]
        self.reward = 0
        self.done = False

    def step(self, action):
        self.reward = 0
        if action == self.moves[0] :
            if abs(self.state[0]-self.state[2]) >= 1:
                self.state[0] += 1
                self.reward -= 0.01
                self.creep_attack()
            else : self.state[0]
        elif action == self.moves[1]  : 
            if abs(self.state[0]-self.state[2]) == 1 :
                self.reward += 0.01
                self.state[3] -= self.agent_damage
                if self.state[3] <= 0 :
                    self.reward += 1
                    self.done = True
            else : self.reward -= 0.05
        elif action == self.moves[2] :
            self.reward -= 0.02
            if self.state[1] <= 50:
                self.reward += 1
        return self.state, self.reward, self.done

    def reset(self):
        self.state = [0, 800, 5, 100]
        self.reward = 0
        return self.state

    def creep_attack(self):
        if self.state[0] == (self.state[2] - 1) :
            self.state[1] -= 20
            self.reward -= 0.01
            return self.state