from svg.box import Box
from svg.svg_defs_element import SvgDefsElement
from svg.svg_element import SvgElement

DEFAULT_WIDTH = 100

class SvgImage(SvgElement):

    def getDefaultAttributes(self) -> dict[str, str]:
        return {
        "width": "100%",
        "height": "100%",
        "xmlns": "http://www.w3.org/2000/svg",
        "viewBox": "-100 -100 200 200",
        "version": "1.1"
    }

    def getDefaultName(self) -> str:
        return "svg"

    out_path: str

    # This element correspond to the final <defs> tag in the svg image
    # Not to be mistaken with defs, which is the list of svgElement that a svgElement reference to
    # This defsElement will be filled with all defs of all content when the svg image is exported
    defsElement: SvgDefsElement

    def __init__(self, out_path: str | None = None, width: int | None = None, height: int | None = None, centered: bool = False):
        super().__init__()
        self.out_path = out_path
        self.defsElement = SvgDefsElement()
        self.content = [self.defsElement]
        self.setSize(width or DEFAULT_WIDTH, height, centered=centered)

    def setSize(self, width: int = DEFAULT_WIDTH, height: int | None = None, centered: bool = False) -> 'SvgImage':
        if height is None:
            height = width

        self.attributes["viewBox"] = Box(width, height).align(centered).toViewBox()
        return self

    def saveTo(self, file: str):
        with open(file, "w") as f:
            f.write(self.export())
            print(f"Saved to {f.name}")

    def _updateDefs(self):
        self.defsElement.clearContent()
        ids = []
        for element in self.getDefs():
            if element.getAttributes("id") in self.ids:
                continue

            ids.append(element.getAttributes("id"))
            self.defsElement.addContent(element)

    def export(self):
        self._updateDefs()
        return super().export()

    def __enter__(self) -> 'SvgImage':
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.saveTo(self.out_path)
