from svg.colored_element import ColoredElement

class Circle(ColoredElement):

    def __init__(self, x: float | None = None, y: float | None = None, radius: float | None = None):
        super().__init__()

        if not x is None:
            self.attributes['cx'] = str(x)

        if not y is None:
            self.attributes['cy'] = str(y)

        if not radius is None:
            self.attributes['r'] = str(radius)


    def getDefaultName(self) -> str:
        return "circle"

    def getDefaultAttributes(self) -> dict[str, str]:
        return dict(super().getDefaultAttributes(), **{
                'cx': '0',
                'cy': '0',
                'r': '50'
            })

    def at(self, x: float, y: float) -> 'Circle':
        self.attributes["cx"] = str(x)
        self.attributes["cy"] = str(y)
        return self

    def radius(self, r: float) -> 'Circle':
        self.attributes["r"] = str(r)
        return self