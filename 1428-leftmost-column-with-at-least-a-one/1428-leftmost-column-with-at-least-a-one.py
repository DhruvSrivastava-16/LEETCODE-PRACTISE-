# """
# This is BinaryMatrix's API interface.
# You should not implement it, or speculate about its implementation
# """
#class BinaryMatrix(object):
#    def get(self, row: int, col: int) -> int:
#    def dimensions(self) -> list[]:

class Solution:
    
    def binarySearch(self,start,end,binaryMatrix,row):
        
        mid = (start+end)//2
        pos = -1
        while start<=end:
            mid = (start+end)//2
            print(mid,row)
            if binaryMatrix.get(row,mid)==1:
                pos = mid
                end = mid - 1
                
            else:
                start = mid+1
                
        return pos
            
    def leftMostColumnWithOne(self, binaryMatrix: 'BinaryMatrix') -> int:
        
        row, col = binaryMatrix.dimensions()
        
        itr = 0
        
        start = 0
        end = col -1 
        
        answer = None
        
        while itr<row:
                
            position = self.binarySearch(start,end,binaryMatrix,itr)
            print(position,answer,itr)
            if position!=-1:
                if answer is not None:
                    answer = min(answer,position)
                else:
                    answer = position
                    
            itr+=1
            
            
        if answer is None:
            return -1
        
        return answer
                
            