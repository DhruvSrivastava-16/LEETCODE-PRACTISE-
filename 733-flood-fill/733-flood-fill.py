class Solution:
    dx = [-1,0,1,0]
    dy = [0,1,0,-1]
    
    def helper(self, sr, sc, image, newColor, nColor,visited):
        if sr<0 or sr>=len(image) or sc<0 or sc>=len(image[0]) or image[sr][sc]==newColor:
            return 
        visited.add((sr,sc))
        if image[sr][sc]==nColor:
            image[sr][sc] = newColor

        
            self.helper(sr+1,sc,image,newColor,nColor,visited)
            self.helper(sr,sc+1,image,newColor,nColor,visited)
            self.helper(sr,sc-1,image,newColor,nColor,visited)
            self.helper(sr-1,sc,image,newColor,nColor,visited)
    
    def floodFill(self, image: List[List[int]], sr: int, sc: int, newColor: int) -> List[List[int]]:
        
        visited = set()
        self.helper(sr, sc, image, newColor,image[sr][sc],visited)
        return image
        
        