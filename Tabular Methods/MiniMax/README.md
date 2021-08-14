## Minimax Algorithm
A minimax algorithm is a recursive program written to find the best gameplay that minimizes any tendency to lose a game while maximizing any opportunity to win the game.
We can represent minimax as an exploration of a game tree's nodes to discover the best game move to make. In such a case, the tree's root is the game's current state, where the minimax algorithm got invoked.

![Tree Search]()

The main aim of minimax algorithm is to find the best possible route amongst all possible routes to maximize rewards. 
Two major problems of minimax algorithm is that- 
1. It works only in episodic tasks i.e. a task which terminates after a finite number of steps.
2. Due to full sweep or deep search, it's time complexity is very high and its memory inefficient.
