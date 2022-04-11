# -*- coding: utf-8 -*-

import os
import geom
import xc
import math
from model import predefined_spaces
from model.geometry import grid_model as gm
from model.mesh import finit_el_model as fem
from model.boundary_cond import spring_bound_cond as sprbc
from model.sets import sets_mng as sets
from materials import typical_materials as tm
from actions import loads
from actions import load_cases as lcases
from actions import combinations as cc
from actions.earth_pressure import earth_pressure as ep
from model.geometry import geom_utils as gut
#from materials.ehe import EHE_materials
#from materials.sia262 import SIA262_materials
from materials.ec3 import EC3_materials
from postprocess.config import default_config

# Default configuration of environment variables.
workingDirectory= default_config.findWorkingDirectory()+'/'
exec(open(workingDirectory+'env_config.py').read())

#Auxiliary data
 #Geometry
LbeamY=5

 #Actions
qunifBeam=50e3

#Materials

eSize= 0.2     #length of elements

#             *** GEOMETRIC model (points, lines, surfaces) - SETS ***
FEcase= xc.FEProblem()
preprocessor=FEcase.getPreprocessor
prep=preprocessor   #short name
nodes= prep.getNodeHandler
elements= prep.getElementHandler
elements.dimElem= 3
# Problem type
modelSpace= predefined_spaces.StructuralMechanics3D(nodes) #Defines the
# dimension of the space: nodes by three coordinates (x,y,z) and 
# six DOF for each node (Ux,Uy,Uz,thetaX,thetaY,thetaZ)

# coordinates in global X,Y,Z axes for the grid generation
xList=[0]
yList=[0,0.1,1,1.5,2,3.5,4.1,LbeamY]  #OK
zList=[0]

lastYpos=len(yList)-1

# grid model definition
gridGeom= gm.GridModel(prep,xList,yList,zList)

# Grid geometric entities definition (points, lines, surfaces)
# Points' generation
gridGeom.generatePoints()


#Ranges for lines and surfaces
# extractIncludedIJranges(step): subranges index K=constant (default step=1)
# extractIncludedIKranges((step): subranges index J=constant (default step=1)
# extractIncludedJKranges((step): subranges index I=constant (default step=1)
# extractIncludedIranges(stepJ,stepK): subranges indexes J,K=constant (default
#                                      stpes= 1)
# idem for J and K ranges
beamY_rg=gm.IJKRange((0,0,0),(0,lastYpos,0))
#Lines generation
beamY=gridGeom.genLinOneRegion(ijkRange=beamY_rg,setName='beamY')

#                         *** MATERIALS *** 
S235JR= EC3_materials.S235JR
S235JR.gammaM= 1.00


# Steel material-section appropiate for 3D beam analysis, including shear
  # deformations.
  # Attributes:
  #   steel:         steel material (
  #   name: name of the standard steel profile. Types: IPEShape, HEShape,
  #         UPNShape, AUShape, CHSShape
  #      (defined in materials.sections.structural_shapes.arcelor_metric_shapes)
beamY_mat= EC3_materials.IPEShape(steel=S235JR,name='IPE_A_450')
beamY_mat.defElasticShearSection3d(preprocessor)


#                         ***FE model - MESH***
# IMPORTANT: it's convenient to generate the mesh of surfaces before meshing
# the lines, otherwise, sets of shells can take also beam elements touched by
# them


beamY_mesh=fem.LinSetToMesh(linSet=beamY,matSect=beamY_mat,elemSize=eSize,vDirLAxZ=xc.Vector([1,0,0]),elemType='ElasticBeam3d',coordTransfType='linear')
beamY_mesh.generateMesh(preprocessor)



#                       ***BOUNDARY CONDITIONS***

#fixed DOF (ux:'0FF_FFF', uy:'F0F_FFF', uz:'FF0_FFF',
#           rx:'FFF_0FF', ry:'FFF_F0F', rz:'FFF_FF0')
n_col1=nodes.getDomain.getMesh.getNearestNode(geom.Pos3d(0,0,0))
modelSpace.fixNode('000_F0F',n_col1.tag)
n_col2=nodes.getDomain.getMesh.getNearestNode(geom.Pos3d(0,yList[lastYpos],0))
modelSpace.fixNode('000_F0F',n_col2.tag)

#                       ***ACTIONS***


#Uniform load on beams
# syntax: UniformLoadOnBeams(name, xcSet, loadVector,refSystem)
#    name:       name identifying the load
#    xcSet:      set that contains the lines
#    loadVector: xc.Vector with the six components of the load: 
#                xc.Vector([Fx,Fy,Fz,Mx,My,Mz]).
#    refSystem: reference system in which loadVector is defined:
#               'Local': element local coordinate system
#               'Global': global coordinate system (defaults to 'Global)
unifLoadBeamsY=loads.UniformLoadOnBeams(name='unifLoadBeamsY', xcSet=beamY, loadVector=xc.Vector([0,0,-qunifBeam,0,0,0]),refSystem='Global')




#    ***LOAD CASES***

qunifBeams=lcases.LoadCase(preprocessor=prep,name="qunifBeams",loadPType="default",timeSType="constant_ts")
qunifBeams.create()
qunifBeams.addLstLoads([unifLoadBeamsY])

    
#    ***LIMIT STATE COMBINATIONS***
combContainer= cc.CombContainer()  #Container of load combinations

# COMBINATIONS OF ACTIONS FOR SERVICEABILITY LIMIT STATES
    # name:        name to identify the combination
    # rare:        combination for a rare design situation
    # freq:        combination for a frequent design situation
    # qp:          combination for a quasi-permanent design situation
    # earthquake:  combination for a seismic design situation
#Characteristic combinations.
combContainer.SLS.rare.add('ELSR01', '1.0*qunifBeams')
#Frequent combinations.
combContainer.SLS.freq.add('ELSF01', '1.0*qunifBeams')
#Quasi permanent combinations.
combContainer.SLS.qp.add('ELSQP01', '1.0*qunifBeams')

# COMBINATIONS OF ACTIONS FOR ULTIMATE LIMIT STATES
    # name:        name to identify the combination
    # perm:        combination for a persistent or transient design situation
    # acc:         combination for a accidental design situation
    # fatigue:     combination for a fatigue design situation
    # earthquake:  combination for a seismic design situation
#Persistent and transitory situations.
combContainer.ULS.perm.add('ELU01', '1.2*qunifBeams')
combContainer.ULS.perm.add('ELU02', '1.0*qunifBeams')

#Fatigue.
# Combinations' names must be:
#        - ELUF0: unloaded structure (permanent loads)
#        - ELUF1: fatigue load in position 1.
combContainer.ULS.fatigue.add('ELUF0','1.00*qunifBeams')
combContainer.ULS.fatigue.add('ELUF1','1.00*qunifBeams')

allBeams=beamY
allBeams.description='Beams+columns'
overallSet=beamY
overallSet.description='overall set'
overallSet.color=cfg.colors['purple02']




 




