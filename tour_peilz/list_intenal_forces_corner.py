# -*- coding: utf-8 -*-
execfile('xc_model_data.py') #data for FE model generation

import csv


sg= geom.Segment3d(geom.Pos3d(42.0633,10.125,6.7937),geom.Pos3d(24.4821,10.125,8.5518))

hingeElements= {} #preprocessor.getSets.defSet('hingeElements')
maximum= {}
minimum= {}

for e in floor_elements.getElements:
    elemCentroid= e.getPosCentroid(True)
    d= sg.distPos3d(elemCentroid)
    if(d<0.18):
        #hingeElements.getElements.append(e)
        hingeElements[e.tag]= e
        maximum[e.tag]= -1e15 #Maximum and minimum values.
        minimum[e.tag]= 1e15
        print 'tag: ', e.tag, ' d= ', d, 'x= ', elemCentroid.x

f= open('./results/internalForces/intForce_ULS_normalStressesResistance.csv', 'rb')
reader = csv.reader(f)
next(reader, None)  # skip the header
for row in reader:
  tag= int(row[1])
  if tag in hingeElements:
      section= int(row[2])
      if(section==1):
          e= hingeElements[tag]
          x= e.getPosCentroid(True).x
          comb= row[0]
          my= float(row[7])
          maximum[tag]= max(maximum[tag],my)
          minimum[tag]= min(minimum[tag],my)
f.close()
writer = csv.writer(open("pp.csv", 'w'))
for tag in hingeElements:
      e= hingeElements[tag]
      x= e.getPosCentroid(True).x
      vMax= maximum[tag]
      vMin= minimum[tag]
      writer.writerow([x,tag,vMin,vMax])
