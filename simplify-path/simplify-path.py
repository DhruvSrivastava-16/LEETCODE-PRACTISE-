class Solution:
    def simplifyPath(self, path: str) -> str:
        stk = []
        for op in path.split('/'):
            if op == '..':
                if stk:
                    stk.pop()
                    
            elif op == '.' or op=='':
                continue

            else:
                stk.append(op)
                    
                    
        answer = '/' + '/'.join(stk)
        
        return answer
                    
            