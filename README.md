# Q-Learning Maze Solver
A visual representation of a q-learning algorithm solving a maze. The project is being developed with Python and pyglet modules.

Q-learning is a model-free reinforcement learning algorithm. Q-learning is also an unsupervised training algorithm and therefore it does not use examples or previously known references.
As of reinforcement learning, q-learning involves an agent, a set of states and a set of actions. In my application:

  The agent is an entity that wants to reach a target/goal position.
  A state would be the current position of the agent.
  A action would be the agent movement to an adjacent position.
  
Q-learning also involves a reward matrix (the R matrix) and a memory/knowledge matrix with all (state, action) pairs and values possible. Q-learning also features a random exploration chance, a chance to decide the next move randomly, to allow the agent to potentially discover new and more rewarding decisions. Currently, the learning rate (gamma) is fixed at 0.9. But user can choose the size of maze, gamma value, start and end point of the agent from the interface. 

After each step, we adjust: Q(state, action) = R(state, action) + Gamma * Max[Q(next state, all actions)]

# Module Dependencies
-pip install pyglet
-pip install tkinter
-pip install matplotlib
-pip install numpy
-pip install threading
-pip install random
-pip install time

# Usage

![image](https://user-images.githubusercontent.com/46266192/119984662-5416a000-bfca-11eb-803e-c9b5e090e571.png)

-Created Maze: <br>
![image](https://user-images.githubusercontent.com/46266192/119984755-70b2d800-bfca-11eb-84ff-7da9b721d62a.png)
-
![image](https://user-images.githubusercontent.com/46266192/119984787-77d9e600-bfca-11eb-8f84-c0db3f4ae9b0.png)
![image](https://user-images.githubusercontent.com/46266192/119984812-86280200-bfca-11eb-8e30-c15f11ae6dfe.png)










