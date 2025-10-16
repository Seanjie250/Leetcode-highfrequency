class Solution:
    def lengthOfLastWord(self, s: str) -> int:
       
        s = s[::-1]
        s = str(s)
        clean_s = s.lstrip()
        rst = ''
        for ch in clean_s:
            if ch != ' ':
                rst += ch
            else:
                break
        return len(rst)



        