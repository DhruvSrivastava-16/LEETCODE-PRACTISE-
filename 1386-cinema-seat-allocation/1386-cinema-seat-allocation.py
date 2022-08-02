class Solution:
    def maxNumberOfFamilies(self, n: int, reservedSeats: List[List[int]]) -> int:
        
        seatMap = defaultdict(set)
        total = 0
        pos1 = True
        pos2 = True
        pos3 = True
        
        for seat in reservedSeats:
            seatMap[seat[0]].add(seat[1])
            
        for row in seatMap.keys():
            pos1 = True
            pos2 = True
            pos3 = True
            
            for j in range(2,6):
                if not pos1:
                    break
                    
                if j in seatMap[row]:
                    pos1 = False
                    
            if pos1:
                total+=1
                
            for j in range(6,10):
                if not pos2:
                    break
                    
                if j in seatMap[row]:
                    pos2 = False
                    
            if pos2:
                total+=1
                
            if not pos1 and not pos2:
                
                for j in range(4,8):
                    if not pos3:
                        break

                    if j in seatMap[row]:
                        pos3 = False   
            
                if pos3:
                    total+=1
            
        rem = (n-len(seatMap.keys()))*2
            
        return total+rem