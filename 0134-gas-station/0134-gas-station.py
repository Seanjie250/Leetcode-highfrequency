class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        extra_gas_get = [0] * len(gas)

        for i in  range(0,len(gas)):
            extra_gas_get[i] = gas[i] - cost[i]
       
        total_gas,curr_gas,start = 0, 0 ,0

        for j in range(len(gas)):
            total_gas += extra_gas_get[j]

            curr_gas += extra_gas_get[j]

            if curr_gas < 0:
                start = j + 1
                curr_gas = 0

    
        return start if total_gas >= 0 else -1 

        
            



            

                    







        