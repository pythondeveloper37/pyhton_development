# Private Class attributes

class Example: 
    def __init__(self): 
        self._count = 10

    def increment(self):
        self._count += 1
        

    def value(self):
        return self._count

    def reset(self):
        self._count = 0

exam = Example()
print(exam._count)
print(exam.value())
print(exam._count)
