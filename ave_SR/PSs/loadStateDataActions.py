# -*- coding: utf-8 -*-

'''In this script we define default data of load cases to be used (or changed)
while displaying loads or results associated to single load cases 
'''
from postprocess.xcVtk import vtk_graphic_base
from postprocess.reports import graphical_reports
'''
Definition of record objects with these attributes:
  loadCaseName:  name of the load case to be depicted
  loadCaseDescr: description text of the load case
  loadCaseExpr:  mathematical expression to define the load case (ex:
                 '1.0*GselfWeight+1.0*DeadLoad')
  setsToDispLoads: ordered list of sets of elements to display loads
  setsToDispBeamLoads: ordered list of sets of beam elements to display loads
                 (defaults to [])
  compElLoad: component of load on beam elements to be represented
              available components: 'axialComponent', 'transComponent',
              'transYComponent','transZComponent'
  unitsScaleLoads: factor to apply to loads if we want to change
                 the units (defaults to 1).
  unitsLoads: text to especify the units in which loads are 
                 represented (defaults to 'units:[m,kN]')
  vectorScaleLoads: factor to apply to the vectors length in the 
                 representation of loads (defaults to 1).
  vectorScalePointLoads: factor to apply to the vectors length in the 
                 representation of nodal loads (defaults to 1).
  multByElemSizeLoads: boolean value that must be True if we want to 
                 represent the total load on each element 
                 (=load multiplied by element size) and False if we 
                 are going to depict the value of the uniform load 
                 per unit size (defaults to False)
  listDspRot: ordered list of displacement or rotations to be displayed
                 available components: 'uX', 'uY', 'uZ', 'rotX', rotY', 'rotZ'
                 (defaults to ['uX', 'uY', 'uZ'])
  setsToDispDspRot: ordered list of sets of elements to display displacements 
                 or rotations
  unitsScaleDispl: factor to apply to displacements if we want to change
                 the units (defaults to 1).
  unitsDispl: text to especify the units in which displacements are 
                 represented (defaults to '[m]'
  listIntForc:   ordered list of internal forces to be displayed as scalar field 
                 over «shell» elements
                 available components: 'N1', 'N2', 'M1', 'M2', 'Q1', 'Q2'
                 (defaults to ['N1', 'N2', 'M1', 'M2', 'Q1', 'Q2'])
  setsToDispIntForc: ordered list of sets of elements (of type «shell»)to 
                    display internal forces
  listBeamIntForc: ordered list of internal forces to be displayed 
                 as diagrams on lines for «beam» elements
                 available components: 'N', 'My', 'Mz', 'Qy', 'Qz','T'
                 (defaults to ['N', 'My', 'Mz', 'Qy', 'Qz','T'])
  setsToDispBeamIntForc: ordered list of sets of elements (of type «beam»)to 
                    display internal forces (defaults to [])
  scaleDispBeamIntForc: tuple (escN,escQ,escM) correponding to the scales to 
                  apply to displays of, respectively, N Q and M beam internal 
                  forces (defaults to (1.0,1.0,1.0))
  unitsScaleForc: factor to apply to internal forces if we want to change
                 the units (defaults to 1).
  unitsForc: text to especify the units in which forces are 
                 represented (defaults to '[kN/m]')
  unitsScaleMom: factor to apply to internal moments if we want to change
                 the units (defaults to 1).
  unitsMom:  text to especify the units in which bending moments are 
                 represented (defaults to '[kN.m/m]')
  cameraParameters: parameters that define the position and orientation of the
                 camera (defaults to "XYZPos")
  
  cameraParametersBeams: parameters that define the position and orientation of the
                 camera for beam elements displays (defaults to "XYZPos")
  
'''

Q1a_1_carro=lcases.LoadCase(preprocessor=prep,name="Q1a_1_carro")
Q1a_1_carro.create()
Q1a_1_carro.addLstLoads([Q1c_vext_v1])

