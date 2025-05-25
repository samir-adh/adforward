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
        if isinstance(other, (int, float)):
            return DualNumber(self.real * other, self.dual * other)

        real = self.real * other.real
        dual = self.dual * other.real + self.real * other.dual
        return DualNumber(real, dual)

    def __truediv__(self, other):
        if isinstance(other, (int, float)):
            return DualNumber(self.real / other, self.dual / other)

        real = self.real / other.real
        dual = (self.dual * other.real - self.real * other.dual) / (other.real**2)
        return DualNumber(real, dual)

    def __neg__(self):
        return DualNumber(-self.real, -self.dual)

    def __invert__(self):
        a = DualNumber(1, 0)
        return a / self

    def __repr__(self) -> str:
        return f"({self.real}+{self.dual}ε)"
