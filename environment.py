"""
### NOTICE ###

You DO NOT need to upload this file.

"""
import random
from ale_python_interface import ALEInterface

class ALE(object):
    def __init__(self, init_seed, action_repeat, random_init_step, screen_tpye):
        self.ale = ALEInterface()
        self.ale.setInt(b'random_seed', init_seed)
        self.ale.loadROM('./breakout.bin')
        self.action_size = 4
        self.action_repeat = action_repeat
        self.random_init_step = random_init_step

        self.screen = None
        self.reward = 0
        self.terminal = True

    def _step(self, action):
        self.reward = self.ale.act(action)
        if screen_tpye == 0:
            self.screen = self.ale.getScreenRGB()
        else:
            self.screen = self.ale.getScreenGrayScale()
        self.terminal = self.ale.game_over()

    def state(self):
        return self.reward, self.screen, self.terminal

    def act(self, action):
        cumulated_reward = 0
        for _ in range(self.action_repeat):
            self._step(action)
            cumulated_reward += self.reward
            if self.terminal:
                break
        self.reward = cumulated_reward
        return self.state()

    def new_game(self):
        if self.ale.game_over():
            self.ale.reset_game()
            if screen_tpye == 0:
                self.screen = self.ale.getScreenRGB()
            else:
                self.screen = self.ale.getScreenGrayScale()

        self._step(0)

        for _ in range(random.randint(0, self.random_init_step - 1)):
            self._step(0)

        return self.screen
