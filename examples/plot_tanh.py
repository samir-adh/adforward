import matplotlib.pyplot as plt

from adforward.dual import DualNumber
import adforward.math as m


def main():
    start = -3
    end = 3
    step = 0.1
    x_real = []
    t = start
    while t < end:
        x_real.append(t)
        t += step
    x_dual = [1 for _ in x_real]
    x = [DualNumber(real, dual) for real, dual in zip(x_real, x_dual)]
    y = [m.tanh(x_i) for x_i in x]

    y_real = [y_i.real for y_i in y]
    y_dual = [y_i.dual for y_i in y]

    # Calculate tanh and its derivative at x = 0.3
    target_x = 1
    x_target = DualNumber(target_x, 1.0)
    y_target = m.tanh(x_target)

    tangent_line = [y_target.real + (h - target_x) * y_target.dual for h in x_real]

    _, ax = plt.subplots(figsize=(10, 6))
    ax.plot(x_real, y_real, label="tanh", color="blue")
    ax.plot(x_real, y_dual, label="tanh'", color="red")
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

