class Solution:
    def maximumUnits(self, boxTypes: List[List[int]], truckSize: int) -> int:
        boxTypes.sort(key = lambda var:var[1])
        print(boxTypes)
        currsize = 0 
        
        currbox = 0
        max_boxes = 0
        
        while currsize!=truckSize:
            if currbox == 0:
                if not boxTypes:
                    break
                temp=boxTypes.pop()
                currbox=temp[0]
                units=temp[1]
                
            currsize+=1
            max_boxes +=units
            currbox-=1
            
        print("CS: ",currsize)
        return(max_boxes)
                
            
        