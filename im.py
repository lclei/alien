# -*- coding: utf-8 -*-
"""
Created on Wed Jan  3 20:23:31 2018

@author: Lcl
"""


"""
==resize图片
"""
from PIL import Image

size = (52,52)

infile = 'image/alien.png'
outfile = 'image/alien2.png'

im = Image.open(infile)
out = im.resize(size,Image.ANTIALIAS)
out.save(outfile,'png')