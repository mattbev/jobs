from multiprocessing import Pipe, Process
from typing import Any, Callable, Iterable


def spawn(f: Callable) -> Callable:
    """
    Spawn a function call with a pipe.

    Args:
        f (Callable): Function for which to spawn a pipe.

    Returns:
        Callable: A function that executes the spawning of the pipe.
    """

    def fun(pipe: Pipe, x: Iterable[Any]) -> None:
        pipe.send(f(x))
        pipe.close()

    return fun


def parmap(f: Callable, X: Iterable[Any]) -> Iterable[Any]:
    """
    Parralelized mapping function.

    Args:
        f (Callable): Function to parallelize operation over.
        X (Iterable): The arguments to the function, over N
            function calls.
            
    Returns:
        Iterable: The N function outputs.
    """
    pipe = [Pipe() for _ in X]
    proc = [Process(target=spawn(f), args=(c, x)) for x, (_, c) in zip(X, pipe)]
    [p.start() for p in proc]
    [p.join() for p in proc]
    return [p.recv() for (p, _) in pipe]
