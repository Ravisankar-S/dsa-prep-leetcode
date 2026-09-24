class Solution:
    def longestContinuousSubstring(self, s: str) -> int:
        current = 1
        maximum = 1

        for i in range(1,len(s)):
            if ord(s[i]) == ord(s[i-1])+1:
                current += 1
            else:
                current = 1
            maximum = max(maximum,current)

        return maximum