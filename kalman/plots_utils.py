from dataclasses import dataclass
from typing import List, cast
from matplotlib.axes import Axes
import matplotlib.pyplot as plt
from pho_utils import value_or_default


@dataclass
class HistogramDataset:
    values: List[float]
    bins: int
    label: str | None = None
    ylabel: str | None = None
    xlabel: str | None = None
    color: str = "blueviolet"


def show_histograms_on_grid(
    datasets: List[HistogramDataset],
    columns: int,
    rows: int,
    title: str | None = None,
    squeeze: bool = False,
):
    _, ax = plt.subplots(rows, columns, squeeze=squeeze)

    for y in range(rows):
        for x in range(columns):
            index = (y * columns) + x
            axis = cast(Axes, ax[y][x])
            data = datasets[index]

            axis.hist(data.values, bins=data.bins, label=data.label, color=data.color)
            axis.set_title(data.label)
            axis.set_xlabel(data.xlabel)
            axis.set_ylabel(data.ylabel)

    plt.suptitle(title)
    plt.show()


def show_histogram(dataset: HistogramDataset):
    show_histograms_on_grid([dataset], 1, 1)


@dataclass
class PlotDataset:
    values_y: List[float]
    values_x: List[float] | None = None
    label: str | None = None
    ylabel: str | None = None
    xlabel: str | None = None
    color: str = "blueviolet"
    linestyle: str = "-"
    linewidth: float = 3.0
    marker: str | None = None


def show_line_plots_grid(
    datasets: List[PlotDataset],
    columns: int,
    rows: int,
    title: str | None = None,
    squeeze: bool = False,
):
    _, ax = plt.subplots(rows, columns, squeeze=squeeze)

    for y in range(rows):
        for x in range(columns):
            index = (y * columns) + x
            axis = cast(Axes, ax[y][x])
            data = datasets[index]

            # if there's no default x values, generate them
            # i do not want to depend on matplotlib for that
            x = value_or_default(data.values_x, list(range(len(data.values_y))))

            axis.plot(
                x,
                data.values_y,
                color=data.color,
                linestyle=data.linestyle,
                linewidth=data.linewidth,
                marker=data.marker,
            )
            axis.set_title(data.label)
            axis.set_xlabel(data.xlabel)
            axis.set_ylabel(data.ylabel)

    plt.suptitle(title)
    plt.show()


def show_line_plot(dataset: PlotDataset):
    show_line_plots_grid([dataset], 1, 1)
