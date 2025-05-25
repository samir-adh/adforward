from adforward.dual import DualNumber


def main():
    a = DualNumber(0.2, 12)
    b = DualNumber(1, 0.52)

    print(f"a = {a}, b = {b}")
    print(f"a + b = {a + b}")
    print(f"a / b = {a / b}")


if __name__ == "__main__":
    main()
