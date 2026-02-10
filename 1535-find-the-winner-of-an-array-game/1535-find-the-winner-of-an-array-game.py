class Solution:
    def getWinner(self, arr: List[int], k: int) -> int:
       
        if k >= len(arr) - 1:
            return max(arr)
        
        champian = arr[0]
        win_count = 0

        for i in range(1,len(arr)):
            if champian > arr[i]:
                win_count += 1
            else:
                champian = arr[i]
                win_count = 1
            
            if win_count == k:
                return champian
        return champian

            

        