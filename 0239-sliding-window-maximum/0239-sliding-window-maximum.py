class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        n = len(nums)
        q = deque()
        rst = []
        for i in range(n):
            while q and nums[i] > nums[q[-1]]:
                q.pop()
            q.append(i)
            
            if q[0] + k - 1 < i:
                q.popleft()
            
            if i - k + 1 >= 0 :
                rst.append(nums[q[0]])
        return rst

        
