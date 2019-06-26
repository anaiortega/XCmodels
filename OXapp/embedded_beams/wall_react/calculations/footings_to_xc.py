# -*- coding: utf-8 -*-

from __future__ import division
from __future__ import print_function
import csv
import xc_base
import geom

csvFile= open('footings_geometry.csv')
reader= csv.reader(csvFile)

#    A     B     C
#    +-----+-----+
#    |     |     |
#    |     |O    |
#   D+-----+-----+E
#    |     |     |
#    |     |     |
#    +-----+-----+
#    F     G     H



kPoints= []
surfaces= []
for row in reader:
    id= row[0]
    center= geom.Pos3d(float(row[2]),float(row[3]),0.0)
    thickness= float(row[5])
    kPoints.append([id,center])
    B= float(row[6])
    ptO= center
    ptA= center+geom.Vector3d(-B/2.0,B/2.0,0.0)
    ptB= center+geom.Vector3d(0.0,B/2.0,0.0) 
    ptC= center+geom.Vector3d(B/2.0,B/2.0,0.0)
    ptD= center+geom.Vector3d(-B/2.0,0.0,0.0)
    ptE= center+geom.Vector3d(B/2.0,0.0,0.0)
    ptF= center+geom.Vector3d(-B/2.0,-B/2.0,0.0)
    ptG= center+geom.Vector3d(0.0,-B/2.0,0.0) #first quadrant
    ptH= center+geom.Vector3d(B/2.0,-B/2.0,0.0)
    
    surfaces.append([ptO,ptE,ptC,ptB]) #first quadrant
    surfaces.append([ptD,ptO,ptB,ptA]) #second quadrant
    surfaces.append([ptF,ptG,ptO,ptD]) #third quadrant
    surfaces.append([ptG,ptH,ptE,ptO]) #fourh quadrant

outputFile.close()
