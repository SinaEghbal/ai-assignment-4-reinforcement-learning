# qlearningAgents.py
# ------------------
# Licensing Information: Please do not distribute or publish solutions to this
# project. You are free to use and extend these projects for educational
# purposes. The Pacman AI projects were originally developed at UC Berkeley,
# primarily by John DeNero (denero@cs.berkeley.edu) and Dan Klein (klein@cs.berkeley.edu).
#
# Further modifications and porting to Python 3 by Miquel Ramirez (miquel.ramirez@gmail.com),
# March and April 2016

""" Student Details
    Student Name:
    Student number:
    Date:
"""
from copy import deepcopy

from game import *
from learningAgents import ReinforcementAgent
from featureExtractors import *

import random,util,math

from util import Counter


class QLearningAgent(ReinforcementAgent):
    """
      Q-Learning Agent

      Functions you should fill in:
        - getQValue
        - getAction
        - getValue
        - getPolicy
        - update

      Instance variables you have access to
        - self.epsilon (exploration prob)
        - self.alpha (learning rate)
        - self.discount (discount rate)

      Functions you should use
        - self.getLegalActions(state)
          which returns legal actions
          for a state
    """
    def __init__(self, **args):
        "You can initialize Q-values here..."
        ReinforcementAgent.__init__(self, **args)
        self.values = Counter()
        # for state in self.getStates():
        #     a = None


    def getQValue(self, state, action):
        """
          Returns Q(state,action)
          Should return 0.0 if we never seen
          a state or (state,action) tuple
        """
        if (state, action) not in self.values:
            self.values[(state, action)]
        return self.values[(state, action)]


    def getValue(self, state):
        """
          Returns max_action Q(state,action)
          where the max is over legal actions.  Note that if
          there are no legal actions, which is the case at the
          terminal state, you should return a value of 0.0.
        """
        value = None
        for action in self.getLegalActions(state):
            currentValue = self.getQValue(state, action)
            if not value or value < currentValue:
                value = currentValue
        if not value:
            return 0
        return value

    def getPolicy(self, state):
        """
          Compute the best action to take in a state.  Note that if there
          are no legal actions, which is the case at the terminal state,
          you should return None.
        """
        return self.getAction(state)

    def getAction(self, state):
        """
          Compute the action to take in the current state.  With
          probability self.epsilon, we should take a random action and
          take the best policy action otherwise.  Note that if there are
          no legal actions, which is the case at the terminal state, you
          should choose None as the action.

          HINT: You might want to use util.flipCoin(prob)
          HINT: To pick randomly from a list, use random.choice(list)
        """
        # Pick Action
        legalActions = self.getLegalActions(state)
        if not legalActions:
            return None
        elif util.flipCoin(self.epsilon):
            return random.choice(legalActions)
        else:
            return self.exploit(legalActions, state)

    def exploit(self, legalActions, state):
        action = None
        actionList = list()
        for currentAction in legalActions:
            currentQValue = self.getQValue(state, currentAction)
            if not actionList or \
                     currentQValue > actionList[0][0]:
                actionList = list()
                actionList.append((currentQValue, currentAction))
            elif currentQValue == actionList[0][0]:
                actionList.append((currentQValue, currentAction))
            action = random.choice(actionList)
        if not action:
            return action
        return action[1]

    def update(self, state, action, nextState, reward):
        """
          The parent class calls this to observe a
          state = action => nextState and reward transition.
          You should do your Q-Value update here

          NOTE: You should never call this function,
          it will be called on your behalf
        """
        self.values[(state, action)] +=\
        self.alpha * (reward + self.discount *
                      self.getValue(nextState) - self.getQValue(state, action))

class PacmanQAgent(QLearningAgent):
    "Exactly the same as QLearningAgent, but with different default parameters"

    def __init__(self, epsilon=0.05,gamma=0.8,alpha=0.2, numTraining=0, **args):
        """
        These default parameters can be changed from the pacman.py command line.
        For example, to change the exploration rate, try:
            python pacman.py -p PacmanQLearningAgent -a epsilon=0.1

        alpha    - learning rate
        epsilon  - exploration rate
        gamma    - discount factor
        numTraining - number of training episodes, i.e. no learning after these many episodes
        """
        args['epsilon'] = epsilon
        args['gamma'] = gamma
        args['alpha'] = alpha
        args['numTraining'] = numTraining
        self.index = 0  # This is always Pacman
        QLearningAgent.__init__(self, **args)

    def getAction(self, state):
        """
        Simply calls the getAction method of QLearningAgent and then
        informs parent of action for Pacman.  Do not change or remove this
        method.
        """
        action = QLearningAgent.getAction(self,state)
        self.doAction(state,action)
        return action


class ApproximateQAgent(PacmanQAgent):
    """
       ApproximateQLearningAgent

       You should only have to overwrite getQValue
       and update.  All other QLearningAgent functions
       should work as is.
    """
    def __init__(self, extractor='IdentityExtractor', **args):
        self.featExtractor = util.lookup(extractor, globals())()
        PacmanQAgent.__init__(self, **args)
        # self.feature = Counter()
        self.weights = Counter()

    def getQValue(self, state, action):
        """
          Should return Q(state,action) = w * featureVector
          where * is the dotProduct operator
        """
        features = self.featExtractor.getFeatures(state, action)
        val = 0
        for feature, feature_val in features.items():
            if feature not in self.weights:
                self.weights[feature] = 0#random.random()
            val += feature_val * self.weights[feature]
        return val

    def update(self, state, action, nextState, reward):
        """
           Should update your weights based on transition
        """
        correction = reward + self.discount * self.getValue(nextState) - self.getQValue(state, action)
        features = self.featExtractor.getFeatures(state, action)
        for feature, val in features.items():
            self.weights[feature] += self.alpha * correction * val

    def final(self, state):
        "Called at the end of each game."
        # call the super-class final method
        PacmanQAgent.final(self, state)
        # print(self.episodesSoFar)

        # did we finish training?
        if self.episodesSoFar == self.numTraining:
            pass
            # you might want to print your weights here for debugging
            # print(self.weights)
