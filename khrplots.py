# -*- coding: utf-8 -*-
"""
Created on Sat Jan 22 18:47:11 2022

@author: zacos
"""


import pandas as pd
from matplotlib import pyplot as plt

mdataaddress = 'c://Users/zacos/Desktop/ResearchNotebook/mosenkovKband.csv'
bdataaddress = 'c://users/zacos/Desktop/ResearchNotebook/bizyaevKband.csv'

mdata = pd.read_csv(mdataaddress)
bdata = pd.read_csv(bdataaddress)
total_data = pd.concat([mdata, bdata], axis = 0) 

bins = bins = [0.5*x for x in range(1,16)]

milkyway = 2.717 #taken from Dr. Mosenkov's paper for single sech^2 disk
color = '#fc4f30'

plt.hist(total_data['hK'], bins = bins, edgecolor = 'black')

plt.axvline(milkyway, color=color, label = 'Milky Way Scale Length')

plt.title('Scale Length of Galaxies in Kpc')
plt.xlabel('Scale Length (kpc)')
plt.ylabel('Count')
plt.legend()

plt.show()

plt.hist(mdata['hK'], bins = bins, edgecolor = 'black')
plt.axvline(milkyway, color=color, label = 'Milky Way Scale Length')

plt.title('Scale Length of Galaxies with Calculated Distances in Kpc')
plt.xlabel('Scale Length (kpc)')
plt.ylabel('Count')
plt.legend()

plt.show()

plt.hist(bdata['hK'], bins = bins, edgecolor = 'black')
plt.axvline(milkyway, color=color, label = 'Milky Way Scale Length')

plt.title('Scale Length of Galaxies with Observed Distances in Kpc')
plt.xlabel('Scale Length (kpc)')
plt.ylabel('Count')
plt.legend()

plt.show()