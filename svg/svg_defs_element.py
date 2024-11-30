from svg.svg_element import SvgElement


class SvgDefsElement(SvgElement):

    def getDefaultName(self) -> str:
        return "defs"

    def getDefaultAttributes(self) -> dict[str, str]:
        return {}