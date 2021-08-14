class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        c = 0
        if len(flowerbed)<=0:
            return False
        
        if len(flowerbed)==1:
            if flowerbed[0]==0:
                c+=1
                return c>=n
        
        if flowerbed[0]==0 and flowerbed[1]==0:
            c +=1
            flowerbed[0] = 1
            
        for i in range(0,len(flowerbed)-2):
            print(i)
            if flowerbed[i] != 1 and flowerbed[i+2]!=1 and flowerbed[i+1]!=1:
                print('G: ',i)
                c+=1 
                flowerbed[i+1] = 1
                
        if flowerbed[-1] == 0 and flowerbed[-2] == 0:
            flowerbed[-1] = 1
            c+=1
        print('C:',c)
        if c>=n:
            return True
        
        return False