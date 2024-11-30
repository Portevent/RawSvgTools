from typing import Tuple, List

from svg.colored_element import ColoredElement

def toCoords(point: Tuple[float, float]) -> str:
    return ", ".join([str(point[0]), str(point[1])])

class Path(ColoredElement):

    def getDefaultName(self) -> str:
        return "path"

    def getDefaultAttributes(self) -> dict[str, str]:
        return dict(super().getDefaultAttributes(), **{
                'd': ''
            })

    d: str
    cursor_x: float
    cursor_y: float

    initial_x: float
    initial_y: float

    def __init__(self):
        super().__init__()
        self.d = ""
        self.cursor_x = 0
        self.cursor_y = 0
        self.initial_x = 0
        self.initial_y = 0

    def moveTo(self, x: float, y: float) -> 'Path':
        self.d += f"M {x}, {y} "
        self.cursor_x = x
        self.cursor_y = y
        self.initial_x = x
        self.initial_y = y
        return self

    def moveBy(self, x: float, y: float) -> 'Path':
        self.d += f"m {x}, {y} "
        self.cursor_x += x
        self.cursor_y += y
        self.initial_x += x
        self.initial_y += y
        return self

    def lineTo(self, x: float, y: float) -> 'Path':
        self.d += f"L {x}, {y} "
        self.cursor_x = x
        self.cursor_y = y
        return self

    def linesTo(self, points: List[Tuple[float, float]]) -> 'Path':
        self.d += f"L {' '.join(map(toCoords, points))} "
        self.cursor_x = points[-1][0]
        self.cursor_y = points[-1][1]
        return self

    def lineBy(self, x: float, y: float) -> 'Path':
        self.d += f"l {x}, {y} "
        self.cursor_x += x
        self.cursor_y += y
        return self

    def linesBy(self, points: List[Tuple[float, float]]) -> 'Path':
        self.d += f"l {' '.join(map(toCoords, points))} "
        for point in points:
            self.cursor_x += point[0]
            self.cursor_y += point[1]
        return self

    def qBezierTo(self, x: float, y: float, cx: float, cy: float) -> 'Path':
        self.d += f"Q {cx}, {cy}, {x}, {y} "
        self.cursor_x = x
        self.cursor_y = y
        return self

    def qBezierBy(self, x: float, y: float, cx: float, cy: float) -> 'Path':
        self.d += f"q {cx}, {cy}, {x}, {y} "
        self.cursor_x += x
        self.cursor_y += y
        return self

    def smoothQuadraBezierTo(self, x: float, y: float) -> 'Path':
        self.d += f"T {x}, {y} "
        self.cursor_x = x
        self.cursor_y = y
        return self

    def smoothQuadraBezierBy(self, x: float, y: float) -> 'Path':
        self.d += f"t {x}, {y} "
        self.cursor_x += x
        self.cursor_y += y
        return self

    def smoothQuadraBeziersTo(self, points: List[Tuple[float, float]]) -> 'Path':
        self.d += f"T {' '.join(map(toCoords, points))} "
        self.cursor_x = points[-1][0]
        self.cursor_y = points[-1][1]
        return self

    def close(self) -> 'Path':
        self.d += f"Z"
        self.cursor_x = self.initial_x
        self.cursor_y = self.initial_y
        return self

    def export(self) -> str:
        self.attributes['d'] = self.d
        return super().export()