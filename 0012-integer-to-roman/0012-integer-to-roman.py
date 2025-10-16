class Solution:
    def intToRoman(self, num: int) -> str:
        val = [
            (1000, 'M'),
            (900, 'CM'),
            (500, 'D'),
            (400, 'CD'),
            (100, 'C'),
            (90, 'XC'),
            (50, 'L'),
            (40, 'XL'),
            (10, 'X'),
            (9, 'IX'),
            (5, 'V'),
            (4, 'IV'),
            (1, 'I')
        ]
        rst = ""
        for v, symbol in val:
            count = num // v       # how many times this Roman symbol fits
            rst += symbol * count  # add it that many times
            num -= v * count       # subtract the value

        return rst
                

        