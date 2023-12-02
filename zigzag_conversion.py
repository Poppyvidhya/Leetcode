class Solution(object):
    def convert(self, s, numRows):
        if numRows == 1:
            return s
        res = ""
        for r in range(0, numRows):
            increment = 2 * (numRows-1)
            for i in range(r, len(s), increment):
                res += s[i]
                if (r>0 and r < numRows - 1 and i + increment - 2 * r < len(s)):
                    res += s[i + increment - 2 * r]
        return res
    
#TIME COMPLEXITY : O(numRows * len(s))
#SPACE COMPLEXITY : O(1)