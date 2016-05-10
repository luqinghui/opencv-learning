# -*- coding: utf-8 -*-
import cv2
import numpy as np
import os
import arcpy

# -*- coding:utf-8 -*-
import arcpy
import cv2
import numpy as np
import os

def display_gray_dem_arcpy(filepath):
	"""
	通过arcpy读取dem数据
	"""
    demN = arcpy.RasterToNumPyArray(filepath)
    if demN.ndim > 2:   #多波段，显示第一个波段
        dem = demN[0,:,:]
    else:               #单波段
        dem = demN[:,:]

    minResult = arcpy.GetRasterProperties_management(filepath,"MINIMUM")
    min = float(minResult.getOutput(0))
    maxResult = arcpy.GetRasterProperties_management(filepath,"MAXIMUM")
    max = float(maxResult.getOutput(0))
    
    d = max - min
    g = map(lambda x:255*(1-(max-x)/d),dem)
    deml = np.array(g,np.uint8)
    
    winname = os.path.split(filepath)[1]
    cv2.namedWindow(winname,cv2.WINDOW_NORMAL)
    cv2.imshow(winname,deml)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

def display_gray_dem_cv2(filepath):
	"""
	通过cv2读取dem数据
	"""
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