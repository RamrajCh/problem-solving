import random

def initialization(N):
    return([
        [random.randint(0,7) for _ in range(8)]
        for _ in range(N)
    ])

def non_attacking(q1, q2, c1, c2):
    # check if they are in same column
    if q1 != q2 and abs(q1-q2) != abs(c1-c2):
        return True
    return False

def fitness(chromosome):
    fit = 0
    # iterating over each queen, lets find the number of non-attacking queens and add 1 each time.
    for c1 in range(8):
        for c2 in range(c1+1, 8):
            if non_attacking(chromosome[c1], chromosome[c2], c1, c2):
                fit += 1
    return fit

def evaluation(population):
    # for each chromosome, evaluate using fitness function
    for chromosome in population:
        fit = fitness(chromosome)
        print(chromosome, fit)

    ...

def main():
    # Initialize
    # population = initialization(10)
    # print(population)
    population = [[0,4,2,6,1,5,3,7], [7, 7, 2, 0, 2, 6, 6, 6], [7, 1, 0, 6, 7, 5, 6, 7], [1, 1, 1, 2, 3, 5, 4, 0], [1, 2, 3, 7, 5, 3, 5, 6], [2, 6, 2, 1, 0, 4, 2, 2], [1, 1, 4, 5, 7, 6, 1, 7], [3, 0, 1, 6, 2, 6, 3, 2], [2, 5, 1, 7, 0, 4, 0, 3], [2, 2, 0, 7, 7, 0, 5, 3], [1, 2, 6, 6, 2, 6, 1, 2]]
    # population = [[0,4,2,6,1,5,3,7]]
    
    # Evaluation
    evaluation(population)
    
    # Selection
    
    # Crossover
    
    # Mutation
    
if __name__ == "__main__":
    main()