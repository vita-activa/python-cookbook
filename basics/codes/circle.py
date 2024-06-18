class Circle:

    def __init__(self, radius) -> None:
        self._radius= None
        # here we set the radius by calling the setter in fact
        self.radius = radius

# here one gets the property: radius
    @property
    def radius(self):
        return self._radius
    
# here we set the value of the property
    @radius.setter
    def radius(self, radius):
        if radius <= 0:
            raise ValueError('Radius must be positive.')
        self._radius = radius

    def __eq__(self, other: object) -> bool:
        if isinstance(other, Circle):
            return self.radius == other.radius
        else:
            return False

    def __repr__(self) -> str:
        return f"Circle({self.radius})"

    def __str__(self) -> str:
        return f"Circle({self.radius})"
    

    def __lt__(self, other):
        if isinstance(other, Circle):
            return self.radius < other.radius
        else:
            return NotImplemented
        

c1=Circle(5)
c2=Circle(8)
c3=Circle(5)
c4=8

print("c1 is equal to c2", c1==c2)
print("c1 is equal to c3", c1==c3)
print("c1 is equal to c4", c1==c4)

try:
    c5=Circle(-5)
except ValueError as e:
    print(e)

print(c1)

print(str(c2))

print(c1<c2)

#print(c1>c4)