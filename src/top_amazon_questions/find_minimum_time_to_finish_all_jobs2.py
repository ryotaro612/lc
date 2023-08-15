class Solution:
    def minimumTime(self, jobs: List[int], workers: List[int]) -> int:
        jobs.sort()
        workers.sort()
        result = 0
        for job, worker in zip(jobs, workers):
            result = max(result, (job + worker - 1)//worker)
        return result
