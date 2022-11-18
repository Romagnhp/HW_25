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
    def __add__(self, __o:float)->float:
        self.radius = float(self.radius) + __o
        return self.radius

# reload operator -
    def __sub__(self, __o:float)->float:
        self.radius = float(self.radius) - __o
        return self.radius


# reload __str__ method
    def __str__(self) -> str:
        return f"Radius:{self.radius}; Central angle = {self.angleArc} Arc length = {(self.lengthArc()):.2f}\n"
    



r1 = float(input("\nEnter first radius of circle = "))
a1 = float(input("Enter first central angel of arc = "))

r2 = float(input("\nEnter second radius of circle = "))
a2 = float(input("Enter second central angle of arc = "))    

c1 = Circle(r1, a1)
c2 = Circle(r2, a2)

# compering by radius
if c1 == c2:
    print("\nradiuses of C1 and C1 are equal\n")
else:
    print("\nradiuses of C1 and C2 are not equal\n")

# compering by arc angle
if c1 > c2:
    print ("arc lenght cicle C1 greater then C2\n")
elif c2 > c1:
    print ("arc length cicle C1 less then C2\n")
else:
    print("arc's of circles are equal\n")

print(c1,c2)

# resizing of radius
c1 + 2
c2 + 5
print(c1,c2)

c1 - 2
c2 - 5
print(c1,c2)
