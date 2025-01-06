class Solution:
    def isPalindrome(self, x: int) -> bool:
        xs= str(x)
        xsr= xs[::-1]
        if xs == xsr:
            return True
        else:
            return False
        