Q1a_2_carro=lcases.LoadCase(preprocessor=prep,name="Q1a_2_carro")
Q1a_2_carro.create()
Q1a_2_carro.addLstLoads([Q1c_vext_v2])

Q1b_1_carro=lcases.LoadCase(preprocessor=prep,name="Q1b_1_carro")
Q1b_1_carro.create()
Q1b_1_carro.addLstLoads([Q1c_vext_v1,Q2c_vcent_v1,Q3c_vint_v1])

Q1b_2_carro=lcases.LoadCase(preprocessor=prep,name="Q1b_2_carro")
Q1b_2_carro.create()
Q1b_2_carro.addLstLoads([Q1c_vext_v2,Q2c_vcent_v2,Q3c_vint_v2])

Q1c_carro=lcases.LoadCase(preprocessor=prep,name="Q1c_carro")
Q1c_carro.create()
Q1c_carro.addLstLoads([Q1c_vcent_v2,Q2c_vint_v2,Q3c_vext_v2])

Q1d_carro=lcases.LoadCase(preprocessor=prep,name="Q1d_carro")
Q1d_carro.create()
Q1d_carro.addLstLoads([Q1e_vcent_v2,Q2e_vint_v2,Q3e_vext_v2])

Q1e_carro=lcases.LoadCase(preprocessor=prep,name="Q1e_carro")
Q1e_carro.create()
Q1e_carro.addLstLoads([Q1e_vcent_v1,Q2e_vint_v1,Q3e_vext_v1])

Q1f_carro=lcases.LoadCase(preprocessor=prep,name="Q1f_carro")
Q1f_carro.create()
Q1f_carro.addLstLoads([Q3c_vext_v1,Q1c_vcent_v1,Q2c_vint_v1])

q_sit1=lcases.LoadCase(preprocessor=prep,name="q_sit1")
q_sit1.create()
q_sit1.addLstLoads(qunif_sit1)

q_sit2=lcases.LoadCase(preprocessor=prep,name="q_sit2")
q_sit2.create()
q_sit2.addLstLoads(qunif_sit2)

q_sit3=lcases.LoadCase(preprocessor=prep,name="q_sit3")
q_sit3.create()
q_sit3.addLstLoads(qunif_sit3)

q_sit4=lcases.LoadCase(preprocessor=prep,name="q_sit4")
q_sit4.create()
q_sit4.addLstLoads(qunif_sit4)

q_sit5=lcases.LoadCase(preprocessor=prep,name="q_sit5")
q_sit5.create()
q_sit5.addLstLoads(qunif_sit5)

frenCent=lcases.LoadCase(preprocessor=prep,name="frenCent")
frenCent.create()
frenCent.addLstLoads([qfren_viaCent])

frenExt=lcases.LoadCase(preprocessor=prep,name="frenExt")
frenExt.create()
frenExt.addLstLoads([qfren_viaExt])


Q1a_1_carro=graphical_reports.LoadCaseDispParameters(loadCaseName='Q1a_1_carro',loadCaseDescr='Q1a_1_carro',loadCaseExpr='1.0*Q1a_1_carro',setsToDispLoads=[overallSet],setsToDispDspRot=[],setsToDispIntForc=[])
Q1a_1_carro.unitsScaleLoads=1e-3
Q1a_1_carro.vectorScaleLoads=0.020
Q1a_1_carro.unitsScaleDispl=1e3
Q1a_1_carro.unitsDispl='[mm]'
Q1a_1_carro.unitsScaleMom=1e-3
Q1a_1_carro.unitsMom='[m.kN]'
Q1a_1_carro.unitsScaleForc=1e-3
Q1a_1_carro.unitsForc='[kN]'
Q1a_1_carro.cameraParameters= vtk_graphic_base.CameraParameters('ZPos')


