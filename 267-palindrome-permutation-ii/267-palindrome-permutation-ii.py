class Solution:
    
    def backtrack(self,output,counter,s,temp):
        
        if len(temp) == len(s):
            output.append(temp)
            return 
        
        if len(s)%2!=0:
            for key, value in counter.items():
                
                if value%2!=0:
                    
                    counter[key]-=1
                    self.backtrack(output,counter,s,key)
                    counter[key]+=1

                        
            
        for key, value in counter.items():

            if value>=2:

                counter[key]-=2
                self.backtrack(output,counter,s,key+temp+key)
                counter[key]+=2
                    
        
    def generatePalindromes(self, s: str) -> List[str]:
        
        counter = Counter(s)
        output = []
        temp = ""
        
        self.backtrack(output,counter,s,temp)
        
        # print(temp,output)
        
        return output

