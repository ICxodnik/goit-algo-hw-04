from merge_sort import merge
from insertion_sort import insertion_sort

def timsort(arr):
    RUN = 32
    n = len(arr)

    # Крок 1: Сортування малих частин сортуванням вставками
    for start in range(0, n, RUN):
        end = min(start + RUN, n)
        insertion_sort(arr[start:end])

    # Крок 2: Злиття частин сортуванням злиттям
    size = RUN
    while size < n:
        for left in range(0, n, 2*size):
            mid = min(n, left + size)
            right = min(n, left + 2*size)
            merged = merge(arr[left:mid], arr[mid:right])
            arr[left:left+len(merged)] = merged
        size *= 2
    return arr