from typing import List

def The_Great_Run(N: int, k: int, arr: List[int]) -> int:
    window_sum = sum(arr[:k])
    maximum = window_sum

    for i in range(k, N):
        window_sum += arr[i] - arr[i - k]
        maximum = max(maximum, window_sum)

    return maximum


if __name__ == '__main__':
    N, k = map(int, input().split())
    path = list(map(int, input().split()))
    print(The_Great_Run(N, k, path))