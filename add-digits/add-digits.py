class Solution:
    def addDigits(self,num: int) -> int:
        if num<9:
            return num

        temp = 0

        while num>0:
            temp = temp+num%10
            num = num//10

        if temp>9:
            #print(temp)
            return self.addDigits(temp)

        else:
            return temp