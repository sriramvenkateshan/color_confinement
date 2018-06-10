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
    n = colors.shape[0]

    D_max = 255*255
    out = np.zeros([w,h,c]).astype(np.int)

    for x in range(w):
        for y in range(h):
            D = D_max
            nearest = 0
            for color in range(n):
                d0 = img[x,y,0] - colors[color,0]
                d1 = img[x,y,1] - colors[color,1]
                d2 = img[x,y,2] - colors[color,2]
                d = d0*d0 + d1*d1 + d2*d2
                if d < D:
                    D = d
                    nearest = color
                out[x,y,:] = colors[nearest]
    return out

def vanilla(img, colors):
    img = img[:,:,0:3]
    w, h, _ = img.shape
    out = np.zeros(img.shape).astype(np.int)
    for (x,y) in np.ndindex(w,h):
        out[x,y] = __nearest(img[x,y], colors)
    return out
