class Solution:
    def isCovered(self, ranges: List[List[int]], left: int, right: int) -> bool:
        arr = []
        for number in range(left, right + 1):
            arr.append(number)
            
        for left, right in ranges:
            for i in range(left, right + 1):
                if i in arr:
                    arr.remove(i)
        return True if len(arr) == 0 else False