class Solution:
    def reverseBits(self, n: int) -> int:
        rst = ''
        while n > 0:
            rst  = str(n % 2) + rst
            n = n // 2
        rst = rst.zfill(32)
        rst = list(rst)
        val = 1
        ans = 0
        for i in range(32):
            if rst[i] == '1':
                ans += val
            val *= 2
        return ans



