import numpy as np
cimport numpy as np
cimport cython

# Types for all scalar elements
DTYPE = np.int
ctypedef np.int_t DTYPE_t 

cpdef np.ndarray __nearest(np.ndarray img_color, np.ndarray colors):
    distances = [ __dist(img_color, color) for color in colors ]
    cdef np.ndarray v = colors[np.argmin(distances)]
    return v

cpdef DTYPE_t __dist(np.ndarray a, np.ndarray b):
    cdef np.ndarray d = a - b
    cdef int v = np.dot(d,d)
    return v

@cython.boundscheck(False)
@cython.wraparound(False)
def optimized(np.ndarray[DTYPE_t,ndim=3] img, np.ndarray[DTYPE_t,ndim=2] colors):
    img = img[:,:,0:3]
    cdef int w = img.shape[0]
    cdef int h = img.shape[1]
    cdef int c = img.shape[2]
    cdef int n = colors.shape[0]
    cdef DTYPE_t d, D, D_max
    cdef np.ndarray[DTYPE_t,ndim=3] out
    cdef np.ndarray[DTYPE_t,ndim=1] delta
    cdef int x, y
    cdef int nearest

    D_max = 255*255
    out = np.zeros([w,h,c], dtype=DTYPE)

    for x in range(w):
        for y in range(h):
            D = D_max
            nearest = 0
            for color in range(n):
                delta = img[x,y] - colors[color]
                d = np.dot(delta, delta)
                if d < D:
                    D = d
                    nearest = color
                out[x,y,:] = colors[nearest]
    return out

def vanilla(np.ndarray img, np.ndarray colors):
    img = img[:,:,0:3]
    cdef int w = img.shape[0]
    cdef int h = img.shape[1]
    cdef int c = img.shape[2]
    cdef np.ndarray out = np.zeros([w,h,c], dtype=DTYPE)
    cdef int x, y
    for (x,y) in np.ndindex(w,h):
        out[x,y,:] = __nearest(img[x,y], colors)
    return out
