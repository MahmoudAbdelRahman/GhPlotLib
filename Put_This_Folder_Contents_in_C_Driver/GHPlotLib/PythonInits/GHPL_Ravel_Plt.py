# -*- coding: utf-8 -*-
"""
Created on Thu Jun 22 13:30:37 2017

@author: gamma
"""

import numpy as np
import cPickle


inputArray = "##inputArray##"



workingDir = "##workingDir##"
fileNameString = "##fileNameString##"


openInput = np.loads(open(inputArray, 'r').read())

RavelArray = np.ravel(openInput)

datafile = open(workingDir+fileNameString+"_Txt.txt", 'w')
dumpsfile = open(workingDir+fileNameString+"_Dump.txt", 'w')

datafile.write(str(RavelArray))
dumpsfile.write(cPickle.dumps(RavelArray))

datafile.close()
dumpsfile.close()