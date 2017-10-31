import itertools
import random

import settings
from basics import initiator
from basics import vector


# Tuple_of_gene_and_fitness -> List_of_gene
# Evolve the genes so that parts of gene with a higher fitness will
# be likelier to appear in the next generation's overall gene pool
# Also introduces potential mutation to each single acc_vector in each gene
# WARNING: if there are less than 2 non-zero fitness scores, this generation goes extinct,
# and evolution returns a new random generation

def evolve_all(togaf):



    gene_tuple = togaf[0]

    fitness_tuple = togaf[1]

    evolved_gene_list = []

    if count_not_zeros(fitness_tuple) < 2:
        return initiator.initiate_random_log(settings.POPULATION, settings.GENE_LENGTH)

    for i in range(0, len(gene_tuple)):

        parents_genes = get_parents_gene(gene_tuple, fitness_tuple)

        crossed_gene = crossover_gene(parents_genes)

        evolved_gene = mutate_gene(crossed_gene)

        evolved_gene_list.append(evolved_gene)

    return evolved_gene_list

# count the number of non-zero fitness scores in lof
def count_not_zeros(lof):
    num = 0
    for fitness in lof:
        if fitness != 0:
            num += 1
    return num


# gene_tuple, accumulated_fitness_tuple -> tuple of 2 parent genes
# This selection function favors parent gene with higher fitness score,
# and it prevents selecting both genes from the same parent
def get_parents_gene(genes, fitness_tuple):

    accumulated_fitnesses = list(itertools.accumulate(fitness_tuple))
    accumulated_fitnesses.insert(0,0) # create a base value 0 for the accumulated fitnesses


    fitness_sum = accumulated_fitnesses[-1]

    first_pick = random.uniform(0, fitness_sum)

    first_index = get_index(accumulated_fitnesses, first_pick)

    second_pick = random.uniform(0, fitness_sum - fitness_tuple[first_index]) # substract the probability portion of picked gene

    if second_pick >= accumulated_fitnesses[first_index]:
        second_pick += fitness_tuple[first_index] #compensate for the cut off probability portion, also avoids falling into the same range again

    second_index = get_index(accumulated_fitnesses, second_pick)

    parent_genes = (genes[first_index], genes[second_index])

    return parent_genes





# Ex: get_index( [1, 3, 6], 2) =  1 because the first number greater than 2 is 3, corresponding to index 1

def get_index(fitnesses, number):

    # range starts at 1 because it ignores comparison to base value 0
    for i in range(1, len(fitnesses)):
        if number < fitnesses[i]:
            return i-1

    raise Exception("Given Number is greater than all values in accumulated fitnesses")


# Tuple of 2 genes -> gene
# crossover two genes, so each acc-vector at specific index comes from one of the parent by chance
def crossover_gene(parent_genes):
    parent_A = parent_genes[0]
    parent_B = parent_genes[1]

    crossed_gene = []

    for index in range(0, len(parent_A)):

        crossed_gene_piece = crossover_gene_piece(parent_A[index], parent_B[index])

        crossed_gene.append(crossed_gene_piece)

    return crossed_gene


# cross over the two gene pieces(acceleration vectors)
# select x and y fields respectively, and randomly from two parents
def crossover_gene_piece(first_acc, second_acc):


    which_x = random.randint(0,1)

    if which_x == 0:
        x = first_acc[0]
    else:
        x = second_acc[0]


    which_y = random.randint(0,1)

    if which_y == 0:
        y = first_acc[1]
    else:
        y = second_acc[1]



    gene_piece = vector.Vector(x,y)

    return gene_piece


def mutate_gene(gene):

    for index in range(0, len(gene)):
        if random.random() < settings.MUTATION_RATE:
            gene[index] = initiator.initiate_random_acc()

    return gene


