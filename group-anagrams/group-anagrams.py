class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        # d1 = {x: "".join(sorted(x)) for x in strs}
        # d2 = {}
        # alsit = list({x for x in d1.values()})
        # grouped = {
        #     x : [ k for k,v in d1.items() if v == x ] for x in alsit
        # }
        # return grouped.values()
        groupMap = defaultdict(list)
        for s in strs:  groupMap["".join(sorted(s))].append(s)
        return groupMap.values()