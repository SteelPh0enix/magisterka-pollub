from dataclasses import dataclass
from typing import List, cast
from matplotlib.axes import Axes
import matplotlib.pyplot as plt


@dataclass
class HistogramDataset:
    values: List[float]
    bins: int
    label: str | None = None
    ylabel: str | None = None
    xlabel: str | None = None
    color: str = "blueviolet"


def show_histogram(dataset: HistogramDataset):
    plt.hist(
        dataset.values, bins=dataset.bins, color=dataset.color, label=dataset.label
    )
    plt.xlabel(dataset.xlabel)
    plt.ylabel(dataset.ylabel)
    plt.title(dataset.label)
    plt.show()


def show_histograms_on_grid(
    datasets: List[HistogramDataset],
    columns: int,
    rows: int,
    title: str = "",
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

    plt.suptitle(title)
    plt.show()


@dataclass
class ChartDataset:
    values_y: List[float]
    values_x: List[float] | None = None
    labels_y: List[str] | None = None
    labels_x: List[str] | None = None
    ylabel: str | None = None
    xlabel: str | None = None
    label: str | None = None
    color: str = "blueviolet"
