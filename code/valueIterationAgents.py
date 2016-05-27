# valueIterationAgents.py
# -----------------------
# Licensing Information: Please do not distribute or publish solutions to this
# project. You are free to use and extend these projects for educational
# purposes. The Pacman AI projects were originally developed at UC Berkeley,
# primarily by John DeNero (denero@cs.berkeley.edu) and Dan Klein (klein@cs.berkeley.edu).
#
# Further modifications and porting to Python 3 by Miquel Ramirez (miquel.ramirez@gmail.com),
# March and April 2016

""" Student Details
    Student Name: Sina Eghbal
    Student number: u5544352
    Date: 27 May 2016
"""
import numbers

import mdp, util

from learningAgents import ValueEstimationAgent

class ValueIterationAgent(ValueEstimationAgent):
    """
        * Please read learningAgents.py before reading this.*

        A ValueIterationAgent takes a Markov decision process
        (see mdp.py) on initialization and runs value iteration
        for a given number of iterations using the supplied
        discount factor.
    """
    def __init__(self, mdp, discount = 0.9, iterations = 100):
        """
          Your value iteration agent should take an mdp on
          construction, run the indicated number of iterations
          and then act according to the resulting policy.

          Some useful mdp methods you will use:
              mdp.getStates()
              mdp.getPossibleActions(state)
              mdp.getTransitionStatesAndProbs(state, action)
              mdp.getReward(state, action, nextState)
        """
        self.mdp = mdp
        self.discount = discount
        self.iterations = iterations
        self.values = util.Counter() # A Counter is a dict with default 0
        self.states = self.mdp.getStates()
        self.terminal = self.states.pop(0)
        # a = self.mdp.getStates()
        for x, y in self.states:
            thisState = self.mdp.grid.data[x][y]
            if isinstance(thisState, numbers.Number):
                self.values[(x, y)] = thisState
            else:
                self.values[(x, y)]

        for i in range(0, iterations):
            for currentState in self.states:
                if self.mdp.isTerminal(currentState):
                    continue
                max = (None, None, None)
                for currentAction in self.mdp.getPossibleActions(currentState):
                   currentProbability = 0
                   # max = (None, None, None)
                   for transition, probability \
                           in self.mdp.getTransitionStatesAndProbs(currentState, currentAction):
                       currentProbability += probability * self.getValue(transition)
                   currentProbability *= discount
                   if not max[0] or currentProbability > max[0]:
                       max = (currentProbability, currentAction, transition)
                currentProbability = max[0] + self.mdp.getReward(currentState, max[1], max[2])
                self.values[currentState] = (self.getValue(currentState) * i + currentProbability)/ (i+1)

    def getValue(self, state):
        """
          Return the value of the state (computed in __init__).
        """
        return self.values[state]


    def getQValue(self, state, action):
        """
          The q-value of the state action pair
          (after the indicated number of value iteration
          passes).  Note that value iteration does not
          necessarily create this quantity and you may have
          to derive it on the fly.
        """
        qValue = 0
        for action, probability in self.mdp.getTransitionStatesAndProbs\
                    (state,action):
            qValue += probability * self.getValue(action)
        return qValue

    def getPolicy(self, state):
        """
          The policy is the best action in the given state
          according to the values computed by value iteration.
          You may break ties any way you see fit.  Note that if
          there are no legal actions, which is the case at the
          terminal state, you should return None.
        """
        max = (None, None)
        for action in self.mdp.getPossibleActions(state):
            x, y = state
            cell = None
            if action == 'north':
                cell = (x, y+1)
            elif action == 'south':
                cell = (x, y-1)
            elif action == 'east':
                cell = (x+1, y)
            elif action == 'west':
                cell = (x-1, y)
            elif action == 'exit':
                return action
            if cell in self.values:
                currentValue = self.getValue(cell)
                if not max[1] or max[1] < currentValue:
                    max = (action, currentValue)
        return max[0]


    def getAction(self, state):
        "Returns the policy at the state (no exploration)."
        return self.getPolicy(state)
