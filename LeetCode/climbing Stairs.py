class Solutions:
    def climbStairs(self , n):

        """
        :type n: int
        :rtype: int
        """
        if n ==0:
            return  1
        elif n ==1:
            return 1

        a , b = 1 , 1

        for i in range(2 , n +1):
            a, b = b, a + b

            return b

obj = Solutions()
print(obj.climbStairs(4))