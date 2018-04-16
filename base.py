import numpy as np

def colorize(img, colors):
    w, h, c = img.shape
    out = np.copy(img)
    if c == 4: # Restrict to 3 colors
        img = img[:,:,0:3]

    for (x,y) in np.ndindex(w,h):
        out[x,y] = __nearest(img[x,y], colors)

    return out

def __nearest(img_color, colors):
    distances = [ __dist(img_color, color) for color in colors ]
    return colors[np.argmax(distances)]

def __dist(a, b):
    d = a - b
    return np.sum(d*d)
