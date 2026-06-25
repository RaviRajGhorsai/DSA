"""

Travelling Salesman Problem

It is an NP problem to solve this.
But P problem to verify the solution.

"""


def verify_tsp(paths: list[list[int]], dist: int, actual_path: list[int]) -> bool:
    total_dist = 0
    for i in range(1, len(actual_path)):
        total_dist += paths[actual_path[i - 1]][actual_path[i]]

    return total_dist < dist


def tsp(cities: list[int], paths: list[list[int]], dist: int) -> bool:
    permutation = permutations(cities)

    for perm in permutation:
        total_dist = 0

        for i in range(1, len(perm)):
            total_dist += paths[perm[i - 1]][perm[i]]

        if total_dist < dist:
            return True
    return False


# don't touch below this line


def permutations(arr: list[int]) -> list[list[int]]:
    res = []
    res = helper(res, arr, len(arr))
    return res


def helper(res: list[list[int]], arr: list[int], n: int) -> list[list[int]]:
    if n == 1:
        tmp = arr.copy()
        res.append(tmp)
    else:
        for i in range(n):
            res = helper(res, arr, n - 1)
            if n % 2 == 1:
                arr[n - 1], arr[i] = arr[i], arr[n - 1]
            else:
                arr[0], arr[n - 1] = arr[n - 1], arr[0]
    return res
