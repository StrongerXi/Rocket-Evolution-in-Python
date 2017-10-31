
import settings
from basics import rocket
from basics.vector import Vector


# list_of_rockets List of Obstacles-> Tuple_of_gene_and_fitness
# evaluate each rocket's fitness score based on their final location
# then attach this score to its gene, and form a list of gene and fitness
def evaluate_fitness_lor(lor,lob):
    print("Evaluating")
    #tuple of gene and tuple of fitness
    tog = ()
    tof = ()

    for rocket in lor:
        gene = rocket.gene
        fitness = evaluate_fitness_rocket(rocket)
        if passed_all_obstacles(rocket, lob):
            fitness *= settings.PASS_OBSTACLE_BONUS
        tog += gene,
        tof += fitness,

    togaf = (tog, tof)

    return togaf



def evaluate_fitness_rocket(rocket):

    r = settings.TARGET_POS.distance(rocket.pos)

    # scale r so that it stays in the range from 0 to 1
    scaled_r = r / settings.MAX_DISTANCE_TO_TARGET

    raw_fitness = fitness_function(scaled_r)

    # A rocket's fitness is default at 1, then it might becomes a bonus or penalty factor
    # depending on whether it has hit a target or boundary
    fitness = rocket.fitness * raw_fitness

    return fitness


def passed_all_obstacles(roc,lob):
    for obs in lob:
        if not passed_obstacle(roc,obs):
            return False
    return True


# Rocket Obstacle -> Boolean
# returns true if the rocket has passed obstacle towards target
def passed_obstacle(roc, obs):


    rocket_pos = obs.rocket_relative_location(roc)

    if rocket_pos == "inside":
        return False

    favored_region = obstacle_favored_region(obs)

    return (rocket_pos in favored_region)

def obstacle_favored_region(obs):

    target_pos = obs.vector_relative_location(settings.TARGET_POS)

    if target_pos == "right":
        return ["top", "top-right", "right", "bottom-right", "bottom"]
    if target_pos == "left":
        return ["top", "top-left", "left", "bottom-left", "bottom"]
    if target_pos == "bottom":
        return ["bottom", "bottom-right", "bottom-left", "left", "right"]
    if target_pos == "top":
        return ["top", "top-right", "top-left", "left", "right"]

    if target_pos == "top-right":
        return ["top", "top-right", "right"]
    if target_pos == "bottom-right":
        return ["bottom", "bottom-right", "right"]
    if target_pos == "top-left":
        return ["top", "top-left", "left"]
    if target_pos == "bottom-left":
        return ["bottom", "bottom-left", "left"]


# assume r is scaled so that it ranges from 0 to 1
# In this case r represents distance from target
def fitness_function(r):

    fitness = (1 - r) ** settings.FITNESS_FUNCTION_POWER

    return fitness


r1 = rocket.Rocket(Vector(800, 0), Vector(0, 0), [Vector(1, 1)])
r2 = rocket.Rocket(Vector(800, 300), Vector(0, 0), [Vector(2, 2)])
r3 = rocket.Rocket(Vector(600, 790), Vector(0, 0), [Vector(3, 3)])
r4 = rocket.Rocket(Vector(0, 600), Vector(0, 0), [Vector(4, 4)])
r5 = rocket.Rocket(Vector(600, 347), Vector(0, 0), [Vector(5, 5)])

lor = [r1,r2,r3,r4,r5]
lob = [settings.OBSTACLE_1, settings.OBSTACLE_2, settings.OBSTACLE_3]

togaf = evaluate_fitness_lor(lor, lob)


print(settings.OBSTACLE_2.rocket_relative_location(r1))
print(obstacle_favored_region(settings.OBSTACLE_2))
print(passed_obstacle(r1,settings.OBSTACLE_2))
print(togaf[1])
