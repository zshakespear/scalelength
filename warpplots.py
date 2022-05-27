# -*- coding: utf-8 -*-
"""
Created on Wed Feb  2 09:26:32 2022

@author: zacos
"""

import pandas as pd
from matplotlib import pyplot as plt
import os

mdataadd = os.getcwd()+'/mwarpRAW.csv'
adataadd = os.getcwd()+'/AnnRAW.csv'

mdata = pd.read_csv(mdataadd)
adata = pd.read_csv(adataadd)
mdatar = mdata[['PGC', 'avg alpha']]
adatar = adata[['PGC', 'avg alpha']]
combinedr = pd.concat([mdatar,adatar])

bins = bins = [-6 + x for x in range(1,21)] 

plt.hist(combinedr['avg alpha'], bins = bins, edgecolor = 'black' )

# plt.title('Warping Angle of Edge-on Galaxies')
plt.xlabel(r'$\theta$')
plt.ylabel('N')
# plt.legend()
plt.rc('xtick',labelsize=20)
plt.rc('ytick',labelsize=20)
plt.rc('axes', titlesize=20)
plt.rc('axes', labelsize=20)
plt.savefig(os.getcwd()+'/Warp.png', dpi = 300, bbox_inches='tight')
# plt.show()

