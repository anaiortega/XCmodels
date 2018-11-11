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
                 representation of loads (defaults to 1 -> auto-scale).
  vectorScalePointLoads: factor to apply to the vectors length in the 
                 representation of nodal loads (defaults to 1).
  multByElemAreaLoads: boolean value that must be True if we want to 
                 represent the total load on each element 
                 (=load multiplied by element area) and False if we 
                 are going to depict the value of the uniform load 
                 per unit area (defaults to False)
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

Q1=graphical_reports.RecordLoadCaseDisp(loadCaseName='Q1',loadCaseDescr='Q1: Prueba de carga estática',loadCaseExpr='1.0*Q1',setsToDispLoads=[overallSet],setsToDispDspRot=[dintel],setsToDispIntForc=[dintel])
Q1.unitsScaleLoads=1e-3
Q1.unitsScaleDispl=1e3
Q1.unitsDispl='[mm]'
Q1.unitsScaleMom=1e-3
Q1.unitsMom='[m.kN]'
Q1.unitsScaleForc=1e-3
Q1.unitsForc='[kN]'
Q1.cameraParameters= vtk_graphic_base.CameraParameters('XYZPos')

Q1.listDspRot=[]
Q1.listIntForc=['M2']

Q2=graphical_reports.RecordLoadCaseDisp(loadCaseName='Q2',loadCaseDescr='Q2: tren de cargas ferroviario (2 vías)',loadCaseExpr='1.00*Q2',setsToDispLoads=[overallSet],setsToDispDspRot=[dintel],setsToDispIntForc=[dintel])
Q2.unitsScaleLoads=1e-3
Q2.unitsScaleDispl=1e3
Q2.unitsDispl='[mm]'
Q2.unitsScaleMom=1e-3
Q2.unitsMom='[m.kN]'
Q2.unitsScaleForc=1e-3
Q2.unitsForc='[kN]'
Q2.cameraParameters= vtk_graphic_base.CameraParameters('XYZPos')

Q2.listDspRot=[]
Q2.listIntForc=['M2']

Q3=graphical_reports.RecordLoadCaseDisp(loadCaseName='Q3',loadCaseDescr='Q3: tren de cargas ferroviario (1 vía)',loadCaseExpr='1.00*Q3',setsToDispLoads=[dintel],setsToDispDspRot=[dintel],setsToDispIntForc=[dintel])
Q3.unitsScaleLoads=1e-3
Q3.unitsScaleDispl=1e3
Q3.unitsDispl='[mm]'
Q3.unitsScaleMom=1e-3
Q3.unitsMom='[m.kN]'
Q3.unitsScaleForc=1e-3
Q3.unitsForc='[kN]'
Q3.cameraParameters= vtk_graphic_base.CameraParameters('XYZPos')

Q3.listDspRot=[]
Q3.listIntForc=['M2']

PrueCarga=graphical_reports.RecordLoadCaseDisp(loadCaseName='PC',loadCaseDescr='PrueCarga: Prueba de carga estática',loadCaseExpr='1.0*G1+1.00*G3+1.0*Q1',setsToDispLoads=[dintel],setsToDispDspRot=[dintel],setsToDispIntForc=[dintel])
PrueCarga.unitsScaleLoads=1e-3
PrueCarga.unitsScaleDispl=1e3
PrueCarga.unitsDispl='[mm]'
PrueCarga.unitsScaleMom=1e-3
PrueCarga.unitsMom='[m.kN]'
PrueCarga.unitsScaleForc=1e-3
PrueCarga.unitsForc='[kN]'
PrueCarga.cameraParameters= vtk_graphic_base.CameraParameters('XYZPos')

PrueCarga.listDspRot=[]
PrueCarga.listIntForc=['M2']

Qtren2vias=graphical_reports.RecordLoadCaseDisp(loadCaseName='TF2',loadCaseDescr='Qtren: tren de cargas ferroviario',loadCaseExpr='1.00*G1 + 1.00*G2 + 1.00*G3 + 1.00*Q2',setsToDispLoads=[dintel],setsToDispDspRot=[dintel],setsToDispIntForc=[dintel])
Qtren2vias.unitsScaleLoads=1e-3
Qtren2vias.unitsScaleDispl=1e3
Qtren2vias.unitsDispl='[mm]'
Qtren2vias.unitsScaleMom=1e-3
Qtren2vias.unitsMom='[m.kN]'
Qtren2vias.unitsScaleForc=1e-3
Qtren2vias.unitsForc='[kN]'
Qtren2vias.cameraParameters= vtk_graphic_base.CameraParameters('XYZPos')

Qtren2vias.listDspRot=[]
Qtren2vias.listIntForc=['M2']

Qtren1via=graphical_reports.RecordLoadCaseDisp(loadCaseName='TF1',loadCaseDescr='Qtren: tren de cargas ferroviario',loadCaseExpr='1.00*G1 + 1.00*G2 + 1.00*G3 + 1.00*Q3',setsToDispLoads=[dintel],setsToDispDspRot=[dintel],setsToDispIntForc=[dintel])
Qtren1via.unitsScaleLoads=1e-3
Qtren1via.unitsScaleDispl=1e3
Qtren1via.unitsDispl='[mm]'
Qtren1via.unitsScaleMom=1e-3
Qtren1via.unitsMom='[m.kN]'
Qtren1via.unitsScaleForc=1e-3
Qtren1via.unitsForc='[kN]'
Qtren1via.cameraParameters= vtk_graphic_base.CameraParameters('XYZPos')

Qtren1via.listDspRot=[]
Qtren1via.listIntForc=['M2']

