class Solution(object):
    def leastInterval(self, tasks, n):
        """
        :type tasks: List[str]
        :type n: int
        :rtype: int
        """
        available = [-frequency for frequency in Counter(tasks).values()]
        heapq.heapify(available)

        cooling_down = deque()
        interval = 0

        while available or cooling_down:
            while cooling_down and cooling_down[0][0] <= interval:
                _, remaining = cooling_down.popleft()
                heapq.heappush(available, -remaining)

            if available:
                remaining = -heapq.heappop(available) - 1

                if remaining:
                    cooling_down.append(
                        (interval + n + 1, remaining)
                    )

            interval += 1

        return interval