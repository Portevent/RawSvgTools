from svg.colored_element import ColoredElement

class Circle(ColoredElement):

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