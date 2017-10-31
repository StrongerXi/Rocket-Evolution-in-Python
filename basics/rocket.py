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

        self.age = 0
        self.stopped = False
        self.fitness = 1


    def get_x(self):
        return self.pos[0]

    def get_y(self):
        return self.pos[1]

    def get_vx(self):
        return self.vel[0]

    def get_vy(self):
        return self.vel[1]


    def update_pos(self, dt):
        self.pos += self.vel * dt

    def update_vel(self, dt):
        self.vel += self.gene[self.age] * dt

    def get_gene(self):
        return self.gene



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




