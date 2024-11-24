class Solution(object):
    def diffWaysToCompute(self, expression):
        """
        :type expression: str
        :rtype: List[int]
        """
        res = []
        ops = {"+","-","*"}
        for i in range(len(expression)):
            op = expression[i]
            if op in ops:
                left = expression[0:i]
                right = expression[i+1:]
                left_res = self.diffWaysToCompute(left)
                right_res = self.diffWaysToCompute(right)
                for i in left_res:
                    for j in right_res:
                        first = str(i)
                        second = str(j)
                        res.append(eval(first+op+second))
        if len(res) == 0:
            res.append(int(expression))
        return res