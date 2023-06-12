class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i,n in enumerate(nums):
            try:
                index = nums.index(target - n)
            except:
                index = -1
            if index >= 0 and index != i:
                return [i, index]
        return []
