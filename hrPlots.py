# -*- coding: utf-8 -*-
"""
Created on Thu Dec 30 13:47:49 2021

@author: zacos
"""

import pandas as pd
from matplotlib import pyplot as plt
import os

calculated_data = pd.read_csv(os.getcwd()+'/MosenkovData/calculateddistancedata.csv')
observed_data = pd.read_csv(os.getcwd()+'/mosenkovdata/observeddistancedata.csv')
total_data = pd.concat([calculated_data, observed_data], axis = 0) 

bins = bins = [0.5*x for x in range(1,16)]

milkyway = 2.717 #taken from Dr. Mosenkov's paper for single sech^2 disk
color = '#fc4f30'

plt.hist(total_data['hr kpc'], bins = bins, edgecolor = 'black')

plt.axvline(milkyway, color=color, label = 'Milky Way Scale Length')

# plt.title('Scale Length of Galaxies in Kpc')
plt.xlabel('hr')
plt.ylabel('N')
plt.rc('xtick',labelsize=20)
plt.rc('ytick',labelsize=20)
plt.rc('axes', titlesize=20)
plt.rc('axes', labelsize=20)
plt.savefig(os.getcwd()+'/S4GhrTot.png', dpi = 300, bbox_inches='tight')
# plt.legend()

plt.show()

plt.figure()
plt.hist(calculated_data['hr kpc'], bins = bins, edgecolor = 'black')
plt.axvline(milkyway, color=color, label = 'Milky Way Scale Length')

# plt.title('Scale Length of Galaxies with Calculated Distances in Kpc')
plt.xlabel('hr)')
plt.ylabel('N')
# plt.legend()
plt.rc('xtick',labelsize=20)
plt.rc('ytick',labelsize=20)
plt.rc('axes', titlesize=20)
plt.rc('axes', labelsize=20)
plt.savefig(os.getcwd()+'/S4GhrCalc.png', dpi = 300, bbox_inches='tight')

plt.figure()

plt.hist(observed_data['hr kpc'], bins = bins, edgecolor = 'black')
plt.axvline(milkyway, color=color, label = 'Milky Way Scale Length')

# plt.title('Scale Length of Galaxies with Observed Distances in Kpc')
plt.xlabel('hr')
plt.ylabel('N')
# plt.legend()
plt.rc('xtick',labelsize=20)
plt.rc('ytick',labelsize=20)
plt.rc('axes', titlesize=20)
plt.rc('axes', labelsize=20)
plt.savefig(os.getcwd()+'/S4GhrObs.png', dpi = 300, bbox_inches='tight')

# plt.show()