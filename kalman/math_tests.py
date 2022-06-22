from math_utils import random_uniform_float, random_normal_float
from typing import List
import matplotlib.pyplot as plt
import numpy as np


def show_histograms(
    data: List[List[float]],
    labels: List[List[str]],
    rows: int,
    columns: int,
    nbins: int,
):
    fig, ax = plt.subplots(rows, columns)

    for x in range(columns):
        for y in range(rows):
            i = x * rows + y
            ax[x][y].hist(data[i], bins=nbins, label=labels[i])
            ax[x][y].set_title(labels[i])

    plt.show()


def test_random_uniform_float():
    numbers_a = [random_uniform_float(10) for _ in range(0, 10000)]
    numbers_b = [random_uniform_float([10]) for _ in range(0, 10000)]
    numbers_c = [random_uniform_float([10, 20]) for _ in range(0, 10000)]
    numbers_d = [random_uniform_float((-20, -10)) for _ in range(0, 10000)]

    show_histograms(
        [numbers_a, numbers_b, numbers_c, numbers_d], ["A", "B", "C", "D"], 2, 2, 20
    )


def test_random_normal_float():
    numbers_a = [random_normal_float() for _ in range(0, 10000)]
    numbers_b = [random_normal_float(0, 10) for _ in range(0, 10000)]
    numbers_c = [random_normal_float(10, 1) for _ in range(0, 10000)]
    numbers_d = [random_normal_float(5, 5) for _ in range(0, 10000)]

    show_histograms(
        [numbers_a, numbers_b, numbers_c, numbers_d], ["A", "B", "C", "D"], 2, 2, 20
    )


def test_random_float():
    test_random_uniform_float()
    test_random_normal_float()


def test_add_noise():
    pass


def test_numbers_generator():
    pass


def test_math():
    test_random_float()
    test_add_noise()
    test_numbers_generator()


if __name__ == "__main__":
    test_math()
