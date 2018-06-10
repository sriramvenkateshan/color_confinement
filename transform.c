#include "transform.h"

void do_transform(long *img, long *color, long *out, long n, long m) {
    long d, D, D_max, d0, d1, d2;
    int p, c, nearest;
    D_max = 255*255;
    for (p = 0; p < n; p++) {
        D = D_max;
        nearest = 0;
        for (c = 0; c < m; c++) {
            d0 = img[3*p + 0] - color[3*c + 0];
            d1 = img[3*p + 1] - color[3*c + 1];
            d2 = img[3*p + 2] - color[3*c + 2];
            d = d0*d0 + d1*d1 + d2*d2;
            if (d < D) {
                D = d;
                nearest = c;
            }
        }
        out[3*p + 0] = color[3*nearest + 0];
        out[3*p + 1] = color[3*nearest + 1];
        out[3*p + 2] = color[3*nearest + 2];
    }
}
