def avg(lst):
    return sum(lst)//5

class Solution:
    
    def highFive(self, items: List[List[int]]) -> List[List[int]]:
        marks = {} 
        for i in items:

            if i[0] not in marks:
                marks[i[0]] = [i[1]]
            else:
                marks[i[0]].append(i[1])
                
        print(marks)
        
        ans = []
        for j in sorted(marks.keys()):
            marks[j].sort()
            print(marks[j][-5:])
            avge = avg( marks[j][-5:])
            ans.append([j,avge])
            
        return ans