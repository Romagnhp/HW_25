class Circle:

    def __init__(self, radius, angleArc) -> None:
        self.radius = radius
        self.angleArc = angleArc

# description of arc length
    def lengthArc(self) ->float:
        return 2*3.14*self.radius*(self.angleArc/360)

# reload operator ==
    def __eq__(self, __o: object) -> bool:
        return True if self.radius == __o.radius else False

# reload operator >
    def __gt__(self, __o:object) -> bool:
        return True if self.lengthArc() > __o.lengthArc() else False 

# reload operator +
    def __add__(self, __o:float):
        return self.radius + __o

# reload __str__ method
    def __str__(self) -> str:
        return f"Radius:{self.radius}; Central angle = {self.angleArc} Arc length = {(self.lengthArc()):.2f}\n"
    






r1 = float(input("Enter first radius of circle = "))
a1 = float(input("Enter first central angel of arc = "))

r2 = float(input("Enter second radius of circle = "))
a2 = float(input("Enter second central angle of arc = "))

# arr = [r1, a1, r2, a2]
# if aar is 

c1 = Circle(r1, a1)
c2 = Circle(r2, a2)

if c1 == c2:
    print("radiuses of C1 and C1 are equal")
else:
    print("radiuses of C1 and C2 are not equal")

if c1 > c2:
    print ("arc cicle C1 greater then C2")
elif c2 > c1:
    print ("arc cicle C1 less then C2")
else:
    print("arc's of circles are equal")

print(c1,c2)

c1 + 2.0
print(c1,c2)

