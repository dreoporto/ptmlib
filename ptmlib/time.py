import time
import os

try:
    from playsound import playsound
except ImportError:
    playsound = None

try:
    import winsound  # requires windows; only used if playsound/colab unavailable
except ImportError:
    winsound = None

try:
    from google.colab import output
except ImportError:
    output = None


def get_time_string():
    return time.strftime("%Y%m%d-%H%M%S")


class Stopwatch:

    sounds_bee5 = 'media/bee5.mp3'
    sounds_dore = 'media/dore.mp3'
    default_colab_sound_url = 'https://upload.wikimedia.org/wikipedia/commons/0/05/Beep-09.ogg'

    def __init__(self):
        self._start_time = None

    def start(self):
        # display actual start time: useful for long-running tasks
        print("Start Time:", time.ctime())

        self._start_time = time.perf_counter()

    def stop(self, silent=False, sound_path=sounds_bee5, colab_sound_url=default_colab_sound_url):

        if self._start_time is None:
            raise ValueError('start time must be set by calling start() before stop()')

        # stop and show duration immediately
        end_time = time.perf_counter()
        print("End Time:  ", time.ctime())
        print(f'Elapsed seconds: {end_time - self._start_time:0.4f}'
              + f' ({(end_time - self._start_time) / 60:0.2f} minutes)')

        # must reset
        self._start_time = None

        if not silent:
            self._alert_finished(sound_path, colab_sound_url)

    def _alert_finished(self, sound_path, colab_sound_url):

        dirname = os.path.dirname(__file__)

        # determine audio file to use
        if os.path.exists(sound_path):
            pass  # no changes needed
        elif os.path.exists(os.path.join(dirname, sound_path)):
            sound_path = os.path.join(dirname, sound_path)
        elif os.path.exists(os.path.join(dirname, self.sounds_bee5)):
            # switch back to default
            sound_path = os.path.join(dirname, self.sounds_bee5)
        else:
            sound_path = None

        if playsound is not None and sound_path is not None:
            # PLAYSOUND ON LOCAL
            playsound(sound_path)
        elif output is not None:
            # RUNNING IN COLAB
            # noinspection PyUnresolvedReferences
            output.eval_js(f'new Audio(\"{colab_sound_url}\").play()')
        elif winsound is not None:
            winsound.Beep(400, 1000)
