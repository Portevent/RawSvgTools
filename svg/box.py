class Box:
    x: float = 0
    y: float = 0
    x2: float = 0
    y2: float = 0

    def __init__(self, width, height):
        self.x = 0
        self.y = 0
        self.y2 = height
        self.x2 = width

    def getWidth(self) -> float:
        return self.x2 - self.x

    def getHeight(self) -> float:
        return self.y2 - self.y

    def align(self, centered: bool = True) -> 'Box':
        if centered:
            return self.center()

        return self.topLeft()

    def center(self) -> 'Box':
        self.x2 = (self.x2 - self.x) / 2
        self.y2 = (self.y2 - self.y) / 2
        self.x = -self.x2
        self.y = -self.y2
        return self

    def topLeft(self) -> 'Box':
        self.x2 = self.x2 - self.x
        self.y2 = self.y2 - self.y
        self.x = 0
        self.y = 0
        return self

    def increase(self, multiplier: float = 1.5) -> 'Box':
        self.x2 *= multiplier
        self.y2 *= multiplier
        self.x *= multiplier
        self.y *= multiplier
        return self

    def toViewBox(self) -> str:
        return f"{self.x} {self.y} {self.getWidth()} {self.getHeight()}"
