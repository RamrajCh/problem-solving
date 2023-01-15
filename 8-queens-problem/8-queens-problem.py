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
    eval = []
    # for each chromosome, evaluate using fitness function
    for chromosome in population:
        fit = fitness(chromosome)
        eval.append((chromosome, fit))
    return sorted(eval, key=lambda x: x[1], reverse=True)


def main():
    # Initialize
    population = initialization(10)
    # population = [[7, 7, 2, 0, 2, 6, 6, 6], [7, 1, 0, 6, 7, 5, 6, 7], [1, 1, 1, 2, 3, 5, 4, 0], [1, 2, 3, 7, 5, 3, 5, 6], [2, 6, 2, 1, 0, 4, 2, 2], [1, 1, 4, 5, 7, 6, 1, 7], [3, 0, 1, 6, 2, 6, 3, 2], [2, 5, 1, 7, 0, 4, 0, 3], [2, 2, 0, 7, 7, 0, 5, 3], [1, 2, 6, 6, 2, 6, 1, 2]]
    # population = [[0,4,2,6,1,5,3,7]]
    print("Initial Population")
    print(population)
    
    while True:
        # Randomize a chromosome if it is same to other
        for i in range(10):
            for j in range(i+1, 10):
                if population[i] == population[j]:
                    population[j] = [random.randint(0,7) for _ in range(8)]
                    print("Population changed")
                    
        # Evaluation
        evaluated = evaluation(population)
        print("Evalauation")
        print(evaluated)
        if evaluated[0][1] == 28:
            print(f"Solution: {evaluated[0][0]}")
            break
        
        population = [
            chromosome[0]
            for chromosome in evaluated
        ]
        
        # Selection
        print("Selection")
        selected = population[:2]
        print(selected)
        
        # Crossover
        # Uniform crossover
        print("Crossover")
        crossover = [
            selected[0][:3]+selected[1][3:],
            selected[1][:3]+selected[0][3:]
        ]
        print(crossover)
        
        # Mutation
        print("Mutation")
        mutation = []
        for c in crossover:
            for _ in range(3):
                i = random.randint(0, 7)
                j = random.randint(0, 7)
                c[i] = j
            mutation.append(c)  
        
        print(mutation)
        
        print("New Population")
        population = population[:8] + mutation
        print(population)
    
    
if __name__ == "__main__":
    main()