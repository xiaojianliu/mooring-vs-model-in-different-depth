# -*- coding: utf-8 -*-
"""
Created on Tue Jan 31 15:50:20 2017

@author: bling
"""
import matplotlib.pyplot as plt
import numpy as np
data = np.genfromtxt('E0130.csv',dtype=None,names=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z','aa','ab','ac'],delimiter=',',skip_header=1)  
u=[]
v=[]
for a in np.arange(len(data['b'])):
    u.append(data['b'][a]/float(100))

    v.append(data['c'][a]/float(100))

#u=np.load('u.npy')
#udr=np.load('udr.npy')
#vdr=np.load('vdr.npy')
#v=np.load('v.npy')
um=np.load('umo.npy')
vm=np.load('vmo.npy')

u=u[0:720]
v=v[0:720]
um=um[0:720]
vm=vm[0:720]

plt.figure()
plt.title('u depth=10m 2013-11')
plt.plot(u,'g-',label='mooring E01')
#plt.plot(udr,'r-',label='drifter')
plt.plot(um,'b-',label='model')
plt.ylabel('m/s')
plt.xlabel('hours')
plt.legend(loc='best')
plt.savefig('u',dpi=700)
plt.figure()
plt.title('v depth=10m 2013-11')
plt.plot(v,'g-',label='mooring E01')
#plt.plot(vdr,'r-',label='drifter')
plt.plot(vm,'b-',label='model')
plt.legend(loc='best')
plt.ylabel('m/s')
plt.xlabel('hours')
plt.savefig('v',dpi=700)
print np.mean(u-um)
print np.mean(v-vm)
print np.std(u-um)
print np.std(v-vm)