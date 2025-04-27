import random
import timeit
from merge_sort import merge_sort
from insertion_sort import insertion_sort
from timsort import timsort 

sizes = [100, 1000, 5000, 10000]

def generate_array(size):
    return [random.randint(0, 100000) for _ in range(size)]

def test_sorting_algorithms():
    for size in sizes:
        arr = generate_array(size)

        print(f"\nРозмір масиву: {size}")

        time_insertion = timeit.timeit(lambda: insertion_sort(arr.copy()), number=1)
        print(f"Insertion Sort: {time_insertion:.6f} секунд")

        time_merge = timeit.timeit(lambda: merge_sort(arr.copy()), number=1)
        print(f"Merge Sort: {time_merge:.6f} секунд")

        time_timsort = timeit.timeit(lambda: timsort(arr.copy()), number=1)
        print(f"Timsort: {time_timsort:.6f} секунд")

        time_sorted = timeit.timeit(lambda: sorted(arr.copy()), number=1)
        print(f"Built-in sorted(): {time_sorted:.6f} секунд")

test_sorting_algorithms()
