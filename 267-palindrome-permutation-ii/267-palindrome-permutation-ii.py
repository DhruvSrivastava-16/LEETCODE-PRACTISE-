class Solution:
    
    def backtrack(self,output,counter,s,temp):
        
        if len(temp) == len(s):
            output.append(temp)
            return 
        
        if len(s)%2!=0:
            print("HERE")
            for key, value in counter.items():
                
                if value%2!=0:
                    
                    counter[key]-=1
                    self.backtrack(output,counter,s,key)
                    counter[key]+=1
                    
                else:
                    
                    if value>=2:
                        print("2",key+temp+key)
                        counter[key]-=2
                        # print()
                        self.backtrack(output,counter,s,key+temp+key)
                        counter[key]+=2
                        
        else:
            
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
        
        print(temp,output)
        
        return output

# from collections import Counter

# class Solution:
#     def generatePalindromes(self, s: str) -> List[str]:
#         counter = Counter(s)
#         output = []
        
#         def backtrack(curr='', counter=counter):
#             if len(curr) == len(s):
#                 output.append(curr)
                
# 			# Start with each letter if length is odd
#             if not curr and len(s) % 2:
#                 for key in counter:
#                     counter[key] -= 1
#                     backtrack(key, counter)
#                     counter[key] += 1
					
#             # Build palindrome around current string  
#             else:
#                 for key, count in counter.items():
#                     if count >= 2:
#                         counter[key] -= 2
#                         backtrack(key + curr + key, counter)
#                         counter[key] += 2
        
#         backtrack()
#         return output