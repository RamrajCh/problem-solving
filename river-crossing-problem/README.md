# River Crossing Problem

## Problem Statement:

A farmer has a wolf, a chicken, and a bag of corn. He needs to cross a river in a small boat, but the boat can only carry him and one other item at a time. If the wolf is left alone with the chicken, it will eat it. If the chicken is left alone with the corn, it will eat it. How can the farmer get all three across the river safely?

## Concepts for solving the problem:

- Logical reasoning and planning
- Constraint satisfaction
- Iterative problem-solving

### Logical Reasoning and Planning

The first step in solving this problem is to use logical reasoning and planning to determine the steps that the farmer needs to take to get all three items across the river safely. This may involve creating a list of actions and determining the order in which they should be taken.

### Constraint Satisfaction

The next step is to use constraint satisfaction to ensure that all the constraints are satisfied. This means that the farmer must take steps to ensure that the wolf is never left alone with the chicken and that the chicken is never left alone with the corn.

### Iterative Problem-Solving

Finally, the farmer can use iterative problem-solving to work through the problem one step at a time. This might involve starting with one item (such as the chicken) and moving on to the next once the first has been safely crossed.

## Text Algorithm

1. Initialize a variable 'side' to represent the starting side of the river
2. Initialize a variable 'safe' to represent the safe side of the river
3. Move the wolf across the river, if the farmer is on the safe side move the wolf, otherwise, move the farmer and chicken or corn first
4. Move the chicken across the river, if the farmer is on the safe side move the chicken, otherwise, move the farmer and wolf or corn first
5. Move the corn across the river, if the farmer is on the safe side move the corn, otherwise, move the farmer and chicken or wolf first
6. Repeat step 3,4, and 5 until the farmer, wolf, chicken, and corn are all safely on the other side of the river.