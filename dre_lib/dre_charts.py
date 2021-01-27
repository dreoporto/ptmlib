import matplotlib.pyplot as plt
import pandas as pd
from dre_lib.dre_time import get_time_string


def format_plt(fig_size=(10, 6)):
    plt.figure(figsize=fig_size)
    plt.grid(True, which='major')
    plt.grid(True, which='minor', alpha=0.3, linestyle='--')
    plt.minorticks_on()


def show_history_chart(history, search_string, fig_size=(10, 6), save_fig_enabled=False):
    filtered_hist = {k: v for (k, v) in history.history.items() if search_string in k}
    pd.DataFrame(filtered_hist).plot(figsize=fig_size)
    plt.grid(True, which='major')
    plt.grid(True, which='minor', alpha=0.3, linestyle='--')
    plt.minorticks_on()
    if save_fig_enabled:
        plt.savefig(f"{search_string}-{get_time_string()}.png")
    plt.show()
