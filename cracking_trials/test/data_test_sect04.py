# -*- coding: utf-8 -*-

# Cracking test 04. Geometric, material and load data

width=1.0     #width (cross-section coordinate Y)
depth=0.5    #depth (cross-section coordinate Z)

cover=0.05    #cover


#M_y=-600e3      #bending moment in mid-span [Nm]
M_y=-600

#Other data
nDivIJ= 20  #number of cells (fibers) in the IJ direction (cross-section coordinate Y)
nDivJK= 20  #number of cells (fibers) in the JK direction (cross-section coordinate Z)

fiBott=26e-3  #diameter of the reinf. bar in the bottom layer
nmbBarsBott=10   #number of reinforcement bars in the bottom layer
fiTop=12e-3  #diameter of the reinf. bar in the top layer
nmbBarsTop=0   #number of reinforcement bars in the top layer


Lbeam= 1     # Beam length

fUnif=xc.Vector([0,0,M_y*8/Lbeam**2,0,0,0])  #uniform load on the beam
