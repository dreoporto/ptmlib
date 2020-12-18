import time

# CURRENTLY ONLY SUPPORT WINDOWS AND COLAB
try:
    import winsound
except ImportError:
    winsound = None

try:
    from google.colab import output
except ImportError:
    output = None


def get_time_string():
    return time.strftime("%Y%m%d-%H%M%S")


class Stopwatch:
    _default_sound = 'https://upload.wikimedia.org/wikipedia/commons/0/05/Beep-09.ogg'

    def __init__(self):
        self._start_time = None

    def start(self):
        # display actual start time: useful for long-running tasks
        print("Start Time:", time.ctime())

        self._start_time = time.perf_counter()

    def stop(self, silent=False, sound_path=_default_sound):

        if self._start_time is None:
            raise ValueError('start time must be set by calling start() before stop()')

        # stop and show duration immediately
        end_time = time.perf_counter()
        print("End Time:  ", time.ctime())
        print(f'Elapsed seconds: {end_time - self._start_time:0.4f}'
              + f'({(end_time - self._start_time) / 60:0.2f} minutes)')

        # must reset
        self._start_time = None

        if not silent:
            if winsound is not None:
                winsound.Beep(400, 1000)
            if output is not None:
                # noinspection PyUnresolvedReferences
                output.eval_js(f'new Audio(\"{sound_path}\").play()')
