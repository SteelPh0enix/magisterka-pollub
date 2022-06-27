import numpy as np
from plots_utils import (
    show_histogram,
    show_histograms_on_grid,
    HistogramDataset,
    show_line_plots_grid,
    show_line_plot,
    PlotDataset,
)


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
            HistogramDataset(
                values=x_c,
                label="C",
                bins=50,
                color="pink",
                xlabel="X label",
                ylabel="Y label",
            ),
            HistogramDataset(values=x_d, label="D", bins=50, color="yellowgreen"),
        ],
        2,
        2,
        "Hello!",
    )


def test_line_plots_grid():
    y1 = np.linspace(0, 4 * np.pi, 1000)
    y2 = [np.sin(i) for i in y1]
    y3 = [np.cos(i) for i in y1]
    y4 = [np.tan(i) for i in y1]

    show_line_plots_grid(
        [
            PlotDataset(
                values_y=y1,
                label="f(x) = x * 4pi / 1000",
                xlabel="x",
                ylabel="x * 4pi / 1000",
            ),
            PlotDataset(
                values_y=y2,
                values_x=y1,
                label="f(x) = sin(x)",
                xlabel="x",
                ylabel="sin(x)",
                linestyle="--",
                linewidth=2.0,
                color="green",
            ),
            PlotDataset(
                values_y=y3,
                values_x=y1,
                label="f(x) = cos(x)",
                xlabel="x",
                ylabel="cos(x)",
            ),
            PlotDataset(
                values_y=y4,
                values_x=y1,
                label="f(x) = tg(x)",
                xlabel="x",
                ylabel="tg(x)",
            ),
        ],
        2,
        2,
        "Some periodic functions",
    )


def test_line_plot():
    x = np.linspace(0, 10 * np.pi, 360 * 10)
    y = [np.sin(xval) for xval in x]
    show_line_plot(PlotDataset(y, x, "f(x) = sin(x)", "sin(x)", "x", "red", ":"))


def test_multiline_plot():
    pass


def test_plots():
    # test_histogram()
    # test_histograms_grid()
    test_line_plots_grid()
    test_line_plot()
    test_multiline_plot()


if __name__ == "__main__":
    test_plots()
