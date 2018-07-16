# -*- coding: utf-8 -*-

# model of a simply supported T-beam bridge, which covers am effective span of 45 m.
#It corresponds to the case study in chapter 8 of the guidebook 2 'Design of bridges',
#by Pietro Croce et al.
#concrete:C50/60 
#reinforcing steel B450C

import os
import xc_base
import geom
import xc
from model.grid_based_oldStyle_deprecated import ijkGrid
from model.grid_based_oldStyle_deprecated import GridModel as gm
from actions import combinations as cc
from postprocess import limit_state_data as lsd
from materials import typical_materials 
from materials.ec3 import EC3_materials
import math


#Auxiliary data
  #Geometry
totalSpan=45     #span between supports
distDiaph=15     #distance between diaphragms
deckSlabTh=0.30  #thickness of the concrete slab
diaphTh=0.235    #thickness of the transverse beams (diaphragms)
diaphHeight=2.26 #height of diaphragms
posZcogBeams=2   
posXbeams=[1,3,5,8]

#Materials 
from materials.ec2 import EC2_materials
concr= EC2_materials.C50
Ec=concr.Ecm()
nuc=concr.nuc
densc= 2500 #specific mass of concrete (kg/m3)

#Prestressed beams
wTF=(0.9+0.82)/2.0 #mean width of the top flange
tTF=0.2+0.35/2.0  #mean thickness of the top flange
tW=0.3             #mean width of the web
hW=1.81            #height of the web
wBF=(0.98+0.8)/2.0 #mean weight of the bottom flange
tBF=0.3+0.3/2.0    #mean thickness of the bottom flange
hTotal=0.6+1.81+0.35  #total height
hCOG=1.24          #position of the center of gravity with respect to the lower face
areaBeam=1.24
IhorizBeam=1.099   #moment of inertia about the horizontal axis
IvertBeam=0.045    #moment of inertia about the vertical axis
alphYBeam=0.32     #shear shape factor with respect to local y-axis
alphZBeam=0.69     #shear shape factor with respect to local z-axis

#torsional moment of inertia
hPrf=hTotal-tTF/2.0-tBF/2.0
Jbeam=(wTF*tTF**3+wBF*tBF**3+hPrf*tW**3)/3.0
#section modulus
WhorizBeam=IhorizBeam/(hTotal-hCOG)
WvertBeam=IvertBeam/(wTF/2.0)


  #Actions
# asphaltDens=2400    #mass density of asphalt (kg/m3)
# asphaltTh=0.12      #thickness of asphalt on the deck (m)
# guardRailWght=500   #weight of the guard rail (N/m)
# firad=math.radians(31)  #internal friction angle (radians)                   
# KearthPress=(1-math.sin(firad))/(1+math.sin(firad))     #Active coefficient of pressure considered 
# densSoil=2200       #mass density of the soil (kg/m3)
# densWater=1000      #mass density of the water (kg/ms)
   #traffic loads
     # coefficients (depending on the traffic composition: hw-highway sr-subsidiary road)
# alphQ1hw=0.9
# alphQ2hw=0.9
# alphq1hw=0.9
# alphq2hw=0.9
# alphq3hw=0.9
# alphqrhw=0.9
# alphQ1sr=0.65
# alphq1sr=0.65

# Qk1=300e3          #(N in each axle)
# Qk1wheel=300e3/2   #(N in each wheel)
# Qk2=200e3          #(N in each axle)
# Qk2wheel=Qk2/2     #(N in each wheel)
# qk1=9e3            #(N/m2)
# qk2=2.5e3          #(N/m2)
# qk3=2.5e3          #(N/m2)
# qkr=2.5e3          #(N/m2)

# #Y positions of traffic lanes in highway and subsidiary road
# YposLane1HwSit1=[9,10]
# YposLane2HwSit1=[8,9]
# YposLane3HwSit1=[7,8]
# YposRestHwSit1=[5,7]
# YposLane1HwSit2=[7,8]
# YposLane2HwSit2=[6,7]
# YposLane3HwSit2=[5,6]
# YposRestHwSit2=[8,10]
# YposLane1Sr=[3,4]

