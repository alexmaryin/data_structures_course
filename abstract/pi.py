# Naive algorithm with iteration
from utils.time_measuring import measured_time


def calc_pi(precision) -> float:
    numerator = 4.0
    denominator = 1.0
    operation = 1.0
    pi = 0.0
    for _ in range(precision):
        pi += operation * (numerator / denominator)
        denominator += 2.0
        operation *= -1.0
    return pi


@measured_time
def main():
    print(calc_pi(80000000))


if __name__ == "__main__":
    main()
