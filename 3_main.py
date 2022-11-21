class Flat:
    def __init__(self, squareFlate, price) -> None:
        self.squareFlate = squareFlate
        self.price = price

    # reload operator ==
    def __eq__(self, __o: object) -> bool:
        return True if self.squareFlate == __o.squareFlate else False

    # reload operator !=
    def __ne__(self, __o: object) -> bool:
        return True if self.squareFlate != __o.squareFlate else False

    # reload operator >
    def __gt__(self, other:object)->bool:
        return True if self.price > other.price else False

    # reload operator <
    def __lt__(self, other:object)->bool:
        return True if self.price < other.price else False

    # reload operator >=
    def __ge__(self, other:object)->bool:
        return True if self.price >= other.price else False

    # reload operator <=
    def __le__(self, other)->bool:
        return True if self.price <= other.price else False

    # reload str
    def __str__(self) -> str:
        return f"\nSquare of flate - {self.squareFlate}(m2); Price - {self.price}(EURO)"


flat1 = Flat(60, 27000)
flat2 = Flat(70, 30000)

# TEST
print(flat1, flat2)

if flat1 == flat2:
    print("Square of flats are equal")
elif flat1 != flat2:
    print("Square of flats are not equal")

if flat1 > flat2:
    print("The price of flat_1 is greater than flat_2 ") 
elif flat1 < flat2:
    print("The price of flat_1 is lower than flat_2 ")

if flat1 >= flat2:
    print ("The price of flat_1 is greater than flat_2 or is the same")
elif flat1 <= flat2:
    print("The price of flat_1 is lower than flat_2 or is the same") 