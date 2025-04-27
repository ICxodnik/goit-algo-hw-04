def merge_sort(arr):
    if len(arr) <= 1:
        return arr
    mid = len(arr) // 2
    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])
    return merge(left, right)

def merge_k_lists(lists):
    if not lists:
        return []
    while len(lists) > 1:
        merged_lists = []
        for i in range(0, len(lists), 2):
            left = lists[i]
            if i + 1 < len(lists):
                right = lists[i + 1]
                merged = merge(left, right)
                merged_lists.append(merged)
            else:
                merged_lists.append(left)  # якщо останній елемент без пари
        lists = merged_lists
    return lists[0]


def merge(left, right):
    merged = []
    i = j = 0
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            merged.append(left[i])
            i += 1
        else:
            merged.append(right[j])
            j += 1
    merged.extend(left[i:])
    merged.extend(right[j:])
    return merged