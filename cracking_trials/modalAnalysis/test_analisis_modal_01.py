# -*- coding: utf-8 -*-
''' Response spectrum modal analysis test
taken from the publication from Andrés Sáez Pérez: «Estructuras III»
 E.T.S. de Arquitectura de Sevilla (España).'''
import geom
import xc

from model import predefined_spaces
from solution import predefined_solutions
from materials import typical_materials
import math

__author__= "Luis C. Pérez Tato (LCPT)"
__copyright__= "Copyright 2014, LCPT"
__license__= "GPL"
__version__= "3.0"
__email__= "l.pereztato@gmail.com"

masaPorPlanta= 134.4e3
nodeMassMatrix= xc.Matrix([[masaPorPlanta,0,0],[0,masaPorPlanta,0],[0,0,0]])
Ehorm= 200000*1e5 # Concrete elastic modulus.

Bbaja= 0.45 # Columns size.
Ibaja= 1/12.0*Bbaja**4 # Cross section moment of inertia.
Hbaja= 4 # Altura de la planta baja.
B1a= 0.40 # Columns size.
I1a= 1/12.0*B1a**4 # Cross section moment of inertia.
H= 3 # Altura del resto de plantas.
B3a= 0.35 # Columns size.
I3a= 1/12.0*B3a**4 # Cross section moment of inertia.


kPlBaja= 20*12*Ehorm*Ibaja/(Hbaja**3)
kPl1a= 20*12*Ehorm*I1a/(H**3)
kPl2a= kPl1a
kPl3a= 20*12*Ehorm*I3a/(H**3)
kPl4a= kPl3a

# Problem type
feProblem= xc.FEProblem()
preprocessor=  feProblem.getPreprocessor
nodes= preprocessor.getNodeHandler
modelSpace= predefined_spaces.StructuralMechanics2D(nodes)

nodes= preprocessor.getNodeHandler
nodes.defaultTag= 0; 
nod0= nodes.newNodeXY(0,0) 
nod0.mass= nodeMassMatrix
nod0.setProp("gdlsCoartados",xc.ID([0,1,2]))
nod1= nodes.newNodeXY(0,4)
nod1.mass= nodeMassMatrix
nod1.setProp("gdlsCoartados",xc.ID([1,2]))
nod2= nodes.newNodeXY(0,4+3)
nod2.mass= nodeMassMatrix
nod2.setProp("gdlsCoartados",xc.ID([1,2]))
nod3= nodes.newNodeXY(0,4+3+3)
nod3.mass= nodeMassMatrix
nod3.setProp("gdlsCoartados",xc.ID([1,2]))
nod4= nodes.newNodeXY(0,4+3+3+3)
nod4.mass= nodeMassMatrix
nod4.setProp("gdlsCoartados",xc.ID([1,2]))
nod5= nodes.newNodeXY(0,4+3+3+3+3)
nod5.mass= nodeMassMatrix
nod5.setProp("gdlsCoartados",xc.ID([1,2]))
setTotal= preprocessor.getSets.getSet("total")
nodes= setTotal.nodes
for n in nodes:
  n.fix(n.getProp("gdlsCoartados"),xc.Vector([0,0,0]))

# Materials definition
materialHandler= preprocessor.getMaterialHandler
#scc= typical_materials.defElasticSection2d(preprocessor, "scc",A,E,I)

sccPlBaja= typical_materials.defElasticSection2d(preprocessor, "sccPlBaja",20*Bbaja*Bbaja,Ehorm,20*Ibaja)
sccPl1a= typical_materials.defElasticSection2d(preprocessor, "sccPl1a",20*B1a*B1a,Ehorm,20*I1a) 
sccPl2a= typical_materials.defElasticSection2d(preprocessor, "sccPl2a",20*B1a*B1a,Ehorm,20*I1a) 
sccPl3a= typical_materials.defElasticSection2d(preprocessor, "sccPl3a",20*B3a*B3a,Ehorm,20*I3a) 
sccPl4a= typical_materials.defElasticSection2d(preprocessor, "sccPl4a",20*B3a*B3a,Ehorm,20*I3a)


# Geometric transformation(s)
lin= modelSpace.newLinearCrdTransf("lin")

