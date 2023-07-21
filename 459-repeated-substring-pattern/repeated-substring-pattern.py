class Solution:
    def repeatedSubstringPattern(self, s: str) -> bool:
        n = 1
        while (n <= len(s)/2):
            if( "".join([s[0:n]] * int(len(s)/n)) == s ): return True
            n +=1
        return False