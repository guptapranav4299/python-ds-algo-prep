class Solution:
    # tabulation
    def minCut(self, s: str) -> int:
        cuts = []

        for i in range(len(s) + 1):
            cuts.append(i - 1)  # Length is n+1 .... 0th index is dummy... s[i] ->  cuts[i+1]

        for i in range(len(s)):
            j = 1
            while i - j >= 0 and i + j < len(s) and s[i - j] == s[i + j]:
                cuts[i + j + 1] = min(cuts[i + j + 1], cuts[i - j - 1 + 1] + 1)
                j += 1

            j = 0
            while i - j >= 0 and i + j + 1 < len(s) and s[i - j] == s[i + j + 1]:
                cuts[i + j + 1 + 1] = min(cuts[i + j + 1 + 1], cuts[i - j - 1 + 1] + 1)
                j += 1

            cuts[i + 1] = min(cuts[i + 1], cuts[i - 1 + 1] + 1)

        return cuts[-1]

