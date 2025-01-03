class Solution(object):
    def garbageCollection(self, garbage, travel):
        """
        :type garbage: List[str]
        :type travel: List[int]
        :rtype: int
        """
        G = garbage[0].count('G')
        P = garbage[0].count('P')
        M = garbage[0].count('M')
        G_travel, P_travel, M_travel = 0, 0, 0
        current=0
        for i in range(1, len(garbage)):
            g_count = garbage[i].count('G')
            G += g_count
            p_count = garbage[i].count('P')
            P += p_count
            m_count = garbage[i].count('M')
            M += m_count
            current += travel[i-1]
            G_travel = current if g_count else G_travel
            P_travel = current if p_count else P_travel
            M_travel = current if m_count else M_travel
        return sum([G, P, M, G_travel, P_travel, M_travel])