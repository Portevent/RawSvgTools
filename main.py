from style import Color
from svg.circle import Circle
from svg.path import Path
from svg.svg_image import SvgImage

path: Path = (Path()
              .moveTo(10,10)
              .linesTo([(-10,10), (-10,-10), (10, -10)])
              .close())

with SvgImage("out/image.svg", width=30, centered=True) as image:
    image.addContent(path)

    image.addContent(Circle().radius(1).color(fill=Color(0, 0, 0)))

    for i in range(1, 11):
        image.addContent(
            Circle().radius(0.90*i).color(line=Color(25 * i, 0, 0))
        )



