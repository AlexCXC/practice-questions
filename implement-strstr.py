class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        _next = [0 for _ in range(len(needle))]
        n_len = len(needle)
        h_len = len(haystack)
        for i in range(1, n_len):
            pass
