# -*- coding: utf-8 -*-

import xc_base
import geom
import xc
from solution import predefined_solutions
from model import predefined_spaces
from materials import typical_materials
import math

E=2.1e11  #Young modulus [Pa]
l=1      #lenght [m]
area=1e-4   #cross-section area [m2]
#sigmaPret=1e-5  #must be >0
sigmaPret=210e6  #prestressing stress [Pa]

# Model definition
FEcase= xc.FEProblem()
preprocessor=  FEcase.getPreprocessor
nodes= preprocessor.getNodeHandler
elements= preprocessor.getElementHandler

# Problem type
modelSpace= predefined_spaces.SolidMechanics3D(nodes) #Defines the dimension of
                  #the space: nodes by three coordinates (x,y,z) and 
                  #three DOF for each node (Ux,Uy,Uz)

# Model definition
nodes.defaultTag= 1 #First node number.
nod1= nodes.newNodeXYZ(0,0,0)    #node 1
nod2= nodes.newNodeXYZ(l,0,0)    #node 2

# Materials definition
typical_materials.defCableMaterial(preprocessor, name="cable",E=E,prestress=sigmaPret,rho=0.0)
              #uniaxial bilinear prestressed material. The stress strain ranges
              #from slack (large strain at zero stress) to taught
              #(linear with modulus E).
              #prestress: prestressing stress
              #rho= effective self weight (gravity component of weight per 
              #     volume transverse to the cable)

# Elements definition
elements.defaultMaterial= "cable"
elements.defaultTag= 1 #First element number.
elements.dimElem= 3
ctruss1= elements.newElement("CorotTruss",xc.ID([1,2])) #newElement(elementType, nodes_IDs)
ctruss1.area= area

# Constraints
modelSpace.fixNode000(1)
constraints= modelSpace.constraints
constraints.newSPConstraint(2,1,0.0) # newSPConstraint(tag_nod,id_gdl,valor)
                                    # Create a single-point boundary constraint
constraints.newSPConstraint(2,2,0.0)

# Loads definition
cargas= preprocessor.getLoadHandler
casos= cargas.getLoadPatterns
#Load modulation.
ts= casos.newTimeSeries("constant_ts","ts")
casos.currentTimeSeries= "ts"
lPattern= "0"
lp0= casos.newLoadPattern("default",lPattern)
# displacement X node 2
#lp0.newSPConstraint(2,0,0.001) #(node, DOF, value)
lp0.newNodalLoad(2,xc.Vector([21e3,0,0]))


casos.addToDomain(lPattern) # Añadimos la hipótesis al dominio

# Solution procedure
# Nstep= 10       #  apply load in 10 steps
# DInc= 1./Nstep 	#  first load increment
solu= FEcase.getSoluProc
solCtrl= solu.getSoluControl
solModels= solCtrl.getModelWrapperContainer

# Definition of the wrapper that will contain the domain, analysis model,
# constrain handler and DOF numberer for the solver
sm= solModels.newModelWrapper("sm")

# Definition of the numberer, the object responsible for assigning the equation
#numbers to the individual DOFs in each of the DOF groups in the analysis model.
numberer= sm.newNumberer("default_numberer")
numberer.useAlgorithm("rcm")   # graph algorithm: reverse Cuthill-Macgee.

# Definition of the constraint handler, the object responsible for enforcing
# the constraints that exist in the domain.
# available constraint handlers: 'lagrange_constraint_handler',
#                'penalty_constraint_handler', 'plain_handler',
#                'transformation_constraint_handler'
cHandler= sm.newConstraintHandler("penalty_constraint_handler")
cHandler.alphaSP= 1.0e15  #Factor applied with single-freedom constraints
cHandler.alphaMP= 1.0e15  #Factor applied with multi-freedom constraints

# Definition of the solution method
  #creation of a solution method
analysisAggregations= solCtrl.getAnalysisAggregationContainer
analysisAggregation= analysisAggregations.newAnalysisAggregation("analysisAggregation","sm") # newAnalysisAggregation(nameAnalysisAggregation,nameWrapper)
  #definition of the solution algoritm
  #Available types: 'bfgs_soln_algo', 'broyden_soln_algo',
  #                  'krylov_newton_soln_algo','linear_soln_algo',
  #                  'modified_newton_soln_algo','newton_raphson_soln_algo',
  #                  'newton_line_search_soln_algo','periodic_newton_soln_algo'   #                  'frequency_soln_algo','standard_eigen_soln_algo',
  #                   'linear_buckling_soln_algo' 
