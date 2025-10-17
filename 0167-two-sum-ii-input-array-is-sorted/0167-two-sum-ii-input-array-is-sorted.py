class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        i ,j = 0 , len(numbers) - 1
        rst = []
        while i < j :
            if numbers[i] + numbers[j] > target:
                j -= 1
            if numbers[i] + numbers[j] < target:
                i += 1
            else:
                if numbers[i] + numbers[j] == target:
                    rst.append(i + 1)
                    rst.append(j + 1)
                    return rst
        return None


        