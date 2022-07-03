class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        
        for itr in range(len(numbers)-1):
            
            low = itr+1
            high = len(numbers)-1
            mid = (low+high)//2
            find = target-numbers[itr]
            
            while low<=high:
                
                mid = (low+high)//2
                if numbers[mid]==find:
                    return [itr+1,mid+1]
                
                elif numbers[mid]<find:
                    low=mid+1
                    
                else:
                    high=mid-1
                    
                    