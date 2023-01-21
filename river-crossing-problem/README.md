# River Crossing Problem

## Introduction

The River Crossing Problem is a classic AI problem in which a farmer needs to transport a wolf, a goat, and a cabbage across a river using a boat. However, the farmer can only take one item across the river at a time, and if left alone, the wolf will eat the goat, and the goat will eat the cabbage. The goal is to find a sequence of steps that will safely transport all items across the river.

## Constraints
- The farmer is the only one who can operate the boat.
- The farmer cannot leave the goat alone with the cabbage or the goat alone with the wolf.
- The boat can only carry the farmer and one other item.

## States
The states of the problem are represented by the location of the farmer, the wolf, the goat, and the cabbage. The location can be either on the left bank or the right bank of the river. Each location is represented by a digit, 0 represents on left bank and 1 represents on right bank of the river.

## Initial State
The initial state of the problem is represented by (0,0,0,0) where the farmer, the wolf, the goat, and the cabbage all being on the left bank of the river.

## Goal State
The goal state of the problem is represented by (1,1,1,1) where the farmer, the wolf, the goat, and the cabbage all being on the right bank of the river.

## Actions
The actions of the problem are represented by the items that the farmer is taking across the river. The farmer can take any one of the following items across the river: the wolf, the goat, or the cabbage.

## Algorithm for State Space Search

1. Initialize a queue with the initial state of the problem, represented by (0,0,0,0)
2. While the queue is not empty, do the following:
    - Dequeue the first state in the queue
    - Check if the current state is the goal state, represented by (1,1,1,1)
    - If it is, return the solution path.
    - Else, generate all possible new states by applying the actions (moving the farmer and one other item across the river) and make sure to check the constraints of the problem.
3. Add all new states to the queue and mark them as visited.
4. If the queue is empty and the goal state has not been reached, return "No solution found"