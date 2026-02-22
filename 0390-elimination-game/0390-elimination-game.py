class Solution:
    def lastRemaining(self, n: int) -> int:
        left = True
        remaining = n
        head = 1
        step = 1
        while remaining > 1:
            if left or remaining % 2 == 1:
                head += step
                print(head)
            remaining //= 2
            step *= 2
            left = not left
        return head


        