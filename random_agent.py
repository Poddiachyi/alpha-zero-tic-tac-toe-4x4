import numpy as np

class RandomAgent(object):

    def __init__(self):
        pass

    def act(self, state):
        action_dist = np.random.dirichlet(np.ones(16), size=1).ravel()
        action_mask = self.get_action_mask(state)
        action_dist = self.apply_mask(action_dist, action_mask)
        return action_dist.argmax()

    def get_action_mask(self, state):
        mask = np.ones(16)
        for i in range(len(state)):
            if state[i] == "X" and state[i] == "O":
                mask[i] = 0
        return mask

    def apply_mask(self, action_dist, mask):
        return action_dist * mask
