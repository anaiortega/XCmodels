# -*- coding: utf-8 -*-
import math

#units
kmh2ms=1/3.6

#Geometry data
diam=3.18      # diameter
R=diam/2.0     #radius
height=20.6    # height of the cylindrical tank
zGround=0      # ground level
zBaseCyl=4.5   #z-coord of the tank base

#Material
steel=astm.A36

#Weight
Wtank=63375 #weight of the tank [kg]
thickness=Wtank/(2*math.pi*R*height)/steel.rho
#Wind data
v=155*kmh2ms #basic speed wind [m/s]
Kd=0.95      #wind directionality factor
Kzt=1.0      #topographic factor
I=1.15       #importance factor
alpha=9.5    #terrain exposure constant (exposure C)
zg=275       #terrain exposure constant (exposure C)
windComp=[1,0] # components [x,y] of a vector in wind direction 

#Thermal data
tempRise=25    #temperature rise (ºC)
tempFall=-15   #temperature fall (ºC)

eSize= 0.35    #length of elements

