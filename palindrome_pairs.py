class Solution(object):
    def palindromePairs(self, words):
        """
        :type words: List[str]
        :rtype: List[List[int]]
        """
        def pal(w,str,end):
            while str<end:
                if w[str]!=w[end]:
                    return False
                str+=1
                end-=1
            return True
        N=len(words)
        output=[]
        pair={w:i for i,w in enumerate(words)}
        for i in range(N):
            w=words[i]
            if w=="":
                for j in range(N):
                    if i!=j and pal(words[j],0,len(words[j])-1):
                        output.append([i,j])
                        output.append([j,i])
                continue
            rev=w[::-1]
            if rev in pair and pair[rev]!=i:
                output.append([i,pair[rev]])
            for k in range(1,len(w)):
                if pal(w,0,k-1) and w[k:][::-1] in pair:
                    output.append([pair[w[k:][::-1]],i])
                if pal(w,k,len(w)-1) and w[:k][::-1] in pair:
                    output.append([i,pair[w[:k][::-1]]])
        return output
    
    
#TIME COMPLEXITY : O(N*k^2)
#SPACE COMPLEXITY : O(N*k)