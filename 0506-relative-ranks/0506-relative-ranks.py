class Solution(object):
    def findRelativeRanks(self, score):
        """
        :type score: List[int]
        :rtype: List[str]
        """
        score = [(i,value) for i,value in enumerate(score)]
        score.sort(key= lambda x:x[1], reverse=True)
        for i in range(len(score)):
            if i == 0:
                score[i] = (score[i][0],score[i][1],"Gold Medal")
            elif i == 1:
                score[i] = (score[i][0],score[i][1],"Silver Medal")
            elif i == 2:
                score[i] = (score[i][0],score[i][1],"Bronze Medal")
            else:
                score[i] = (score[i][0],score[i][1],str(i+1))
        score.sort(key= lambda x:x[0])
        return [x[2] for x in score]
        
