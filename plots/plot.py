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


def benchmark():
    chrome = pd.read_csv("benchmark_chrome.csv")
    firefox = pd.read_csv("benchmark_firefox.csv")

    def plot_type(type):
        data_chrome = chrome.loc[chrome["type"] == type]
        data_firefox = firefox.loc[firefox["type"] == type]

        bar_width = 0.35

        fig, ax = plt.subplots(figsize=(PAGE_WIDTH, 3))
        ax.set_ymargin(0.1)

        ticks_x, ticks_val = [], []

        for i, (language, time) in enumerate(zip(data_chrome["language"], data_chrome["time"])):
            bars = ax.bar(i, time, bar_width, color="#4285f4", label="Google Chrome")
            ax.bar_label(bars, padding=2, fmt="%d ms", size="x-small")
            ticks_x.append(i + bar_width / 2)
            ticks_val.append(language)

        for i, (language, time) in enumerate(zip(data_firefox["language"], data_firefox["time"])):
            bars = ax.bar(i + bar_width, time, bar_width, color="orange", label="Mozilla Firefox")
            ax.bar_label(bars, padding=2, fmt="%d ms", size="x-small")

        ax.set_xticks(ticks_x, ticks_val)
        ax.set(ylabel="Czas wykonania (ms)")
        handles, labels = plt.gca().get_legend_handles_labels()
        by_label = dict(zip(labels, handles))
        plt.legend(by_label.values(), by_label.keys())
        fig.savefig(f"{type}.pgf")
        plt.close(fig)

    plot_type("sort6")
    plot_type("fib40")


# def nbody():
#     bar_plot(
#         ["JavaScript", "Rust"],
#         [5.9, 6.4],
#         "Średni czas jednego kroku symulacji (ms)",
#         "nbody_chrome.pgf",
#         fmt="%.1f ms",
#     )

#     bar_plot(
#         ["JavaScript", "Rust"],
#         [6.3, 6.5],
#         "Średni czas jednego kroku symulacji (ms)",
#         "nbody_firefox.pgf",
#         fmt="%.1f ms",
#     )


# def matrix():
#     bar_plot(
#         ["JavaScript", "Rust", "Rust SIMD"],
#         [994, 417, 365],
#         "Czas wykonania (ms)",
#         "matrix_chrome.pgf",
#         fmt="%d ms",
#     )

#     bar_plot(
#         ["JavaScript", "Rust", "Rust SIMD"],
#         [1171, 534, 458],
#         "Czas wykonania (ms)",
#         "matrix_firefox.pgf",
#         fmt="%d ms",
#     )


# def edges():
#     bar_plot(
#         [
#             "JS (Chrome)",
#             "JS (Firefox)",
#             "WASM (Chrome)",
#             "WASM (Firefox)",
#             "Rust (Native)",
#         ],
#         [51.11, 14.93, 7.43, 9.57, 0.609476],
#         "Czas procesowania klatki (ms)",
#         "edges.pgf",
#         fmt="%.2f ms",
#     )


benchmark()
# nbody()
# matrix()
# edges()
