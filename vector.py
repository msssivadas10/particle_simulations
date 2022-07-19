
from math import sqrt, atan2
from random import uniform
from typing import Any

class Vector:
    """
    A 2D vector class.
    """

    __slots__ = 'x', 'y', 

    def __init__(self, x: float, y: float) -> None:
        self.x, self.y = x, y

    def mag(self) -> float:
        """
        Return the length (magnitude) of the vector.
        """
        return sqrt( self.x**2 + self.y**2 )

    def heading(self) -> float:
        """
        Return the direction of the vector.
        """
        return atan2(self.y, self.x)

    def add(self, other: Any) -> None:
        """
        Add another vector or scalar with this vector.
        """
        if isinstance(other, Vector):
            self.x += other.x
            self.y += other.y
            return
        self.x += other
        self.y += other
        return

    def mult(self, value: float) -> None:
        """
        Multiply this vector with a scalar.
        """
        self.x *= value
        self.y *= value
        return
    
    def __repr__(self) -> str:
        return f'Vector({self.x:<10.8g}, {self.y:<10.8g})'
    
    def __add__(self, other: Any) -> 'Vector':
        if isinstance(other, Vector):
            return Vector( self.x + other.x, self.y + other.y )
        return Vector( self.x + other, self.y + other )

    def __radd__(self, other: Any) -> 'Vector':
        return self.__add__(other)

    def __sub__(self, other: Any) -> 'Vector':
        if isinstance(other, Vector):
            return Vector( self.x - other.x, self.y - other.y )
        return Vector( self.x - other, self.y - other )
    
    def __rsub__(self, other: Any) -> 'Vector':
        return Vector( other - self.x, other - self.y )

    def __mul__(self, other: Any) -> 'Vector':
        if isinstance(other, Vector):
            return NotImplemented
        return Vector( self.x * other, self.y * other )

    def __rmul__(self, other: Any) -> 'Vector':
        return self.__mul__(other)

    def __truediv__(self, other: Any) -> 'Vector':
        if isinstance(other, Vector):
            return NotImplemented
        return Vector( self.x / other, self.y / other )

    def dot(self, other: 'Vector') -> float:
        """
        Return the dot product with another vector.
        """
        return self.x * other.x + self.y * other.y

    def normalize(self) -> None:
        """
        Normalise the vector.
        """
        length  = self.mag()
        self.x /= length
        self.y /= length
        return 

    def astuple(self) -> tuple:
        """
        Return the components as a tuple.
        """
        return self.x, self.y

    @classmethod
    def random(cls) -> 'Vector':
        """
        Return a random normalized vector.
        """
        x = uniform(-1.0, 1.0)
        y = sqrt(1 - x**2)
        return cls(x, y)    


