class Solution(object):
    def mincostToHireWorkers(self, quality, wage, k):
        """
        :type quality: List[int]
        :type wage: List[int]
        :type k: int
        :rtype: float
        """
        n, cost = len(quality), float("inf")
        wq_ratio = [(float(w) / q, q) for w, q in zip(wage, quality)]
        total_q, q_heap = 0, []

        wq_ratio.sort(key=lambda x: x[0])
        for wq, q in wq_ratio:
            total_q += q
            heappush(q_heap, -q)

            if len(q_heap) > k:
                total_q += heappop(q_heap)
            
            if len(q_heap) == k:
                cost = min(cost, total_q * wq)

        return cost