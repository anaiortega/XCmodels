# -*- coding: utf-8 -*-

from postprocess.reports import graphical_reports as gr
from postprocess.xcVtk import vtk_graphic_base

execfile('../model_gen.py')
# Solution procedure
solu= FEcase.getSoluProc
solCtrl= solu.getSoluControl
solModels= solCtrl.getModelWrapperContainer
sm= solModels.newModelWrapper("sm")
#cHandler= sm.newConstraintHandler("transformation_constraint_handler")
cHandler= sm.newConstraintHandler("penalty_constraint_handler")
cHandler.alphaSP= 1.0e18
cHandler.alphaMP= 1.0e18
numberer= sm.newNumberer("default_numberer")
numberer.useAlgorithm("rcm")
analysisAggregations= solCtrl.getAnalysisAggregationContainer
analysisAggregation= analysisAggregations.newAnalysisAggregation("analysisAggregation","sm")

solAlgo= analysisAggregation.newSolutionAlgorithm("ill-conditioning_soln_algo")
integ= analysisAggregation.newIntegrator("ill-conditioning_integrator",xc.Vector([]))

soe= analysisAggregation.newSystemOfEqn("band_arpack_soe")
soe.shift= 0.0
solver= soe.newSolver("band_arpack_solver")
# soe= analysisAggregation.newSystemOfEqn("sym_band_eigen_soe")
# solver= soe.newSolver("sym_band_eigen_solver")

analysis= solu.newAnalysis("ill-conditioning_analysis","analysisAggregation","")
analOk= analysis.analyze(1)
eig1= analysis.getEigenvalue(1)

rlcd= gr.RecordDisp()
rlcd.cameraParameters= vtk_graphic_base.CameraParameters('Custom')
rlcd.cameraParameters.viewUpVc= [0,1,0]
rlcd.cameraParameters.posCVc= [-100,100,100]
rlcd.setsToDispEigenvectors=[xcTotalSet]

rlcd.displayEigenvectorsOnSets(eigenMode= 1)


print 'eig1=', eig1
threshold= 1e-2
for n in xcTotalSet.nodes:
    disp3d= n.getEigenvectorDisp3dComponents(1)
    rot3d= n.getEigenvectorRot3dComponents(1)
    modDisp3d= disp3d.getModulus()
    if(modDisp3d>threshold):
        p=n.getCurrentPos3d(1.0)
        print 'disp', modDisp3d, [p.x,p.y,p.z],[disp3d.x,disp3d.y,disp3d.z]
    modRot3d= rot3d.getModulus()
    if(modRot3d>threshold):
        p=n.getCurrentPos3d(1.0)
        print 'rot', modDisp3d, [p.x,p.y,p.z],[rot3d.x,rot3d.y,rot3d.z]
    