solAlgo= analysisAggregation.newSolutionAlgorithm("newton_raphson_soln_algo")
  #definition of the convergence test
  #Available types: 'energy_inc_conv_test', 'fixed_num_iter_conv_test', 'norm_disp_incr_conv_test', 'norm_unbalance_conv_test', 'relative_energy_incr_conv_test', 'relative_norm_disp_incr_conv_test', 'relative_norm_unbalance_conv_test', 'relative_total_norm_disp_incr_conv_test'
ctest= analysisAggregation.newConvergenceTest("norm_unbalance_conv_test")
ctest.tol= 1e-4
ctest.maxNumIter= 10
ctest.printFlag= 1 #flag used to print information on convergence (optional)
  #definition of the integrator
  #Available types:'arc_length_integrator', 'arc_length1_integrator',  'displacement_control_integrator', 'distributed_displacement_control_integrator', 'HS_constraint_integrator', 'load_control_integrator', 'load_path_integrator', 'min_unbal_disp_norm_integrator', 'eigen_integrator', 'linear_buckling_integrator', 'alpha_os_integrator', 'alpha_os_generalized_integrator', 'central_difference_integrator', 'central_difference_alternative_integrator', 'central_difference_no_damping_integrator', 'collocation_integrator', 'collocation_hybrid_simulation_integrator', 'HHT_integrator', 'HHT1_integrator', 'HHT_explicit_integrator', 'HHT_generalized_integrator', 'HHT_generalized_explicit_integrator', 'HHT_hybrid_simulation_integrator', 'newmark_integrator', 'newmark1_integrator', 'newmark_explicit_integrator' 'newmark_hybrid_simulation_integrator', 'wilson_theta_integrator'
integ= analysisAggregation.newIntegrator("load_control_integrator",xc.Vector([]))
integ.dLambda1= 0.1
  #definition of the system of equations.
  #vailable types: 'band_arpack_soe', 'band_arpackpp_soe', 'sym_arpack_soe', 'sym_band_eigen_soe', 'full_gen_eigen_soe', 'band_gen_lin_soe', 'distributed_band_gen_lin_soe', 'band_spd_lin_soe', 'distributed_band_spd_lin_soe', 'diagonal_soe', 'distributed_diagonal_soe', 'full_gen_lin_soe', 'profile_spd_lin_soe', 'distributed_profile_spd_lin_soe', 'sparse_gen_col_lin_soe', 'distributed_sparse_gen_col_lin_soe', 'sparse_gen_row_lin_soe', 'distributed_sparse_gen_row_lin_soe', 'sym_sparse_lin_soe'.
soe= analysisAggregation.newSystemOfEqn("band_gen_lin_soe")
# newSolver(tipo).
#  Available solvers for eigenproblem Systems Of Equations:
#    'band_arpack_solver', 'band_arpackpp_solver', 'sym_band_eigen_solver',
#    'full_gen_eigen_solver', 'sym_arpack_solver'
#  Available solvers for linear Systems Of Equations:
#    'band_gen_lin_lapack_solver', 'band_spd_lin_lapack_solver',
#    'diagonal_direct_solver', 'distributed_diagonal_solver',
#    'full_gen_lin_lapack_solver', 'profile_spd_lin_direct_solver',
#    'profile_spd_lin_direct_block_solver', 'super_lu_solver',
#    'sym_sparse_lin_solver'
solver= soe.newSolver("band_gen_lin_lapack_solver")
# newAnalysis(nmb,cod_solu_metodo,cod_solu_eigenM). Available types of analysis:
#    'direct_integration_analysis', 'eigen_analysis', 'modal_analysis',
#    'linear_buckling_analysis', 'linear_buckling_eigen_analysis',
#    'static_analysis', 'variable_time_step_direct_integration_analysis'   
analysis= solu.newAnalysis("static_analysis","analysisAggregation","")
result= analysis.analyze(1)

nodes.calculateNodalReactions(True,1e-6)
#nod1= nodes.getNode(1)
R2X= nod1.getReaction[0]
R2Y= nod1.getReaction[1] 
nod2= nodes.getNode(2)
deltaX= nod2.getDisp[0]
deltaY= nod2.getDisp[1]  

sigmaElem= ctruss1.getN()/area*1e-6

print 'R2X= ', R2X, 'N'
print 'R2Y= ', R2Y, 'N'
print 'deltaX= ', deltaX, 'm'
print 'deltaY= ', deltaY, 'm'
print 'sigmaElem= ',sigmaElem, 'MPa'
