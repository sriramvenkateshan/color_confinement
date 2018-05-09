import numpy as np

def __nearest(img_color, colors):
    distances = [ __dist(img_color, color) for color in colors ]
    return colors[np.argmin(distances)]

def __dist(a, b):
    d = a - b
    return np.dot(d,d)

def optimized(img, colors):
    img = img[:,:,0:3]
    w, h, c = img.shape
    p = w*h
    img = img.reshape((p, c))
    for x in range(0, p):
        img[x] = __nearest(img[x], colors)
    img = img.reshape((w, h, c))
    return img

def vanilla(img, colors):
    img = img[:,:,0:3]
    w, h, _ = img.shape
    out = np.zeros(img.shape).astype(np.int)
    for (x,y) in np.ndindex(w,h):
        out[x,y] = __nearest(img[x,y], colors)
    return out
