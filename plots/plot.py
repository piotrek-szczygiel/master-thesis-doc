import matplotlib.pyplot as plt
import matplotlib
import pandas as pd

width = 5.23724  # inches

matplotlib.use("pgf")
matplotlib.rcParams.update(
    {
        "pgf.texsystem": "pdflatex",
        "font.family": "serif",
        "text.usetex": True,
        "pgf.rcfonts": False,
    }
)

colors = {
    "JavaScript": "#efd81d",
    "AssemblyScript": "#0076c6",
    "Rust": "#ef4900",
    "Zig": "#ef9f1c",
}


def bar_plot(xs, ys, color, ylabel, filename, fmt="%s", log=False):
    ys_pos = range(len(ys))
    fig, ax = plt.subplots(figsize=(width, 3))
    ax.set_ymargin(0.1)
    bars = ax.bar(ys_pos, ys, color=color)
    ax.bar_label(bars, padding=2, fmt=fmt)
    ax.set_xticks(ys_pos, xs)

    if log:
        ax.set_yscale("log")

    ax.set(ylabel=ylabel)
    fig.savefig(filename)
    plt.close(fig)


def benchmark():
    chrome = pd.read_csv("benchmark_chrome.csv")
    firefox = pd.read_csv("benchmark_firefox.csv")

    def plot_type(df, type):
        data = df.loc[df["type"] == type]

        if df is chrome:
            file_suffix = "chrome"
        elif df is firefox:
            file_suffix = "firefox"

        bar_plot(
            data["language"],
            data["time"],
            [colors[lang] for lang in data["language"]],
            "Czas wykonania (ms)",
            f"{type}_{file_suffix}.pgf",
            fmt="%d ms",
        )

    plot_type(chrome, "sort6")
    plot_type(firefox, "sort6")

    plot_type(chrome, "fib40")
    plot_type(firefox, "fib40")


def nbody():
    bar_plot(
        ["JavaScript", "Rust"],
        [5.9, 6.4],
        "Średni czas jednego kroku symulacji (ms)",
        "nbody_chrome.pgf",
        fmt="%.1f ms",
    )

    bar_plot(
        ["JavaScript", "Rust"],
        [6.3, 6.5],
        "Średni czas jednego kroku symulacji (ms)",
        "nbody_firefox.pgf",
        fmt="%.1f ms",
    )


def matrix():
    bar_plot(
        ["JavaScript", "Rust", "Rust SIMD"],
        [994, 417, 365],
        "Czas wykonania (ms)",
        "matrix_chrome.pgf",
        fmt="%d ms",
    )

    bar_plot(
        ["JavaScript", "Rust", "Rust SIMD"],
        [1171, 534, 458],
        "Czas wykonania (ms)",
        "matrix_firefox.pgf",
        fmt="%d ms",
    )


def edges():
    bar_plot(
        [
            "JS (Chrome)",
            "JS (Firefox)",
            "WASM (Chrome)",
            "WASM (Firefox)",
            "Rust (Native)",
        ],
        [51.11, 14.93, 7.43, 9.57, 0.609476],
        "Czas procesowania klatki (ms)",
        "edges.pgf",
        fmt="%.2f ms",
    )


benchmark()
# nbody()
# matrix()
# edges()
