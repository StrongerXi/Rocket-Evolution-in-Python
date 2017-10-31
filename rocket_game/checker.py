import settings


# The Checker checks whether any rocket is out of bound, or has hit something.
# it also checks if game should end(all rockets has stopped)
class Checker():

    def __init__(self,game_state):

        self.gs = game_state
        self.lor = game_state.lor


    def check_all(self,*args):

        check_boundary_lor(self.lor) # Stop out of bound rockets
        check_target_lor(self.lor)  # Stop rockets that hit target
        check_obstacles_lor(self.lor, self.gs.lob)
        check_gameover(self.gs) # check if all rockets have stopped


def check_boundary_lor(lor):

        for rocket in lor:
            if rocket.stopped == True:
                continue
            check_boundary_rocket(rocket)


def check_boundary_rocket(rocket):
    #check Left, Right, Bottom and Top respectively
    #if rocket is out of boundary, its stopped flag becomes true, and fitness changes to settings.HIT_BOUNDARY_PENALTY
    posx = rocket.pos[0]
    posy = rocket.pos[1]

    if (posx < 0 + settings.ROCKET_RADIUS or
        posx > settings.BACKG_WIDTH - settings.ROCKET_RADIUS or
        posy < 0 + settings.ROCKET_RADIUS or
        posy > settings.BACKG_HEIGHT - settings.ROCKET_RADIUS):
        rocket.fitness = settings.HIT_BOUNDARY_PENALTY
        rocket.stopped = True



def check_target_lor(lor):
        for rocket in lor:
            if rocket.stopped == True:
                continue
            check_target_rocket(rocket)


def check_target_rocket(rocket):
    # if the distance between rocket and target goes under the sum of their radii:
    # Rocket stops, also change its fitness to setting.TARGET_BONUS

    critical_distance = settings.ROCKET_RADIUS + settings.TARGET_RADIUS
    distance = rocket.pos.distance(settings.TARGET_POS)

    if distance < critical_distance:
        rocket.fitness = settings.TARGET_BONUS
        rocket.stopped = True



def check_obstacles_lor(lor,lob):

    for obs in lob:
        for rocket in lor:
            if rocket.stopped == True:
                continue
            check_obstacle_rocket(rocket,obs)


def check_obstacle_rocket(rocket,obs):

    rx = rocket.get_x()
    ry = rocket.get_y()
    rad = rocket.radius


    rocket_pos = obs.rocket_relative_location(rocket)

    if rocket_pos == "inside":
        rocket.fitness = settings.HIT_OBSTALCE_PENALTY
        rocket.stopped = True

    if rocket_pos == "right" and (rx < obs.right + rad):
        rocket.fitness = settings.HIT_OBSTALCE_PENALTY
        rocket.stopped = True
    if rocket_pos == "left" and (rx > obs.left - rad):
        rocket.fitness = settings.HIT_OBSTALCE_PENALTY
        rocket.stopped = True
    if rocket_pos == "top" and (ry < obs.top + rad):
        rocket.fitness = settings.HIT_OBSTALCE_PENALTY
        rocket.stopped = True
    if rocket_pos == "bottom" and (ry > obs.bottom - rad):
        rocket.fitness = settings.HIT_OBSTALCE_PENALTY
        rocket.stopped = True

    if rocket_pos == "top-right" and (rad > rocket.pos.distance(obs.topright)):
        rocket.fitness = settings.HIT_OBSTALCE_PENALTY
        rocket.stopped = True
    if rocket_pos == "top-left" and (rad > rocket.pos.distance(obs.topleft)):
        rocket.fitness = settings.HIT_OBSTALCE_PENALTY
        rocket.stopped = True
    if rocket_pos == "bottom-right" and (rad > rocket.pos.distance(obs.bottomright)):
        rocket.fitness = settings.HIT_OBSTALCE_PENALTY
        rocket.stopped = True
    if rocket_pos == "bottom-left" and (rad > rocket.pos.distance(obs.bottomleft)):
        rocket.fitness = settings.HIT_OBSTALCE_PENALTY
        rocket.stopped = True

# if all rockets have stopped, turn the gameover flag in Game State to True
def check_gameover(gs):

    for rocket in gs.lor:
        if rocket.stopped == False:
            return
    gs.game_over_flag = True

