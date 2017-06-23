# -*- coding: utf-8 -*-
"""
Created on Thu Jun 22 13:40:57 2017

@author: gamma
"""

import numpy as np
import cPickle


inputArray = ##inputArray##



workingDir = "##workingDir##"
fileNameString = "##fileNameString##"


Array = np.array(inputArray)

datafile = open(workingDir+fileNameString+"_Txt.txt", 'w')
dumpsfile = open(workingDir+fileNameString+"_Dump.txt", 'w')

datafile.write(str(Array))
dumpsfile.write(cPickle.dumps(Array))

datafile.close()
dumpsfile.close()