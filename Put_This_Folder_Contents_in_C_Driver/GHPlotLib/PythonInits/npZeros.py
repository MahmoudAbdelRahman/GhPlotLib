# -*- coding: utf-8 -*-
"""
Created on Fri Jun 16 04:51:14 2017

@author: gamma
"""

import numpy as np
import pickle 



matrixShape = ##Shape##
matrixDType = ##Dtype##
workingDir = ##workingDir##
log = ""



LogFile = open(workingDir+"logfile.txt", 'w')
MatrixDumps = open(workingDir+"Matrix.txt", 'w')


try:
    matrix = np.zeros(matrixShape,dtype = matrixDType)
except Exception as e:
    log+= str(e)+"\n"
try:    
    LogFile.write(str(matrix))
except Exception as e:
    log+= str(e)+"\n"

MatrixDumps.write(np.ndarray.dumps(matrix))
