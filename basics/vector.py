import math
import operator
from numbers import Number

class Vector:

    #Attribute: vec_tuple (Vector fields are stored as elements in a tuple)

    def __init__(self, *num):

        if isinstance(num[0], tuple):
            self.vec_tuple = num[0]

        elif isinstance(num[0], Number):

           for n in num:
               assert(isinstance(n,Number))

           self.vec_tuple = num

        else:
            raise Exception("Vector initiator expects 1 tuple, or numbers, but received", type(num[0]))

    def __iter__(self):
        return self.vec_tuple.__iter__()

    def __str__(self):
        return str(self.vec_tuple)

    def __repr__(self):
        return str(self.vec_tuple)

    def __getitem__(self, item):
        return self.vec_tuple[item]


    # An Abstraction for applying operator to self and another Vector
    def operation(self, op , other):

        tup = ()
        index = 0

        if isinstance(other,Vector):

            for v1, v2 in zip(self, other):
                tup += op(v1,v2),

        elif isinstance(other,Number):
            for v1 in self:
                tup += op(v1,other),

        else:
            raise Exception("Vector operation expects a Vector or Number, but received: " , type(other))


        return Vector(tup)


    def __add__(self, other):
        return self.operation(operator.add, other)

    def __sub__(self, other):
        return self.operation(operator.sub, other)

    def __mul__(self, other):
        return self.operation(operator.mul, other)

    def __truediv__(self, other):
        return self.operation(operator.div, other)

    #compute the mathematical dot product between two vectors
    def dot_product(self,other):

        assert isinstance(other,Vector)

        product = self * other

        sum = 0

        for num in product:
            sum += num

        return sum

    #compute the magnitude of the difference between two vectors
    def distance(self,other):

        assert isinstance(other,Vector)

        diff = self - other

        dis = math.sqrt( diff.dot_product(diff))

        return dis




u = Vector(1,1)



