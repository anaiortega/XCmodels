# -*- coding: utf-8 -*-
from __future__ import division 
from __future__ import print_function

import os
import xc_base
import geom
import xc
import math
from model import predefined_spaces
from model.geometry import grid_model as gm
from model.mesh import finit_el_model as fem
from model.boundary_cond import spring_bound_cond as sprbc
from materials.astm_aisc import ASTM_materials as astm
from actions import loads
from actions import load_cases as lcases

from postprocess.config import default_config
from postprocess import output_styles as outSty
from postprocess import output_handler as outHndl

# Example 5.1 of AISC Steel Design Guide 9 Torsional Analysis of Structural Steel Members

#units
in2m=0.0254
kip2N=4448.22
m2in=1/in2m
N2kip=1/kip2N
Pa2ksi=1.45038e-7
#data
L=15*12*in2m # beam length
T=60*kip2N*in2m # service load torque (60 kip-in)

sty=outSty.OutputStyle() 
FEcase= xc.FEProblem()
preprocessor=FEcase.getPreprocessor
prep=preprocessor   #short name
nodes= prep.getNodeHandler
elements= prep.getElementHandler
elements.dimElem= 3
modelSpace= predefined_spaces.StructuralMechanics3D(nodes) #Defines the
out=outHndl.OutputHandler(modelSpace,sty)


grid=gm.GridModel(prep,xList=[0,L/2,L],yList=[0],zList=[0])
grid.generatePoints()

steel_W=astm.A992   #steel W shapes
beam=grid.genLinOneXYZRegion([(0,0,0),(L,0,0)],'beam')
beam_mat=astm.WShape(steel_W,'W10X49') 
beam_mat.defElasticShearSection3d(prep)

beam_mesh=fem.LinSetToMesh(linSet=beam,matSect=beam_mat,elemSize=0.25,vDirLAxZ=xc.Vector([0,1,0]),elemType='ElasticBeam3d')
beam_mesh.generateMesh(prep)

J=beam_mat.J()*(m2in**4)
Jcomp=1.39
ratio0=(J-Jcomp)/Jcomp

G=steel_W.G()*Pa2ksi
Gcomp=11200
ratio1=(G-Gcomp)/Gcomp

#boundary conditions
extr1=grid.getPntXYZ((0,0,0))
modelSpace.fixNode000_0FF(extr1.getNode().tag)
extr2=grid.getPntXYZ((L,0,0))
modelSpace.fixNodeF00_0FF(extr2.getNode().tag)
#out.displayFEMesh()

#load
midPoint=grid.getPntXYZ((L/2.,0,0))
torsBeam=loads.NodalLoad(name='torsBeam',lstNod=[midPoint.getNode()],loadVector=xc.Vector([0,0,0,T,0,0]))

LC=lcases.LoadCase(preprocessor=prep,name="LC",loadPType="default",timeSType="constant_ts")
LC.create()
LC.addLstLoads([torsBeam])

modelSpace.addLoadCaseToDomain("LC")
modelSpace.analyze(calculateNodalReactions=True)
#out.displayLoads()

#modelSpace.removeLoadCaseFromDomain("LC")

# abs(ratio0)<1e-3 and abs(ratio1)<5e-3