Q1a_2_carro=graphical_reports.LoadCaseDispParameters(loadCaseName='Q1a_2_carro',loadCaseDescr='Q1a_2_carro',loadCaseExpr='1.0*Q1a_2_carro',setsToDispLoads=[overallSet],setsToDispDspRot=[],setsToDispIntForc=[])
Q1a_2_carro.unitsScaleLoads=1e-3
Q1a_2_carro.vectorScaleLoads=0.020
Q1a_2_carro.unitsScaleDispl=1e3
Q1a_2_carro.unitsDispl='[mm]'
Q1a_2_carro.unitsScaleMom=1e-3
Q1a_2_carro.unitsMom='[m.kN]'
Q1a_2_carro.unitsScaleForc=1e-3
Q1a_2_carro.unitsForc='[kN]'
Q1a_2_carro.cameraParameters= vtk_graphic_base.CameraParameters('ZPos')


Q1b_1_carro=graphical_reports.LoadCaseDispParameters(loadCaseName='Q1b_1_carro',loadCaseDescr='Q1b_1_carro',loadCaseExpr='1.0*Q1b_1_carro',setsToDispLoads=[overallSet],setsToDispDspRot=[],setsToDispIntForc=[])
Q1b_1_carro.unitsScaleLoads=1e-3
Q1b_1_carro.vectorScaleLoads=0.020
Q1b_1_carro.unitsScaleDispl=1e3
Q1b_1_carro.unitsDispl='[mm]'
Q1b_1_carro.unitsScaleMom=1e-3
Q1b_1_carro.unitsMom='[m.kN]'
Q1b_1_carro.unitsScaleForc=1e-3
Q1b_1_carro.unitsForc='[kN]'
Q1b_1_carro.cameraParameters= vtk_graphic_base.CameraParameters('ZPos')


Q1b_2_carro=graphical_reports.LoadCaseDispParameters(loadCaseName='Q1b_2_carro',loadCaseDescr='Q1b_2_carro',loadCaseExpr='1.0*Q1b_2_carro',setsToDispLoads=[overallSet],setsToDispDspRot=[],setsToDispIntForc=[])
Q1b_2_carro.unitsScaleLoads=1e-3
Q1b_2_carro.vectorScaleLoads=0.020
Q1b_2_carro.unitsScaleDispl=1e3
Q1b_2_carro.unitsDispl='[mm]'
Q1b_2_carro.unitsScaleMom=1e-3
Q1b_2_carro.unitsMom='[m.kN]'
Q1b_2_carro.unitsScaleForc=1e-3
Q1b_2_carro.unitsForc='[kN]'
Q1b_2_carro.cameraParameters= vtk_graphic_base.CameraParameters('ZPos')


Q1c_carro=graphical_reports.LoadCaseDispParameters(loadCaseName='Q1c_carro',loadCaseDescr='Q1c_carro',loadCaseExpr='1.0*Q1c_carro',setsToDispLoads=[overallSet],setsToDispDspRot=[],setsToDispIntForc=[])
Q1c_carro.unitsScaleLoads=1e-3
Q1c_carro.vectorScaleLoads=0.020
Q1c_carro.unitsScaleDispl=1e3
Q1c_carro.unitsDispl='[mm]'
Q1c_carro.unitsScaleMom=1e-3
Q1c_carro.unitsMom='[m.kN]'
Q1c_carro.unitsScaleForc=1e-3
Q1c_carro.unitsForc='[kN]'
Q1c_carro.cameraParameters= vtk_graphic_base.CameraParameters('ZPos')


Q1d_carro=graphical_reports.LoadCaseDispParameters(loadCaseName='Q1d_carro',loadCaseDescr='Q1d_carro',loadCaseExpr='1.0*Q1d_carro',setsToDispLoads=[overallSet],setsToDispDspRot=[],setsToDispIntForc=[])
Q1d_carro.unitsScaleLoads=1e-3
Q1d_carro.vectorScaleLoads=0.020
Q1d_carro.unitsScaleDispl=1e3
Q1d_carro.unitsDispl='[mm]'
Q1d_carro.unitsScaleMom=1e-3
Q1d_carro.unitsMom='[m.kN]'
Q1d_carro.unitsScaleForc=1e-3
Q1d_carro.unitsForc='[kN]'
Q1d_carro.cameraParameters= vtk_graphic_base.CameraParameters('ZPos')


