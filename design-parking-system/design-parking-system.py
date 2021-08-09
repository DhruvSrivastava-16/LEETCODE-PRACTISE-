class ParkingSystem:

    def __init__(self, big: int, medium: int, small: int):
        self.cap = [[big,0],[medium,0],[small,0]]
      
    def addCar(self, carType: int) -> bool:
        sm = 3
        med = 2
        big = 1
        
        if self.cap[carType-1][1]<self.cap[carType-1][0]:
            self.cap[carType-1][1]+=1
            return True
        
        return False
        


# Your ParkingSystem object will be instantiated and called as such:
# obj = ParkingSystem(big, medium, small)
# param_1 = obj.addCar(carType)