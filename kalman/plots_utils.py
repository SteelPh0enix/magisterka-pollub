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


def show_multiline_plot(
    datasets: List[PlotDataset],
    title: str | None = None,
    ylabel: str | None = None,
    xlabel: str | None = None,
    show_legend: bool = True,
):
    """Note: `xlabel` and `ylabel` dataset settings will be ignored. Use `ylabel` and `xlabel` function arguments instead."""
    _, ax = plt.subplots(1, 1)
    axis = cast(Axes, ax)

    for data in datasets:
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
            label=data.label,
        )

    axis.set_xlabel(xlabel)
    axis.set_ylabel(ylabel)
    plt.suptitle(title)
    if show_legend:
        plt.legend()
    plt.show()


@dataclass
class BoxPlotDataset:
    values: List[float] | List[List[float]]
    notch: bool = False
    vertical: bool = True
    label: str | None = None
    ylabel: str | None = None
    xlabel: str | None = None
    values_labels: List[str] | None = None


def show_box_plots_grid(
    datasets: List[BoxPlotDataset],
    rows: int,
    columns: int,
    title: str | None = None,
    squeeze: bool = False,
):
    _, ax = plt.subplots(rows, columns, squeeze=squeeze)

    for y in range(rows):
        for x in range(columns):
            index = (y * columns) + x
            axis = cast(Axes, ax[y][x])
            data = datasets[index]

            axis.boxplot(data.values, notch=data.notch, vert=data.vertical)
            axis.set_title(data.label)
            axis.set_xlabel(data.xlabel)
            axis.set_ylabel(data.ylabel)
            if data.values_labels is not None:
                axis.set_xticklabels(data.values_labels)

    plt.suptitle(title)
    plt.show()


def show_box_plot(dataset: BoxPlotDataset):
    show_box_plots_grid([dataset], 1, 1)
