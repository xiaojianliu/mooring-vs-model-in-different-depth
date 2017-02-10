# -*- coding: utf-8 -*-
"""
Created on Tue Feb  7 11:21:10 2017

@author: bling
"""
import numpy as np
import netCDF4
import math
import datetime as dt
from datetime import datetime,timedelta
lonc=np.load('lonc.npy')
latc=np.load('latc.npy')
lon=np.load('lon.npy')
lat=np.load('lat.npy')
lon1=-69.3558#Lon of mooring E
lat1=43.71517#Lat ofF Mooring E
dis=[]
for a in np.arange(len(lonc)):
    dis.append((lonc[a]-lon1)*(lonc[a]-lon1)+(latc[a]-lat1)*(latc[a]-lat1))
l=np.argmin(dis)
print l

dis=[]
for a in np.arange(len(lon)):
    dis.append((lon[a]-lon1)*(lon[a]-lon1)+(lat[a]-lat1)*(lat[a]-lat1))
l1=np.argmin(dis)
print l1

