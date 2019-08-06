# -*- coding: utf-8 -*-

'''Limit state controller for cracking straight (using a concrete with tension 
stiffening definition) control.'''

__author__= "Luis C. Pérez Tato (LCPT) , Ana Ortega (AO_O) "
__copyright__= "Copyright 2018, LCPT, AO_O"
__license__= "GPL"
__version__= "3.0"
__email__= "l.pereztato@ciccp.es, ana.ortega@ciccp.es "


import math
import xc_base
import geom
import xc
from solution import predefined_solutions
from model import predefined_spaces
from materials import typical_materials
from materials.ehe import EHE_materials
from materials.ehe import EHE_limit_state_checking
from materials.sections import section_properties
from actions import combinations as combs
from postprocess import limit_state_data as lsd
from postprocess import RC_material_distribution
from materials.sections.fiber_section import defSimpleRCSection
import sys
import logging
from materials.sections.fiber_section import fiber_sets

#Hide logging messages from modules.
rootLogger = logging.getLogger()
lhStdout = rootLogger.handlers[0]  # stdout is the only handler initially
fileHandler = logging.FileHandler("{0}/{1}.log".format('/tmp/', 'test'))
rootLogger.addHandler(fileHandler)
rootLogger.removeHandler(lhStdout)

# Geometry
L= 1.0 # Bar length (m)

feProblem= xc.FEProblem()
preprocessor=  feProblem.getPreprocessor
nodes= preprocessor.getNodeHandler

# Materials
sectionGeometry= section_properties.RectangularSection("test",b=.3,h=.4)
concr= EHE_materials.HA25
concr.alfacc=0.85    #f_maxd= 0.85*fcd concrete long term compressive strength factor (normally alfacc=1)
concr.initTensStiff='Y'  #initialize concrete with tension-stiffening branch
                         #(diagram of type concrete02)

section= concr.defElasticShearSection3d(preprocessor, sectionGeometry)

# Problem type
modelSpace= predefined_spaces.StructuralMechanics3D(nodes)

#Mesh.
n1= nodes.newNodeXYZ(0,0.0,0.0)
n2= nodes.newNodeXYZ(L/2.0,0.0,0.0)
n3= nodes.newNodeXYZ(L,0.0,0.0)

lin= modelSpace.newLinearCrdTransf("lin",xc.Vector([0,1,0]))

elements= preprocessor.getElementHandler
elements.defaultTransformation= "lin"
elements.defaultMaterial= section.name
e1= elements.newElement("ElasticBeam3d",xc.ID([n1.tag,n2.tag]));
e2= elements.newElement("ElasticBeam3d",xc.ID([n2.tag,n3.tag]));

#Constraints.
modelSpace.fixNode000_000(n1.tag)

#Loads.
Fx= 0 
My= 1e3 
Mz= 0 
cargas= preprocessor.getLoadHandler
casos= cargas.getLoadPatterns
#Load modulation.
ts= casos.newTimeSeries("constant_ts","ts")
casos.currentTimeSeries= "ts"
#Load case definition
lp0= casos.newLoadPattern("default","lp0")
lp0.newNodalLoad(n3.tag,xc.Vector([Fx,0,0,0,My,Mz]))
#We add the load case to domain.
casos.addToDomain(lp0.getName())

# # Solution
# analisis= predefined_solutions.simple_static_linear(feProblem)
# result= analisis.analyze(1)

# Load combinations
combContainer= combs.CombContainer()
combContainer.SLS.freq.add('allLoads', '1.0*lp0')
totalSet= preprocessor.getSets.getSet('total')
lsd.LimitStateData.internal_forces_results_directory= '/tmp/'
lsd.freqLoadsCrackControl.saveAll(feProblem,combContainer,totalSet) 

# Define available sections for the elements (spatial distribution of RC sections).
# It refers to the reinforced concrete sections associated with the element
# (i.e. for shell elements we typically define two RC sections, one for each
# main direction; in the case of beam elements the most common way is to define
# RC sections in the front and back ends of the elements)
reinfConcreteSectionDistribution= RC_material_distribution.RCMaterialDistribution()
sectContainer= reinfConcreteSectionDistribution.sectionDefinition #creates an RC sections container

#Generic layers (rows of rebars). Other instance variables that we can define
#for MainReinfLayers are coverLat and nRebars.If we define nRebars that
#value overrides the rebarsSpacing
barArea= 4e-4
barDiameter= math.sqrt(barArea)/math.pi

reinfLayer= defSimpleRCSection.MainReinfLayer(rebarsDiam= barDiameter,areaRebar= barArea,rebarsSpacing=0.075,width=0.25,nominalCover=0.050)

