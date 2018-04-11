"""
Given a string, your task is to count how many palindromic substrings in this string.

The substrings with different start indexes or end indexes are counted as different substrings even they consist of same characters.

Example 1:
Input: "abc"
Output: 3
Explanation: Three palindromic strings: "a", "b", "c".
Example 2:
Input: "aaa"
Output: 6
Explanation: Six palindromic strings: "a", "a", "a", "aa", "aa", "aaa".
Note:
The input string length won't exceed 1000.
"""


class Solution:
    def countSubstrings(self, s):
        """
        :type s: str
        :rtype: int
        """
        lenth=len(s)
        res=lenth
        for i in range(2,lenth+1):
            for j in range(lenth+1-i):
                if self.isPalindromic(s[j:j+i]):
                    res+=1
                    print(s[j:j+i])
        return res
                
                
    def isPalindromic(self,s):
        lenth=len(s)
        for i in range(lenth//2):
            if s[i]!=s[lenth-1-i]:
                return False
        return True