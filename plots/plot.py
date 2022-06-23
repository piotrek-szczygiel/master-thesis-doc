import matplotlib.pyplot as plt
import pandas as pd


def bar_plot(xs, ys, title, ylabel, filename, fmt="%s", log=False):
    ys_pos = range(len(ys))
    fig, ax = plt.subplots(figsize=(9, 6))
    bars = ax.bar(ys_pos, ys)
    ax.bar_label(bars, fmt=fmt)
    ax.set_xticks(ys_pos, xs)

    if log:
        ax.set_yscale("log")

    ax.set(title=title, ylabel=ylabel)
    fig.savefig(filename, bbox_inches="tight", dpi=300)
    plt.close(fig)


def benchmark_chrome():
    chrome = pd.read_csv("benchmark_chrome.csv")
    firefox = pd.read_csv("benchmark_firefox.csv")

    def plot_type(df, type, title=None):
        data = df.loc[df["type"] == type]

        if df is chrome:
            file_suffix = "chrome"
        elif df is firefox:
            file_suffix = "firefox"

        bar_plot(
            data["language"],
            data["time"],
            title,
            "Czas sortowania (ms)",
            f"{type}_{file_suffix}.svg",
            fmt="%d ms",
        )

    plot_type(chrome, "sort6")  # , title="Sortowanie miliona liczb (Chrome)")
    plot_type(firefox, "sort6")  # , title="Sortowanie miliona liczb (Firefox)")

    plot_type(chrome, "fib40")  # , title="40 liczba Fibonacciego rekursywnie (Chrome)")
    plot_type(firefox, "fib40")  # , title="40 liczba Fibonacciego rekursywnie (Firefox)")


def nbody():
    bar_plot(
        ["JavaScript", "Rust"],
        [5.9, 6.4],
        None,  # "Symulacja N ciał (Chrome)",
        "Średni czas jednego kroku symulacji (ms)",
        "nbody_chrome.svg",
        fmt="%.1f ms",
    )

    bar_plot(
        ["JavaScript", "Rust"],
        [6.3, 6.5],
        None,  # "Symulacja N ciał (Firefox)",
        "Średni czas jednego kroku symulacji (ms)",
        "nbody_firefox.svg",
        fmt="%.1f ms",
    )


def matrix():
    bar_plot(
        ["JavaScript", "Rust", "Rust SIMD"],
        [994, 417, 365],
        None,  # "Dodawanie 1KB wektorów milion razy (Chrome)",
        "Czas wykonania (ms)",
        "matrix_chrome.svg",
        fmt="%d ms",
    )

    bar_plot(
        ["JavaScript", "Rust", "Rust SIMD"],
        [1171, 534, 458],
        None,  # "Dodawanie 1KB wektorów milion razy (Firefox)",
        "Czas wykonania (ms)",
        "matrix_firefox.svg",
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
        None,  # "Wykrywanie krawędzi w OpenCV",
        "Czas procesowania klatki (ms)",
        "edges.svg",
        fmt="%.2f ms",
    )


benchmark_chrome()
nbody()
matrix()
edges()
