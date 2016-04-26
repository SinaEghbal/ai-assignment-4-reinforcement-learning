## Introduction

In this project, you will implement Value Iteration and Q-learning. You will test your agents first on ```Gridworld``` (from class), then apply them to a simulated robot controller (```Crawler```) and ```Pacman```.

The code for this project contains the following files, which are available in the
folder ```code``` of this repository.

### Files you will edit and you NEED to submit

- [```valueIterationAgents.py```](../master/code/valueIterationAgents.py) - A
Value Iteration agent for solving known Markov Decision Processes (*MDPs*)

- [```qlearningAgents.py```](../master/code/qlearningAgents.py) - Q-Learning agents
for ```GridWorld```, ```Crawler``` and ```PacMan```.

- [```analysis.py```](../master/code/analysis.py) - A file to put your answers to
questions given in the handout.

### Files you SHOULD read but NOT edit

- [```mdp.py```](../master/code/mdp.py) - Defines methods on general *MDPs*.

- [```learningAgents.py```](../master/code/learningAgents.py) - Defines the base
classes ```ValueEstimationAgent``` and ```QLearningAgent```, which your agents
will extend.

- [```util.py```](../master/code/util.py) - Utilities, including ```util.Counter```,
which is particularly useful for Q-learners.

- [```gridworld.py```](../master/code/gridworld.py) - The ```GridWorld``` implementation.

- [```featureExtractors.py```](../master/code/featureExtractors.py) - Classes for
extracting features on _(state,action)_ pairs. Used for the approximate Q-Learning
agent (in [```qlearningAgents.py```](../master/code/qlearningAgents.py)).

### Files you CAN ignore

- [```environment.py```](../master/code/environment.py) - Abstract class for general
reinforcement learning environments. Used by [```gridworld.py```](../master/code/gridworld.py).

- [```graphicsGridworldDisplay.py```](../master/code/graphicsGridworldDisplay.py) -
 ```Gridworld``` graphical display.

- [```graphicsUtils.py```](../master/code/graphicsUtils.py) - Assorted graphics
utilities.

- [```textGridworldDisplay.py```](../master/code/textGridworldDisplay.py) - Plug-in
for the ```Gridworld``` text interface.

- [```crawler.py```](../master/code/crawler.py) - The ```Crawler``` code and test
harness. You will run this but not edit it.

- [```graphicsCrawlerDisplay.py```](../master/code/graphicsCrawlerDisplay.py) - 
Graphical display of the crawler robot.

### What to Submit


You will fill in portions of <code><a href="docs/valueIterationAgents.html">valueIterationAgents.py</a></code>, <code><a href="docs/qlearningAgents.html">qlearningAgents.py</a></code>, and <code><a href="docs/analysis.html">analysis.py</a></code> during the assignment. You should submit **only** these files.  Please don't change any others.</p>

### Evaluation

Your code will be run against an automated testing suite to determine its technical
correctness. Please <em>do not</em> change the names of any provided functions or classes
within the code, or you will wreak havoc on the automated tester. If your code works
correctly on one or two of the provided examples but doesn't get full credit from the auto
tester, you most likely have a subtle bug that breaks one of our more thorough test cases;
you will need to debug more fully by reasoning about your code and trying small examples of
your own. That said, bugs in the auto tester are not impossible, so please do contact the
relevant staff if you believe that there has been an error in the grading.


### Getting Help

If you find yourself stuck on something, contact the lab tutors (David Nalder and
Leon Sheldon) for help. Wattle forums are there for your support; please use them.
We want these projects to be rewarding and instructional, not frustrating and
demoralising.  But, we don't know when or how to help unless you ask.
