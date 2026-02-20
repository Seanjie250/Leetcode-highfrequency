class Solution:
    def removeDuplicates(self, s: str, k: int) -> str:
        count = [['$' , 0]]

        for c in s:
            if count[-1][0] == c:
                count[-1][1] += 1
                if count[-1][1] == k:
                    count.pop()
            else:
                count.append([c , 1])
        print(count)
        return ''.join(c * cnt for c , cnt in count)





        