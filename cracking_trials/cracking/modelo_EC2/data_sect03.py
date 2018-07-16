# -*- coding: utf-8 -*-

# Cracking test 03. Geometric, material and load data

width=0.4     #width (cross-section coordinate Y)
depth=0.6     #depth (cross-section coordinate Z)
f_ck=30e6      #concrete characteristic strength [Pa] (concrete C30-37 adopted)
f_ct=2.9*1e6   # concrete tensile strength
               # (in the test the calculated fctm=2896468.15 is used)

cover=0.04     #cover
A_s=2712e-6    #area of bottom reinforcement layer (6 fi 24)
A_sp=452e-6    #area of top reinforcement layer (4 fi 12)

N_x=0           #axial force [N]
M_y=-300e3      #bending moment [Nm]
M_z=0      #bending moment [Nm]

#ro_s_eff=0.05215      #effective ratio of reinforcement

#Other data
nDivIJ= 20  #number of cells (fibers) in the IJ direction (cross-section coordinate Y)
nDivJK= 20  #number of cells (fibers) in the JK direction (cross-section coordinate Z)

fiBott=24e-3  #diameter of the reinf. bar in the bottom layer
nmbBarsBott=6   #number of reinforcement bars in the bottom layer
fiTop=12e-3  #diameter of the reinf. bar in the top layer
nmbBarsTop=4   #number of reinforcement bars in the top layer


l= 1e-7     # Distance between nodes

