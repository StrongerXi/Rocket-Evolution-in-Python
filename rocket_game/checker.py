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
        check_obstacles_lor(self.lor, self.gs.lobs) # Stop rockets that hit any obstacle
        check_gameover(self.gs) # check if all rockets have stopped


# [List-of Rocket], [Rocket -> Rocket] -> Void
# An Abstraction to apply input check function to all
# flying rockets in lor
# NOTE: The map function here returns an iterable, so only the elements which we iterate over is evaluated
# Thus, it is imperative to add a list() around map()...
def check_for_flying_lor(lor, check_function):

    list(map(lambda rocket:
                check_function(rocket)
                if rocket.is_flying()
                else rocket,
            lor))
    return lor



#check whether any rocket in lor has hit boundary
#Skip for those that have already stopped(has hit boundary/target/obstacle)
def check_boundary_lor(lor):
    check_for_flying_lor(lor,check_boundary_rocket)

    return lor


# Rocket -> Rocket
# If the rocket hits any of the boundary, set its state to hit_boundary
def check_boundary_rocket(rocket):


    posx = rocket.pos[0]
    posy = rocket.pos[1]


    # check Left,
    #       Right,
    #       Bottom
    #   and Top respectively
    if (posx < 0 + settings.ROCKET_RADIUS or
        posx > settings.BACKG_WIDTH - settings.ROCKET_RADIUS or
        posy < 0 + settings.ROCKET_RADIUS or
        posy > settings.BACKG_HEIGHT - settings.ROCKET_RADIUS):


        rocket.set_state(settings.State.hit_boundary)

    return rocket



def check_target_lor(lor):

    check_for_flying_lor(lor,check_target_rocket)


# Rocket -> Rocket
# If the rocket hits the target, set its state to hit_boundary
def check_target_rocket(rocket):
    # if the distance between rocket and target goes under the sum of their radii:

    critical_distance = settings.ROCKET_RADIUS + settings.TARGET_RADIUS
    distance = rocket.pos.distance(settings.TARGET_POS)

    if distance < critical_distance:
        rocket.set_state(settings.State.hit_target)

    return rocket


def check_obstacles_lor(lor,lob):

    for obs in lob:
        check_for_flying_lor(lor, lambda rocket: check_obstacle_rocket(rocket, obs))


# Rocket Obstacle -> Rocket
# Based on rocket's relative location to the obstacle, determine
# whether the rocket has hit the obstacle; and if so, set the rocket state to hit_obstacle
def check_obstacle_rocket(rocket,obs):

    rx = rocket.get_x()
    ry = rocket.get_y()
    rad = rocket.radius

    rocket_relative_loc = obs.rocket_relative_location(rocket)

    if rocket_relative_loc == "inside":
        rocket.set_state(settings.State.hit_obstacle)

    if rocket_relative_loc == "right" and (rx < obs.right + rad):
        rocket.set_state(settings.State.hit_obstacle)

    if rocket_relative_loc == "left" and (rx > obs.left - rad):
        rocket.set_state(settings.State.hit_obstacle)

    if rocket_relative_loc == "top" and (ry < obs.top + rad):
        rocket.set_state(settings.State.hit_obstacle)

    if rocket_relative_loc == "bottom" and (ry > obs.bottom - rad):
        rocket.set_state(settings.State.hit_obstacle)

    if rocket_relative_loc == "top-right" and (rad > rocket.pos.distance(obs.topright)):
        rocket.set_state(settings.State.hit_obstacle)

    if rocket_relative_loc == "top-left" and (rad > rocket.pos.distance(obs.topleft)):
        rocket.set_state(settings.State.hit_obstacle)

    if rocket_relative_loc == "bottom-right" and (rad > rocket.pos.distance(obs.bottomright)):
        rocket.set_state(settings.State.hit_obstacle)

    if rocket_relative_loc == "bottom-left" and (rad > rocket.pos.distance(obs.bottomleft)):
        rocket.set_state(settings.State.hit_obstacle)

    return rocket


# if all rockets have stopped, turn the gameover flag in Game State to True
def check_gameover(gs):

    for rocket in gs.lor:
        if rocket.is_flying():
            return False
    gs.game_over_flag = True



