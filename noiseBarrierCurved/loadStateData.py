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
  setsToDispLoads: ordered list of sets of shell elements to display loads
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
                 representation of element loads (defaults to 1 -> auto-scale).
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
                  forces (defaults to (1.0,1.0,1.0) -> auto-scale)
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
                 camera when displaying beam elements (defaults to "XYZPos")
  

'''
G1=graphical_reports.RecordLoadCaseDisp(loadCaseName='GselfWeight',loadCaseDescr='G1: self weight',loadCaseExpr='1.0*GselfWeight',setsToDispLoads=[],setsToDispDspRot=[colsSet],setsToDispIntForc=[])
G1.unitsScaleDispl=1e3
G1.unitsDispl='[mm]'
G1.unitsScaleLoads=1e-3
G1.unitsScaleMom=1e-3
G1.unitsMom='[m.kN]'
G1.unitsScaleForc=1e-3
G1.unitsForc='[kN]'
G1.setsToDispBeamIntForc=[colsSet]
G1.listBeamIntForc=['Mz','Qy','N']
G1.cameraParametersBeams= vtk_graphic_base.CameraParameters('YPos')
G1.setsToDispBeamLoads=[colsSet]
G1.vectorScalePointLoads=0.005
G1.compElLoad='transComponent'

Q1=graphical_reports.RecordLoadCaseDisp(loadCaseName='Qwind',loadCaseDescr='Q1: wind',loadCaseExpr='1.0*Qwind',setsToDispLoads=[],setsToDispDspRot=[colsSet],setsToDispIntForc=[])
Q1.unitsScaleDispl=1e3
Q1.unitsDispl='[mm]'
Q1.unitsScaleLoads=1e-3
Q1.unitsScaleMom=1e-3
Q1.unitsMom='[m.kN]'
Q1.unitsScaleForc=1e-3
Q1.unitsForc='[kN]'
Q1.setsToDispBeamIntForc=[colsSet]
Q1.listBeamIntForc=['Mz','Qy','N']
Q1.cameraParametersBeams= vtk_graphic_base.CameraParameters('YPos')
Q1.setsToDispBeamLoads=[colsSet]
Q1.vectorScalePointLoads=0.005
Q1.compElLoad='transComponent'

A1=graphical_reports.RecordLoadCaseDisp(loadCaseName='AvehicCrash',loadCaseDescr='A1: vehicle crash',loadCaseExpr='1.0*AvehicCrash',setsToDispLoads=[],setsToDispDspRot=[colsSet],setsToDispIntForc=[])
A1.unitsScaleDispl=1e3
A1.unitsDispl='[mm]'
A1.unitsScaleLoads=1e-3
A1.unitsScaleMom=1e-3
A1.unitsMom='[m.kN]'
A1.unitsScaleForc=1e-3
A1.unitsForc='[kN]'
A1.setsToDispBeamIntForc=[colsSet]
A1.listBeamIntForc=['Mz','Qy','N']
A1.cameraParametersBeams= vtk_graphic_base.CameraParameters('YPos')
A1.setsToDispBeamLoads=[colsSet]
A1.vectorScalePointLoads=0.005
A1.compElLoad='transComponent'

