from skimage.io import imread
from skimage.io import imsave
import numpy as np
import json
import base
import css
import glob
import os

if __name__ == "__main__":
    cfg = sys.argv[1]
    data = {
        "dataset"    : "images/",
        "output"     : "output/",
        "colorspace" : "css.BlackWhite",
        "compute"    : "base.colorize"
    }
    data.update(json.loads(open(cfg, "r").read()))
    colorspace = eval(data["colorspace"])(usenumpy=True)
    computealgo = eval(data["compute"])
    for img_path in glob.glob(os.path.join(data["dataset"], "*.png")):
        out_img_path = os.path(data["output"], os.basename(img))
        img = imread(img_path)
        out_img = computealgo(img, colorspace())
        imsave(out_img_path, out_img)

