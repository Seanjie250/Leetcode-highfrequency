class Solution:
    def minOperations(self, n: int) -> int:
        ans = 0

        while n:
            if n & 1 == 0:
                n >>= 1
                print(n)
            else:
                if n == 1 or n & 3 == 1:
                    n -= 1
                else:
                    n += 1
                ans += 1

        return ans