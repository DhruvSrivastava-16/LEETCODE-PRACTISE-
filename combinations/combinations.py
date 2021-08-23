
class Solution:
    ans = []
    def helper(self,list_range: list[int],k: int,temp: list[int]) -> list[list[int]]:
        if k == 0:
            self.ans.append(temp[:])
            return

        #ans = []
        for j in range(0,len(list_range)):
            temp.append(list_range[j])
            self.helper(list_range[j+1:],k-1,temp)
            temp.pop()

        return self.ans


    def combine(self,n: int,k: int) -> list[list[int]]:
        list_range = [i for i in range(1,n+1)]
        self.ans = []
        answer = self.helper(list_range,k,[])
        return answer
        