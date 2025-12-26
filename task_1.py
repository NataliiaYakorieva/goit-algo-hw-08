import heapq
from typing import List


def min_cost_to_connect_cables(cables: List[int]) -> int:
    """
    Calculates the minimum total cost to connect all cables into one.
    Each time, two shortest cables are connected, and the cost is their sum.
    The process repeats until all cables are connected into one.

    Args:
        cables (List[int]): List of cable lengths.

    Returns:
        int: The minimum total cost to connect all cables.
    """
    if not cables:
        return 0

    heapq.heapify(cables)
    total_cost = 0

    while len(cables) > 1:
        first = heapq.heappop(cables)
        second = heapq.heappop(cables)
        cost = first + second
        total_cost += cost

        heapq.heappush(cables, cost)

    return total_cost


if __name__ == "__main__":
    test_cables = [4, 3, 2, 6]
    result = min_cost_to_connect_cables(test_cables)
    print("Minimum cost to connect all cables:", result)
    # Expected output: 29
