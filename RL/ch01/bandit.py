import numpy as np

class Bandit:
    def __init__(self, arms=10):
        self.rates = np.random.rand(arms)

    def play(self, arm):
        rate = self.rates[arm]
        if rate > np.random.rand():
            return 1
        else:
            return 0

bandit = Bandit()
Q = 0

for n in range(1, 11):
    reward = bandit.play(0)
    Q += (reward - Q) / n
    print(Q)