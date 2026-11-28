class Solution(object):
    def findClosestElements(self, arr, k, x):
        """
        :type arr: List[int]
        :type k: int
        :type x: int
        :rtype: List[int]
        """
        i = 0
        while i < len(arr) and arr[i]<=x:
            i+=1
        if i == 0:
            return arr[:k]
        if i == len(arr):
            return arr[-k:]
        res = []
        if arr[i] == x:
            res.append(arr[i])
            left = i-1
            right = i+1
            k-= 1
        else:
            left = i-1
            right = i
        
        while len(res)<k:
            if left >= 0 and right < len(arr):
                if (abs(arr[left] - x) < abs(arr[right] - x)) or (abs(arr[left] - x) == abs(arr[right] - x) and arr[left] < arr[right]):
                    res.append(arr[left])
                    left-=1
                else:
                    res.append(arr[right])
                    right+=1
            elif left < 0:
                res.append(arr[right])
                right+=1
            else:
                res.append(arr[left])
                left-=1
        return sorted(res)