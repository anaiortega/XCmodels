# -*- coding: utf-8 -*-

# Cracking test 05. Geometric, material and load data

width=1.0     #width (cross-section coordinate Y)
depth=0.5    #depth (cross-section coordinate Z)
f_ck=336      #concrete characteristic strength [Pa] (concrete C30-37 adopted)
f_ct=3.086*1e6   # concrete tensile strength
               # (in the test the calculated fctm=2896468.15 is used)

cover=0.05    #cover
# A_s=5310e-6    #area of bottom reinforcement layer (13 fi 26)
# A_sp=0    #area of top reinforcement layer 

N_x=0           #axial force [N]
M_y=-600e3      #bending moment [Nm]
M_z=0      #bending moment [Nm]


#Other data
nDivIJ= 20  #number of cells (fibers) in the IJ direction (cross-section coordinate Y)
nDivJK= 20  #number of cells (fibers) in the JK direction (cross-section coordinate Z)

fiBott=26e-3  #diameter of the reinf. bar in the bottom layer
nmbBarsBott=13   #number of reinforcement bars in the bottom layer
fiTop=12e-3  #diameter of the reinf. bar in the top layer
nmbBarsTop=0   #number of reinforcement bars in the top layer


l= 1e-7     # Distance between nodes

