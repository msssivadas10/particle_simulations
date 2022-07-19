
from vector import Vector

class Particle:

    __slots__ = 'pos', 'vel', 'mass', 'attrs'

    def __init__(self, pos: Vector, vel: Vector, mass: float = 1.0, **attrs) -> None:
        
        assert isinstance(pos, Vector), "position must be a 'Vector'"
        assert isinstance(vel, Vector), "velocity must be a 'Vector'"

        self.pos  = pos
        self.vel  = vel
        self.mass = mass

        self.attrs = { **attrs } # particle attributes

    def drift(self, dt: float = 1.0, constraints: tuple = None, bc: str = 'reflect') -> None:
        """
        Update the particle positions.
        """
        self.pos.add( self.vel * dt )

        if constraints is None:
            return 

        xLeft, yLeft, xRight, yRight = constraints # boundary box

        if bc == 'reflect':

            if self.pos.x < xLeft:
                self.pos.x = -self.pos.x
                self.vel.x = -self.vel.x
            elif self.pos.x > xRight:
                self.pos.x = 2*xRight - self.pos.x # TODO: check
                self.vel.x = - self.vel.x

            if self.pos.y < yLeft:
                self.pos.y = -self.pos.y
                self.vel.y = -self.vel.y
            elif self.pos.y > yRight:
                self.pos.y = 2*yRight - self.pos.y # TODO: check
                self.vel.y = - self.vel.y
            return

        elif bc == 'periodic':

            xWidth, yWidth = xRight - xLeft, yRight - yLeft

            self.pos.x = (self.pos.x - xLeft) % xWidth + xLeft
            self.pos.y = (self.pos.y - yLeft) % yWidth + yLeft
            return

        raise ValueError(f"invalid value for bc: '{bc}'")

    def kick(self, force: Vector, dt: float = 1.0) -> None:
        """
        Update the particle velocity.
        """
        return self.vel.add( force / self.mass * dt )

    def energy(self) -> float:
        """
        Return the kinetic energy of the particle. 
        """
        v = self.vel.mag()
        return 0.5 * self.mass * v**2

        
