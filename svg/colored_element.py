from abc import ABC

from style import Color
from svg.svg_element import SvgElement

class ColoredElement(SvgElement, ABC):

    def getDefaultAttributes(self) -> dict[str, str]:
        return {
        'stroke': 'red',
        'fill': 'none',
        'stroke-linecap': 'round',
        'stroke-linejoin': 'round',
        'stroke-width': '1'
    }

    def color(self, fill: str | Color | None = None, line: str | Color | None = None) -> 'ColoredElement':

        self.attributes['fill'] = 'none' if fill is None else (fill.to_hex() if isinstance(fill, Color) else fill)
        self.attributes['stroke'] = 'none' if line is None else (line.to_hex() if isinstance(line, Color) else line)
        return self
