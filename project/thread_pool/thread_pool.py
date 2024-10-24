import threading
from typing import Callable, Any, Tuple, Optional


class ThreadPool:
    """
    A simple thread pool implementation using the threading module.

    Attributes:
        num_threads (int): Number of threads in the pool.
        tasks (list): List of tasks to be executed by threads.
        lock (threading.Lock): Lock to synchronize access to the tasks list.
        threads (list): List of threads in the pool.
        stop_signal (threading.Event): Event to signal threads to stop working.
    """

    def __init__(self, num_threads: int) -> None:
        """
        Initialize the thread pool.

        Args:
            num_threads (int): Number of threads to create in the pool.
        """
        self.tasks: list[
            Tuple[Callable, Tuple[Any, ...], dict[str, Any], "ResultWrapper"]
        ] = []
        self.lock = threading.Lock()
        self.threads: list[threading.Thread] = []
        self.num_threads = num_threads
        self.stop_signal = threading.Event()

        for _ in range(num_threads):
            thread = threading.Thread(target=self.worker)
            thread.start()
            self.threads.append(thread)

    def worker(self) -> None:
        """
        Worker function that each thread runs to execute tasks from the pool.
        Continuously checks for new tasks until a stop signal is received.
        """
        while not self.stop_signal.is_set():
            task: Optional[Callable] = None
            args: Optional[Tuple[Any, ...]] = None
            kwargs: Optional[dict[str, Any]] = None
            result_wrapper: Optional["ResultWrapper"] = None

            with self.lock:
                if self.tasks:
                    task, args, kwargs, result_wrapper = self.tasks.pop(0)

            if task:
                try:
                    result = task(*args, **kwargs)
                    result_wrapper.set_result(result)
                except Exception as e:
                    result_wrapper.set_error(e)
            else:
                threading.Event().wait(0.1)  # Sleep a little to avoid busy-waiting

    def enqueue(self, task: Callable, *args: Any, **kwargs: Any) -> "ResultWrapper":
        """
        Submit a task to the thread pool.

        Args:
            task (Callable): The task (function) to be executed.
            *args: Positional arguments for the task function.
            **kwargs: Keyword arguments for the task function.

        Returns:
            ResultWrapper: A wrapper to obtain the result of the task execution.
        """
        result_wrapper = ResultWrapper()
        with self.lock:
            self.tasks.append((task, args, kwargs, result_wrapper))
        return result_wrapper

    def dispose(self, wait: bool = True) -> None:
        """
        Stop all threads and shut down the pool.

        Args:
            wait (bool): Whether to wait for all threads to finish.
        """
        self.stop_signal.set()
        if wait:
            for thread in self.threads:
                thread.join()


class ResultWrapper:
    """
    A wrapper class to handle the result of a task executed by a thread.

    Attributes:
        _result (Any): The result of the executed task.
        _error (Optional[Exception]): An exception raised during task execution, if any.
        _completed (threading.Event): An event to indicate task completion.
    """

    def __init__(self) -> None:
        """
        Initialize a ResultWrapper instance.
        """
        self._result: Optional[Any] = None
        self._error: Optional[Exception] = None
        self._completed = threading.Event()

    def set_result(self, result: Any) -> None:
        """
        Set the result of the task execution.

        Args:
            result (Any): The result to set.
        """
        self._result = result
        self._completed.set()

    def set_error(self, error: Exception) -> None:
        """
        Set an error if the task execution failed.

        Args:
            error (Exception): The exception raised during task execution.
        """
        self._error = error
        self._completed.set()

    def result(self, timeout: Optional[float] = None) -> Any:
        """
        Get the result of the task execution.

        Args:
            timeout (Optional[float]): Maximum time to wait for the result.

        Returns:
            Any: The result of the executed task.

        Raises:
            Exception: If an error occurred during task execution.
        """
        self._completed.wait(timeout)
        if self._error:
            raise self._error
        return self._result
