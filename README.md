# Artificial Intelligence

## Assignment-1 Search Algorithms

Suppose there is a maze in which the agent can move one tile at a time, horizontally or vertically. It starts at a given starting tile and searches for the goal tile. Each action costs 1 movement point. Additionally, the destination tiles may take additional movement points as stated on the tiles. The maze also has walls that are represented with ‘-’ and cannot be passed through. The agent can sense the walls and does not consider the action to go towards them.</br>
**For any given maze**, you are expected to program an agent (in PYTHON) to perform:
* breadth first search
* depth first search
* uniform cost search, for which the costs will be taken as the total cost in movement points:
  * not taking extra move points into consideration
  * taking extra move points into consideration
* A* search using two sensible distance heuristics that you determine and which are
  * inadmissable
  * admissable
  
For the report, questions below should be answered.
* Explain how you decide on the heuristics you determine.</br>
* Comment on your findings with each approach:
  * Can the agent find all possible paths from the starting tile to the goal tile? How can this be made possible?</br>
  * Can the agent find the path from the starting tile to the goal tile with minimum number of actions? If so, how? If not, what are the causes?</br>
  * Can the agent find the path that it reaches the goal tile with the minimum cost in movement points? If so, how? If not, what are the causes?</br>
  * What would happen if additional movement points were negative?</br>
  
## Assignment-2 Bayesian Networks

![alt text](https://github.com/nuwandda/Artificial-Intelligence/blob/master/Bayesian-Networks/graph.png "Logo Title Text 1")

For the given Bayesian Network, calculate **P(+D), P(+D,-A), P(+E|-B), P(+A|+D,-E) and P(+B,-E|+A)** using:

* Complete enumeration
* Variable elimination (if possible)
* Monte Carlo technique

And implement the Monte Carlo Technique in Python. For the other techniques, a report is included with the answers.
