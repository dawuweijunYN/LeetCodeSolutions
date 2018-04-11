"""
Given a non-negative integer c, your task is to decide whether there're two integers a and b such that a2 + b2 = c.

Example 1:
Input: 5
Output: True
Explanation: 1 * 1 + 2 * 2 = 5
Example 2:
Input: 3
Output: False
"""


class Solution(object):
    def judgeSquareSum(self, c):
        """
        :type c: int
        :rtype: bool
        """
        highList=self.SquareNum(c//2,c)
        for i in highList:
            j=c-i
            lowList=self.SquareNum(j,j)
            if lowList: return True
        return False
    
    def SquareNum(self,low,high):
        ans=[]
        i=self.Square(low)
        temp=i**2
        while(temp<=high):
            ans.append(temp)
            i+=1
            temp=i**2
        return ans
    
    def Square(self,Num):
        if Num == 0:
            return 0
        i=1
        while(i**2-Num>0.5 or Num-i**2>0.5):
            i=(i+Num/i)/2.0
        if (i//1)**2>=Num:return i//1
        else: return i//1+1