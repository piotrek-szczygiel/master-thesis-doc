import matplotlib.pyplot as plt
import matplotlib
import pandas as pd

PAGE_WIDTH = 5.23724  # inches

matplotlib.use("pgf")
matplotlib.rcParams.update(
    {
        "pgf.texsystem": "pdflatex",
        "font.family": "serif",
        "text.usetex": True,
        "pgf.rcfonts": False,
    }
)


def plot_times(languages, chrome, firefox, filename, max=None, ylabel="Czas wykonania (ms)", fmt="%d"):
    bar_width = 0.35

    fig, ax = plt.subplots(figsize=(PAGE_WIDTH, 3))
    ax.set_ymargin(0.1)

    xs = range(len(languages))
    if len(languages) == 2:
        xs = [0.75, 2.25]
    elif len(languages) == 3:
        xs = [0.15, 1.5, 2.85]

    ticks_x, ticks_val = [], []

    for i, (language, time) in enumerate(zip(languages, chrome)):
        bars = ax.bar(xs[i], time, bar_width, color="#006e3d", edgecolor="black", linewidth=0.1, label="Google Chrome")
        ax.bar_label(bars, padding=2, fmt=fmt, size="small")
        ticks_x.append(xs[i] + bar_width / 2)
        ticks_val.append(language)

    for i, (language, time) in enumerate(zip(languages, firefox)):
        bars = ax.bar(
            xs[i] + bar_width,
            time,
            bar_width,
            color="#be1d24",
            edgecolor="black",
            linewidth=0.1,
            label="Mozilla Firefox",
        )
        ax.bar_label(bars, padding=2, fmt=fmt, size="small")

    ax.set_xticks(ticks_x, ticks_val)
    ax.set(ylabel=ylabel)
    handles, labels = plt.gca().get_legend_handles_labels()
    by_label = dict(zip(labels, handles))
    plt.legend(by_label.values(), by_label.keys())

    if max:
        plt.ylim(top=max)

    plt.xlim(-0.5, 3 + bar_width + 0.5)

    fig.savefig(f"{filename}.pgf")
    plt.close(fig)


def benchmark():
    chrome = pd.read_csv("benchmark_chrome.csv")
    firefox = pd.read_csv("benchmark_firefox.csv")

    def plot(type):
        data_chrome = chrome.loc[chrome["type"] == type]
        data_firefox = firefox.loc[firefox["type"] == type]
        plot_times(data_chrome["language"], data_chrome["time"], data_firefox["time"], type)

    plot("sort6")
    plot("fib40")


def matrix():
    plot_times(["JavaScript", "Rust", "Rust SIMD"], [1001, 665, 399], [1169, 507, 415], "matrix")


def nbody():
    plot_times(
        ["JavaScript", "Rust"],
        [5.9, 6.4],
        [6.3, 6.5],
        "nbody",
        max=10,
        ylabel="Średni czas jednego kroku symulacji (ms)",
        fmt="%.1f",
    )


def edges():
    bar_width = 0.35

    fig, ax = plt.subplots(figsize=(PAGE_WIDTH, 3))
    ax.set_ymargin(0.1)

    languages = ["JavaScript", "WebAssembly"]
    chrome = [51.11, 7.43]
    firefox = [14.93, 9.57]
    native = 0.609476

    fmt = "%.2f"

    xs = [0.15, 1.5, 2.85]

    ticks_x, ticks_val = [], []

    for i, (language, time) in enumerate(zip(languages, chrome)):
        bars = ax.bar(xs[i], time, bar_width, color="#006e3d", edgecolor="black", linewidth=0.1, label="Google Chrome")
        ax.bar_label(bars, padding=2, fmt=fmt, size="x-small")
        ticks_x.append(xs[i] + bar_width / 2)
        ticks_val.append(language)

    for i, (language, time) in enumerate(zip(languages, firefox)):
        bars = ax.bar(
            xs[i] + bar_width,
            time,
            bar_width,
            color="#be1d24",
            edgecolor="black",
            linewidth=0.1,
            label="Mozilla Firefox",
        )
        ax.bar_label(bars, padding=2, fmt=fmt, size="small")

    bars = ax.bar(
        xs[2], native, bar_width, color="#2c2e35", edgecolor="black", linewidth=0.1, label="Aplikacja natywna"
    )
    ax.bar_label(bars, padding=2, fmt=fmt, size="small")
    ticks_x.append(xs[2])
    ticks_val.append("Natywna")

    ax.set_xticks(ticks_x, ticks_val)
    ax.set(ylabel="Średni czas procesowania klatki (ms)")
    handles, labels = plt.gca().get_legend_handles_labels()
    by_label = dict(zip(labels, handles))
    plt.legend(by_label.values(), by_label.keys())
    plt.xlim(-0.5, 3.5)
    fig.savefig("edges.pgf")
    plt.close(fig)


benchmark()
matrix()
nbody()
edges()
