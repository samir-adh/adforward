class DualNumber:
    def __init__(self, real: float, dual: float) -> None:
        self.real = real
        self.dual = dual

    def __add__(self, other):
        real = self.real + other.real
        dual = self.dual + other.dual
        return DualNumber(real, dual)

    def __sub__(self, other):
        real = self.real - other.real
        dual = self.dual - other.dual
        return DualNumber(real, dual)

    def __mul__(self, other):
        real = self.real * other.real
        dual = self.dual * other.real + self.real * other.dual
        return DualNumber(real, dual)

    def __truediv__(self, other):
        real = self.real / other.real
        dual = (self.dual * other.real - self.real * other.dual) / (other.real**2)
        return DualNumber(real, dual)

    def __repr__(self) -> str:
        return f"({self.real}+{self.dual}ε)"
