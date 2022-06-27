import numpy as np
from plots_utils import show_histogram
from plots_utils import show_histograms_on_grid, HistogramDataset


def test_histogram():
    np.random.seed(12345678)

    x1 = 0 + 1 * np.random.randn(10000)
    x2 = 100 + 100 * np.random.randn(10000)

    show_histogram(HistogramDataset(values=x1, label="X1", bins=100))
    show_histogram(
        HistogramDataset(
            values=x2,
            label="X2",
            bins=100,
            xlabel="This is X axis",
            ylabel="This is Y axis",
            color="orange",
        )
    )


def test_histograms_grid():
    np.random.seed(12345678)

    x_a = 100 + 15 * np.random.randn(10000)
    x_b = 100 + 150 * np.random.randn(10000)
    x_c = 10 + 15 * np.random.randn(10000)
    x_d = 0 + 1 * np.random.randn(10000)

    show_histograms_on_grid(
        [
            HistogramDataset(values=x_a, label="A", bins=50),
            HistogramDataset(values=x_b, label="B", bins=50, color="r"),
            HistogramDataset(values=x_c, label="C", bins=50, color="pink"),
            HistogramDataset(values=x_d, label="D", bins=50, color="yellowgreen"),
        ],
        2,
        2,
        "Hello!",
    )


def test_plots():
    test_histogram()
    test_histograms_grid()


if __name__ == "__main__":
    test_plots()
