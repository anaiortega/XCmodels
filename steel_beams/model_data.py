# -*- coding: utf-8 -*-

import math
import vtk
import xc_base
import geom
import xc
from solution import predefined_solutions
from model import predefined_spaces
from materials import typical_materials
from materials.ec3 import EC3_materials

from materials.sections import structural_steel as steel
from actions import load_cases as lcm
from actions import combinations as combs


# Problem type
mainBeam= xc.FEProblem()
mainBeam.title= 'Warehouse main beams'
preprocessor= mainBeam.getPreprocessor   
nodos= preprocessor.getNodeHandler
modelSpace= predefined_spaces.StructuralMechanics3D(nodos)

#Materials
S235JR= EC3_materials.S235JR
S235JR.gammaM= 1.00
IPE450A= EC3_materials.IPEShape(S235JR,'IPE_A_450')
fs3dIPE450= IPE450A.defElasticShearSection3d(preprocessor,S235JR)

points= preprocessor.getMultiBlockTopology.getPoints
pt= dict()
pt[0]= points.newPntIDPos3d(0,geom.Pos3d(8.64308749,0.0,10.22679239))
pt[1]= points.newPntIDPos3d(1,geom.Pos3d(8.73795117,0.0,10.20466246))
pt[2]= points.newPntIDPos3d(2,geom.Pos3d(10.9911389,0.0,9.67903555))
pt[3]= points.newPntIDPos3d(3,geom.Pos3d(13.41396022,0.0,9.11383628))

pt[4]= points.newPntIDPos3d(4,geom.Pos3d(13.55101619,0.0,9.12256754))
pt[5]= points.newPntIDPos3d(5,geom.Pos3d(16.56769638,0.0,9.31474758))
pt[6]= points.newPntIDPos3d(6,geom.Pos3d(19.70712774,0.0,9.51474758))
pt[7]= points.newPntIDPos3d(7,geom.Pos3d(22.8465591,0.0,9.71474758))
pt[8]= points.newPntIDPos3d(8,geom.Pos3d(25.98599046,0.0,9.91474758))
pt[9]= points.newPntIDPos3d(9,geom.Pos3d(29.00267066,0.0,10.10692762))

pos10= geom.Pos3d(29.11111701,0.0,10.11383628)
pt[10]= points.newPntIDPos3d(10,pos10)
pt[21]= points.newPntIDPos3d(21,pos10)

pt[11]= points.newPntIDPos3d(11,geom.Pos3d(29.21956337,0.0,10.10692762))
pt[12]= points.newPntIDPos3d(12,geom.Pos3d(32.23624356,0.0,9.91474758))
pt[13]= points.newPntIDPos3d(13,geom.Pos3d(35.37567492,0.0,9.71474758))
pt[14]= points.newPntIDPos3d(14,geom.Pos3d(38.51510628,0.0,9.51474758))
pt[15]= points.newPntIDPos3d(15,geom.Pos3d(41.65453764,0.0,9.31474758))
pt[16]= points.newPntIDPos3d(16,geom.Pos3d(44.67121784,0.0,9.12256754))

pt[17]= points.newPntIDPos3d(17,geom.Pos3d(44.80827381,0.0,9.11383628))
pt[18]= points.newPntIDPos3d(18,geom.Pos3d(47.12805698,0.0,9.67980755))
pt[19]= points.newPntIDPos3d(19,geom.Pos3d(49.27649338,0.0,10.20397434))
pt[20]= points.newPntIDPos3d(20,geom.Pos3d(49.37001923,0.0,10.22679239))

lines= preprocessor.getMultiBlockTopology.getLines
lineDict= dict()
lineDict[0]= lines.newLine(pt[0].tag,pt[1].tag)
lineDict[1]= lines.newLine(pt[1].tag,pt[2].tag)
lineDict[2]= lines.newLine(pt[2].tag,pt[3].tag)
lineDict[3]= lines.newLine(pt[3].tag,pt[4].tag)
lineDict[4]= lines.newLine(pt[4].tag,pt[5].tag)
lineDict[5]= lines.newLine(pt[5].tag,pt[6].tag)
lineDict[6]= lines.newLine(pt[6].tag,pt[7].tag)
lineDict[7]= lines.newLine(pt[7].tag,pt[8].tag)
lineDict[8]= lines.newLine(pt[8].tag,pt[9].tag)
lineDict[9]= lines.newLine(pt[9].tag,pt[10].tag)
lineDict[10]= lines.newLine(pt[21].tag,pt[11].tag)
lineDict[11]= lines.newLine(pt[11].tag,pt[12].tag)
lineDict[12]= lines.newLine(pt[12].tag,pt[13].tag)
lineDict[13]= lines.newLine(pt[13].tag,pt[14].tag)
lineDict[14]= lines.newLine(pt[14].tag,pt[15].tag)
lineDict[15]= lines.newLine(pt[15].tag,pt[16].tag)
lineDict[16]= lines.newLine(pt[16].tag,pt[17].tag)
lineDict[17]= lines.newLine(pt[17].tag,pt[18].tag)
lineDict[18]= lines.newLine(pt[18].tag,pt[19].tag)
lineDict[19]= lines.newLine(pt[19].tag,pt[20].tag)

