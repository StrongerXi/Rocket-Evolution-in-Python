import settings
from basics.vector import Vector


class Rocket:
    # Input: Vector Vector [List-of Vector]
    # "age" represents the current index for the acceleration vector in acc list
    # Ex: age = 3 means that, the current acc vector is gene[3]
    # Stopped is a flag that helps determine whether the rocket has stopped, (Ex: having hit something)
    def __init__(self, pos, vel, list_of_acc, radius = settings.ROCKET_RADIUS):

        assert (isinstance(pos, Vector))
        assert (isinstance(vel, Vector))
        assert (isinstance(list_of_acc, list))

        self.pos = pos
        self.vel = vel
        self.gene = list_of_acc
        self.radius = radius
        self.state = settings.State.flying
        self.age = 0
        self.fitness = 1


    # State -> Void
    # Set the state of rocket to the state given
    def set_state(self, state):
        assert isinstance(state,settings.State)
        self.state = state

    # The following 4 functions are
    # Boolean Functions that returns true if the rocket is in the state specified
    def is_flying(self):
        return self.state == settings.State.flying

    def hit_boundary(self):
        return self.state == settings.State.hit_boundary

    def hit_target(self):
        return self.state == settings.State.hit_target

    def hit_obstacle(self):
        return self.state == settings.State.hit_obstacle

    def used_up_gene(self):
        return self.state == settings.State.used_up_gene


    # Accessor Functions for the Position & Velocity Vector components,
    # current acceleration vector, gene list, or state
    def get_x(self):
        return self.pos[0]

    def get_y(self):
        return self.pos[1]

    def get_vx(self):
        return self.vel[0]

    def get_vy(self):
        return self.vel[1]

    def get_acc(self):
        return self.gene[self.age]

    def get_gene(self):
        return self.gene

    def get_state(self):
        return self.state


    # Update functions for the position and velocity vectors of Rocket
    def update_pos(self, dt):
        self.pos += self.vel * dt

    def update_vel(self, dt):
        self.vel += self.gene[self.age] * dt



    def increment_age(self):
        self.age += 1

    def __str__(self):
        info = ""

        info += "pos: "
        info += str(self.pos)
        info += " \tvel: "
        info += str(self.vel)
        info += " \tgene/accs: "
        info += str(self.gene)
        info += " \tage: "
        info += str(self.age)

        return info




