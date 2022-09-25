class Solution:
    def checkIfPrerequisite(self, numCourses: int, prerequisites: List[List[int]], queries: List[List[int]]) -> List[bool]:
        
        mat = [[float('inf') for i in range(numCourses)] for j in range(numCourses)]
        
        
        for preq in prerequisites:
            mat[preq[0]][preq[1]] = 1
        
        
        for k in range(numCourses):
            for i in range(numCourses):
                for j in range(numCourses):
                    
                    if mat[i][j]>mat[i][k] + mat[k][j]:
                        mat[i][j] = mat[i][k] + mat[k][j]
        
        answer = []
                        
        for query in queries:
            i = query[0]
            j = query[1]
                
            if mat[i][j] == float('inf'):
                answer.append(False)
            else:
                answer.append(True)
                
        return answer
        