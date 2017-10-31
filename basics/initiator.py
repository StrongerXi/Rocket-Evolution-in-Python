import random

import settings
from basics.rocket import Rocket
from basics.vector import Vector


# Integer -> List-of Rocket
# initiate a random list of rocket
def initiate_random_lor(population,gene_length):

    genes = initiate_random_log(population,gene_length)

    lor = initiate_lor(genes)

    return lor



# Integer Integer -> List-of Gene(List-of Vectors)
# Initiate a list of random genes
def initiate_random_log(population,gene_length):

    log = []

    for i in range(0,population):
        log.append(initiate_random_gene(gene_length))

    return log



# List-of Gene(list-of Vectors) -> List of Rocket
# initiate a list of rocket based on given list of Genes
def initiate_lor(log):
    lor = []

    for gene in log:
        lor.append(initiate_rocket(gene))

    return lor



# Gene (list-of Vectors) -> Rocket
# initiate a rocket with given gene, and predetermined pos, vel in settings
# , and age as 0
def initiate_rocket(gene):
    roc = Rocket(settings.INIT_POS, settings.INIT_VEL, gene)
    return roc



# Integer -> Gene (list-of Vectors)
# initiate a gene as a list of random vectors(acc)
# The length of gene is given as input
def initiate_random_gene(length):
    gene = []

    for i in range(0,length):
        gene.append(initiate_random_acc())

    return gene



# __ -> Vector
# generate an acceleration Vector with 2 random field
# their limits are defined in settings
def initiate_random_acc():
    randx = random.uniform(-settings.ACC_LIMIT_X, settings.ACC_LIMIT_X)
    randy = random.uniform(-settings.ACC_LIMIT_Y, settings.ACC_LIMIT_Y)
    acc = Vector(randx, randy)
    return acc

