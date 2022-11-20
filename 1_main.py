class Circle():
    def __init__(self, radius) -> None:
        self.radius = radius

# description of arc length
    def lengthArc(self) ->float:
        return 2*3.14*self.radius

# reload operator ==
    def __eq__(self, __o: object) -> bool:
        return True if self.radius == __o.radius else False

# reload operator >
    def __gt__(self, __o:object) -> bool:
        return True if self.lengthArc() > __o.lengthArc() else False 

# reload operator +
    def __add__(self, __o:float | int):
        return Circle(self.radius + __o)

# reload operator -
    def __sub__(self, __o:float | int):
        return Circle(self.radius - __o)

# reload operator +=
    def __iadd__(self, __o:float | int):
        return Circle(self.radius + __o)

# reload operator -=
    def __isub__(self, __o:float | int):
        return Circle(self.radius - __o)

# reload __str__ method
    def __str__(self) -> str:
        return f"Radius:{self.radius}; Arc length = {(self.lengthArc()):.2f}\n"
    



r1 = float(input("\nEnter first radius of circle = "))
r2 = float(input("Enter second radius of circle = "))

c1 = Circle(r1)
c2 = Circle(r2)

# compering by radius
if c1 == c2:
    print("\n- radiuses of C1 and C1 are equal\n")
else:
    print("\n- radiuses of C1 and C2 are not equal\n")

# compering by arc angle
if c1 > c2:
    print ("- arc lenght cicle C1 greater then C2\n")
elif c2 > c1:
    print ("- arc length cicle C1 less then C2\n")
else:
    print("- arc's of circles are equal\n")

# TEST
print(c1,c2)

# resizing of radius

# TEST
c1 += 10
c2 = c2 - 1
print(c1,c2)

