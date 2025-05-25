import matplotlib.pyplot as plt
import numpy as np
from adforward.dual import DualNumber
import adforward.math as m


def u(x: DualNumber):
    # return m.log(DualNumber(1) + x * x)
    return x * m.log(x**2 + DualNumber(1, 0)) + m.sin(x * 1)


def v(x: DualNumber):
    return DualNumber(2) ** (DualNumber(1) / (DualNumber(1) + x**2))


def sign_log(x: DualNumber):
    return m.sign(x) * m.log(DualNumber(1) + m.abs(x))


def LeakyReLU(x, alpha=0.001):
    if x > 0:
        return x
    else:
        return x * alpha


def main():
    f = v
    m = 32
    start = -m
    end = m
    n_points = 1000
    step = 2 * m / n_points
    x_real = []
    t = start
    while t < end:
        x_real.append(t)
        t += step
    x_dual = [1 for _ in x_real]
    x = [DualNumber(real, dual) for real, dual in zip(x_real, x_dual)]
    y = [f(x_i) for x_i in x]

    y_real = [y_i.real for y_i in y]
    y_dual = [y_i.dual for y_i in y]

    # Calculate tanh and its derivative at x = 0.3
    target_x = 5
    x_target = DualNumber(target_x, 1.0)
    y_target = f(x_target)

    tangent_line = [y_target.real + (h - target_x) * y_target.dual for h in x_real]

    _, ax = plt.subplots(figsize=(10, 6))
    ax.plot(x_real, y_real, label="f", color="blue")
    ax.plot(x_real, y_dual, label="f'", color="red")
    ax.plot(
        x_real,
        tangent_line,
        label=f"tangent line at x={target_x}",
        color="green",
        linestyle="--",
    )

    ax.set_xlabel("x")
    ax.set_ylabel("y")
    ax.legend()
    ax.grid()

    plt.tight_layout()
    plt.show()


if __name__ == "__main__":
    main()
