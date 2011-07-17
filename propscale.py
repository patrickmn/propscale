#!/usr/bin/env python
import sys

class BoundaryException(Exception): pass

maxInt = sys.maxint

def propScale(width, height, maxWidth=0, maxHeight=0):
    width = int(width)
    height = int(height)
    maxWidth = int(maxWidth)
    maxHeight = int(maxHeight)
    if maxWidth <= 0:
        if maxHeight <= 0:
            raise BoundaryException("Set either maxWidth or maxHeight")
        else:
            maxWidth = maxInt
    elif maxHeight <= 0:
        maxHeight = maxInt

    imageAspect = float(width) / float(height)
    boundaryAspect = float(maxWidth) / float(maxHeight)
    if imageAspect > boundaryAspect:
        # Width maxed
        newWidth = maxWidth
        newHeight = int(round(newWidth / imageAspect))
    else:
        # Height maxed
        newHeight = maxHeight
        newWidth = int(round(imageAspect * newHeight))
    return newWidth, newHeight

def main():
    if len(sys.argv) > 1:
        print(propScale(*sys.argv[1:]))
    else:
        print("Usage: %s <width> <height> <new width, or 0> <new height, or 0>" % (sys.argv[0],))

if __name__ == '__main__':
    main()
