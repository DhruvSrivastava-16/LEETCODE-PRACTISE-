class MedianFinder:

    def __init__(self):
        self.data = []
        

    def addNum(self, num: int) -> None:
        self.data.append(num)
        

    def findMedian(self) -> float:
        self.data.sort()

        sz = len(self.data)
        if sz%2==0:
            m1 = len(self.data)//2
            m2 = m1 - 1

            return (self.data[m1]+self.data[m2])/2
            
        else:
            return (self.data[len(self.data)//2])

        


# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()