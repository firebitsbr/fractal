#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Created on Tue Apr 08 08:45:59 2014
# @author: Danilo de Jesus da Silva Bellini
"""
Gaston Julia fractal (1917)
"""

from __future__ import division
import pylab

# Parameters
c = -.7102 + .2698j
depth = 512
width, height = 512, 512

# Algorithm
def val(x, y):
  """
  Gaston Julia Fractal value for pixel at coords [x, y] for values
  within the (-1; 1) range.
  """
  result = 0
  while x ** 2 + y ** 2 < 4 and result < depth:
    number = (x + y * 1j) ** 2 + c
    x, y = number.real, number.imag
    result += 1
  return result

# Generates the intensities for each pixel
side = max(width, height)
img = pylab.array([
  [val(2 * col / (width - 1) - 1, 2 * row / (height - 1) - 1)
    for col in range(width)]
  for row in range(height)
])

# Plots and saves the desired fractal raster image
pylab.imsave("julia_{width}x{height}_d={depth}_c={c}.png".format(**locals()), img, cmap="cubehelix")
pylab.imshow(img, cmap="cubehelix")
pylab.show()

