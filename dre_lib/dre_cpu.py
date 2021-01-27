
# TODO AEO - use Linting and Type Annotations

import multiprocessing


class CpuCount:

    _default_excluded = 1
    _default_excluded_percent = 0.25

    def __init__(self):
        self._cpu_count = multiprocessing.cpu_count()

    def adjusted_count(self, excluded_processors=_default_excluded):
        single_processor = 1

        # we must have at least one processor
        if self._cpu_count <= excluded_processors:
            return single_processor

        return self._cpu_count - excluded_processors

    def adjusted_count_by_percent(self, excluded_percent=_default_excluded_percent):
        excluded_processors = int(self._cpu_count * excluded_percent)
        return self.adjusted_count(excluded_processors)

    def total_count(self):
        return self._cpu_count

    def print_stats(self):
        print(f"{'Total CPU Count:':<20}{self._cpu_count:>4}")
        print(f"{'Adjusted Count:':<20}{self.adjusted_count():>4}")
        print(f"{'  By Percent:':<20}{self.adjusted_count_by_percent():>4}")
        print(f"{'  By 50 Percent:':<20}{self.adjusted_count_by_percent(0.5):>4}")
