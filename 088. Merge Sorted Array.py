"""Given two sorted integer arrays nums1 and nums2, merge nums2 into nums1 as one sorted array.Note:You may assume that nums1 has enough space (size that is greater or equal to m + n) to hold additional elements from nums2.The number of elements initialized in nums1 and nums2 are m and n respectively."""class Solution(object):    def merge(self, nums1, m, nums2, n):        """        :type nums1: List[int]        :type m: int        :type nums2: List[int]        :type n: int        :rtype: void Do not return anything, modify nums1 in-place instead.        """        temp=nums1[0:m+1]        i=0        j=0        while i<m or j<n:            if j==n:                nums1[i+j]=temp[i]                i+=1            elif i==m:                nums1[i+j]=nums2[j]                j+=1            elif  temp[i]<=nums2[j]:                nums1[i+j]=temp[i]                i+=1            else:                nums1[i+j]=nums2[j]                j+=1