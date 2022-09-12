class Solution:
    def removeDuplicateLetters(self, s: str) -> str:
        
        charLocMap = defaultdict(int)
        
        for pos, char in enumerate(s):
            charLocMap[char] = pos
            
        print(charLocMap)
        seen = set()
        stk = []
        
        for key, value in enumerate(s):
            if not stk:
                
                stk.append(value)
                seen.add(value)
                
            else:
                
                if value not in seen:
                    while stk and value<stk[-1] and key<charLocMap[stk[-1]]:
                        print(stk)
                        seen.discard(stk.pop())
                        
                    stk.append(value)
                    seen.add(value)
                    
        return ''.join(stk)