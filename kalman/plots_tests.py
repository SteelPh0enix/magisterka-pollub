import numpy as np
from plots_utils import (
    show_histogram,
    show_histograms_on_grid,
    HistogramDataset,
    show_line_plots_grid,
    show_line_plot,
    show_multiline_plot,
    PlotDataset,
    BoxPlotDataset,
    show_box_plot,
    show_box_plots_grid,
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
                label="f(x) = x * something",
                xlabel="x",
                ylabel="x * something",
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
                color="red",
            ),
            PlotDataset(
                values_y=y4,
                values_x=y1,
                label="f(x) = tg(x)",
                xlabel="x",
                ylabel="tg(x)",
                color="blue",
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
    y1 = np.linspace(0, 4 * np.pi, 1000)
    y2 = [np.sin(i) for i in y1]
    y3 = [np.cos(i) for i in y1]
    y4 = [np.tan(i) for i in y1]

    show_multiline_plot(
        [
            PlotDataset(
                values_y=y1,
                values_x=y1,
                label="f(x) = x something",
                xlabel="x",
                ylabel="x * something",
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
                color="red",
            ),
        ],
        "Some functions on top of each other",
        "f(x)",
        "x",
    )


def test_box_plots():
    np.random.seed(12345678)

    x1 = 0 + 1 * np.random.randn(10000)
    x2 = 100 + 100 * np.random.randn(10000)
    x3 = 100 + 1 * np.random.randn(10000)
    x4 = 1 + 100 * np.random.randn(10000)

    show_box_plot(
        BoxPlotDataset(
            [x1, x2, x3, x4],
            label="Some random numbers",
            xlabel="datasets",
            ylabel="values probability",
            values_labels=["A", "B", "C", "D"],
        )
    )

    show_box_plots_grid(
        [
            BoxPlotDataset(x1, label="X1"),
            BoxPlotDataset(x2, label="X2", notch=False),
            BoxPlotDataset(x3, label="X3", vertical=False),
            BoxPlotDataset(x4, label="X4", notch=False, vertical=False),
        ],
        2,
        2,
        "random stuff",
    )


def test_plots():
    test_histogram()
    test_histograms_grid()
    test_line_plots_grid()
    test_line_plot()
    test_multiline_plot()
    test_box_plots()


if __name__ == "__main__":
    test_plots()
