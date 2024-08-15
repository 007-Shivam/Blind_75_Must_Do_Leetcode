class Solution(object):
    def climbStairs(self, n):
        if n == 1:
            return 1
        if n == 2:
            return 2
        
        t2 = 2  
        t1 = 1

        for i in range(3, n + 1):
            current = t2 + t1  
            t1 = t2  
            t2 = current  
        
        return t2
