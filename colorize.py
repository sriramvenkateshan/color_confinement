from skimage.io import imread
from skimage.io import imsave
import numpy as np
import json
import glob
import os
import sys
import csv
import time

# Add imports here for all implemented classes
import vanilla
import optimized


def colorspace(colorspace_name):
    colors = []
    with open(colorspace_name, "r") as colorfile:
        for row in csv.reader(colorfile, delimiter=','):
            colors.append(row)
    return np.array(colors).astype(np.int)

if __name__ == "__main__":
    cfg = sys.argv[1]

    # Default parameters
    data = {
        "dataset"       : "images",         # Image dir
        "only"          : "*.jpg",          # All images under images/
        "output"        : "output",         # Output dir
        "colorspace"    : "blackwhite",
        "algo"          : "vanilla.Loopall", # Plain cpu Loopall class
        "algoparams"    : {},
    }
    data.update(json.loads(open(cfg, "r").read()))

    # Load required colors
    algoclass = eval(data["algo"])

    colorspaces = glob.glob(os.path.join("colorspaces", data["colorspace"] + ".colors"))

    if not os.path.isdir(data["output"]):
        os.makedirs(data["output"])
    for outimg in glob.glob(os.path.join(data["output"],"*")):
        os.unlink(outimg)

    for img_path in glob.glob(os.path.join(data["dataset"], data["only"])):
        img = imread(img_path).astype(np.int)
        w, h, _ = img.shape
        # print( "Picking up {}x{} image {} ...".format(
        #        w, h, os.path.basename(img_path)))
        for c in colorspaces:
            cname = os.path.splitext(os.path.basename(c))[0]
            # print( "Using colorspace {} ...".format(cname))
            colorizer = algoclass(colorspace(c), params=data["algoparams"])
            out_img_path = os.path.join(data["output"], cname + "_" + os.path.basename(img_path))
            start = time.time()
            out_img = colorizer(img)
            end = time.time()
            print( "Colorized {}x{} image {} into {} colorspace in {} s".format(
                    w, h, os.path.basename(img_path), cname, end-start))
            # print("")
            imsave(out_img_path, out_img)
        # print("-----")

