import argparse
import random

# 8 Queens
# Default values:
default_population  = 100
default_mutation    = 0.1
default_generations = 1000


def generate_individual():
    return [random.randint(0, 7) for _ in range(8)]


# fitness = max conflicting pairs (28) - individual conflicting pairs
def fitness(individual):
    conflicts = 0
    for i in range(len(individual)):
        for j in range(i + 1, len(individual)):
            if individual[i] == individual[j] or abs(individual[i] - individual[j]) == j - i:
                conflicts += 1
    return 28 - conflicts


# pick best half to breed
def select_population(population):
    sorted_population = sorted(population, key=lambda x: fitness(x), reverse=True)
    return sorted_population[:len(population) // 2]


# picks a point between 1 and 6, 
# splits the two parents at that point, 
# combines and returns a newborn 8-queens solution
def crossover(parent1, parent2):
    point = random.randint(1, len(parent1) - 2)
    return parent1[:point] + parent2[point:]


# gamma radiation mutation machine
# picks a random queen column and changes it
def mutate(individual, mutation_rate):
    if random.random() < mutation_rate:
        i = random.randint(0, len(individual) - 1)
        individual[i] = random.randint(0, 7)
    return individual


# the Function
def genetic_algorithm(population_size, mutation_rate, generations):
    population = [generate_individual() for _ in range(population_size)]
    
    for generation in range(generations):
        for individual in population:
            if fitness(individual) == 28:
                return individual, generation  # Solution found
        
        selected = select_population(population)
        next_population = selected[:]
        
        while len(next_population) < population_size:
            parent1, parent2 = random.sample(selected, 2)
            child = crossover(parent1, parent2)
            child = mutate(child, mutation_rate)
            next_population.append(child)
        
        population = next_population
    
    return None, generations  # No solution found


def main():
    parser = argparse.ArgumentParser(description="Solve 8-Queens problem using Genetic Algorithm.")

    parser.add_argument("-p", "--population_size", 
        type=int, 
        default=default_population, 
        help=f"Size of the population. Default is {default_population}.")

    parser.add_argument("-m", "--mutation_rate", 
        type=float, 
        default=default_mutation, 
        help=f"Mutation rate (0-1). Default is {default_mutation}.")

    parser.add_argument("-g", "--generations", 
        type=int, 
        default=default_generations, 
        help=f"Number of generations to run. Default is {default_generations}.")

    args = parser.parse_args()


    # Run the algo
    solution, generation = genetic_algorithm(args.population_size, args.mutation_rate, args.generations)


    if solution:
        print(f"Solution found in generation {generation}: {solution}")
    else:
        print("No solution found within generation limit.")


if __name__ == "__main__":
    main()
