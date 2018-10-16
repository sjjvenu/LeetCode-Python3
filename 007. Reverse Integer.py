class Solution:
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        sign = 1;
        if x < 0:
            sign = -1
            x = sign*x
            
        x = int(str(x)[::-1])
        
        if sign*x < math.pow(-2,31) or sign*x > math.pow(2,31)-1:
            return 0
        else:
            return sign*x