# #Exceptional transport (model 3)
# YposAxe=9    
# excentr=0.5
# distTrWheels=3
# distLnWheels=1.8
# xminTruck=1
# QwheelExcTr=100e3     #load/wheel [N]
# alphQExcTr=1.00   

#       #Braking load
# brakingQhw=min(1.2*alphQ1hw*Qk1+0.1*alphq1hw*qk1*3*totalwidth,900e3)  #in highway
# brakingQsr=min(1.2*alphQ1sr*Qk1+0.1*alphq1sr*qk1*3*totalwidth,900e3)  #in subsidiary road
#     #Road sub-base thickness
# subbThHw=1.8         #mean sub-base thickness under the highway
# subbThSr=1.2         #mean sub-base thickness under the subsidiary road
# densSubb=2.2e3        #mass density (kg/m3) of the sub-base material




# *** GEOMETRY ***
TBBridge= xc.FEProblem()
model= gm.GridModel(TBBridge)


# coordinates in global X,Y,Z axes for the grid generation
xList=[0,1.475,2.15,4.425,5.15,7.375,8.15,9.65,10.325,11.8]
yList=[0,15,30,45]
zList=[0,1.24-0.3,diaphHeight,diaphHeight+0.20+deckSlabTh/2.0]
#auxiliary data
lastXpos=len(xList)-1
lastYpos=len(yList)-1
lastZpos=len(zList)-1

# grid of X,Y,Z axes coordinates
rejXYZ= model.setGrid(xList,yList,zList)

#Displacements of the grid points in a range
#syntax: moveRange(ijkGrid.IJKRange([minIindex,minJindex,minKindex],[maxIindex,maxJindex,maxKindex],[dispX,dispY,dispZ])
# for i in range(1,len(xList)):
#   r= ijkGrid.IJKRange([i,0,lastZpos],[i,lastYpos,lastZpos])
#   mr= ijkGrid.moveRange(r,[0.0,0.0,trSlope*xList[i]])
#   rejXYZ.rangesToMove.append(mr)



# *** MATERIALS *** 
#*Auxiliary data
#fck=30e6  #characteristic strength of concrete (Pa)
#fcm=fck+8e6 #mean strength of concrete (Pa)
#Ec=8500*fcm/1e6**(1/3.0)*1e6 #modulus of elasticity of concrete

concrDeckBeam=typical_materials.MaterialData(name='concrDeckBeam',E=Ec,nu=nuc,rho=densc)
# S275JR= EC3_materials.S275JR
# S275JRbeam=typical_materials.MaterialData(name='S275JRbeam',E=S275JR.E,nu=S275JR.nu,rho=7850)

#geometric sections
  # Isotropic elastic section-material appropiate for plate and shell analysis
  # Attributes:
  #   name:         name identifying the section
  #   E:            Young’s modulus of the material
  #   nu:           Poisson’s ratio
  #   rho:          mass density
  #   thickness:    overall depth of the section

deckSlab= gm.DeckMaterialData(name= 'deckSlab', thickness= deckSlabTh, material=concrDeckBeam)
stiffTBeams=gm.DeckMaterialData(name= 'stiffTBeams', thickness= diaphTh, material=concrDeckBeam)

  # Elastic section appropiate for 3D beam analysis, including shear deformations.
#Rectangular sections:
  # Attributes:
  #   name:         name identifying the section
  #   b:            cross-section width (parallel to local z axis)
  #   h:            cross-section height (parallel to local y axis)
  #   E:            Young’s modulus of the material
  #   nu:           Poisson’s ratio
# from materials.sections import section_properties
# sect_beam0_5x0_75=section_properties.RectangularSection(name='sect_beam0_5x0_75',b=0.5,h=0.75)  #section definition

