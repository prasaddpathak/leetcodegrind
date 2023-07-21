class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        l = len(nums)
        i=0
        while(i<len(nums)):
            if nums[i] == 0:
                del(nums[i])
            else:
                i +=1
        nums += [0] * (l - i)
