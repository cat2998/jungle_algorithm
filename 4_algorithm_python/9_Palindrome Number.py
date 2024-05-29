class Solution:
    def isPalindrome(self, x: int) -> bool:
        x = str(x)
        l = len(x) // 2
        for i in range(l + 1):
            if x[i] != x[-(i + 1)]:
                return False
        return True