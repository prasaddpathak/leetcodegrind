class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if len(nums) == 0 : return 0
        # Sort the numbers and get the set
        snums = sorted(set(nums))
        maxSeq = 1
        q = 1
        print(snums)
        for i in range(len(snums) -1):    
            # check if the difference is 1 between two conseq numbers
            if snums[i+1] - snums[i] == 1: 
                q += 1
                maxSeq = max(maxSeq, q)
            else:
                q = 1

        return maxSeq