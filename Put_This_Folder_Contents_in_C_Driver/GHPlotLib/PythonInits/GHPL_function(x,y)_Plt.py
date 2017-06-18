# -*- coding: utf-8 -*-
"""
Created on Sat Jun 17 14:11:35 2017

@author: gamma
"""

import numpy as np
import cPickle


#data
_x = "##x##"
_y = "##y##"
_z = "##z##"
_u = "##u##"
_v = "##v##"
_w = "##w##"

workingDir = "##workingDir##"
fileNameString = "##fileNameString##"


if _x != "None" :
    fx = open(_x, 'r')
    gx = fx.read()
    x=cPickle.loads(gx)
    
if _y != "None" :
    fy = open(_y, 'r')
    gy = fy.read()
    y=cPickle.loads(gy)
    
if _z != "None" :
    fz = open(_z, 'r')
    gz = fz.read()
    z=cPickle.loads(gz)
    
if _u != "None" :
    fu = open(_u, 'r')
    gu = fu.read()
    u=cPickle.loads(gu)
    
if _v != "None" :
    fv = open(_v, 'r')
    gv = fx.read()
    v=cPickle.loads(gv)
    
if _w != "None" :
    fw = open(_w, 'r')
    gw = fw.read()
    w=cPickle.loads(gw)

_fucntion = ##function##


datafile = open(workingDir+fileNameString+"_Txt.txt", 'w')
dumpsfile = open(workingDir+fileNameString+"_Dump.txt", 'w')


datafile.write(str(_fucntion))
dumpsfile.write(cPickle.dumps(_fucntion))

datafile.close()
dumpsfile.close()

