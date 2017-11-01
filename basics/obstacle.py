from basics.vector import Vector

class Obstacle:

    # Constructor requires at least the width and height of obstacle
    # default location of obstacle is the center of Game Background
    def __init__(self, width, height, x, y, image,):

        self.image = image

        self.width = width
        self.height = height
        self.x = x
        self.y = y


        # These represent the location of the sides of obstacles
        self.left = self.x - self.width/2
        self.right = self.x + self.width/2
        self.top = self.y + self.height/2
        self.bottom = self.y - self.height/2

        # These Vectors represent the four corners of obstacles
        self.topleft =      Vector(self.left, self.top)
        self.topright =     Vector(self.right, self.top)
        self.bottomleft =   Vector(self.left, self.bottom)
        self.bottomright =  Vector(self.right, self.bottom)

    def rocket_relative_location(self,rocket):


        return self.vector_relative_location(rocket.pos)

    # Rocket -> String
    # Determine the rocket's position relative to this obstacle
    def vector_relative_location(self, vec):

        rx = vec[0]
        ry = vec[1]

        if rx > self.right and ry > self.bottom and ry < self.top:
            return "right"
        if rx < self.left and ry > self.bottom and ry < self.top:
            return "left"
        if rx < self.right and rx > self.left and ry > self.top:
            return "top"
        if rx < self.right and rx > self.left and ry < self.bottom:
            return "bottom"

        if rx > self.right and ry > self.top:
            return "top-right"
        if rx > self.right and ry < self.bottom:
            return "bottom-right"
        if rx < self.left and ry > self.top:
            return "top-left"
        if rx < self.left and ry < self.bottom:
            return "bottom-left"

        return "inside"





