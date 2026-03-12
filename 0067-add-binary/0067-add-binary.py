class Solution:
    def addBinary(self, a: str, b: str) -> str:
        val = int(a, 2) + int(b , 2)
        print(val)
        return format(val , 'b')
        