# 8-queens problem

The 8 queens problem is a classic problem in computer science and artificial intelligence. The goal is to place 8 queens on a standard chessboard such that no two queens are attacking each other. This means that no two queens can be placed in the same row, column, or diagonal. The problem can be solved using a genetic algorithm by representing each possible placement of the queens on the board as a chromosome, and then using genetic operators such as crossover and mutation to generate new solutions. The goal is to find a chromosome (or set of chromosomes) that represents a valid solution to the problem.

---

## Algorithm for solving using genetics algorithm

1. Initialization: Create an initial population of N chromosomes, each representing a possible arrangement of the 8 queens on the chessboard. The chromosomes can be generated randomly or using some heuristic method.

2. Evaluation: Evaluate the fitness of each chromosome in the population. The fitness function should assign a higher score to chromosomes that have a higher number of non-attacking queens.

3. Selection: Select the best-performing chromosomes to form the mating pool for the next generation. Techniques such as tournament selection or roulette wheel selection can be used.

4. Crossover: Create new chromosomes by combining the genetic information of chromosomes in the mating pool. Crossover operators such as one-point crossover or uniform crossover can be used.

5. Mutation: Introduce small random changes to some of the chromosomes in the new generation. Mutation operators such as bit-flip or swap mutation can be used.

6. Repeat steps 2-5 for a specified number of generations or until a satisfactory solution is found.

The best chromosome from the final population represents a solution to the 8 queens problem.