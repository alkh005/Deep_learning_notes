"""Create the plotted figures used by the Deep Learning Notes lessons."""

from pathlib import Path

import matplotlib

matplotlib.use("Agg")

import matplotlib.pyplot as plt
import numpy as np


OUT = Path(__file__).resolve().parents[1] / "docs" / "assets"
OUT.mkdir(parents=True, exist_ok=True)

plt.rcParams.update(
    {
        "font.family": "DejaVu Sans",
        "font.size": 11,
        "axes.titlesize": 15,
        "axes.labelsize": 11,
        "axes.spines.top": False,
        "axes.spines.right": False,
        "figure.facecolor": "#ffffff",
        "axes.facecolor": "#f8fafc",
        "axes.edgecolor": "#cbd5e1",
        "axes.labelcolor": "#334155",
        "xtick.color": "#475569",
        "ytick.color": "#475569",
        "text.color": "#0f172a",
        "grid.color": "#e2e8f0",
    }
)


def save_activation_plot() -> None:
    x = np.linspace(-5, 5, 500)
    curves = [
        (np.maximum(0, x), "ReLU", "#4f46e5"),
        (1 / (1 + np.exp(-x)), "Sigmoid", "#0891b2"),
        (np.tanh(x), "Tanh", "#ea580c"),
    ]
    fig, axes = plt.subplots(1, 3, figsize=(11, 3.4), constrained_layout=True)
    for ax, (y, name, color) in zip(axes, curves):
        ax.plot(x, y, color=color, linewidth=3)
        ax.axhline(0, color="#94a3b8", linewidth=0.8)
        ax.axvline(0, color="#94a3b8", linewidth=0.8)
        ax.grid(True, linewidth=0.7)
        ax.set_title(name, fontweight="bold")
        ax.set_xlabel("Input (z)")
        ax.set_xlim(-5, 5)
        ax.set_xticks([-4, -2, 0, 2, 4])
    axes[0].set_ylabel("Output")
    axes[0].set_ylim(-0.5, 5.3)
    axes[0].set_yticks([0, 2, 4])
    axes[1].set_ylim(-0.1, 1.1)
    axes[1].set_yticks([0, 0.5, 1])
    axes[2].set_ylim(-1.2, 1.2)
    axes[2].set_yticks([-1, 0, 1])
    fig.savefig(OUT / "activation-functions.png", dpi=180, bbox_inches="tight")
    plt.close(fig)


def save_loss_plot() -> None:
    epochs = np.arange(1, 31)
    train = 1.25 * np.exp(-epochs / 8) + 0.08
    validation = 1.0 * np.exp(-epochs / 9) + 0.16
    fig, ax = plt.subplots(figsize=(8, 4.2), constrained_layout=True)
    ax.plot(epochs, train, color="#4f46e5", linewidth=3, label="Training loss")
    ax.plot(epochs, validation, color="#0891b2", linewidth=3, label="Validation loss")
    ax.set_title("Example: loss falls as learning progresses", fontweight="bold", pad=14)
    ax.set_xlabel("Epoch (one pass through training examples)")
    ax.set_ylabel("Loss (smaller means fewer mistakes)")
    ax.set_xlim(1, 30)
    ax.set_ylim(0, 1.4)
    ax.set_xticks([1, 5, 10, 15, 20, 25, 30])
    ax.grid(True, linewidth=0.7)
    ax.legend(frameon=False, ncol=2, loc="upper right")
    fig.savefig(OUT / "training-loss.png", dpi=180, bbox_inches="tight")
    plt.close(fig)


if __name__ == "__main__":
    save_activation_plot()
    save_loss_plot()
    print(f"Saved plots to {OUT}")
