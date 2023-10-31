import random

# Define the box weights and values
boxes = [(20, 6), (30, 5), (60, 8), (90, 7), (50, 6), (70, 9),  
         (30, 4), (30, 5), (70, 4), (20, 9), (20, 2), (60, 1)]

# Knapsack capacity   
capacity = 250

# Population size
pop_size = 100

# Number of generations  
num_generations = 50

# Mutation rate
mutation_rate = 0.1

# Tournament size for selection
tournament_size = 3

# Function to generate a random genome
def generate_genome():
    return [random.randint(0,1) for _ in range(len(boxes))]

# Function to calculate genome fitness
def fitness(genome):
    weight = 0
    value = 0
    
    for i, item in enumerate(boxes):
        if genome[i] == 1:
            weight += item[0]
            value += item[1]
    
    if weight > capacity:
        return 0
    
    return value

# Function for tournament selection
def selection(pop):
    winner = random.choice(pop)
    for i in range(tournament_size-1):
        competitor = random.choice(pop)
        if fitness(competitor) > fitness(winner):
            winner = competitor
    return winner

# Function for crossover
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
            genome[i] = random.randint(0,1)
    return genome

# Generate initial population
pop = [generate_genome() for _ in range(pop_size)]

# Evolve population
for i in range(num_generations):
    
    # Evaluate fitness
    fitnesses = {}
    for genome in pop:
        fitnesses[tuple(genome)] = fitness(genome)
        
    # Select parents
    parent1 = selection(pop)
    parent2 = selection(pop)
    
    # Crossover
    child = crossover(parent1, parent2)
    
    # Mutate
    child = mutate(child)
    
    # Evaluate child fitness
    fitnesses[tuple(child)] = fitness(child)
    
    # Add child to population  
    pop.append(child)
    
    # Cull population
    # pop = sorted(pop, key=lambda genome: fitnesses[tuple(genome)], reverse=True)[:pop_size]
    # Cull population
    pop_size = len(pop)
    next_pop_size = pop_size // 2
    pop = sorted(pop, key=lambda genome: fitnesses[tuple(genome)], reverse=True)[:next_pop_size]
        
    
# Print final results
print(fitnesses[tuple(pop[0])])
print(pop[0])
