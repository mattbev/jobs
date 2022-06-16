from typing import Any, Callable, Dict, Iterable, List, Tuple

from .multiprocessing import parmap


class Jobs:
    def add(self):
        """
        Add a job to be executed.
        """
        raise NotImplementedError

    def execute(self) -> Iterable[Any]:
        """
        Execute all jobs in queue.

        Returns:
            Iterable: the output of each job
        """
        raise NotImplementedError

class MultiprocessJobs(Jobs):
    def __init__(self, queue: List[Tuple[Callable, Tuple, Dict]] = []):
        super().__init__()
        self.queue = queue

    def add(self, f: Callable, *args, **kwargs):
        """
        Add a job to be executed.

        Args:
            f (Callable): the function to execute with the job,
                followed in-order by any arguments.
        """
        self.queue.append((f, args, kwargs))

    def execute(self) -> Iterable[Any]:
        """
        Execute all jobs in the queue.

        Returns:
            Iterable: The output of each job
        """

        def run(job):
            f, args, kwargs = job
            return f(*args, **kwargs)

        results = parmap(run, self.queue)

        return results
