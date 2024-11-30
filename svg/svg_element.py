from abc import ABC, abstractmethod
from typing import List


def exportDict(dictionary: dict[str, str]) -> str:
    return ' '.join([f'{name}=\"{value}\"' for (name, value) in dictionary.items()])

def attributeToHash(key: str, value: str) -> str:
    return f"{key[:4]:_<4}.{value[:4]:_<4}"


class SvgElement(ABC):
    """
    Represents an SVG element
    name is the tag name of the element, like <circle> or <path>
    attributes are key value pairs

    content is a list of all element within this tag. If empty, the tag will self-closing (e.g. <circle />)
    defs is a list of all element this element refers to. See SvgDefElement class for further details
    """
    name: str
    attributes: dict[str, str]

    content: List['SvgElement'] = []
    defs: List['SvgElement'] = []

    @abstractmethod
    def getDefaultName(self) -> str:
        raise NotImplementedError

    @abstractmethod
    def getDefaultAttributes(self) -> dict[str, str]:
        raise NotImplementedError

    def __init__(self):
        self.name = self.getDefaultName()
        self.attributes = self.getDefaultAttributes()
        self.content = []
        self.defs = []

    def clearContent(self) -> 'SvgElement':
        self.content = []
        self.defs = []
        return self

    def addContents(self, elements: List['SvgElement']) -> 'SvgElement':
        for element in elements:
            self.addContent(element)

        return self

    def addContent(self, element: 'SvgElement') -> 'SvgElement':
        self.content.append(element)
        return self

    def getDefs(self) -> List['SvgElement']:
        return self.defs + sum([element.getDefs() for element in self.content], [])

    def setAttributes(self, attribute: str, value: str) -> 'SvgElement':
        self.attributes[attribute] = value
        return self

    def getAttributes(self, key: str) -> str:
        return self.attributes.get(key, None)

    def addDefsElement(self, element: 'SvgElement', id: str = None) -> str:
        """
        Save the elements within the defs, and return the id it can be referenced from
        The id given to the element can be specified, otherwise the hash is taken
        """
        value = id or element._hash()
        element.setAttributes("id", value)
        self.defs.append(element)

        return value


    def _hash(self) -> str:
        """
        Generate a hash, based on its name and parameters
        """
        return f"{self.name}.{'.'.join([attributeToHash(key, value) for (key, value) in self.attributes.items()])}"

    def export(self) -> str:
        return (f"<{self.name} {exportDict(self.attributes)}"
                + ("/>" if len(self.content) == 0 else
                   (">\n" + '\n'.join([element.export() for element in self.content]) + '\n' + f"</{self.name}>")))

