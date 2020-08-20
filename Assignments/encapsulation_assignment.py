


class Protected:
    def __init__(self):
        self._protectedVar = 6
        self.__privateVar = 13

    def getSum(self):
        obj1 = Protected()._protectedVar
        obj2 = Protected().__privateVar
        varSum = obj1 + obj2
        print("{} + {} = {}".format(obj1,obj2,varSum))

Protected().getSum()
        
    
