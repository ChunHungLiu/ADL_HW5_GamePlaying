"""
### NOTICE ###

You need to upload this file.
You can add any function you want in this file.

"""
class Agent(object):
    def __init__(self, env, sess):
        self.sess = sess
        min_action_set = env.getMinimalActionSet()
        self.build_dqn()

    def build_dqn(self):
        """
            # TODO
        """
        self.saver = tf.train.Saver(tf.trainable_variables())
        self.saver.restore(sess, './best_model.ckpt')

    # return 0 for RGB; return 1 for GrayScale
    def getSetting(self):
        """
            # TODO
            You can only modify these three parameters.
            Adding any other parameters are not allowed.
        """
        action_repeat = 4
        random_init_step = 30
        screen_tpye = 0
        return action_repeat, random_init_step, screen_tpye

    """
     The "action" is your DQN argmax ouput.
     The "min_action_set" is used to transform DQN argmax ouput into real action number.
     For example,
         DQN output = [0.1, 0.2, 0.1, 0.6]
         argmax = 3
         min_action_set = [0, 1, 3, 4]
         real action number = 4
    """
    def play(self, screen):
        """
        # TODO
        """
        return min_action_set[action]
