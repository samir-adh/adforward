class DualNumber:
    def __init__(self, real: float, dual: float = 0) -> None:
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

    def __eq__(self, value: object) -> bool:
        if isinstance(value, (int, float)):
            return self.real == value
        elif isinstance(value, DualNumber):
            return self.real == value.real
        else:
            return False

    def __lt__(self, value: object) -> bool:
        if isinstance(value, (int, float)):
            return self.real < value
        elif isinstance(value, DualNumber):
            return self.real < value.real
        else:
            raise ValueError(f"Cannot compare 'DualNumber' with {value.__class__}")

    def __le__(self, value: object) -> bool:
        if isinstance(value, (int, float)):
            return self.real <= value
        elif isinstance(value, DualNumber):
            return self.real <= value.real
        else:
            raise ValueError(f"Cannot compare 'DualNumber' with {value.__class__}")

    def __gt__(self, value: object) -> bool:
        if isinstance(value, (int, float)):
            return self.real > value
        elif isinstance(value, DualNumber):
            return self.real > value.real
        else:
            raise ValueError(f"Cannot compare 'DualNumber' with {value.__class__}")

    def __ge__(self, value: object) -> bool:
        if isinstance(value, (int, float)):
            return self.real >= value
        elif isinstance(value, DualNumber):
            return self.real >= value.real
        else:
            raise ValueError(f"Cannot compare 'DualNumber' with {value.__class__}")

    def __ne__(self, value: object) -> bool:
        return not self == value

    def __repr__(self) -> str:
        return f"({self.real}+{self.dual}ε)"

    def __pow__(self, other):
        if isinstance(other, int):
            result = DualNumber(1)
            for i in range(other):
                result = result * self
            return result
        elif isinstance(other, DualNumber):
            return self.__pow__(other.real)
        else:
            raise RuntimeError("invalid value encountered in __pow__")
