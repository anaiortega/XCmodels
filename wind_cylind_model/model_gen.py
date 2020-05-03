# -*- coding: utf-8 -*-
from __future__ import division 

import os
import xc_base
import geom
import xc
import math
from model import predefined_spaces
from model.geometry import grid_model as gm
from model.mesh import finit_el_model as fem
from model.boundary_cond import spring_bound_cond as sprbc
from model.sets import sets_mng as sets
from materials import typical_materials as tm
from model.geometry import geom_utils as gut
from materials.astm_aisc import ASTM_materials as astm
from actions import loads
from actions import load_cases as lcases
from actions.wind import base_wind as bw

# Default configuration of environment variables.
from postprocess.config import default_config
from postprocess import output_styles as outSty
from postprocess import output_handler as outHndl

workingDirectory= default_config.findWorkingDirectory()+'/'
execfile(workingDirectory+'env_config.py')
sty=outSty.OutputStyle() 

#Data
execfile(workingDirectory+'data.py')


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
out=outHndl.OutputHandler(modelSpace,sty)

# coordinates in global X,Y,Z axes for the grid generation
xList=[R]   #radius coordinate

ndiv=20
incr=180/ndiv 
yList=[i*incr for i in range(ndiv+1)]    #angular coordinate
zList=[zBaseCyl,zBaseCyl+height]         #level coordinate
#auxiliary data
lastXpos=len(xList)-1
lastYpos=len(yList)-1
lastZpos=len(zList)-1

# grid model definition
gridGeom= gm.GridModel(prep,xList,yList,zList)

# Grid geometric entities definition (points, lines, surfaces)
# Points' generation
gridGeom.generateCylZPoints(xCent=0,yCent=0)

# ranges
tankwall_rg=[gm.IJKRange((0,0,0),(lastXpos,lastYpos,lastZpos))]


#Surfaces generation
tankwall=gridGeom.genSurfMultiRegion(lstIJKRange=tankwall_rg,nameSet='tankwall')

'''
tankwall.description='Cylindrical wall'
tankwall.color=cfg.colors['purple02']
'''

#                         *** MATERIALS *** 
steelProp=tm.MaterialData(name='steelProp',E=steel.E,nu=steel.nu,rho=steel.rho)
# Isotropic elastic section-material appropiate for plate and shell analysis
wall_mat=tm.DeckMaterialData(name='wall_mat',thickness= thickness,material=steelProp)
wall_mat.setupElasticSection(preprocessor=prep)   #creates the section-material



#                         ***FE model - MESH***
# Enforced line division
st=sets.get_subset_lin_parallel_to_axis(axis='Z',fromSet=tankwall,toSetName='st')
fem.assign_ndiv_to_lines_in_set(lnSet=st,ndiv=20)
st.clear()
#Meshing
tankwall_mesh=fem.SurfSetToMesh(surfSet=tankwall,matSect=wall_mat,elemSize=None,elemType='ShellMITC4')
tankwall_mesh.generateMesh(prep) 

#out.displayFEMesh()
#out.displayLocalAxes()

#local axis Z toward exterior of cylindrical body

#                       ***BOUNDARY CONDITIONS***

#fixed DOF (ux:'0FF_FFF', uy:'F0F_FFF', uz:'FF0_FFF',
#           rx:'FFF_0FF', ry:'FFF_F0F', rz:'FFF_FF0')
nodBase=sets.get_set_nodes_plane_XY(setName='nodBase', setBusq=tankwall, zCoord=zList[0], tol=0.001)
for n in nodBase.nodes:
    modelSpace.fixNode('000_FFF',n.tag)

nodSym=sets.get_set_nodes_plane_XZ(setName='nodSym', setBusq=tankwall, yCoord=0, tol=0.001)
for n in nodSym.nodes:
    modelSpace.fixNode('F0F_0F0',n.tag)
    
out.displayFEMesh()


#Wind action definition
windParams=bw.windParams(v,Kd,Kzt,I,alpha,zg)
tankWind=bw.cylindrWind(diam,height,windParams,windComp,zGround,xCent=0,yCent=0)

#elems=[e for e in tankwall.getElements]

#                       ***ACTIONS***
#Inertial load (density*acceleration) applied to the elements in a set
grav=9.81 #Gravity acceleration (m/s2)
selfWeight=loads.InertialLoad(name='selfWeight', lstMeshSets=[tankwall_mesh], vAccel=xc.Vector( [0.0,0.0,-grav]))

#Thermal expansion
## tangential
thermExpansTang=loads.StrainLoadOnShells(name='thermExpansTang', xcSet=tankwall, DOFstrain=0, strain=tempRise*steel.alpha)
## vertical
thermExpansVert=loads.StrainLoadOnShells(name='thermExpansVert', xcSet=tankwall, DOFstrain=1, strain=tempRise*steel.alpha)
                                      
#Thermal contraction
## tangential
thermContrTang=loads.StrainLoadOnShells(name='thermContrTang', xcSet=tankwall, DOFstrain=0, strain=tempFall*steel.alpha)
## vertical
thermContrVert=loads.StrainLoadOnShells(name='thermContrVert', xcSet=tankwall, DOFstrain=1, strain=tempFall*steel.alpha)

#    ***LOAD CASES***

GselfWeight=lcases.LoadCase(preprocessor=prep,name="GselfWeight",loadPType="default",timeSType="constant_ts")
GselfWeight.create()
GselfWeight.addLstLoads([selfWeight])
'''
modelSpace.addLoadCaseToDomain("GselfWeight")
out.displayLoadVectors()
modelSpace.removeLoadCaseFromDomain("GselfWeight")
'''


wind=lcases.LoadCase(preprocessor=prep,name="wind",loadPType="default",timeSType="constant_ts")
wind.create()
for e in tankwall.elements:
    vCoo=e.getCooCentroid(0)
    pres=tankWind.getWindPress(vCoo[0],vCoo[1],vCoo[2])
    loadVector=xc.Vector([0,0,-pres])
    e.vector3dUniformLoadLocal(loadVector)
'''
modelSpace.addLoadCaseToDomain("wind")
out.displayLoadVectors()
modelSpace.removeLoadCaseFromDomain("wind")
'''

thermalExpans=lcases.LoadCase(preprocessor=prep,name="thermalExpans",loadPType="default",timeSType="constant_ts")
thermalExpans.create()
thermalExpans.addLstLoads([thermExpansTang,thermExpansVert])


thermalContr=lcases.LoadCase(preprocessor=prep,name="thermalContr",loadPType="default",timeSType="constant_ts")
thermalContr.create()
thermalContr.addLstLoads([thermContrTang,thermContrVert])



from solution import predefined_solutions
modelSpace.removeAllLoadPatternsFromDomain()
modelSpace.addLoadCaseToDomain('wind')
analysis= predefined_solutions.simple_static_linear(FEcase)
result= analysis.analyze(1)
out.displayDispRot('uZ')
out.displayIntForcDiag('Mz',beamXsteel)
out.displayIntForc('M1',decklv1)
out.displayReactions()

