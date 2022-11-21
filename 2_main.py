class AirPlane:
    def __init__(self, planeType, passengersNumber, passengersNumbe = 0 ) -> None:
        self.planeType = planeType
        self.passengersNumber = passengersNumber
        match self.planeType:
            case "Privat Jets":
                self.__maxPassengers = 6
            case "Regional Jets":
                self.__maxPassengers = 100
            case "Narrow Body Aircraft":
                self.__maxPassengers = 295
            case "Wide Body Airliners":
                self.__maxPassengers = 850 

    # reload operator ==
    def __eq__(self, o: object) -> bool:
        return True if self.planeType == o.planeType else False

    # reload operator +
    def __add__(self, other:int):
        return AirPlane(self.planeType, self.passengersNumber + other, self.__maxPassengers)

    # reload operator +=
    def __iadd__(self, other:int):
        return AirPlane(self.planeType, self.passengersNumber + other, self.__maxPassengers)

    # reload operator - 
    def __sub__(self, other:int):
        return AirPlane(self.planeType, self.passengersNumber - other, self.__maxPassengers)

    # reload operator -=
    def __isub__(self, other:int):
        return AirPlane(self.planeType, self.passengersNumber - other, self.__maxPassengers)

    # reload operator >
    def __gt__(self, o:object)->bool:
        return True if self.__maxPassengers > o.__maxPassengers else False

    # reload operator < 
    def __lt__(self, o:object)->bool:
        return True if self.__maxPassengers < o.__maxPassengers else False

    # reload operator >=
    def __ge__(self, o:object)->bool:
        return True if self.__maxPassengers >= o.__maxPassengers else False

    # reload operator <=
    def __le__(self, o:object)->bool:
        return True if self.__maxPassengers <= o.__maxPassengers else False

    # reload __str__
    def __str__(self) -> str:
        return f'type of plane - {self.planeType}; number of passengeres - {self.passengersNumber}; Max passengers - {self.__maxPassengers}\n'


plane_1 = AirPlane("Regional Jets", 50)
plane_2 = AirPlane("Wide Body Airliners", 200)


# TEST
if plane_1 == plane_2:
    print("\nplanes have the same type")
else:
    print("\nplanes have different type")

plane_1 +=  1
plane_2 -= 1
print(plane_1, plane_2)

if plane_1 > plane_2:
    print("Max passengers capacity on plane_1 greater than on plane_2")
elif plane_1 < plane_2:
    print("Max passengers capacity on plane_1 lower than on plane_2")