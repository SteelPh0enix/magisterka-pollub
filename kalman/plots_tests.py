from dataclasses import dataclass
from typing import List, cast
from matplotlib.axes import Axes
import matplotlib.pyplot as plt


@dataclass
class HistogramDataset:
    values: List[float]
    label: str
    bins: int


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

            print(f"x = {x}, y = {y}, index = {index}")

            axis.hist(data.values, bins=data.bins, label=data.label)
            axis.set_title(data.label)

    plt.show()
