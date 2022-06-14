class Solution:
    def sequentialDigits(self, low: int, high: int) -> List[int]:
        
        sample = "123456789"
        ans = []
        n = 10
        
        for length in range(len(str(low)),len(str(high))+1):
            
            for st in range(n-length):
                num = int(sample[st:st+length])
                if num >= low and num<=high:
                    ans.append(num)
                    
                    
                    
        return ans