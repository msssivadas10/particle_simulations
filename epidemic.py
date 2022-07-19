
from vector import Vector
from particle import Particle

SUSCEPTIBLE, INFECTED, RECOVERED = 0, 1, 2

class Agent(Particle):

    def __init__(self, pos: Vector, vel: Vector, ri: float, protected: bool = False) -> None:

        super().__init__(
                            pos, vel, 
                            mass = 1.0, 
                            radius = ri, 
                            protected = protected, 
                            state = SUSCEPTIBLE, 
                            lifetime = 0.0
                        )
    @property
    def ri(self) -> float:
        return self.attrs['radius']

    @property 
    def protected(self) -> bool:
        return self.attrs['protected']

    @protected.setter 
    def protected(self, state: bool) -> None:
        self.attrs['protected'] = state

    @property
    def state(self) -> int:
        return self.attrs['state']

    @state.setter
    def state(self, value: int) -> None:
        self.attrs['state'] = value

    @property 
    def lifetime(self) -> float:
        return self.attrs['lifetime']

    @lifetime.setter
    def lifetime(self, value: float) -> None:
        self.attrs['lifetime'] = value