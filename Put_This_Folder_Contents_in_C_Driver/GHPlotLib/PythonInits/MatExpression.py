# -*- coding: utf-8 -*-
"""
Created on Fri Jun 16 13:24:11 2017

@author: gamma
"""
import numpy as np
import pickle

sourceFileName = "##sourceFileName##"
workingDir = "##WorkingDir##"
fileName= "##fileName##"

openFile = open(sourceFileName, 'r')
fileText = openFile.read()

loadsFile = pickle.loads(fileText)

result =  ##Expression## loadsFile

print result

SaveFile = open(workingDir+"matX.txt", 'w')
SaveFileText = SaveFile.write(pickle.dumps(result))

SaveLogFile = open(workingDir+fileName, 'w')
SaveLogFile.write(str(result))

SaveFile.close()
openFile.close()