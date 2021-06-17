class Solution:
    def bracket_generator(self,out,curr_idx,n,openn,close,l):
     
    #base case
        if curr_idx == 2*n:


           l.append(out)    
          # print(out)

           return

        #recursion
        if (openn<n):
            out= out + '('
            self.bracket_generator(out, curr_idx + 1, n, openn + 1, close,l)
            out = out[:-1]


        if(close<openn):
            out = out + ')'        
            self.bracket_generator(out, curr_idx + 1, n, openn , close + 1,l)
            out = out[:-1]

    
        return l

    def generateParenthesis(self, n: int) -> List[str]:
        l = []
        return self.bracket_generator("",0,n,0,0,l)
        