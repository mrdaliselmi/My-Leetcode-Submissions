class Solution(object):
    def canCompleteCircuit(self, gas, cost):
        """
        :type gas: List[int]
        :type cost: List[int]
        :rtype: int
        """
        total, curr, index = 0, 0, 0
        for i in range(len(gas)):
            total += gas[i] - cost[i]
            curr += gas[i] - cost[i]
            if curr < 0:
                index = i + 1
                curr = 0
        if total >= 0:
            return index
        return -1