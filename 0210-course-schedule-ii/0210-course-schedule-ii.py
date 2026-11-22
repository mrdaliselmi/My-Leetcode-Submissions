class Solution(object):
    def findOrder(self, numCourses, prerequisites):
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: List[int]
        """
        prereq = {course: [] for course in range(numCourses)}
        for course, pre in prerequisites:
            prereq[course].append(pre)
        
        res = []
        visited = set()
        curr = set()
        def dfs(course):
            if course in curr:
                return False
            if course in visited:
                return True
            curr.add(course)
            for pre in prereq[course]:
                if dfs(pre) == False:
                    return False
            visited.add(course)
            curr.remove(course)
            res.append(course)
            return True
        
        for course in range(numCourses):
            if dfs(course) == False:
                return []
        return res