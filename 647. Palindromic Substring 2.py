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
        res=0
        for mid in range(lenth):
            for maxlen in reversed(range(1+min(mid,lenth-1-mid))):
                print("maxlen:",maxlen)
                if self.isPalindromic(s[mid-maxlen:mid+maxlen+1]):
                    res+=maxlen+1
                    print(res)
                    break
        for mid in range(lenth-1):
            for maxlen in reversed(range(1+min(mid,lenth-2-mid))):
                print("maxlen:",maxlen)
                if self.isPalindromic(s[mid-maxlen:mid+maxlen+2]):
                    res+=maxlen+1
                    print(res)
                    break
        return res
                
                
    def isPalindromic(self,s):
        lenth=len(s)
        for i in range(lenth//2):
            if s[i]!=s[lenth-1-i]:
                return False
        return True
