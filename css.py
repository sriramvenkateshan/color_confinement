import numpy as np

class Blackwhite:
    colors = {
        "Black"    :   "000000",
        "White"    :   "FFFFFF",
    }

    def __init__ (self, usenumpy=False):
        self.usenumpy = usenumpy

    def __call__ (self):
        if self.usenumpy:
            colors = [ self.__convert_hex_to_array(c) for c in self.colors.values() ]
            return np.array(colors)
        else:
            return self.colors.values()

    def convert_hex_to_array(self, hexcode):
        length = len(hexcode)
        if length is not 6:
            raise Exception("Malformed hexcode of length {}".format(length))
        return [
            int(hexcode[0:2], 16),
            int(hexcode[2:4], 16),
            int(hexcode[4:], 16)
        ]

class Css1_16:
    colors = {
        "Aqua"     :   "00FFFF",
        "Black"    :   "000000",
        "Blue"     :   "0000FF",
        "Fuchsia"  :   "FF00FF",
        "Gray"     :   "808080",
        "Green"    :   "008000",
        "Lime"     :   "00FF00",
        "Maroon"   :   "800000",
        "Navy"     :   "000080",
        "Olive"    :   "808000",
        "Purple"   :   "800080",
        "Red"      :   "FF0000",
        "Silver"   :   "C0C0C0",
        "Teal"     :   "008080",
        "White"    :   "FFFFFF",
        "Yellow"   :   "FFFF00"
    }

    def __init__ (self, **kwargs):
        super(Css1_16, self).__init__(kwargs)

