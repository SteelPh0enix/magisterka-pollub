from plots_tests import HistogramDataset, show_histograms_on_grid
from math_utils import random_uniform_float, random_normal_float, add_noise
import numpy as np


def test_random_uniform_float():
    numbers_a = [random_uniform_float(10) for _ in range(0, 10000)]
    numbers_b = [random_uniform_float([10]) for _ in range(0, 10000)]
    numbers_c = [random_uniform_float([10, 20]) for _ in range(0, 10000)]
    numbers_d = [random_uniform_float((-20, -10)) for _ in range(0, 10000)]

    show_histograms_on_grid(
        [
            HistogramDataset(values=numbers_a, label="A", bins=50),
            HistogramDataset(values=numbers_b, label="B", bins=50),
            HistogramDataset(values=numbers_c, label="C", bins=50),
            HistogramDataset(values=numbers_d, label="D", bins=50),
        ],
        2,
        2,
        "Random uniform floats",
    )


def test_random_normal_float():
    numbers_a = [random_normal_float() for _ in range(0, 10000)]
    numbers_b = [random_normal_float(0, 10) for _ in range(0, 10000)]
    numbers_c = [random_normal_float(10, 1) for _ in range(0, 10000)]
    numbers_d = [random_normal_float(5, 5) for _ in range(0, 10000)]

    show_histograms_on_grid(
        [
            HistogramDataset(values=numbers_a, label="A", bins=50),
            HistogramDataset(values=numbers_b, label="B", bins=50),
            HistogramDataset(values=numbers_c, label="C", bins=50),
            HistogramDataset(values=numbers_d, label="D", bins=50),
        ],
        2,
        2,
        "Random normal floats",
    )


def test_random_float():
    test_random_uniform_float()
    test_random_normal_float()


def test_add_noise():
    numbers_args = np.linspace(0, 2 * np.pi, 10000)
    numbers = [np.sin(x) for x in numbers_args]
    noised_numbers = [add_noise(number, 0.0, 1.0) for number in numbers]

    # plot_lines_on_single_plot(
    #     [(numbers_args, numbers), (numbers_args, noised_numbers)],
    #     ["Original", "Noised"],
    #     ["b", "r"],
    # )


def test_numbers_generator():
    pass


def test_math():
    test_random_float()
    test_add_noise()
    test_numbers_generator()


if __name__ == "__main__":
    test_math()
