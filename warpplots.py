# -*- coding: utf-8 -*-
"""
Created on Wed Feb  2 09:26:32 2022

@author: zacos
"""

import pandas as pd
from matplotlib import pyplot as plt

mdataadd = 'c://users/zacos/desktop/ResearchNotebook/mwarpRAW.csv'
adataadd = 'c://users/zacos/desktop/ResearchNotebook/AnnRAW.csv'

mdata = pd.read_csv(mdataadd)
adata = pd.read_csv(adataadd)
mdatar = mdata[['PGC', 'avg alpha']]
adatar = adata[['PGC', 'avg alpha']]
combinedr = pd.concat([mdatar,adatar])

bins = bins = [-6 + x for x in range(1,21)] 

plt.hist(combinedr['avg alpha'], bins = bins, edgecolor = 'black' )

plt.title('Warping Angle of Edge-on Galaxies')
plt.xlabel('Warping Angle (deg)')
plt.ylabel('Count')
plt.legend()
plt.show()

