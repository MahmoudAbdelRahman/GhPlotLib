# -*- coding: utf-8 -*-
"""
Created on Thu Jun 22 14:15:18 2017

@author: Mahmoud M. Abdelrahman
"""

import numpy as np
import pickle 



matrixShape = ##Shape##
matrixDType = ##Dtype##
workingDir = "##workingDir##"
fileNameString = "##fileNameString##"


datafile = open(workingDir+fileNameString+"_Txt.txt", 'w')
dumpsfile = open(workingDir+fileNameString+"_Dump.txt", 'w')

matrix = np.ones(matrixShape,dtype = matrixDType)

datafile.write(str(matrix))
dumpsfile.write(np.ndarray.dumps(matrix))


datafile.close()
dumpsfile.close()
