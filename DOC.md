from svg import SvgImagefrom svg import SvgImagefrom svg import SvgImagefrom svg import SvgImagefrom svg import SvgImage

# Documentation
## Basic Element
Each svg elements have a name and attributes, and may contains content within.
```xml
<{{name}} {{attributes}}>
    {{content}}
</{{name}}>
or
<{{name}} {{attributes}} />
```
The library provide several class that create SvgElements with specified name, relevant attribute and implements method
that help build the element accordingly. \
Names and attributes are theoricly editable, but it isn't recommanded to change them by yourself as it isn't foolproof.

### Adding new content
One SvgElement can be added within another (in its `content`) by calling `.addContent()`
```python
image = SvgImage()
circle = Circle(radius=10)
image.addContent(circle)
```

## Svg Image Element
The SvgImage class allow to create the root tag of the image. 
Its viewport can be defined with the constructor or later with `.setSize()`

```python
# Equivalent
imageA = SvgImage(width=100, height=60)

imageB = SvgImage()
imageB.setSize(width=100, height=60)
```
Without specified height, the viewport will be square. The origin can be specified yet, it is set 0, 0.
However, you can add the parameter `centered=True` to create a viewport that centered around 0, 0

```python
image = SvgImage(width=100, centered=True) # viewBox="-50.0 -50.0 100.0 100.0"
```

To save the image to a file, you can use `.saveTo()`, or use context manager :
```python
# Equivalent
imageA = SvgImage(width=100)
imageA.addContent(...)
imageA.saveTo("a.svg")

with SvgImage("b.svg", width=100) as imageB:
    imageB.addContent(...)
```