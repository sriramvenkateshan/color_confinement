import numpy as np
cimport numpy as cnp
cimport cython

# Types for all scalar elements
ctypedef cnp.int_t DTYPE_t 

cdef extern from "transform.h":
    void do_transform(DTYPE_t *img, DTYPE_t *color, DTYPE_t *out, DTYPE_t n, DTYPE_t m)

@cython.boundscheck(False)
@cython.wraparound(False)
@cython.profile(True)
cpdef optimized(cnp.ndarray[DTYPE_t,ndim=3] img, cnp.ndarray[DTYPE_t,ndim=2] colors):
    img = img[:,:,0:3]
    cdef int w = img.shape[0]
    cdef int h = img.shape[1]
    cdef cnp.ndarray[DTYPE_t, ndim=2] lin_img = np.reshape(img, [-1, 3])
    cdef int m = colors.shape[0]
    cdef int n = w*h
    cdef DTYPE_t [:, :] img_view = lin_img
    cdef DTYPE_t [:, :] colors_view = colors
    out = np.zeros([n,3], dtype=np.int)
    cdef DTYPE_t [:, :] out_view = out

    cdef DTYPE_t d, D, D_max
    cdef DTYPE_t d0, d1, d2
    cdef int x, y
    cdef int nearest
    D_max = 255*255

    for pixel in range(n):
        D = D_max
        nearest = 0
        for color in range(m):
            d0 = img_view[pixel,0] - colors_view[color,0]
            d1 = img_view[pixel,1] - colors_view[color,1]
            d2 = img_view[pixel,2] - colors_view[color,2]
            d = d0*d0 + d1*d1 + d2*d2
            if d < D:
                D = d
                nearest = color
            out_view[pixel,:] = colors_view[nearest]

    out = np.reshape(out, [w, h, 3])
    return out

@cython.boundscheck(False)
@cython.wraparound(False)
@cython.profile(True)
cpdef extern_optimized(cnp.ndarray[DTYPE_t,ndim=3] img, cnp.ndarray[DTYPE_t,ndim=2] colors):
    img = img[:,:,0:3]
    cdef int w = img.shape[0]
    cdef int h = img.shape[1]
    cdef cnp.ndarray[DTYPE_t, ndim=2] lin_img = np.reshape(img, [-1, 3])
    cdef int m = colors.shape[0]
    cdef int n = w*h
    cdef DTYPE_t [:, :] img_view = lin_img
    cdef DTYPE_t [:, :] colors_view = colors
    out = np.zeros([n,3], dtype=np.int)
    cdef DTYPE_t [:, :] out_view = out

    do_transform(&img_view[0,0], &colors_view[0,0], &out_view[0,0], n, m)

    out = np.reshape(out, [w, h, 3])
    return out
