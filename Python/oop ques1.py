class plane():
    wings=2
    def __init__(self, colour):
        self.colour=colour
    @staticmethod
    def fly():
        print("able to fly")

class jet(plane):
    wings=6
    def __inti__(self, colour):
        self.colour=colour

class passenger(plane):
    wings=9
    def __init__(self, colour):
        self.colour=colour

p1=plane("black")
p2=plane("white")
p3=jet("red")
p4=jet("green")
p5=passenger("blue")
p6=passenger("pink")

print(p1.colour)
p1.fly()

print(p3.wings)
print(p3.colour)
p3.fly()

print(p5.wings)
print(p5.colour)
p5.fly()
