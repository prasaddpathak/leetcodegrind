class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        # Sort both arrays
        s = sorted(s)
        t = sorted(t)

        # Traverse and check if the elements are equal
        for i in range(len(s)):
            if s[i] != t[i]:
                return t[i]
        
        # Return the last char as that is the only one left
        return t[len(s)]
