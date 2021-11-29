import os
from typing import Any, List

import matplotlib.image as mpimg
import matplotlib.pyplot as plt
from tensorflow import keras

import ptmlib.charts as pch
from ptmlib.time import Stopwatch


def default_load_model_function(model_file_name: str):
    return keras.models.load_model(f'{model_file_name}.h5')


# TODO AEO - change train_set to x, y; change test_set to validation_data

def _default_fit_model_function(model: Any, train_set: Any, test_set: Any = None, epochs: int = 1):
    return model.fit(train_set, validation_data=test_set, epochs=epochs)


def load_or_fit_model(model: Any, model_file_name: str, train_set: Any, test_set: Any = None, epochs: int = 1,
                      metrics: List[str] = None, images_enabled=True,
                      load_model_function=default_load_model_function,
                      fit_model_function=_default_fit_model_function):
    history = None

    if os.path.exists(f'{model_file_name}.h5'):
        model = load_model_function(model_file_name)
        if images_enabled:
            _show_saved_images(metrics, model_file_name)
    else:
        stopwatch = Stopwatch()
        stopwatch.start()
        history = fit_model_function(model, train_set, test_set, epochs)
        stopwatch.stop()
        model.save(f'{model_file_name}.h5')
        if images_enabled:
            _show_new_images(history, model_file_name, metrics)

    return model, history


def _show_new_images(history: Any, model_file_name: str, metrics: List[str]):
    # TODO AEO add error handling to show_history_chart in case 'accuracy' is not available
    if metrics is not None:
        for metric in metrics:
            pch.show_history_chart(history, metric, save_fig_enabled=True, file_name_suffix=model_file_name)
    pch.show_history_chart(history, "loss", save_fig_enabled=True, file_name_suffix=model_file_name)


def _show_saved_images(metrics: List[str], model_file_name: str):
    if metrics is not None:
        for metric in metrics:
            if os.path.exists(f'{metric}-{model_file_name}.png'):
                _show_saved_image(f'{metric}-{model_file_name}.png')
    if os.path.exists(f'loss-{model_file_name}.png'):
        _show_saved_image(f'loss-{model_file_name}.png')


def _show_saved_image(filename: str):
    image_data = mpimg.imread(filename)
    plt.axis('off')
    plt.imshow(image_data)
    plt.show()
