# -*- coding: utf-8 -*-
"""
Created on Wed Sep 16 22:14:17 2015

@author: nausheenfatma
"""
import numpy

inFile = numpy.memmap("testfile", dtype = 'float32', mode = 'w+', shape = (9,4))
inFile[0,3] = 3.2
inFile[1,3]=1
inFile[2,2]=2
inFile[3,]=[1,2,3,4]
inFile[4,]=[1,5,6,7]
inFile[5,]=[2,3,5,6]
inFile[6,]=[8,0,1,2]
inFile[7,]=[9,5,5,7]
inFile[8,]=[1,3,3,1]
print inFile
myNewVariable = inFile[3,]
print myNewVariable
inFile.flush()
