# -*- coding: utf-8 -*-
"""
Created on Tue Jun 20 16:00:22 2017

@author: Mahmoud M. Abdelrahman
"""

import numpy as np
import matplotlib.pyplot as plt

x  = "##x##"
y = "##y##"

_cmap = '##cmap##'
_marker = ##marker##
_size = ##size##
_color = ##color##
_alpha = ##alpha##

workingDir = "##workingDir##"
fileNameString = "##fileNameString##"


openX = open(x, 'r')
x = openX.read()
_x = np.loads(x)


openY = open(y, 'r')
y = openY.read()
_y = np.loads(y)

openX.close()
openY.close()


plt.scatter(_x, _y,s = _size, color = _color, cmap=_cmap, marker = _marker, alpha=_alpha)
plt.savefig(workingDir+fileNameString+"_fig_.png")
