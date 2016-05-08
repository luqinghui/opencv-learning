# -*- coding: utf-8 -*-
"""
Created on Sun May 08 18:22:10 2016

@author: lu
"""

import cv2
import numpy as np

filepath = r'D:\Tmp\dem\data\dem1.tif'
dem = cv2.imread(filepath,cv2.IMREAD_LOAD_GDAL|cv2.IMREAD_ANYDEPTH)

min, max, minloc, maxloc = cv2.minMaxLoc(dem)
d = max-min
g = map(lambda x:255*(1-(max-x)/d),dem)
deml = np.array(g,np.uint8)

cv2.imshow('dem', deml)

thg = cv2.adaptiveThreshold(deml,255,cv2.ADAPTIVE_THRESH_GAUSSIAN_C,cv2.THRESH_BINARY,11,2)

cv2.imshow('threshold',thg)
cv2.waitKey(0)
cv2.destroyAllWindows()