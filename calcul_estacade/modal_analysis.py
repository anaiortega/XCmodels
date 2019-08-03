# -*- coding: utf-8 -*-

execfile("model_data.py")
#gilamontDock.errFileName= './err.txt'

for part in modelSurfaces:
  weight= part.selfWeight
  for e in part.elements:
    mats= e.getPhysicalProperties.getVectorMaterials #Materials at gauss points.
    for m in mats:
      m.rho= 0.0
  part.computeTributaryAreas(False)
  rhoPart= -part.selfWeight[2]/9.81
  for nn in part.nodes:
    dM= rhoPart*nn.getTributaryArea()
    nn.setProp("deadMass",dM)
    nn.mass= xc.Matrix([[dM,0,0,0,0,0],
                           [0,dM,0,0,0,0],
                           [0,0,dM,0,0,0],
                           [0,0,0,1e-4,0,0],
                           [0,0,0,0,1e-4,0],
                           [0,0,0,0,0,1e-4]])
    
for part in modelLines:
  part.computeTributaryLengths(False)
  rhoPart= -part.selfWeight[2]/9.81
  for nn in part.nodes:
    dM= rhoPart*nn.getTributaryLength()
    nn.setProp("deadMass",dM)
    nn.mass= xc.Matrix([[dM,0,0,0,0,0],
                           [0,dM,0,0,0,0],
                           [0,0,dM,0,0,0],
                           [0,0,0,1e-4,0,0],
                           [0,0,0,0,1e-4,0],
                           [0,0,0,0,0,1e-4]])

#Check nodal masses.
for n in xcTotalSet.nodes:
  norm= n.mass.Norm()
  if(norm<1e-4):
    n.mass= xc.Matrix([[1e-4,0,0,0,0,0],
                           [0,1e-4,0,0,0,0],
                           [0,0,1e-4,0,0,0],
                           [0,0,0,1e-4,0,0],
                           [0,0,0,0,1e-4,0],
                           [0,0,0,0,0,1e-4]])
  #norm= n.mass.Norm()
  #print 'tag= ', n.tag, ' norm= ', norm, ' mass= ', n.mass

    
class PP(object):

  def frequencyAnalysis(self,prb):
    self.solu= prb.getSoluProc
    self.solCtrl= self.solu.getSoluControl
    solModels= self.solCtrl.getModelWrapperContainer
    self.sm= solModels.newModelWrapper("sm")
    self.cHandler= self.sm.newConstraintHandler("transformation_constraint_handler")
    self.numberer= self.sm.newNumberer("default_numberer")
    self.numberer.useAlgorithm("rcm")
    analysisAggregations= self.solCtrl.getAnalysisAggregationContainer
    self.analysisAggregation= analysisAggregations.newAnalysisAggregation("analysisAggregation","sm")
    self.solAlgo= self.analysisAggregation.newSolutionAlgorithm("frequency_soln_algo")
    self.integ= self.analysisAggregation.newIntegrator("eigen_integrator",xc.Vector([1.0,1,1.0,1.0]))
    self.soe= self.analysisAggregation.newSystemOfEqn("band_arpack_soe")
    self.solver= self.soe.newSolver("band_arpack_solver")
    self.analysis= self.solu.newAnalysis("modal_analysis","analysisAggregation","")
    return self.analysis

pp= PP()
analysis= pp.frequencyAnalysis(gilamontDock)
analOk= analysis.analyze(5)
periodos= analysis.getPeriods()

print "periodos= ", periodos
