class Solution:
    def maxActiveSectionsAfterTrade(self, s: str) -> int:
        n = len(s)
        runs = []
        i = 0
        while i < n:
            j = i
            while j < n and s[j] == s[i]:
                j += 1
            runs.append((s[i], j - i))
            i = j
        
        original_ones = s.count('1')
        
        max_pair = 0
        for k in range(len(runs) - 2):
            c1, len1 = runs[k]
            c2, len2 = runs[k + 1]
            c3, len3 = runs[k + 2]
            if c1 == '0' and c2 == '1' and c3 == '0':
                max_pair = max(max_pair, len1 + len3)
        
        return original_ones + max_pair