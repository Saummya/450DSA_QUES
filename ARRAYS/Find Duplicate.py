class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        m1=max(nums)
        a1=[0]*(m1+1)

        for i in range(len(nums)):
            a1[nums[i]]+=1

        for i in range(m1+1):
            if a1[i]>1:
                return i

        return -1

     
       
        
