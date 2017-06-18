# -*- coding: utf-8 -*-
"""
Created on Sat Jun 17 17:49:01 2017
@author: Mahmoud M. Abdelrahman

GHPL_ReshapeArray

"""
import numpy as np
import cPickle


array = "##inputArray##"
shape = ##shape##


workingDir = "##workingDir##"
fileNameString = "##fileNameString##"


DumpFile = cPickle.loads(open(array, 'r').read())

reshapedArr = np.reshape(DumpFile,shape)

datafile = open(workingDir+fileNameString+"_Txt.txt", 'w')
dumpsfile = open(workingDir+fileNameString+"_Dump.txt", 'w')


datafile.write(str(reshapedArr))
dumpsfile.write(cPickle.dumps(reshapedArr))

datafile.close()
dumpsfile.close()