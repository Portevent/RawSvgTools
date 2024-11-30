# RawSvgTools

Simple python library to create SVG images

```python
from svg import SvgImage, Circle

with SvgImage("out/image.svg", width=40) as image:
    image.addContent(Circle().at(20,20).radius(10))
```

Raw in RawSvgTools is here to remind that basic understanding of svg is required. \
Most svg features are coded as is, and you need to know what you want your svg file to be. \
For instance, the Path class can be confusing without knowing about svg.

```python
from svg import SvgImage, Path

path: Path = Path()
path.moveTo(10,10)  # One can geniuly expect this method to draw a line from 0,0 to 10,10
path.linesTo([(-10,10), (-10,-10), (10, -10)])
path.close()

with SvgImage("out/image.svg", width=30, centered=True) as image:
    image.addContent(path)
```

## Elements

| Supported | Coming         | Not planned      |
|-----------|----------------|------------------|
| Circle    | Rect           | AnimateMotion    |
| Path      | A              | AnimateTransform |
| Animate   | Desc           | ClipPath         |
| Defs      | Ellipse        | Fe<...>          |
| Svg       | G              | Filter           |
|           | Image          | ForeinObject     |
|           | Line           | Filter           |
|           | LinearGradient | Metadata         |
|           | Marker         | Filter           |
|           | Pattern        | Switch           |
|           | Polygon        | Style            |
|           | Polyline       |                  |
|           | RadialGradient |                  |

## Known bugs
### Over specified elements
Elements have every possible attributes. Default values are choosed to be as neutral as possible, but the output are often quite thick
```python
Circle().radius(10)
Circle().radius(10).color(line="blue")
```
```svg
<circle stroke="red" fill="none" stroke-linecap="round" stroke-linejoin="round" stroke-width="1" cx="0" cy="0" r="10"/>
<circle stroke="blue" fill="none" stroke-linecap="round" stroke-linejoin="round" stroke-width="1" cx="0" cy="0" r="10"/>
```


## Notes
The library is built with a method chaining syntax eventho Python isn't the best language to make proper use of it. \
This decision is based on my personal preferences (I wanted to train a bit on this syntax), but also because this library may be rewritted in C# or Java for future projects. You don't have to chain method if you don't want to