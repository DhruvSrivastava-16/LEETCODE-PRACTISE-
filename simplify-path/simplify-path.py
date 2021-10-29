class Solution:
    def simplifyPath(self, path: str) -> str:
        
        stk = []
        path = path.split('/')
        for i in path:
            if i=='..':
                if stk:
                    stk.pop()
                    
            elif i=='.' or i=='':
                continue
            
            else:
                stk.append(i)
                
                
        return '/' + '/'.join(stk)