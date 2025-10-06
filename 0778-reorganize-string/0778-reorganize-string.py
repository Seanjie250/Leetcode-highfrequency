from collections import Counter
class Solution:
    def reorganizeString(self, s: str) -> str:
        count = Counter(s)
        maxheap = [(-cnt,char) for char , cnt in count.items()]
        #make a maxheap
        heapq.heapify(maxheap)

        prev = None
        rst = []

        while maxheap or prev:
            if not maxheap and prev:
                return ""

            cnt , char = heapq.heappop(maxheap)
            rst.append(char)
            cnt += 1

            if prev:
                heapq.heappush(maxheap,prev)
                prev = 0
            if cnt != 0:
                prev = (cnt,char)

        return "".join(rst)

            



        

        