import os
from typing import Any

from IPython.core.display import display
from IPython.display import Image
from tensorflow import keras

import ptmlib.charts as pch
from ptmlib.time import Stopwatch


def default_load_model_function(model_file_name: str):
    return keras.models.load_model(f'{model_file_name}.h5')


def default_fit_model_function(model: Any, train_set: Any, test_set: Any, epochs: int):
    return model.fit(train_set, validation_data=test_set, epochs=epochs)


def load_or_fit_model(model, model_file_name, train_set, test_set=None, epochs=1,
                      load_model_function=default_load_model_function,
                      fit_model_function=default_fit_model_function):
    history = None

    if os.path.exists(f'{model_file_name}.h5'):
        model = load_model_function(model_file_name)
        if os.path.exists(f'accuracy-{model_file_name}.png'):
            display(Image(filename=f'accuracy-{model_file_name}.png'))
        if os.path.exists(f'loss-{model_file_name}.png'):
            display(Image(filename=f'loss-{model_file_name}.png'))
    else:
        stopwatch = Stopwatch()
        stopwatch.start()
        history = fit_model_function(model, train_set, test_set, epochs)
        stopwatch.stop()
        model.save(f'{model_file_name}.h5')
        # TODO AEO add error handling to show_history_chart in case 'accuracy' is not available
        pch.show_history_chart(history, "accuracy", save_fig_enabled=True, file_name_suffix=model_file_name)
        pch.show_history_chart(history, "loss", save_fig_enabled=True, file_name_suffix=model_file_name)

    return model, history
