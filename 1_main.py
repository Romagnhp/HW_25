class Circle:
    def __init__(self, radius, angleArc) -> None:
        self.radius = radius
        self.angleArc = angleArc

    def __eq__(self, __o: object) -> bool:
        return True if self.radius == __o.radius else False

    def __str__(self) -> str:
        return f"Radius = {self.radius}; Central angle = {self.angleArc}"
        
try :
    r1 = float(input("Enter first radius of circle = "))
    a1 = float(input("Enter first central angel of arc = "))

    r2 = float(input("Enter second radius of circle = "))
    a2 = float(input("Enter second central angle of arc = "))

except:
    print("Data is not correct")


c1 = Circle(r1, a1)
c2 = Circle(r2, a2)

if c1 == c2:
    print("radiu's of circles are equal")
else:
    print("radiu's of circles are not equal")

print(c1, c2)

