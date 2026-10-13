class Solution(object):
    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        digit_to_letters = {
            '2': 'abc',
            '3': 'def',
            '4': 'ghi',
            '5': 'jkl',
            '6': 'mno',
            '7': 'pqrs',
            '8': 'tuv',
            '9': 'wxyz',
        }
        res = []
        def dfs(i, current):
            if i>=len(digits):
                res.append(current)
                return
            digit = digits[i]
            for letter in digit_to_letters[digit]:
                dfs(i+1, current+letter)
        
        dfs(0,'')
        return res