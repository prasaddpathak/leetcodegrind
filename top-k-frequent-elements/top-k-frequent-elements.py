class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        sortedc = sorted(Counter(nums).items(), key=lambda x:x[1], reverse=True)
        res = [ sortedc[i][0] for i in range(k)]
        return res