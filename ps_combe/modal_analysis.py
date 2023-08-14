# -*- coding: utf-8 -*-

exec(open("model_data.py").read())
from postprocess.xcVtk.FE_model import quick_graphics as qg

for e in shells.elements:
    mats= e.physicalProperties.getVectorMaterials #Materials at gauss points.
    for m in mats:
      m.rho= 0.0

for n in xcTotalSet.nodes:
    if(n.hasProp('tributaryMass')):
        dM= n.getProp('tributaryMass')
        if(dM>0.0):
            n.mass= xc.Matrix([[dM,0,0,0,0,0],
                               [0,dM,0,0,0,0],
                               [0,0,dM,0,0,0],
                               [0,0,0,1e-4,0,0],
                               [0,0,0,0,1e-4,0],
                               [0,0,0,0,0,1e-4]])

class PP(object):

  def frequencyAnalysis(self,prb):
    self.solu= prb.getSoluProc
    self.solCtrl= self.solu.getSoluControl
    solModels= self.solCtrl.getModelWrapperContainer
    self.sm= solModels.newModelWrapper("sm")
    self.cHandler= self.sm.newConstraintHandler("transformation_constraint_handler")
    self.numberer= self.sm.newNumberer("default_numberer")
    self.numberer.useAlgorithm("rcm")
    solutionStrategies= self.solCtrl.getSolutionStrategyContainer
    self.solutionStrategy= solutionStrategies.newSolutionStrategy("solutionStrategy","sm")
    self.solAlgo= self.solutionStrategy.newSolutionAlgorithm("frequency_soln_algo")
    self.soe= self.solutionStrategy.newSystemOfEqn("band_arpack_soe")
    self.solver= self.soe.newSolver("band_arpack_solver")
    self.analysis= self.solu.newAnalysis("modal_analysis","solutionStrategy","")
    self.integ= self.solutionStrategy.newIntegrator("eigen_integrator",xc.Vector([1.0,1,1.0,1.0]))
    return self.analysis

pp= PP()
analysis= pp.frequencyAnalysis(model)
analOk= analysis.analyze(5)
periods= analysis.getPeriods()
modalParticipationFactors= analysis.getModalParticipationFactors()
effectiveModalMasses= analysis.getEffectiveModalMasses()
totalMass= analysis.getTotalMass()

#Accelerations.
from actions.quake import seismeSIA
soilClass= 'C' # Tableau 24 SIA231 et rapport géotechnique Géotest 23/03/1978
accelTerrain= 1.3 # Bex->Zone 3a. Article 16.2.1.2 SIA 261:214
CO= 2 #CO II Classe d'ouvrage. Tableau 25 SIA 231:2014 et CU 6.5.1
q= 1.5 #Tableau 14 SIA 262:2013
ah= [] 
av= []
a= seismeSIA.designSpectrum(soilClass,accelTerrain,CO,periods[0],q)
ah.append(a)
av.append(0.7*a)

print("periods= ", periods, ' s')
print("accelerations: ", ah, ' m/s2')
print("modalParticipationFactors: ",modalParticipationFactors)
print("effectiveModalMasses: ",effectiveModalMasses)
print("totalMass: ",totalMass)
#Display de deformed shape and the equivalent static loads 
#associated with mode
modeToDisplay= 1
figureCaption= 'Mode '+str(modeToDisplay)+' deformed shape and equivalent static loads.'
lcs= qg.LoadCaseResults(model)
lcs.outputStyle.equivalentLoadVectorsScaleFactor= 1.5
lcs.displayEigenResult(eigenMode=modeToDisplay, setToDisplay=xcTotalSet,accelMode=ah[modeToDisplay-1],caption= figureCaption,fileName=None, defFScale= 2.0)

import csv
with open('earthquake_loads.csv','w') as csvfile:
    nodes= xcTotalSet.nodes
    data= [['nodeTag','Fx','Fy','Fz','Mx','My','Mz']]
    writer = csv.writer(csvfile)
    for n in nodes:
        forces= n.getEquivalentStaticLoad(1,ah[0])
        data.append([n.tag,forces[0],forces[1],forces[2],forces[3],forces[4],forces[5]])
    writer.writerows(data)