#instances of defSimpleRCSection.RecordRCSlabBeamSection that defines the
#variables that make up THE TWO reinforced concrete sections in the two
#reinforcement directions of a slab or the front and back ending sections
#of a beam element
reinfSteel= EHE_materials.B500S
beamRCsect= defSimpleRCSection.RecordRCSlabBeamSection(name='beamRCsect',sectionDescr='beam section',concrType=concr, reinfSteelType=reinfSteel,width= sectionGeometry.b,depth= sectionGeometry.h)
beamRCsect.dir1PositvRebarRows=[reinfLayer]
beamRCsect.dir1NegatvRebarRows=[reinfLayer]
beamRCsect.dir2PositvRebarRows=[reinfLayer]
beamRCsect.dir2NegatvRebarRows=[reinfLayer]
beamRCsect.creaTwoSections()
sectContainer.append(beamRCsect)

# Spatial distribution of reinforced concrete
# sections (assign RC sections to elements).
reinfConcreteSectionDistribution.assign(elemSet=totalSet.elements,setRCSects=beamRCsect)

####!!!!To erase
e0=preprocessor.getElementHandler.getElement(0)
e1=preprocessor.getElementHandler.getElement(1)

sect1E0=reinfConcreteSectionDistribution.getSectionDefinitionsForElement(0)[0]
sect2E0=reinfConcreteSectionDistribution.getSectionDefinitionsForElement(0)[1]
sect1E1=reinfConcreteSectionDistribution.getSectionDefinitionsForElement(1)[0]
sect2E1=reinfConcreteSectionDistribution.getSectionDefinitionsForElement(1)[1]

####
#Crack checking.
lsd.freqLoadsCrackControl.controller= EHE_limit_state_checking.CrackStraightController(limitStateLabel= lsd.freqLoadsCrackControl.label)
lsd.freqLoadsCrackControl.controller.analysisToPerform= predefined_solutions.simple_newton_raphson
lsd.LimitStateData.check_results_directory= '/tmp/'
lsd.normalStressesResistance.outputDataBaseFileName= 'resVerif'

###!!! Step by step
sectContainer.createRCsections(preprocessor=preprocessor,matDiagType='k')
sectContainer.calcInteractionDiagrams(preprocessor=preprocessor,matDiagType='k')
from postprocess import phantom_model as phm
phantomModel= phm.PhantomModel(preprocessor,reinfConcreteSectionDistribution)
limitStateData=lsd.freqLoadsCrackControl
intForcCombFileName= limitStateData.getInternalForcesFileName()
controller= limitStateData.controller
meanCFs= -1.0
phantomElements=phantomModel.build(intForcCombFileName,controller) #=> elements ZeroLengthSections, whose sections (reachable by means of method .getSection()) are fiber section models.
combs= preprocessor.getLoadHandler.getLoadPatterns
elements= [e for e in preprocessor.getSets.getSet("total").elements]
#the elasticBeam3d are also in the model. We pop them from elements:
elements.pop(0)
elements.pop(0)
key=combs.getKeys()[0]
comb= combs[key]
predefined_solutions.resuelveComb(preprocessor,nmbComb=key,analysis=predefined_solutions.simple_static_modified_newton(feProblem),numSteps=1)

for e in elements:
  e.getResistingForce()
  scc=e.getSection()
  sccProp=scc.getProp("datosSecc")
  concrTag=sccProp.concrType.matTagK
  rsteelTag=sccProp.reinfSteelType.matTagK
  setsRC= fiber_sets.fiberSectionSetupRCSets(scc=scc,concrMatTag=concrTag,concrSetName="concrSetFb",reinfMatTag=rsteelTag,reinfSetName="reinfSetFb")
  setsRC.reselTensionFibers(scc=scc,tensionFibersSetName='tensSetFb')
  ###Borrar
  setTfib=setsRC.tensionFibers
  print 'AsTens=' , setTfib.getArea(1.0), 'nFibers= ', setTfib.getNumFibers()
  ###
  As=setsRC.tensionFibers.getArea(1.0)
  x= scc.getNeutralAxisDepth()
  d=scc.getEffectiveDepth()
  h=scc.getLeverArm()
  print 'x= ', x, 'd= ',d, 'h= ', h
  hceff=min(2.5*abs(h-d),abs(h-x)/3.0,abs(h)/2.0)
  Aceff=scc.getNetEffectiveConcreteArea(hceff,"reinfSetFb",15.0)
  print 'Aceff= ', Aceff


mats=preprocessor.getMaterialHandler
print mats.getName(concrTag)
quit()


(FEcheckedModel,meanFCs)= reinfConcreteSectionDistribution.runChecking(lsd.freqLoadsCrackControl, matDiagType="k",threeDim= True)  

quit()






#print "mean FCs: ", meanFCs

meanFC0Teor= 0.89306075607898694
ratio1= abs(meanFCs[0]-meanFC0Teor)/meanFC0Teor
meanFC1Teor= 0.97448959156755022
ratio2= abs(meanFCs[1]-meanFC1Teor)/meanFC1Teor

'''
print "meanFCs[0]= ", meanFCs[0]
print "ratio1= ",ratio1
print "meanFCs[1]= ", meanFCs[1]
print "ratio2= ",ratio2
'''

# Show logging messages.
#sys.stdout = sysstdout
import os
fname= os.path.basename(__file__)
if (ratio1<0.01) & (ratio2<0.01):
  print "test ",fname,": ok."
else:
  lmsg.error(fname+' ERROR.')
