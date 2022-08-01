import matplotlib.pyplot as plt
import matplotlib
import pandas as pd
from scipy.interpolate import make_interp_spline
import numpy as np

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


def network():
    fig, ax = plt.subplots(figsize=(PAGE_WIDTH, 3.5))
    ax.set_ymargin(0.1)

    color_ws, color_rtc = "#006e3d", "#be1d24"

    websocket = [
        31.8,
        31.9,
        32.0,
        31.7,
        31.5,
        31.3,
        32.1,
        32.1,
        31.3,
        31.1,
        31.4,
        31.4,
        32.0,
        31.5,
        31.4,
        31.5,
        31.6,
        32.2,
        32.0,
        31.7,
        31.1,
    ]

    webrtc = [
        34.0,
        33.1,
        33.2,
        33,
        38.3,
        36.2,
        37.4,
        35.3,
        33.9,
        38.3,
        32.9,
        34.8,
        36.6,
        42.2,
        34,
        35.5,
        34.5,
        34.1,
        36.3,
        33.6,
        35.1,
    ]

    assert len(websocket) == len(webrtc)

    x = list(range(len(websocket)))

    websocket_spline = make_interp_spline(x, websocket)
    webrtc_spline = make_interp_spline(x, webrtc)

    x_spline = np.linspace(min(x), max(x), len(x) * 100)
    y_spline_websocket = websocket_spline(x_spline)
    y_spline_webrtc = webrtc_spline(x_spline)

    ax.plot(x_spline, y_spline_webrtc, color=color_rtc, linewidth=0.5)
    ax.plot(x_spline, y_spline_websocket, color=color_ws, linewidth=0.5)

    ax.scatter(x, webrtc, label="WebRTC", color=color_rtc, marker=".")
    ax.scatter(x, websocket, label="WebSocket", color=color_ws, marker=".")
    ax.legend()

    webrtc_mean = [np.mean(webrtc)] * (len(x) + 2)
    ax.plot([-1] + x + [21], webrtc_mean, color=color_rtc, linestyle="--", linewidth=0.5, label="WebRTC avg.")

    websocket_mean = [np.mean(websocket)] * (len(x) + 2)
    ax.plot([-1] + x + [21], websocket_mean, color=color_ws, linestyle="--", linewidth=0.5, label="WebSocket avg.")

    ax.set_xlim(-1, 21)
    plt.xticks(np.arange(min(x), max(x) + 2, 5))

    plt.xlabel("Czas trwania testu (s)")
    plt.ylabel("Round Trip Time (ms)")

    fig.savefig("network.pgf")
    plt.close(fig)


network()
benchmark()
matrix()
nbody()
edges()
