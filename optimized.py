import numpy as np


class Loopall:
    def __init__(self, colors, params={}):
        self.colors = colors
        self.params = {
            "usegpu" : False
        }
        self.params.update(params)
        self.maxdistance = 1 + 255*255

    def __call__(self, img):
        img = img[:,:,0:3]
        w, h, _ = img.shape
        out = np.zeros(img.shape).astype(np.int)
        for (x,y) in np.ndindex(w,h):
            out[x,y] = self.__nearest(img[x,y])
        return out

    def __nearest(self, img_color):
        mindistance, idx = self.maxdistance, -1
        for c, color in enumerate(self.colors):
            distance = self.__dist(img_color, color)
            if distance < mindistance:
                mindistance = distance
                idx = c
        return self.colors[idx]

    def __dist(self, a, b):
        d = a - b
        return np.dot(d,d)
