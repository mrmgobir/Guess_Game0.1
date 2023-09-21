class Number:
    def __init__(self):
        self.number = 2

class FirstNumber(Number):
    def __init__(self):
        super().__init__()
        self.number *= 2


class SecondNumber(FirstNumber):
    def __init__(self):
        super().__init__()
        self.number *= 2


parent = Number()
child1 = FirstNumber()
child2 = SecondNumber()


print("Number:", parent.number)
print("FirstNumber:", child1.number)
print("SecondNumber:",child2.number)