# beam0_5x0_75=gm.BeamMaterialData(name='beam0_5x0_75',section=sect_beam0_5x0_75,material=concrDeckBeam) #material definition (rho: mass density)

#Circular sections:
  # Attributes:
  #  name:      name identifying the section
  #  r:         radius
  #  E:         Young’s modulus of the material
  #  nu:        Poisson’s ratio
# from materials.sections import section_properties
# sect_beamR0_5=section_properties.CircularSection(name='sect_beamR0_5',r=0.5)  #section definition
# beamR0_5=gm.BeamMaterialData(name='beamR0_5',section=sect_beamR0_5,material=concrDeckBeam) #material definition (rho: mass density)

#I sections:
  #  name:         name identifying the section
  #  wdTopFlange:  width of the top flange (parallel to local z-axis)
  #  thTopFlange:  thickness of the top flange (parallel to local y-axis)
  #  thWeb:        thickness of the web (parallel to local z-axis)
  #  hgWeb:        height of the web (parallel to local y-axis)
  #  wdBotFlange:  width of the bottom flange (parallel to local z-axis)
  #  thBotFlange:  thickness of the bottom flange (parallel to local y-axis)
  #  E:            Young’s modulus of the material
  #  nu:           Poisson’s ratio

# from materials.sections import section_properties
# sect_Ibeam=section_properties.ISection(name='sect_Ibeam',wdTopFlange=0.9,thTopFlange=0.3,thWeb=0.25,hgWeb=1.80,wdBotFlange=0.95,thBotFlange=0.5)  #section definition
# Ibeam=gm.BeamMaterialData(name='Ibeam',section=sect_Ibeam,material=concrDeckBeam)     #material definition (rho: mass density)

#Generic sections
  # name:         name identifying the section
  # area:         cross-sectional area
  # Iy:           second moment of area about the local y-axis
  # Iz:           second moment of area about the local z-axis
  # Jtors:        torsional moment of inertia of the section
  # Wy:           section modulus with respect to local y-axis
  # Wz:           section modulus with respect to local z-axis
from materials.sections import section_properties
sect_generic=section_properties.GenericSection(name='sect_generic',area=areaBeam,I_y=IhorizBeam,I_z=IvertBeam,Jtors=Jbeam,W_y=WhorizBeam,W_z=WvertBeam,alphY=alphYBeam,alphZ=alphZBeam)  #section definition
prestBeam=gm.BeamMaterialData(name='prestBeam',section=sect_generic,material=concrDeckBeam)     #material definition (rho: mass density)


#steel shape
  # steel:    steel object (e.g. S275JR)
  # table:    module containing a dictionary with mechanical characteristics
  #                of a series of shapes 
  #                (e.g. materials.sections.structural_shapes.arcelor_metric_shapes.HE)
  # name:     name identifying the section in the table

# from materials.sections.structural_shapes import arcelor_metric_shapes
# from materials.ec3 import EC3_materials
# S275JR= EC3_materials.S275JR
# sect_HE400B= stP.SteelShape(S275JR,"HE_400_B",arcelor_metric_shapes.HE)
# HE400B=gm.BeamMaterialData(name='HE_400_B',section=sect_HE400B,material=S275JRbeam)


#  Dictionary of materials
matElMembPlat= model.setMaterials([deckSlab,stiffTBeams,prestBeam])

eSize= 0.5
    # Types of surfaces to be discretized from the defined 
    # material, type of element and size of the elements.
    # Parameters:
    #   name:     name to identify the type of surface
    #   material: name of the material that makes up the surface
    #   elemType: element type to be used in the discretization
    #   elemSize: mean size of the elements
    #   ranges:   lists of grid ranges to delimit the surfaces of 
    #             the type in question
