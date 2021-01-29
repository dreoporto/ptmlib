# PTMLib - Pendragon Tiny ML Library

## Summary

**PTMLib** is a set of utilities that I have used with Machine Learning frameworks such as Scikit-Learn and TensorFlow.  The purpose is to eliminate code that I kept repeating in multiple projects.  

- **ptmlib.time.Stopwatch** - measure the time it takes to complete a long-running task, with an audio alert for task completion
- **ptmlib.cpu.CpuCount** - get info on CPUs available, with options to adjust/exclude based on a specific number/percentage.  Useful for setting `n_jobs` in Scikit-Learn tools that support multiple CPUs, such as `RandomForestClassifier`
- **ptmlib.charts** - render separate line charts for TensorFlow accuracy and loss, with corresponding validation data if available

*This code is brought to you by yours truly at [Pendragon AI](https://www.pendragonai.com)*

## ptmlib.time.Stopwatch

The `Stopwatch` class lets you measure the amount of time it takes to complete a long-running task. This can be useful for evaluating different machine learning models.

When `stop()` is called, an audio prompt will alert you that the task has completed. This helps when you are time constrained and multi-tasking while your code is executing, for example taking the [TensorFlow Developer Certificate](https://www.tensorflow.org/certificate) exam.

### Example:

```
stopwatch = Stopwatch()

...

stopwatch.start()

history = model.fit(
    training_images,
    training_labels,
    validation_split=hp_validation_split,
    epochs=hp_epochs,
    callbacks=[early_callback]
)

stopwatch.stop()
```

### Output:

```
Start Time: Thu Jan 28 16:57:32 2021
Epoch 1/50
1500/1500 [==============================] - 2s 1ms/step - loss: 0.5316 - accuracy: 0.8086 - val_loss: 0.4141 - val_accuracy: 0.8503

...

1500/1500 [==============================] - 2s 1ms/step - loss: 0.2337 - accuracy: 0.9101 - val_loss: 0.3212 - val_accuracy: 0.8879
End Time:   Thu Jan 28 16:58:03 2021
Elapsed seconds: 30.8191 (0.51 minutes)
```

Start Time and End Time/Elapsed Seconds/Minutes are output when the `start()` and `stop()` methods are called, respectively.  All other information in the above example output will be generated based on your ML framework.  

Stopwatch has been tested using Scikit-Learn and TensorFlow, and can be used for any long-running Python code for which you want to measure execution time performance, or be notified of task completion.

Stopwatch has been tested on Windows (VS Code, PyCharm IDEs and Jupyter Notebook) and Google Colab environments.

## ptmlib.cpu.CpuCount

The CpuCount class provides information on the number of CPUs available on the host machine.  The exact number of *logical* CPUs is returned by the `total_count()` method.

Knowing your CPU count, you can programmatically set the number of processors used in Scikit-Learn tools that support the `n_jobs` parameter, such as `RandomForestClassifier` and `model_selection.cross_validate`.

In many cases (ex: a developer desktop), you will not want to use *all* your available processors for a task.  The `adjusted_count()` and `adjusted_count_by_percent()` methods allow you to specify the number and percentage of processors to exclude, with default exclusion values of `1` and `0.25`, respectively.  The *defaults* are reflected in the `print_stats()` output in the example below.

### Example:
```
cpu_count = CpuCount()
cpu_count.print_stats()

max_cpu = cpu_count.adjusted_count(excluded_processors=2)

...

rnd_clf = RandomForestClassifier(
    n_estimators=hp_estimators, 
    random_state=hp_random_state, 
    n_jobs=max_cpu
)
```

### Output:
```
Total CPU Count:      16
Adjusted Count:       15
  By Percent:         12
  By 50 Percent:       8
```

While certain Scikit-Learn classifiers/tools benefit greatly from concurrent multi-CPU processing,  TensorFlow deep learning acceleration [requires a supported GPU](https://www.tensorflow.org/install/gpu) or [TPU](https://cloud.google.com/tpu).  As far as CPUs are concerned, TensorFlow handles this automatically; there is no benefit to using CpuCount here.