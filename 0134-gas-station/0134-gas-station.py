class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:

        extra_gas_get = [0] * len(gas)
        for i in range(len(gas)):
            extra_gas_get[i] = gas[i] - cost[i]

        total_gas , cur_gas , start = 0, 0, 0

        for j in range(len(gas)):
            total_gas += extra_gas_get[j]

            cur_gas += extra_gas_get[j]

            if cur_gas < 0:
                start = j + 1
                cur_gas = 0
            
        return start if total_gas >= 0 else -1



                

            



        
            



            

                    







        