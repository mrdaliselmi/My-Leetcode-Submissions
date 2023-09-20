class Solution(object):
    def minCostClimbingStairs(self, cost):
        """
        :type cost: List[int]
        :rtype: int
        """
        mem = [0]*(len(cost)+1)
        for i in range(2,len(mem)):
            mem[i]=(min(mem[i-1]+cost[i-1],mem[i-2]+cost[i-2]))
        return mem[len(cost)]