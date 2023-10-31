import random

# Define items with weights and values
items = [(20, 6), (30, 5), (60, 8), (90, 7), (50, 6), (70, 9),  
         (30, 4), (30, 5), (70, 4), (20, 9), (20, 2), (60, 1)]

# Knapsack capacity   
capacity = 250

# Population size
population_size = 100

# Number of generations  
num_generations = 50

# Mutation rate
mutation_rate = 0.1

# Tournament size for selection
tournament_size = 3

# Function to generate a random genome
def generate_individual():
    return [random.randint(0, 1) for _ in range(len(items))]

# Function to calculate individual fitness
def calculate_fitness(individual):
    total_weight = 0
    total_value = 0
    
    for i, item in enumerate(items):
        if individual[i] == 1:
            total_weight += item[0]
            total_value += item[1]
    
    if total_weight > capacity:
        return 0
    
    return total_value

# Function for tournament selection
def select_parent(population):
    parent = random.choice(population)
    for _ in range(tournament_size - 1):
        competitor = random.choice(population)
        if calculate_fitness(competitor) > calculate_fitness(parent):
            parent = competitor
    return parent

# Function for one-point crossover
def crossover(parent1, parent2):
    crossover_point = random.randint(1, len(items) - 1)
    child = parent1[:crossover_point] + parent2[crossover_point:]
    return child

# Function for mutation       
def mutate(individual):
    for i in range(len(individual)):
        if random.random() < mutation_rate:
            individual[i] = 1 - individual[i]
    return individual

# Generate an initial population
population = [generate_individual() for _ in range(population_size)]

# Evolve the population
for _ in range(num_generations):
    # Evaluate fitness for each individual
    fitness_scores = [calculate_fitness(individual) for individual in population]
    
    # Select parents
    parent1 = select_parent(population)
    parent2 = select_parent(population)
    
    # Crossover
    child = crossover(parent1, parent2)
    
    # Mutate
    child = mutate(child)
    
    # Evaluate child fitness
    child_fitness = calculate_fitness(child)
    
    # Replace the worst 50% of the population with the child
    sorted_population = [x for _, x in sorted(zip(fitness_scores, population), reverse=True)]
    num_to_replace = population_size // 2
    for i in range(num_to_replace):
        sorted_population[i] = child

    population = sorted_population


# Find the best individual in the final population
best_fitness = max(fitness_scores)
best_individual = population[fitness_scores.index(best_fitness)]

# Print the final results
print("Best fitness:", best_fitness)
print("Best individual:", best_individual)

