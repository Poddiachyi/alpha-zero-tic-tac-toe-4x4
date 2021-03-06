import numpy as np

class RandomAgent(object):

    def __init__(self, action_size):
        self.action_size = action_size

    def act(self, state, mask):
        action_dist = np.random.dirichlet(np.ones(self.action_size), size=1).ravel()
        action_dist = self.apply_mask(action_dist, mask)
        return action_dist.argmax()


    def apply_mask(self, action_dist, mask):
        return action_dist * mask