Q1e_carro=graphical_reports.LoadCaseDispParameters(loadCaseName='Q1e_carro',loadCaseDescr='Q1e_carro',loadCaseExpr='1.0*Q1e_carro',setsToDispLoads=[overallSet],setsToDispDspRot=[],setsToDispIntForc=[])
Q1e_carro.unitsScaleLoads=1e-3
Q1e_carro.vectorScaleLoads=0.020
Q1e_carro.unitsScaleDispl=1e3
Q1e_carro.unitsDispl='[mm]'
Q1e_carro.unitsScaleMom=1e-3
Q1e_carro.unitsMom='[m.kN]'
Q1e_carro.unitsScaleForc=1e-3
Q1e_carro.unitsForc='[kN]'
Q1e_carro.cameraParameters= vtk_graphic_base.CameraParameters('ZPos')


Q1f_carro=graphical_reports.LoadCaseDispParameters(loadCaseName='Q1f_carro',loadCaseDescr='Q1f_carro',loadCaseExpr='1.0*Q1f_carro',setsToDispLoads=[overallSet],setsToDispDspRot=[],setsToDispIntForc=[])
Q1f_carro.unitsScaleLoads=1e-3
Q1f_carro.vectorScaleLoads=0.020
Q1f_carro.unitsScaleDispl=1e3
Q1f_carro.unitsDispl='[mm]'
Q1f_carro.unitsScaleMom=1e-3
Q1f_carro.unitsMom='[m.kN]'
Q1f_carro.unitsScaleForc=1e-3
Q1f_carro.unitsForc='[kN]'
Q1f_carro.cameraParameters= vtk_graphic_base.CameraParameters('ZPos')


q_sit1=graphical_reports.LoadCaseDispParameters(loadCaseName='q_sit1',loadCaseDescr='Carga uniforme tráfico Q1a_1 y Q1a_2',loadCaseExpr='1.0*q_sit1',setsToDispLoads=[overallSet],setsToDispDspRot=[],setsToDispIntForc=[])
q_sit1.unitsScaleLoads=1e-3
q_sit1.vectorScaleLoads=0.20
q_sit1.unitsScaleDispl=1e3
q_sit1.unitsDispl='[mm]'
q_sit1.unitsScaleMom=1e-3
q_sit1.unitsMom='[m.kN]'
q_sit1.unitsScaleForc=1e-3
q_sit1.unitsForc='[kN]'
q_sit1.cameraParameters= vtk_graphic_base.CameraParameters('XYZPos')


q_sit2=graphical_reports.LoadCaseDispParameters(loadCaseName='q_sit2',loadCaseDescr='Carga uniforme tráfico Q1b_1 y Q1b_2',loadCaseExpr='1.0*q_sit2',setsToDispLoads=[overallSet],setsToDispDspRot=[],setsToDispIntForc=[])
q_sit2.unitsScaleLoads=1e-3
q_sit2.vectorScaleLoads=0.20
q_sit2.unitsScaleDispl=1e3
q_sit2.unitsDispl='[mm]'
q_sit2.unitsScaleMom=1e-3
q_sit2.unitsMom='[m.kN]'
q_sit2.unitsScaleForc=1e-3
q_sit2.unitsForc='[kN]'
q_sit2.cameraParameters= vtk_graphic_base.CameraParameters('XYZPos')


