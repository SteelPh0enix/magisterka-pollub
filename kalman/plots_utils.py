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
    labels_y: List[str] | None = None
    labels_x: List[str] | None = None
    ylabel: str | None = None
    xlabel: str | None = None
    label: str | None = None
    color: str = "blueviolet"
    linestyle: str = "-"
    linewidth: float = 3.0
    marker: str | None = None


def show_line_plots_grid(datasets: List[PlotDataset], title: str | None = None):
    pass


# def show_line_plot(dataset: PlotDataset):
#     # i know pyplot does that when only 'y' values are passed
#     # but i don't see why wouldn't i do it anyway
#     # kinda not sure if it'll work when x=None, maybe i'll check that later
#     # inb4 lazy programming, yes, it is, it's a bit too hot to think
#     x = value_or_default(dataset.values_x, list(range(len(dataset.values_y))))

#     fig,ax = plt.subplots(1, 1)

#     lines = plt.plot(
#         xdata=x,
#         ydata=dataset.values_y,
#         color=dataset.color,
#         linestyle=dataset.linestyle,
#         linewidth=dataset.linewidth,
#         marker=dataset.marker,
#     )
