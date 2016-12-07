"""
### NOTICE ###

You DO NOT need to upload this file.

"""
import sys, random
import tensorflow as tf

from agent import Agent
from environment import ALE

tf.set_random_seed(123)
random.seed(123)

seed = int(sys.argv[1])

with tf.Session() as sess:

    # Init agent
    agent = Agent(sess)
    action_repeat, random_init_step, screen_tpye = agent.getSetting()

    # Init env
    env = ALE(seed, action_repeat, random_init_step, screen_tpye)

    screen = env.new_game()
    
    current_reward = 0
    for _ in range(5000):
        action = agent.play(screen)
        reward, screen, terminal = env.act(action)
        current_reward += reward
        if terminal:
            break
    print(seed, current_reward)
