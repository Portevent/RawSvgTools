class Color:

    r: int
    g: int
    b: int

    def __init__(self, r, g, b):
        self.r = r
        self.g = g
        self.b = b

    def to_hex(self) -> str:
        return "#" + format(self.r, '02x') + format(self.g, '02x') + format(self.b, '02x')

    def to_int(self) -> int:
        return self.r * 256 * 256 + self.g * 256 + self.b

    def __str__(self):
        return str(self.to_hex())

    @staticmethod
    def from_hex(hex_str: str) -> 'Color':
        return Color(int(hex_str[0:2], 16), int(hex_str[2:4], 16), int(hex_str[4:6], 16))

    @staticmethod
    def from_rgb(r: int, g: int, b: int) -> 'Color':
        return Color(r, g, b)

    @staticmethod
    def from_int(rgb: int) -> 'Color':
        return Color(rgb // 65536, rgb // 256 % 256, rgb % 256)
