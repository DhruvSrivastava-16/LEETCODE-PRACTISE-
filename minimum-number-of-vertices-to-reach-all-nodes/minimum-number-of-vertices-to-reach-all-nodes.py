class Solution:
    def findSmallestSetOfVertices(self, n: int, edges: List[List[int]]) -> List[int]:
        incoming = {i:0 for i in range(0,n)}
        print(incoming)
        
        for i in edges:
            incoming[i[1]]+=1
                
        ans = [i for i in incoming if incoming[i]==0]
        return(ans)