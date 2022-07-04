from libs.math_utils import (
    random_normal_float,
    random_uniform_float,
    noisy_numbers_generator,
    add_noise,
)
import numpy as np

def test_random_uniform_float():
    numbers_a = [random_uniform_float(10) for _ in range(0, 10)]
    numbers_b = [random_uniform_float([10]) for _ in range(0, 10)]
    numbers_c = [random_uniform_float([10, 20]) for _ in range(0, 10)]
    numbers_d = [random_uniform_float((-20, -10)) for _ in range(0, 10)]

    print("\ntest_random_uniform_float")
    print(numbers_a)
    print(numbers_b)
    print(numbers_c)
    print(numbers_d)


def test_random_normal_float():
    numbers_a = [random_normal_float() for _ in range(0, 10)]
    numbers_b = [random_normal_float(0, 10) for _ in range(0, 10)]
    numbers_c = [random_normal_float(10, 1) for _ in range(0, 10)]
    numbers_d = [random_normal_float(5, 5) for _ in range(0, 10)]

    print("\ntest_random_normal_float")
    print(numbers_a)
    print(numbers_b)
    print(numbers_c)
    print(numbers_d)


def test_random_float():
    test_random_uniform_float()
    test_random_normal_float()


def test_add_noise():
    numbers_args = np.linspace(0, 2 * np.pi, 10)
    numbers = [np.sin(x) for x in numbers_args]
    noised_numbers = [add_noise(number, 0.0, 0.1) for number in numbers]

    print("\ntest_add_noise")
    print(numbers)
    print(noised_numbers)


def test_numbers_generator():
    number_gen = noisy_numbers_generator((0, 10), 0, 1)

    print("\ntest_numbers_generator")
    for _ in range(0, 20):
        print(next(number_gen))


def test_math():
    test_random_float()
    test_add_noise()
    test_numbers_generator()


if __name__ == "__main__":
    test_math()
