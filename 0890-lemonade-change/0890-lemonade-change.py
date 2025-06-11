class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:
        cashier = defaultdict(int)
        for bill in bills:
            if bill == 5:
                cashier[5] += 1
            elif bill == 10:
                if cashier[5] == 0:
                    return False
                else:
                    cashier[5] -= 1
                    cashier[10] += 1
            elif bill == 20:
                if cashier[10] >0 and cashier[5] >0:
                    cashier[5] -= 1
                    cashier[10] -= 1
                elif cashier[5] >= 3:
                    cashier[5] -= 3
                else:
                    return False
        return True





        