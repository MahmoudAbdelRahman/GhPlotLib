# -*- coding: utf-8 -*-
"""
Created on Sun Jun 18 04:08:56 2017
@author: Mahmoud M. Abdelrahman
GHPL_contour
"""

import numpy as np
import matplotlib.pyplot as plt

data  = "##input##"
cmap = '##cmap##'
levels = ##levels##

workingDir = "##workingDir##"
fileNameString = "##fileNameString##"


openData = open(data, 'r')
data = openData.read()
data = np.loads(data)

openData.close()


min_ = np.min(data)
max_ = np.max(data)


plt.contour(data, cmap=cmap, levels = np.linspace(min_, max_, levels))
plt.savefig(workingDir+fileNameString+"_fig_.png")