q_sit3=graphical_reports.LoadCaseDispParameters(loadCaseName='q_sit3',loadCaseDescr='Carga uniforme tráfico Q1c',loadCaseExpr='1.0*q_sit3',setsToDispLoads=[overallSet],setsToDispDspRot=[],setsToDispIntForc=[])
q_sit3.unitsScaleLoads=1e-3
q_sit3.vectorScaleLoads=0.20
q_sit3.unitsScaleDispl=1e3
q_sit3.unitsDispl='[mm]'
q_sit3.unitsScaleMom=1e-3
q_sit3.unitsMom='[m.kN]'
q_sit3.unitsScaleForc=1e-3
q_sit3.unitsForc='[kN]'
q_sit3.cameraParameters= vtk_graphic_base.CameraParameters('XYZPos')


q_sit4=graphical_reports.LoadCaseDispParameters(loadCaseName='q_sit4',loadCaseDescr='Carga uniforme tráfico Q1d y Q1e',loadCaseExpr='1.0*q_sit4',setsToDispLoads=[overallSet],setsToDispDspRot=[],setsToDispIntForc=[])
q_sit4.unitsScaleLoads=1e-3
q_sit4.vectorScaleLoads=0.20
q_sit4.unitsScaleDispl=1e3
q_sit4.unitsDispl='[mm]'
q_sit4.unitsScaleMom=1e-3
q_sit4.unitsMom='[m.kN]'
q_sit4.unitsScaleForc=1e-3
q_sit4.unitsForc='[kN]'
q_sit4.cameraParameters= vtk_graphic_base.CameraParameters('XYZPos')


q_sit5=graphical_reports.LoadCaseDispParameters(loadCaseName='q_sit5',loadCaseDescr='Carga uniforme tráfico Q1f',loadCaseExpr='1.0*q_sit5',setsToDispLoads=[overallSet],setsToDispDspRot=[],setsToDispIntForc=[])
q_sit5.unitsScaleLoads=1e-3
q_sit5.vectorScaleLoads=0.20
q_sit5.unitsScaleDispl=1e3
q_sit5.unitsDispl='[mm]'
q_sit5.unitsScaleMom=1e-3
q_sit5.unitsMom='[m.kN]'
q_sit5.unitsScaleForc=1e-3
q_sit5.unitsForc='[kN]'
q_sit5.cameraParameters= vtk_graphic_base.CameraParameters('XYZPos')


frenCent=graphical_reports.LoadCaseDispParameters(loadCaseName='frenCent',loadCaseDescr='frenCent',loadCaseExpr='1.0*frenCent',setsToDispLoads=[overallSet],setsToDispDspRot=[],setsToDispIntForc=[])
frenCent.unitsScaleLoads=1e-3
frenCent.vectorScaleLoads=0.20
frenCent.unitsScaleDispl=1e3
frenCent.unitsDispl='[mm]'
frenCent.unitsScaleMom=1e-3
frenCent.unitsMom='[m.kN]'
frenCent.unitsScaleForc=1e-3
frenCent.unitsForc='[kN]'
frenCent.cameraParameters= vtk_graphic_base.CameraParameters('ZPos')


frenExt=graphical_reports.LoadCaseDispParameters(loadCaseName='frenExt',loadCaseDescr='frenExt',loadCaseExpr='1.0*frenExt',setsToDispLoads=[overallSet],setsToDispDspRot=[],setsToDispIntForc=[])
frenExt.unitsScaleLoads=1e-3
frenExt.vectorScaleLoads=0.20
frenExt.unitsScaleDispl=1e3
frenExt.unitsDispl='[mm]'
frenExt.unitsScaleMom=1e-3
frenExt.unitsMom='[m.kN]'
frenExt.unitsScaleForc=1e-3
frenExt.unitsForc='[kN]'
frenExt.cameraParameters= vtk_graphic_base.CameraParameters('ZPos')


Qcarro=[G2,Q1a_1_carro,Q1a_2_carro,Q1b_1_carro,Q1b_2_carro,Q1c_carro,Q1d_carro,Q1e_carro,Q1f_carro]
qunif=[q_sit1,q_sit2,q_sit3,q_sit4,q_sit5]
