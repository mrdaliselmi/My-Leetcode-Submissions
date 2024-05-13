class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        carry=0
        for i in range(len(digits)-1,-1,-1):
            if (i==len(digits)-1):
                digits[i]+=1
            else:
                digits[i]+=carry
            if (digits[i]//10):
                carry=digits[i]//10
                digits[i]=digits[i]%10
            else:
                carry=0
                break
        if carry:
            digits= [carry]+ digits
        return digits