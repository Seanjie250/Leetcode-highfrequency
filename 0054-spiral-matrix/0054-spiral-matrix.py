from typing import List

class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        count = 0
        total_amount = len(matrix) * len(matrix[0])
        offset = 0
        rst = []

        while count < total_amount:
            # top row
            for i in range(offset, len(matrix[0]) - offset):
                rst.append(matrix[offset][i])
                count += 1
                if count == total_amount:
                    return rst

            # right column
            for i in range(offset + 1, len(matrix) - offset):
                rst.append(matrix[i][len(matrix[0]) - offset - 1])
                count += 1
                if count == total_amount:
                    return rst

            # bottom row
            for i in range(len(matrix[0]) - offset - 2, offset - 1, -1):
                if len(matrix) - offset - 1 != offset:  # avoid double-counting
                    rst.append(matrix[len(matrix) - offset - 1][i])
                    count += 1
                    if count == total_amount:
                        return rst

            # left column
            for i in range(len(matrix) - offset - 2, offset, -1):
                if len(matrix[0]) - offset - 1 != offset:  # avoid double-counting
                    rst.append(matrix[i][offset])
                    count += 1
                    if count == total_amount:
                        return rst

            offset += 1

        return rst