# Elements definition
elements= preprocessor.getElementHandler
elements.defaultTransformation= "lin"
elements.defaultMaterial= "sccPlBaja"
elements.defaultTag= 1 #Tag for next element.
beam2d= elements.newElement("ElasticBeam2d",xc.ID([0,1]))
beam2d.h= Bbaja
elements.defaultMaterial= "sccPl1a" 
beam2d= elements.newElement("ElasticBeam2d",xc.ID([1,2]))
beam2d.h= B1a
elements.defaultMaterial= "sccPl2a" 
beam2d= elements.newElement("ElasticBeam2d",xc.ID([2,3]))
beam2d.h= B1a
elements.defaultMaterial= "sccPl3a" 
beam2d= elements.newElement("ElasticBeam2d",xc.ID([3,4]))
beam2d.h= B3a
elements.defaultMaterial= "sccPl4a" 
beam2d= elements.newElement("ElasticBeam2d",xc.ID([4,5]))
beam2d.h= B3a



# Solution procedure
solu= feProblem.getSoluProc
solCtrl= solu.getSoluControl
solModels= solCtrl.getModelWrapperContainer
sm= solModels.newModelWrapper("sm")
cHandler= sm.newConstraintHandler("transformation_constraint_handler")
numberer= sm.newNumberer("default_numberer")
numberer.useAlgorithm("rcm")
solutionStrategies= solCtrl.getSolutionStrategyContainer
solutionStrategy= solutionStrategies.newSolutionStrategy("solutionStrategy","sm")
solAlgo= solutionStrategy.newSolutionAlgorithm("frequency_soln_algo")
integ= solutionStrategy.newIntegrator("eigen_integrator",xc.Vector([]))
soe= solutionStrategy.newSystemOfEqn("sym_band_eigen_soe")
solver= soe.newSolver("sym_band_eigen_solver")
analysis= solu.newAnalysis("modal_analysis","solutionStrategy","")
analOk= analysis.analyze(5)
periodos= analysis.getPeriods()
modos= analysis.getNormalizedEigenvectors()
factoresParticipacionModal= analysis.getModalParticipationFactors()
masasModalesEfectivas= analysis.getEffectiveModalMasses()
masaTotal= analysis.getTotalMass()
factoresDistribucion= analysis.getDistributionFactors()

#Displaying
from postprocess.xcVtk.FE_model import quick_graphics as qg
lcs= qg.LoadCaseResults(feProblem)
lcs.outputStyle.equivalentLoadVectorsScaleFactor= 0.0001
lcs.displayEigenResult(eigenMode=2, setToDisplay=setTotal,caption= '',fileName=None,defFScale=1.0)

quit()


periodosTeor= xc.Vector([0.468,0.177,0.105,0.084,0.065])
ratio1= (periodos-periodosTeor).Norm()
modesFromExample= xc.Matrix([[0.323,-0.764,0.946,0.897,-0.623],[0.521,-0.941,0.378,-0.251,1.000],[0.685,-0.700,-0.672,-0.907,-0.658],[0.891,0.241,-1.000,1.000,0.195],[1.000,1.000,0.849,-0.427,-0.042]])
resta= (modos-modesFromExample)
ratio2= resta.Norm()
ratio3= abs(masaTotal-5*masaPorPlanta)/5/masaPorPlanta
''' The values of the first three distribution factors values (fist 3 columns)
   were taken from the reference example. The two others (which are not given
in the example) are those obtained from the program (they can always get
wrong because of some error). ''' 
exampleDistributionFactors= xc.Matrix([[0.419,0.295,0.148,0.0966714,0.0429946],
                         [0.676,0.363,0.059,-0.0270432,-0.0689994],
                         [0.889,0.27,-0.105,-0.0978747,0.0453662],
                         [1.157,-0.093,-0.156,0.1078,-0.0134259],
                         [1.298,-0.386,0.133,-0.0461473,0.00292086]])
resta= factoresDistribucion-exampleDistributionFactors
ratio4= resta.Norm()

''' 
print "kPlBaja= ",kPlBaja
print "kPl1a= ",kPl1a
print "kPl3a= ",kPl3a
print "periodos: ",periodos
print "ratio1= ",ratio1
print "modos: ",modos
print "resta: ",resta
print "ratio2= ",ratio2
print "factoresParticipacionModal: ",factoresParticipacionModal
print "masasModalesEfectivas: ",masasModalesEfectivas
print "masaTotal: ",masaTotal
print "ratio3= ",ratio3
print "factoresDistribucion: ",factoresDistribucion
print "ratio4= ",ratio4
 '''

import os
from misc_utils import log_messages as lmsg
fname= os.path.basename(__file__)
if((ratio1<1e-3) & (ratio2<5e-2) & (ratio3<1e-12) & (ratio4<5e-2)):
  print("test ",fname,": ok.")
else:
  lmsg.error(fname+' ERROR.')

