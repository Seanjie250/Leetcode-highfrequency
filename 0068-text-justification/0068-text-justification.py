class Solution:
    def fullJustify(self, words: List[str], maxWidth: int) -> List[str]:
        rst , cur = [] , []
        cur_width = 0
        for word in words:
            if cur_width + len(word) + len(cur) > maxWidth:
                total_spaces = maxWidth - cur_width
                gaps = len(cur) - 1
                if gaps == 0:
                    rst.append(cur[0] + ' '*total_spaces)
                else:
                    space_per_gap = total_spaces // gaps
                    extra_spaces = total_spaces % gaps
                    line = ''
                    for i , w in enumerate(cur):
                        line += w
                        if i < gaps:
                            line += ' '*space_per_gap
                            if i < extra_spaces:
                                line += ' '
                    rst.append(line)
                cur , cur_width = [] , 0
            cur.append(word)
            cur_width += len(word)
        last_line = ' '.join(cur)
        remaining_spaces = maxWidth - len(last_line)
        rst.append(last_line + ' '*remaining_spaces)
        return rst

        