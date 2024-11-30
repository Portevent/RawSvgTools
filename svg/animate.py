from svg.svg_element import SvgElement


class Animate(SvgElement):

    def getDefaultName(self) -> str:
        return "animate"

    def getDefaultAttributes(self) -> dict[str, str]:
        return {
        "attributeName": "",
        "begin": "0s",
        "dur": "5s",
        "repeatCount": "indefinite",
        "fill": "freeze"
    }

    def setAttribute(self, attribute) -> 'Animate':
        self.attributes["attributeName"] = attribute
        return self

    def setDuration(self, duration: int) -> 'Animate':
        self.attributes["duration"] = f"{duration}s"
        return self

    def setRepeatCount(self, repeat: int) -> 'Animate':
        self.attributes["repeatCount"] = str(repeat) if repeat > 0 else "indefinite"
        return self

    def setValues(self, *values: *str) -> 'Animate':
        self.attributes["values"] = ";".join(values) + ";" + values[0]
        return self

    @staticmethod
    def animate(element: SvgElement, attribute: str, to: str) -> 'Animate':
        animate = Animate().setAttribute(attribute).setValues(element.attributes[attribute], to)
        element.addContent(animate)
        return animate