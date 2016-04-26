<h3>Q-learning </h3>

<p>Note that your value iteration agent does not actually learn from experience.&nbsp; Rather, it ponders its MDP model to arrive at a complete policy before ever interacting with a real environment.&nbsp; When it does interact with the environment, it simply follows the precomputed policy (e.g. it becomes a reflex agent).  This distinction may be subtle in a simulated environment like a Gridword, but it's very important in the real world, where the real MDP is not available.&nbsp; </p>

<p><strong><em>Question 4 (5 points) </em></strong> You will now write a Q-learning agent, which does very little on construction, but instead learns by trial and error from interactions with the environment through its <code>update(state, action, nextState, reward)</code> method.&nbsp; A stub of a Q-learner is specified in <code>QLearningAgent</code> in <code><a href="docs/qlearningAgents.html">qlearningAgents.py</a></code>, and you can select it with the option <code>'-a q'</code>.  For this question, you must implement the <code>update</code>, <code>getValue</code>, <code>getQValue</code>, and <code>getPolicy</code> methods.

<p><em>Note:</em> For <code>getPolicy</code>, you should break ties randomly for better behavior. The <code>random.choice()</code> function will help.  In a particular state, actions that your agent <em>hasn't</em> seen before still have a Q-value, specifically a Q-value of zero, and if all of the actions that your agent <em>has</em> seen before have a negative Q-value, an unseen action may be optimal.</p>

<p><em>Important:</em> Make sure that in your <code>getValue</code> and <code>getPolicy</code> functions, you only access Q values by calling <code>getQValue</code> . This
  abstraction will be useful for question 9 when you
  override <code>getQValue</code> to use features of state-action
  pairs rather than state-action pairs directly.

<p>With the Q-learning update in place, you can watch your Q-learner learn under manual control, using the keyboard:

<pre>python gridworld.py -a q -k 5 -m</pre>

Recall that <code>-k</code> will control the number of episodes your agent gets to learn.
Watch how the agent learns about the state it was just in, not the one it moves to, and "leaves learning in its wake."

Hint: to help with debugging, you can turn off noise by using the <code>--noise 0.0</code> parameter (though this obviously makes Q-learning less interesting). If you manually steer Pacman north and then east along the optimal path for four episodes, you should see the following Q-values:
<br>
<br>
<center>
<img src="q-learning.png" width="50%" alt="QLearning"/>
</center>
<br>

<p><em>Grading:</em> We will run your Q-learning agent on an example of our own and check that it learns the same Q-values and policy as our reference implementation when each is presented with the same set of examples.

<p><strong><em>Question 5 (2 points) </em></strong> Complete your Q-learning agent by implementing epsilon-greedy action selection in <code>getAction</code>, meaning it chooses random actions an epsilon fraction of the time, and follows its current best Q-values otherwise.

<pre>python gridworld.py -a q -k 100 </pre>

Your final Q-values should resemble those of your value iteration agent, especially along well-traveled paths.  However, your average returns will be lower than the Q-values predict because of the random actions and the initial learning phase.

<p> You can choose an element from a list uniformly at random by calling the <code>random.choice</code> function.
You can simulate a binary variable with probability <code>p</code>
of success by using <code>util.flipCoin(p)</code>, which returns <code>True</code> with
probability <code>p</code> and <code>False</code> with probability <code>1-p</code>.

<p><strong><em>Question 6 (1 points) </em></strong> First, train a completely random Q-learner with the default learning rate on the noiseless BridgeGrid for 50 episodes and observe whether it finds the optimal policy.

<pre>python gridworld.py -a q -k 50 -n 0 -g BridgeGrid -e 1</pre>

Now try the same experiment with an epsilon of 0. Is there an epsilon and a learning rate for which it is highly likely (greater than 99%) that the optimal policy will be learned after 50 iterations? <code>question6()</code> in <code><a href="docs/analysis.html">analysis.py</a></code> should return EITHER a 2-item tuple of <code>(epsilon, learning rate)</code> OR the string <code>'NOT POSSIBLE'</code> if there is none.  Epsilon is controlled by <code>-e</code>, learning rate by <code>-l</code>.

<p><em>Note:</em> Your response should be not depend on the exact
   tie-breaking mechanism used to choose actions. This means your
   answer should be correct even if for instance we rotated the entire
   bridge grid world 90 degrees.

<p><strong><em>Question 7 (1 point) </em></strong> With no additional code, you should now be able to run a Q-learning crawler robot:

<pre>python crawler.py</pre>

If this doesn't work, you've probably written some code too specific to the <code>GridWorld</code> problem and you should make it more general to all MDPs.

<p>This will invoke the crawling robot from class using your Q-learner.&nbsp; Play around with the various learning parameters to see how they affect the agent's policies and actions.&nbsp;&nbsp; Note that the step delay is a parameter of the simulation, whereas the learning rate and epsilon are parameters of your learning algorithm, and the discount factor is a property of the environment. &nbsp;

<p><em>Grading:</em> We give you a point for free here, but play around with the crawler anyway!
