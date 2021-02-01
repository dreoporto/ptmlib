import matplotlib.pyplot as plt
import pandas as pd
from ptmlib.time import get_time_string
from typing import Any


def format_plt(fig_size: (int, int) = (10, 6)) -> None:
    plt.figure(figsize=fig_size)
    plt.grid(True, which='major')
    plt.grid(True, which='minor', alpha=0.3, linestyle='--')
    plt.minorticks_on()


def show_history_chart(history: Any, search_string: str, fig_size: (int, int) = (10, 6),
                       save_fig_enabled: bool = False) -> None:

    """
    Renders line charts for TensorFlow training history (ex: accuracy, loss),
    with corresponding validation data if available

    :param history: history object returned by TensorFlow fit()
    :param search_string: string to filter history; ex: accuracy, loss
    :param fig_size: chart size tuple; default is (10, 6)
    :param save_fig_enabled: save chart image with search_string-YYYYmmdd-HHMMSS.png file format
    :return: None
    """

    filtered_hist = {k: v for (k, v) in history.history.items() if search_string in k}

    pd.DataFrame(filtered_hist).plot(figsize=fig_size)
    plt.grid(True, which='major')
    plt.grid(True, which='minor', alpha=0.3, linestyle='--')
    plt.minorticks_on()

    if save_fig_enabled:
        plt.savefig(f"{search_string}-{get_time_string()}.png")

    plt.show()
