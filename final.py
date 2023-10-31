import random

# Define items with weights and values
items = [(20, 6), (30, 5), (60, 8), (90, 7), (50, 6), (70, 9),
         (30, 4), (30, 5), (70, 4), (20, 9), (20, 2), (60, 1)]

# Knapsack capacity
knapsack_capacity = 250

# Population size
population_size = 100

# Number of generations
num_generations = 50

# Mutation rate
mutation_rate = 0.1

# Tournament size for selection
tournament_size = 3

# Function to generate a random genome (representing item selection)
def generate_genome():
    return [random.randint(0, 1) for _ in range(len(items))]

# Function to calculate genome fitness
def calculate_fitness(genome):
    total_weight = 0
    total_value = 0
    
    for i, item in enumerate(items):
        if genome[i] == 1:
            total_weight += item[0]
            total_value += item[1]
    
    if total_weight > knapsack_capacity:
        return 0
    
    return total_value

# Function for tournament selection
def select_parent(population):
    winner = random.choice(population)
    for i in range(tournament_size - 1):
        competitor = random.choice(population)
        if calculate_fitness(competitor) > calculate_fitness(winner):
            winner = competitor
    return winner

# Function for one-point crossover
def crossover(parent1, parent2):
    child = []
    for i in range(len(parent1)):
        if random.random() < 0.5:
            child.append(parent1[i])
        else:
            child.append(parent2[i])
    return child

# Function for mutation
def mutate(genome):
    for i in range(len(genome)):
        if random.random() < mutation_rate:
            genome[i] = 1 - genome[i]
    return genome

#function for displying selected items 
def dispRes(result, items):
    for i in range(len(result)):
        if result[i] == 1:
            item = items[i]
            print("Item " + str(i) + ": priority of the item -> " + str(item[1]) + " , weight of the item -> " + str(item[0]))

# Generate an initial population
population = [generate_genome() for _ in range(population_size)]

# Evolve the population through generations
for generation in range(num_generations):
    # Evaluate fitness for each genome
    fitnesses = [calculate_fitness(genome) for genome in population]

    # Select parents
    parent1 = select_parent(population)
    parent2 = select_parent(population)

    # Crossover
    child = crossover(parent1, parent2)

    # Mutate
    child = mutate(child)

    # Evaluate child fitness
    child_fitness = calculate_fitness(child)
    
    # Replace a random individual with the child
    replace_index = random.randint(0, population_size - 1)
    population[replace_index] = child

# Find the best genome in the final population
best_fitness = max(fitnesses)
best_genome = population[fitnesses.index(best_fitness)]

# Print the final results
print("Best fitness:", best_fitness)
print("Best genome:", best_genome)
print("\nBest items selected to pack : ")
dispRes(best_genome, items)