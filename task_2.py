import heapq
from typing import List


def merge_k_lists(lists: List[List[int]]) -> List[int]:
    """
    Merges k sorted lists into a single sorted list using a min-heap.

    Args:
        lists (List[List[int]]): A list of sorted integer lists.

    Returns:
        List[int]: A single sorted list containing all elements from the input lists.
    """
    heap = []
    result = []

    for i, lst in enumerate(lists):
        if lst:
            heapq.heappush(heap, (lst[0], i, 0))

    while heap:
        val, list_idx, element_idx = heapq.heappop(heap)
        result.append(val)

        if element_idx + 1 < len(lists[list_idx]):
            next_tuple = (lists[list_idx][element_idx + 1],
                          list_idx, element_idx + 1)
            heapq.heappush(heap, next_tuple)

    return result


if __name__ == "__main__":
    test_lists = [[1, 4, 5], [1, 3, 4], [2, 6]]
    merged_list = merge_k_lists(test_lists)
    print("Merged sorted list:", merged_list)
    # Expected output: [1, 1, 2, 3, 4, 4, 5, 6]
