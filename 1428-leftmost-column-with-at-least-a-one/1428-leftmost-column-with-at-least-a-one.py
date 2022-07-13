# """
# This is BinaryMatrix's API interface.
# You should not implement it, or speculate about its implementation
# """
#class BinaryMatrix(object):
#    def get(self, row: int, col: int) -> int:
#    def dimensions(self) -> list[]:

class Solution:
    
    def binSearch(self,row,left,right,binaryMatrix):
        
        Found = False
        
        while left<=right:
            mid = (left+right)//2

            if binaryMatrix.get(row,mid)==1:
                Found = True
                loc = mid
                right = mid-1
                
            else:
                left = mid+1
                
        if Found:
            return loc
        
        return -1

        
        
    
    def leftMostColumnWithOne(self, binaryMatrix: 'BinaryMatrix') -> int:
        r, c = binaryMatrix.dimensions()
        left = 0
        right = c-1
        rowN = 0
        pos = -1
        itr = 0
        answer = []
        
        while itr<r:
            if itr==0:
                pos = self.binSearch(itr,left,right,binaryMatrix)
                
            elif pos==-1:
                pos = self.binSearch(itr,left,right,binaryMatrix)
                
            elif pos>=0 and pos<c and binaryMatrix.get(itr,pos)==1:
                right = pos-1
                pos = self.binSearch(itr,left,right,binaryMatrix)
            
            if pos>=0:
                answer.append(pos)
            itr+=1
        
        if not answer:
            return -1
        
        return min(answer)
                
                
            
            
            
        