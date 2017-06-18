# -*- coding: utf-8 -*-
"""
Created on Sat Jun 17 04:44:56 2017

@author: gamma
"""

import numpy as np
import matplotlib.pyplot as plt

data  = "##input##"
cmap = '##cmap##'
workingDir = "##workingDir##"




openData = open(data, 'r')
data = openData.read()
data = np.loads(data)

openData.close()


min_ = np.min(data)
max_ = np.max(data)


plt.pcolor(data, cmap=cmap, shading = 'faceted')
plt.savefig(workingDir+"fig_.png")
