class Solution(object):
    def similarPairs(self, words):
        """
        :type words: List[str]
        :rtype: int
        """

        k=0
     
        for i in range(len(words)):
            for j in range(i+1,len(words)):
                if set(words[i]) == set(words[j]):
                    k+=1
        return k
        
     