#Meshing
trfs= preprocessor.getTransfCooHandler
lin= trfs.newLinearCrdTransf3d('lin')
lin.xzVector= xc.Vector([0,1,0])
seedElem= preprocessor.getElementHandler.seedElemHandler
seedElem.defaultTransformation= 'lin'
seedElem.defaultMaterial= IPE450A.sectionName
elem= seedElem.newElement("ElasticBeam3d",xc.ID([0,0]))
for key in lineDict:
  l= lineDict[key]
  l.nDiv= 12
  l.genMesh(xc.meshDir.I)

joint= EC3_materials.IPEShape(S235JR,'IPE_300')
fs3djoint= joint.defElasticShearSection3d(preprocessor,S235JR)
elements= preprocessor.getElementHandler
elements.defaultMaterial= joint.sectionName
zl= elements.newElement("ZeroLengthSection",xc.ID([pt[10].getNode().tag,pt[21].getNode().tag]))
zl.setupVectors(xc.Vector([1,0,0]),xc.Vector([0,0,1]))
# print 'order= ', zl.getOrder
# print 'numDOF= ', zl.getNumDOF
# print 'section type= ', zl.getSection().getType
# print 'transformation= ', zl.getTransformation
# print 'I vector= ', zl.getIVector, 'J vector= ', zl.getJVector

# Constraints
appuis= [pt[3],pt[10],pt[21],pt[17]]
supportNodes= list()
for p in appuis:
  supportNodes.append(p.getNode())

for n in supportNodes:
  modelSpace.fixNode000_FFF(n.tag)

modelSpace.constraints.newSPConstraint(pt[0].getNode().tag,2,0.0) #Z disp not allowed
modelSpace.constraints.newSPConstraint(pt[20].getNode().tag,2,0.0) #Z disp not allowed

supportNodes.append(pt[0].getNode())
supportNodes.append(pt[20].getNode())

#ACTIONS
loadCaseManager= lcm.LoadCaseManager(preprocessor)
loadCaseNames= ['selfWeight','deadLoad','liveLoad','pvPanels','snowLoad']
loadCaseManager.defineSimpleLoadCases(loadCaseNames)

appuiPannes= [pt[1],pt[2], pt[4],pt[5],pt[6],pt[7],pt[8],pt[9], pt[11],pt[12],pt[13],pt[14],pt[15],pt[16], pt[18],pt[19]]

def appliPanneLoads(lc,load):
  for p in appuiPannes:
    node= p.getNode()
    lc.newNodalLoad(node.tag,load) 


#Self weight.
cLC= loadCaseManager.setCurrentLoadCase('selfWeight')
grav=9.81 #Aceleración de la gravedad (m/s2)
massIPE450= IPE450A.getRho()

selfWeightLoad= grav*massIPE450
selfWeightLoadVector= xc.Vector([0.0, 0.0,-selfWeightLoad])
for key in lineDict:
  l= lineDict[key]
  elems= l.getElements()
  for e in elems:
    e.vector3dUniformLoadGlobal(selfWeightLoadVector)

appliPanneLoads(cLC,xc.Vector([0.0,0.0,-0.960596e3,0,0,0]))

#Dead load.
cLC= loadCaseManager.setCurrentLoadCase('deadLoad')
deadLoad= 12.0875e3 #Reaction from panne analysis.
deadLoadVector= xc.Vector([0.0, 0.0,-deadLoad,0,0,0])
appliPanneLoads(cLC,deadLoadVector) 

#PV panels
cLC= loadCaseManager.setCurrentLoadCase('pvPanels')
pvPanels= 4.874e3 #Reaction from panne analysis.
pvPanelsLoadVector= xc.Vector([0.0, 0.0,-pvPanels,0,0,0])
for p in appuiPannes:
  node= p.getNode()
  cLC.newNodalLoad(node.tag,pvPanelsLoadVector) 

#Live load.
cLC= loadCaseManager.setCurrentLoadCase('liveLoad')
liveLoad= 7.79841e3 #Reaction from panne analysis.
liveLoadVector= xc.Vector([0.0, 0.0,-liveLoad,0,0,0])
appliPanneLoads(cLC,liveLoadVector) 

#Snow.
cLC= loadCaseManager.setCurrentLoadCase('snowLoad')
snowLoad= 17.9363e3 #Reaction from panne analysis.
snowLoadVector= xc.Vector([0.0, 0.0,-snowLoad,0,0,0])
appliPanneLoads(cLC,snowLoadVector) 

#Load combinations
combContainer= combs.CombContainer()

#Quasi-permanent situations.
combContainer.SLS.qp.add('ELS00', '1.0*selfWeight+1.0*deadLoad')
combContainer.SLS.qp.add('ELS01', '1.0*selfWeight+1.0*deadLoad+1.0*pvPanels')

#Permanent and transitory situations.
combContainer.ULS.perm.add('ELU00', '1.2*selfWeight+1.2*deadLoad+1.5*liveLoad')
combContainer.ULS.perm.add('ELU01', '1.2*selfWeight+1.2*deadLoad+1.5*snowLoad')
combContainer.ULS.perm.add('ELU02', '1.2*selfWeight+1.2*deadLoad+1.35*pvPanels+1.5*liveLoad')
combContainer.ULS.perm.add('ELU03', '1.2*selfWeight+1.2*deadLoad+1.35*pvPanels+1.5*snowLoad')

#Sets
setTotal= preprocessor.getSets.getSet("total")
setMainBeam= preprocessor.getSets.defSet("main_beam")

for e in setTotal.getElements:
  if(e.getVtkCellType== vtk.VTK_LINE):
    setMainBeam.getElements.append(e)
