from adforward.dual import DualNumber
import math


def exp(x: DualNumber) -> DualNumber:
    real = math.exp(x.real)
    dual = x.dual * math.exp(x.real)
    return DualNumber(real, dual)


def log(x: DualNumber) -> DualNumber:
    real = math.log(x.real)
    dual = x.dual / x.real
    return DualNumber(real, dual)


def pow(a: DualNumber, b: DualNumber) -> DualNumber:
    return exp(b * log(a))


def cos(x: DualNumber) -> DualNumber:
    real = math.cos(x.real)
    dual = x.dual * -math.sin(x.real)
    return DualNumber(real, dual)


def sin(x: DualNumber) -> DualNumber:
    real = math.sin(x.real)
    dual = x.dual * math.cos(x.real)
    return DualNumber(real, dual)


def tan(x: DualNumber) -> DualNumber:
    return sin(x) / cos(x)


def cosh(x: DualNumber) -> DualNumber:
    return (exp(x) + exp(-x)) / 2


def sinh(x: DualNumber) -> DualNumber:
    return (exp(x) - exp(-x)) / 2


def tanh(x: DualNumber) -> DualNumber:
    return sinh(x) / cosh(x)
