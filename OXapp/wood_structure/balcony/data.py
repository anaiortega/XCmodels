# -*- coding: utf-8 -*-
from __future__ import division

import math

ft2m=0.3048
in2m=0.0254
pound2N=4.45

#Geometry
width=round(5*ft2m+5.5*in2m,2)
lenght=round(9*ft2m+(6+13/16.)*in2m,2)
heigth=10*ft2m
nAnchors=10 #number of decking anchorages 
anchSpac=lenght/(nAnchors-1)
deckTh=10e-3 #thickness (not considered)
tieDiam=10e-3 #tie diameter
tieArea=math.pi*tieDiam**2/4.
#Materials
Ealum=6.3e10  #Pa
nualum=0.2
rhoalum=2700  #kg/m3

#Loads
deckingW=3*pound2N/(ft2m)**2  #aluminium decking weight (3 psf)
liveL=75*pound2N/(ft2m)**2    # live load (40 psf)
snowL=42*pound2N/(ft2m)**2    # snow load (42 psf)

xList=[i*anchSpac for i in range(nAnchors)]
yList=[0,width]
zList=[0,heigth]

eSize=0.25
