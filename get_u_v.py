# -*- coding: utf-8 -*-
"""
Created on Wed Jan 25 16:15:52 2017

@author: bling
"""
import numpy as np
import netCDF4
import math
import datetime as dt
from datetime import datetime,timedelta
def get_u_v(time,lon,lat,depth):
    url='''http://www.smast.umassd.edu:8080/thredds/dodsC/models/fvcom/NECOFS/Archive/Seaplan_33_Hindcast_v1/gom3_201311.nc?lonc[0:1:90414],latc[0:1:90414],Times[0:1:720],u[0:1:720][0:1:44][0:1:90414],v[0:1:720][0:1:44][0:1:90414],h[0:1:48450],lon[0:1:48450],lat[0:1:48450],siglay[0:1:44][0:1:48450],zeta[0:1:720][0:1:48450]'''
    #url='''http://www.smast.umassd.edu:8080/thredds/dodsC/fvcom/archives/necofs_mb?lonc[0:1:165094],latc[0:1:165094],Times[0:1:34655],u[0:1:34655][0:1:9][0:1:165094],v[0:1:34655][0:1:9][0:1:165094]'''
    #url = '''http://www.smast.umassd.edu:8080/thredds/dodsC/fvcom/hindcasts/30yr_gom3?u[0:1:333551][0:1:44][0:1:90414],v[0:1:333551][0:1:44][0:1:90414]'''       
    nc = netCDF4.Dataset(url)
    args=['u','v','Times','lonc','latc','lon','lat','h','siglay','zeta']
    data = {}
    for arg in args:
        data[arg] = nc.variables[arg]
    Times=np.load('Time.npy')#model time
    #print 'Times',Times[0]
    Time=[]
    for a in np.arange(len(Times)):
        Time.append(dt.datetime(int(str(Times[a][0])+str(Times[a][1])+str(Times[a][2])+str(Times[a][3])),int(str(Times[a][5])+str(Times[a][6])),int(str(Times[a][8])+str(Times[a][9])),int(str(Times[a][11])+str(Times[a][12]))))#,datetime.strptime(str(Times[a][0:13]), '%Y-%m-%d'+'T'+'%H'))
    lonc=np.load('lonc.npy')
    latc=np.load('latc.npy')
    lon1=np.load('lon.npy')
    lat1=np.load('lat.npy')
    t=[]
    #print 'len(Time)',len(Time)
    #print time
    for a in np.arange(len(Time)):
        t.append(abs(Time[a]-time))
    #print Time
    print 't',len(t)
    t1=np.argmin(t)
    print 't1',t1
    print time
    print Time[t1]
    l=57843# index in lonc
    l1=29602# index in lon
    print lon,lat
    print lonc[l],latc[l]
    print lon1[l1],lat1[l1]
    h=data['h'][l1]+data['zeta'][t1,l1]
    depth_total = data['siglay'][:,l1]*h; 
    layer = np.argmin(abs(depth_total+depth)); #print 'layer',layer
    print layer
    return data['u'][t1][layer][l],data['v'][t1][layer][l]

data = np.genfromtxt('E01.csv',dtype=None,names=['s','time','c','sudu','e','jiao','g','tem','i','lon','lat','depth'],delimiter=',',skip_header=2)  
u=[]
v=[]

depth=10
time=[]
lon=[]
lat=[]
for a in np.arange(len(data['time'])):
    print a
    time.append(datetime.strptime(data['time'][a], '%Y-%m-%d'+'T'+'%H:%M:%SZ')-timedelta(365))
    lon.append(data['lon'][a])
    lat.append(data['lat'][a])
uu=[]
vv=[]
n=[]

for a in np.arange(len(lon)):
    print 'a',a
    u1,v1=get_u_v(time[a],lon[a],lat[a],depth)
    n.append(a)
    uu.append(u1)
    vv.append(v1)
np.save('umo',uu)
np.save('vmo',vv)
np.save('n',n)

