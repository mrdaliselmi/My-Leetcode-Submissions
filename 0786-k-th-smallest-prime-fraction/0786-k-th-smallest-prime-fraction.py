import heapq
class Solution:
    def kthSmallestPrimeFraction(self, arr: List[int], k: int) -> List[int]:
        pq = []
        for i in range(len(arr)):
            heapq.heappush(pq, ((arr[i] / arr[-1]), i, len(arr) - 1))
        for _ in range(k - 1):
            cur = heapq.heappop(pq)
            up_index = cur[1]
            down_index = cur[2] - 1
            if down_index > up_index:
                heapq.heappush(pq, (
                    (arr[up_index] / arr[down_index]), 
                    up_index, 
                    down_index
                ))
        result = heapq.heappop(pq)
        return [arr[result[1]], arr[result[2]]]