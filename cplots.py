# -*- coding: utf-8 -*-
"""
Created on Mon Jan 24 14:28:12 2022

@author: zacos
"""

import pandas as pd
import numpy as np
from matplotlib import pyplot as plt
import os

dataaddress = os.getcwd()+'/comeronReduced.csv'

cdata = pd.read_csv(dataaddress)

cdata['rthinmax arcsec'] = cdata[['h1thin arcsec', 'h2thin arcsec', 
                               'h3thin arcsec', 'h4thin arcsec',
                               'r12thin arcsec', 'r23thin arcsec', 
                               'r34thin arcsec']].max(axis=1)

cdata['rthickmax arcsec'] = cdata[['h1thick arcsec', 'h2thick arcsec', 
                               'h3thick arcsec',
                               'r12thick arcsec', 'r23thick arcsec']].max(axis=1)

conversionF = 1/3600 * np.pi/180 * 1000
cdata['rthinmax kpc'] = cdata['rthinmax arcsec'] *conversionF *cdata['Dist Mpc'] 
cdata['rthickmax kpc'] = cdata['rthickmax arcsec']*conversionF * cdata['Dist Mpc']
cdata['sc-thin kpc'] = cdata['sc-thin arcsec'] *conversionF * cdata['Dist Mpc']
cdata['sc-thick kpc'] = cdata['sc-thick arcsec'] *conversionF * cdata['Dist Mpc']

bins = bins = [x for x in range(1,20)] #This cuts off a small number of galaxies with much larger scale lengths

milkywaythin = 2.516 #taken from Dr. Mosenkov's paper for double sech^2 disk & added effects
milkywaythick = 2.793 #as above
color = '#fc4f30'

plt.hist(cdata['rthinmax kpc'], bins = bins, edgecolor = 'black')
plt.axvline(milkywaythin, color=color, label = 'Milky Way Thin Disk Scale Length')

# plt.title('Thin Disk Scale Length of Galaxies in Kpc')
plt.xlabel('hr')
plt.ylabel('N')
# plt.legend()
plt.rc('xtick',labelsize=20)
plt.rc('ytick',labelsize=20)
plt.rc('axes', titlesize=20)
plt.rc('axes', labelsize=20)
plt.savefig(os.getcwd()+'\CThinDiskLength.png', dpi = 300, bbox_inches='tight')

plt.figure()
plt.hist(cdata['rthickmax kpc'], bins = bins, edgecolor = 'black')
plt.axvline(milkywaythick, color=color, label = 'Milky Way Thick Disk Scale Length')

# plt.title('Thick Disk Scale Length of Galaxies in Kpc')
plt.xlabel('hr')
plt.ylabel('N')
# plt.legend()
plt.rc('xtick',labelsize=20)
plt.rc('ytick',labelsize=20)
plt.rc('axes', titlesize=20)
plt.rc('axes', labelsize=20)
plt.savefig(os.getcwd()+'\CThickDiskLength.png', dpi = 300, bbox_inches='tight')


milkywaythinsc = .238 #taken from Dr. Mosenkov's paper
milkywaythicksc = .976
bins = [x*.1 for x in range(1,10)]

plt.figure()
plt.hist(cdata['sc-thin kpc'], bins = bins, edgecolor = 'black')
plt.axvline(milkywaythinsc, color=color, label = 'Milky Way Thin Disk Scale Height')

# plt.title('Thin Disk Scale Height of Galaxies in Kpc')
plt.xlabel('hz')
plt.ylabel('N')
# plt.legend()
plt.rc('xtick',labelsize=20)
plt.rc('ytick',labelsize=20)
plt.rc('axes', titlesize=20)
plt.rc('axes', labelsize=20)
plt.savefig(os.getcwd()+'\CThinDiskHeight.png', dpi = 300, bbox_inches='tight')

bins = [x*.25 for x in range(1,16)]

plt.figure()
plt.hist(cdata['sc-thick kpc'], bins = bins, edgecolor = 'black')
plt.axvline(milkywaythicksc, color=color, label = 'Milky Way Thick Disk Scale Height')

# plt.title('Thick Disk Scale Height of Galaxies in Kpc')
plt.xlabel('hz')
plt.ylabel('N')
# plt.legend()
plt.rc('xtick',labelsize=20)
plt.rc('ytick',labelsize=20)
plt.rc('axes', titlesize=20)
plt.rc('axes', labelsize=20)
plt.savefig(os.getcwd()+'\CThickDisk.png', dpi = 300, bbox_inches='tight')