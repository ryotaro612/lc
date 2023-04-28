"""Compute the median of time spent on a problem."""
import csv


def time_to_min(time):
    """Format HH:mm:ss to minutes."""
    h, m, s = time.split(":")
    return (int(h) * 3600 + int(m) * 60 + int(s)) / 60


def compute_median(difficulty):
    """Compute the median of time spent on a problem."""
    with open('./sessions.csv') as f:
        reader = csv.DictReader(f)
        times = sorted(
            [time_to_min(r["Time"]) for r in reader if r["Difficulty"] == difficulty]
        )
        if len(times) % 2:
            median = times[len(times) // 2]
        else:
            median = (times[len(times) // 2 - 1] + times[len(times) // 2]) / 2
        return [["Median(Elapsed time)"], None, [int(median)]]