deck= model.newMaterialSurface('deck', material=deckSlab, elemType='ShellMITC4',elemSize= eSize)
deck.ranges= [ ijkGrid.IJKRange([0,0,lastZpos],[lastXpos,lastYpos,lastZpos]) ]
#stiff transverse beams (diaphragms)
diaph=model.newMaterialSurface('diaph', material=stiffTBeams, elemType='ShellMITC4',elemSize= eSize)
diaph.ranges= [ ijkGrid.IJKRange([posXbeams[0],0,0],[posXbeams[3],0,2]), ijkGrid.IJKRange([posXbeams[0],1,0],[posXbeams[3],1,2]),ijkGrid.IJKRange([posXbeams[0],2,0],[posXbeams[3],2,2]),ijkGrid.IJKRange([posXbeams[0],3,0],[posXbeams[3],3,2])]

#Dictionary of material-surfaces
conjSup= model.setMaterialSurfacesMap([deck,diaph])

    # Types of lines to be discretized from the defined 
    # material, type of element and size of the elements.
    # Parameters:
    #   name:     name to identify the material-line
    #   material: name of the material that makes up the line
    #   elemType: element type to be used in the discretization
    #   elemSize: mean size of the elements
    #   vDirLAxZ: direction vector for the element local axis Z 
    #             defined as xc.Vector([x,y,z]). This is the direction in which
    #             the Z local axis of the reinforced concrete sections will be
    #             oriented (i.e. in the case of rectangular sections this Z 
    #             local axis of the RC section is parallel to the dimension
    #             defined as width of the rectangle)
    #   ranges:   lists of grid ranges to delimit the lines of 
    #             the type in question
beams= model.newMaterialLine('beams', material= prestBeam, elemType='ElasticBeam3d',elemSize= eSize,vDirLAxZ=xc.Vector([1,0,0]))
beams.ranges= [ ijkGrid.IJKRange([posXbeams[0],0,1],[posXbeams[0],lastYpos,1]), ijkGrid.IJKRange([posXbeams[1],0,1],[posXbeams[1],lastYpos,1]), ijkGrid.IJKRange([posXbeams[2],0,1],[posXbeams[2],lastYpos,1]), ijkGrid.IJKRange([posXbeams[3],0,1],[posXbeams[3],lastYpos,1])]

#Dictionary of material-lines
conjLines= model.setMaterialLinesMap([beams])


    # Regions resting on springs (Winkler elastic foundation)
    #   name:     name to identify the region
    #   wModulus: Winkler modulus of the foundation (springs in Z direction)
    #   cRoz:     fraction of the Winkler modulus to apply for friction in
    #             the contact plane (springs in X, Y directions)
    #   ranges:   lists of grid ranges to delimit the regions of 
    #             the type of foundation in question
# foundationElasticSupports= model.newElasticFoundationRanges('apElT1', wModulus= winkMod,cRoz=coefHorVerSprings)
# foundationElasticSupports.ranges.extend(foundExtSlab.ranges)
# foundationElasticSupports.ranges.extend(foundIntSlab.ranges)

#Dictionary with the list of Winkler elastic foundations given as a parameter
# elasticSupports= model.setElasticFoundationRangesMap([foundationElasticSupports])

#Boundary conditions
    #Constrains in the nodes belonging to the lines of a range-region
    #    name:        name to identify the boundary condition
    #    constraints: constraint conditions, expressed as [uX, uY, uZ,rotX, rotY, rotZ], where:
    #                 - uX, uY, uZ: translations in the X, Y and Z directions; 
    #                 - rotX, rotY, rotZ: rotations about the X, Y and Z axis
    #                 - 'free': means no constraint

constrainedSupports=model.newConstrainedRanges(name='abutmentSupp',constraints=[0,0,0,'free','free','free'])
constrainedSupports.ranges.extend([ijkGrid.IJKRange([posXbeams[0],0,0],[posXbeams[3],0,0]),ijkGrid.IJKRange([posXbeams[0],lastYpos,0],[posXbeams[3],lastYpos,0])])


#Dictionary with the list of constraints given as a parameter
simpleSupports=model.setConstrainedRangesMap([constrainedSupports])
 

dicGeomEnt= model.generateMesh() #surfaces dictionary.????

