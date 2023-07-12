# Private Class attributes

class Example: 
    def __init__(self): 
        self.__count = 10

    def increment(self):
        self.__count += 1
        

    def value(self):
        return self.__count

    def reset(self):
        self.__count = 0

exam = Example()
print(exam._Example__count)




