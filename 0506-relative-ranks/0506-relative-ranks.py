class Solution(object):
    def findRelativeRanks(self, score):
        """
        :type score: List[int]
        :rtype: List[str]
        """
        score = [(i,value) for i,value in enumerate(score)]
        score.sort(key= lambda x:x[1], reverse=True)
        score= [(score[i][0],"Gold Medal") if i==0 else (score[i][0],"Silver Medal") if i==1 else (score[i][0],"Bronze Medal") if i==2 else (score[i][0],str(i+1)) for i in range(len(score))]
        score.sort(key= lambda x:x[0])
        return [x[1] for x in score]
        
