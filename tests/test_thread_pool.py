import pytest
from project.thread_pool.thread_pool import ThreadPool


def test_task_addition():
    def add(x, y):
        return x + y

    pool = ThreadPool(4)
    result = pool.enqueue(add, 3, 5)

    assert result.result() == 8, "Task should return the sum of 3 and 5"
    pool.dispose()


def test_multiple_tasks():
    def multiply(x, y):
        return x * y

    pool = ThreadPool(4)
    result1 = pool.enqueue(multiply, 2, 3)
    result2 = pool.enqueue(multiply, 5, 5)

    assert result1.result() == 6, "Task should return the product of 2 and 3"
    assert result2.result() == 25, "Task should return the product of 5 and 5"
    pool.dispose()


def test_exception_handling():
    def divide(x, y):
        return x / y

    pool = ThreadPool(4)
    result = pool.enqueue(divide, 10, 0)

    with pytest.raises(ZeroDivisionError):
        result.result()

    pool.dispose()


def test_delayed_result():
    import time

    def delayed_task():
        time.sleep(1)
        return "done"

    pool = ThreadPool(4)
    result = pool.enqueue(delayed_task)

    assert result.result(timeout=2) == "done", "Task should return 'done' after sleep"
    pool.dispose()


def test_concurrent_tasks():
    import time

    def quick_task(n):
        time.sleep(0.1)
        return n

    pool = ThreadPool(4)
    results = [pool.enqueue(quick_task, i) for i in range(10)]

    assert all(
        res.result(timeout=1) == i for i, res in enumerate(results)
    ), "Each task should return its respective input"
    pool.dispose()
