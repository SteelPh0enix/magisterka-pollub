from dataclasses import dataclass
from typing import List, cast
from matplotlib.axes import Axes
import matplotlib.pyplot as plt


@dataclass
class HistogramDataset:
    values: List[float]
    bins: int
    label: str = ""
    color: str = "blueviolet"


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
