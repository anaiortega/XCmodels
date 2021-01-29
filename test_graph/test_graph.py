# -*- coding: utf-8 -*-
import os
import xc_base
import geom
import xc
import math
from materials import typical_materials as tm
from materials.ehe import EHE_materials
from postprocess.config import default_config
from model import predefined_spaces
from model.geometry import grid_model as gm
from model.mesh import finit_el_model as fem
from actions import loads
from actions import load_cases as lcases

# Default configuration of environment variables.
from postprocess import output_styles as outSty
from postprocess import output_handler as outHndl

workingDirectory= default_config.findWorkingDirectory()+'/' #search env_config.py
execfile(workingDirectory+'env_config.py')
sty=outSty.OutputStyle() 

FEcase= xc.FEProblem()
prep=FEcase.getPreprocessor
nodes= prep.getNodeHandler
elements= prep.getElementHandler
elements.dimElem= 3
# Problem type
modelSpace= predefined_spaces.StructuralMechanics3D(nodes) #Defines the
# dimension of the space: nodes by three coordinates (x,y,z) and 
# six DOF for each node (Ux,Uy,Uz,thetaX,thetaY,thetaZ)
out=outHndl.OutputHandler(modelSpace,sty)
xList=[0,0.5,1]
yList=[0,0.5,1]
zList=[0,1]
gridGeom= gm.GridModel(prep,xList,yList,zList)
gridGeom.generatePoints()

deck=gridGeom.genSurfOneXYZRegion(xyzRange=((0,0,1),(1,1,1)),setName='deck')

column=gridGeom.genLinOneXYZRegion(((0.5,0.5,0),(0.5,0.5,1)),'column')

concrete=EHE_materials.HA30
concrProp=tm.MaterialData(name='concrProp',E=concrete.Ecm(),nu=concrete.nuc,rho=concrete.density())

deck_mat=tm.DeckMaterialData(name='deck_mat',thickness= 0.2,material=concrProp)
deck_mat.setupElasticSection(preprocessor=prep)   #creates the section-material
deck_mesh=fem.SurfSetToMesh(surfSet=deck,matSect=deck_mat,elemSize=0.5,elemType='ShellMITC4')
deck_mesh.generateMesh(prep)     #mesh the set of surfaces

from materials.sections import section_properties as sectpr
geomSectColumnZ=sectpr.RectangularSection(name='geomSectColumnZ',b=0.2,h=0.2)

columnZconcr_mat= tm.BeamMaterialData(name= 'columnZconcr_mat', section=geomSectColumnZ, material=concrProp)
columnZconcr_mat.setupElasticShear3DSection(preprocessor=prep)

column_mesh=fem.LinSetToMesh(linSet=column,matSect=columnZconcr_mat,elemSize=0.5,vDirLAxZ=xc.Vector([1,0,0]),elemType='ElasticBeam3d',coordTransfType='linear')
column_mesh.generateMesh(prep)  
#out.displayFEMesh()

selfWeight=loads.InertialLoad(name='selfWeight', lstSets=[deck], vAccel=xc.Vector( [0.0,0.0,-9.81]))

unifLoadDeck= loads.UniformLoadOnSurfaces(name= 'unifLoadDeck',xcSet=deck,loadVector=xc.Vector([0,0,-5e3,0,0,0]),refSystem='Global')
unifLoadColumn=loads.UniformLoadOnBeams(name='unifLoadColumn', xcSet=column, loadVector=xc.Vector([4e3,0,0,0,0,0]),refSystem='Global')

nodDeck=[n for n in deck.nodes]
nodDeck
pointLoadDeck=loads.NodalLoad(name='pointLoadDeck',lstNod=nodDeck,loadVector=xc.Vector([0,0,-10e3,0,0,0]))

nodColumn=[n for n in column.nodes]
nodColumn.pop(1)
pointLoadColumn=loads.NodalLoad(name='pointLoadColumn',lstNod=nodColumn,loadVector=xc.Vector([0,-20e3,0,0,0,0]))

LC1=lcases.LoadCase(preprocessor=prep,name="LC1",loadPType="default",timeSType="constant_ts")
LC1.create()
LC1.addLstLoads([selfWeight])


LC2=lcases.LoadCase(preprocessor=prep,name="LC2",loadPType="default",timeSType="constant_ts")
LC2.create()
LC2.addLstLoads([unifLoadDeck,unifLoadColumn,pointLoadDeck,pointLoadColumn])

allSets=modelSpace.setSum('allSets',[deck,column])
allSets.fillDownwards()
loads2disp=[LC1]
for l in loads2disp:
    print('load case', l.name)
    modelSpace.addLoadCaseToDomain(l.name)
    out.displayLoads(deck)
#    out.displayLoads(column)
    out.displayLoads()
    modelSpace.removeLoadCaseFromDomain(l.name)
loads2disp=[LC2]
for l in loads2disp:
    print('load case', l.name)
    modelSpace.addLoadCaseToDomain(l.name)
    out.displayLoads(deck)
    out.displayLoads(column)
    out.displayLoads()
    modelSpace.removeLoadCaseFromDomain(l.name)

