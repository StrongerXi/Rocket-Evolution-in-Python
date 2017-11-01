from pyglet import image
from basics.obstacle import Obstacle
from basics.vector import Vector
from enum import Enum, auto

# Background Constants
BACKG_WIDTH = 1000
BACKG_HEIGHT = 700
BACKG_COLOR = (255,255,255,255)
BACKG_IMAGE = image.SolidColorImagePattern(BACKG_COLOR).create_image(BACKG_WIDTH, BACKG_HEIGHT)

#Corners
LEFT_BOTTOM = Vector(0,0)
RIGHT_BOTTOM = Vector(BACKG_WIDTH,0)
RIGHT_TOP = Vector(BACKG_WIDTH, BACKG_HEIGHT)
LEFT_TOP = Vector(0,BACKG_HEIGHT)

CORNERS = (LEFT_BOTTOM, RIGHT_BOTTOM, RIGHT_TOP, LEFT_TOP)

# Rocket Image Constants
ROCKET_IMAGE_PATH = "images/ROCKET_IMAGE.png"

ROCKET_RADIUS = 5 #desired radius in the game / not necessary the original radius of image


# Target Image Constants
TARGET_IMAGE_PATH = "images/TARGET_IMAGE.png"

TARGET_RADIUS = 20 # desired radius as well, see ROCKET_IMAGE_RADIUS

TARGET_X = 600
TARGET_Y = 350

TARGET_POS = Vector(TARGET_X, TARGET_Y)

MAX_DISTANCE_TO_TARGET = max(map(TARGET_POS.distance, CORNERS))


# Obstacle Constants
OBSTACLE_1_WIDTH = 30
OBSTACLE_1_HEIGHT = 200
OBSTACLE_1_POSX = 500
OBSTACLE_1_POSY = 350
OBSTACLE_1_COLOR = (200,0,0,255)
OBSTACLE_1_IMAGE = image.SolidColorImagePattern(OBSTACLE_1_COLOR).create_image(OBSTACLE_1_WIDTH, OBSTACLE_1_HEIGHT)
OBSTACLE_1 = Obstacle(OBSTACLE_1_WIDTH, OBSTACLE_1_HEIGHT, OBSTACLE_1_POSX, OBSTACLE_1_POSY,OBSTACLE_1_IMAGE)


# Obstacle Constants
OBSTACLE_2_WIDTH = 200
OBSTACLE_2_HEIGHT = 280
OBSTACLE_2_POSX = 615
OBSTACLE_2_POSY = 140
OBSTACLE_2_COLOR = (200,100,0,255)
OBSTACLE_2_IMAGE = image.SolidColorImagePattern(OBSTACLE_2_COLOR).create_image(OBSTACLE_2_WIDTH, OBSTACLE_2_HEIGHT)
OBSTACLE_2 = Obstacle(OBSTACLE_2_WIDTH, OBSTACLE_2_HEIGHT, OBSTACLE_2_POSX, OBSTACLE_2_POSY,OBSTACLE_2_IMAGE)


# Obstacle Constants
OBSTACLE_3_WIDTH = 200
OBSTACLE_3_HEIGHT = 30
OBSTACLE_3_POSX = 615
OBSTACLE_3_POSY = 265
OBSTACLE_3_COLOR = (200,0,100,255)
OBSTACLE_3_IMAGE = image.SolidColorImagePattern(OBSTACLE_3_COLOR).create_image(OBSTACLE_3_WIDTH, OBSTACLE_3_HEIGHT)
OBSTACLE_3  = Obstacle(OBSTACLE_3_WIDTH, OBSTACLE_3_HEIGHT, OBSTACLE_3_POSX, OBSTACLE_3_POSY,OBSTACLE_3_IMAGE)

ACTIVE_OBSTACLES = [OBSTACLE_1, OBSTACLE_3]


# Game State Constants
POPULATION = 70
GENE_LENGTH = 80


# Rocket State Constants

class State(Enum):

    flying       = "Rocket is flying"
    hit_target   = "Rocket has hit the target"
    hit_obstacle = "Rocket has hit an obstacle"
    hit_boundary = "Rocket has hit a boundary"
    used_up_gene = "Rocket has used up all of its acceleration vectors in gene"


# Init Pos Constants
INIT_POS_X = 100
INIT_POS_Y = 100
INIT_POS = Vector(INIT_POS_X, INIT_POS_Y)


# Init Vel Constants
INIT_VEL_X = -100
INIT_VEL_Y = -100
INIT_VEL = Vector(INIT_VEL_X, INIT_VEL_Y)


# Gene(acceleration Vectors Limit Constants)
ACC_LIMIT_X = 300
ACC_LIMIT_Y = 300


# default fps for game state/ events handling
DEFAULT_FPS = 80

# Unit Time is used for updating positions, it represents the smallest discrete time for the rocket world
DEFAULT_UNIT_TIME = 1/60


# Tick interval constant for activating the next Gene, used in Game State and Updater
# This means that for every 10 ticks/ (times that update-all has been executed)
# , the rockets activate the next acc vector in their gene
GENE_INTERVAL = 10


# Fitness Constants
HIT_TARGET_BONUS = 5
HIT_BOUNDARY_PENALTY = 0.01
HIT_OBSTALCE_PENALTY = 0.01
PASS_OBSTACLE_BONUS = 100
FITNESS_FUNCTION_POWER = 5


#Evolution Constants
MUTATION_RATE = 0.07

