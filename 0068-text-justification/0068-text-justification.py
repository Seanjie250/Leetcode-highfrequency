class Solution:
    def calculatelength(self, words, maxWidth, start):
        total_len = 0
        count = 0
        i = start

        while i < len(words):
            word_len = len(words[i])
            # need +1 space between words except the first
            if total_len + word_len + count <= maxWidth:
                total_len += word_len
                i += 1
                count += 1
            else:
                break
        return count, total_len  # only pure word length

    def division(self, words, maxWidth, length, num, is_last=False):
        # Handle single word or last line
        if num == 1 or is_last:
            line = " ".join(words)
            line += " " * (maxWidth - len(line))
            return line

        total_space = maxWidth - length
        base_space = total_space // (num - 1)
        extra_space = total_space % (num - 1)

        rst = ""
        for i in range(num - 1):
            rst += words[i]
            rst += " " * (base_space + (1 if i < extra_space else 0))
        rst += words[-1]
        return rst

    def fullJustify(self, words: List[str], maxWidth: int) -> List[str]:
        rst = []
        i = 0
        while i < len(words):
            num, length = self.calculatelength(words, maxWidth, i)
            is_last = (i + num >= len(words))
            rst.append(self.division(words[i:i + num], maxWidth, length, num, is_last))
            i += num
        return rst
