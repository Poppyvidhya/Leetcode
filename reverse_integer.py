class Solution(object):
    def reverse(self, x):
        rev=0
        sign=-1
        if x>0:
            sign=1
        else:
            sign=-1
        x*=sign
        while x:
            rev = rev * 10 + x % 10
            x //=10
        return 0 if rev < -2**31 or rev > 2**31 -1  else sign * rev
    
#TIME COMPLEXITY : O(log10(x))
#SPACE COMPLEXITY : O(1)