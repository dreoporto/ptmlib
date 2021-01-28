import multiprocessing


class CpuCount:

    _default_excluded: int = 1
    _default_excluded_percent: float = 0.25

    def __init__(self):
        self._cpu_count: int = multiprocessing.cpu_count()

    def adjusted_count(self, excluded_processors: int = _default_excluded) -> int:
        single_processor: int = 1

        # we must have at least one processor
        if self._cpu_count <= excluded_processors:
            return single_processor

        return self._cpu_count - excluded_processors

    def adjusted_count_by_percent(self, excluded_percent: float = _default_excluded_percent) -> int:
        excluded_processors = int(self._cpu_count * excluded_percent)
        return self.adjusted_count(excluded_processors)

    def total_count(self) -> int:
        return self._cpu_count

    def print_stats(self) -> None:
        print(f"{'Total CPU Count:':<20}{self._cpu_count:>4}")
        print(f"{'Adjusted Count:':<20}{self.adjusted_count():>4}")
        print(f"{'  By Percent:':<20}{self.adjusted_count_by_percent():>4}")
        print(f"{'  By 50 Percent:':<20}{self.adjusted_count_by_percent(0.5):>4}")
