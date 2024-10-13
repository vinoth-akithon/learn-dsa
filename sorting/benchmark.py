import time
import random
from typing import Callable, TypeVar
from bubble_sort import bubble_sort
from selection_sort import selection_sort
from insertion_sort import insertion_sort
from shell_sort import shell_sort
from merge_sort import merge_sort

T = TypeVar("T", int, float)


def benchmark(algo: Callable, arr: list[T]) -> float:
    start_time = time.time()
    algo(arr)
    end_time = time.time()
    return end_time - start_time

def run_benchmark():
    array_size = [100, 1000, 10000, 100000, 1000000, 10000000]
    algos = [merge_sort]
    results = []

    print(f"{'Array Size':<12} {'Algo':<{max([len(algo.__name__) for algo in algos])+5}} {'Time taken':<12}")
    print("-" * 48)
    for size in array_size:
        input_arr = [random.randint(0, 10000) for _ in range(size)]
        for algo in algos:
            total_time_taken = benchmark(algo, input_arr)
            results.append({
                "size": size,
                "algo": algo.__name__,
                "time": total_time_taken
            })
            print(f"{size:<12} {algo.__name__:<{max([len(algo.__name__) for algo in algos])+5}} {total_time_taken:.6f}s")


    # for result in results:
        # print(f"{result['size']:<12} {result['algo']:<{max([len(algo.__name__) for algo in algos])+5}} {result['time']:.6f}s")

run_benchmark()