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

a=Solution()

s="abc"

# print(a.isPalindromic(s))
print(a.countSubstrings(s))
