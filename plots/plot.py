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
    fig.savefig(filename, bbox_inches="tight")
    plt.close(fig)


def benchmark_chrome():
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
            None,
            "Czas sortowania (ms)",
            f"{type}_{file_suffix}.svg",
            fmt="%.1f ms",
        )

    plot_type(chrome, "sort6")
    plot_type(firefox, "sort6")

    plot_type(chrome, "fib40")
    plot_type(firefox, "fib40")


benchmark_chrome()
