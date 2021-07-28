class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        curr_tank = 0
        total_tank = 0
        starting_station = 0
        
        for i in range(0,len(gas)):
            total_tank = total_tank + gas[i] - cost[i]
            curr_tank += gas[i] - cost[i]
            
            if curr_tank<0:
                starting_station =i+1 
                
                curr_tank = 0
                
                
        if total_tank>=0:
            return starting_station
        
        else:
            return -1
        