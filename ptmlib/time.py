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


class AlertSounds:
    BEE5: str = 'media/bee5.mp3'
    DORE: str = 'media/dore.mp3'


class Stopwatch:

    default_colab_sound_url: str = 'https://upload.wikimedia.org/wikipedia/commons/3/3b/Bee5th.ogg'

    def __init__(self):
        self._start_time = None

    def start(self) -> None:
        # display actual start time: useful for long-running tasks
        print("Start Time:", time.ctime())

        self._start_time = time.perf_counter()

    def stop(self, silent: bool = False, sound_path: str = AlertSounds.BEE5,
             colab_sound_url: str = default_colab_sound_url) -> None:

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
            # DO NOT allow audio error to impact processing
            try:
                self._alert_finished(sound_path, colab_sound_url)
            except Exception as ex:
                print('STOPWATCH _alert_finished ERROR:', ex)

    @staticmethod
    def _alert_finished(sound_path: str, colab_sound_url: str) -> None:

        dirname = os.path.dirname(__file__)

        # determine audio file to use
        if os.path.exists(sound_path):
            pass  # no changes needed
        elif os.path.exists(os.path.join(dirname, sound_path)):
            # relative path
            sound_path = os.path.join(dirname, sound_path)
        elif os.path.exists(os.path.join(dirname, str(AlertSounds.BEE5))):
            # switch back to default
            sound_path = os.path.join(dirname, str(AlertSounds.BEE5))
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
