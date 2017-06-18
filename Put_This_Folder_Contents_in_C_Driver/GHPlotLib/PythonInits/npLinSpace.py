# -*- coding: utf-8 -*-
"""
Created on Sat Jun 17 01:49:58 2017

@author: gamma
"""

import numpy as np
import cPickle

start = ##start##
end = ##end##
steps = ##steps##
workingDir = "##workingDir##"

dumpsFile = "npLinspaceDump.txt"
dataLogfile = "npLinspaceTxt.txt"

a = np.linspace(start,end, steps)
print a

datafile = open(workingDir+dataLogfile, 'w')
dumpsfile = open(workingDir+dumpsFile, 'w')

datafile.write(str(a))
dumpsfile.write(cPickle.dumps(a))

datafile.close()
dumpsfile.close()
