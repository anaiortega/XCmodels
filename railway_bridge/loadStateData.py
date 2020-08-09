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
                 camera for beam elements displays (defaults to "XYZPos")
  
'''
G1=graphical_reports.LoadCaseDispParameters(loadCaseName='GselfWeight',loadCaseDescr='G1: self weight',loadCaseExpr='1.0*GselfWeight',setsToDispLoads=[deck,found],setsToDispDspRot=[deck,found],setsToDispIntForc=[])
G1.unitsScaleLoads=1e-3
G1.unitsScaleDispl=1e3
G1.unitsDispl='[mm]'
G1.unitsScaleMom=1e-3
G1.unitsMom='[m.kN]'
G1.unitsScaleForc=1e-3
G1.unitsForc='[kN]'
G1.setsToDispBeamIntForc=[columnZ,beamX,beamY]
G1.listBeamIntForc=['My','Mz','Qy','Qz','N']
G1.cameraParameters= vtk_graphic_base.CameraParameters('XYZPos')
G1.setsToDispBeamLoads=[beamY]
G1.vectorScalePointLoads=0.005
G1.compElLoad='axialComponent'


Q1=graphical_reports.LoadCaseDispParameters(loadCaseName='Qdeck',loadCaseDescr='Q1: uniform load on the deck',loadCaseExpr='1.0*Qdeck',setsToDispLoads=[overallSet],setsToDispDspRot=[overallSet],setsToDispIntForc=[deck,found])
Q1.unitsScaleLoads=1e-3
Q1.unitsScaleDispl=1e3
Q1.unitsDispl='[mm]'
Q1.unitsScaleMom=1e-3
Q1.unitsMom='[m.kN]'
Q1.unitsScaleForc=1e-3
Q1.unitsForc='[kN]'
Q1.setsToDispBeamIntForc=[columnZ,beamX,beamY]
Q1.listBeamIntForc=['My','Mz','Qy','Qz','N']
Q1.cameraParameters= vtk_graphic_base.CameraParameters('XYZPos')
Q1.setsToDispBeamLoads=[beamY]
Q1.vectorScalePointLoads=0.005
Q1.compElLoad='transComponent'

Q2=graphical_reports.LoadCaseDispParameters(loadCaseName='QearthPressWall',loadCaseDescr='Q2: earth pressure columns',loadCaseExpr='1.0*QearthPressWall',setsToDispLoads=[overallSet],setsToDispDspRot=[overallSet],setsToDispIntForc=[deck,found])
Q2.unitsScaleLoads=1e-3
Q2.unitsScaleDispl=1e3
Q2.unitsDispl='[mm]'
Q2.unitsScaleMom=1e-3
Q2.unitsMom='[m.kN]'
Q2.unitsScaleForc=1e-3
Q2.unitsForc='[kN]'
Q2.setsToDispBeamIntForc=[columnZ,beamX,beamY]
Q2.listBeamIntForc=['My','Mz','Qy','Qz','N']
Q2.cameraParameters= vtk_graphic_base.CameraParameters('XYZPos')
Q2.setsToDispBeamLoads=[overallSet]
Q2.vectorScalePointLoads=0.005
Q2.compElLoad='transComponent'


Q3=graphical_reports.LoadCaseDispParameters(loadCaseName='QearthPressCols',loadCaseDescr='Q3: earth pressure columns',loadCaseExpr='1.0*QearthPressCols',setsToDispLoads=[overallSet],setsToDispDspRot=[overallSet],setsToDispIntForc=[deck,found])
Q3.unitsScaleLoads=1e-3
Q3.unitsScaleDispl=1e3
Q3.unitsDispl='[mm]'
Q3.unitsScaleMom=1e-3
Q3.unitsMom='[m.kN]'
Q3.unitsScaleForc=1e-3
Q3.unitsForc='[kN]'
Q3.setsToDispBeamIntForc=[columnZ,beamX,beamY]
Q3.listBeamIntForc=['My','Mz','Qy','Qz','N']
Q3.cameraParameters= vtk_graphic_base.CameraParameters('XYZPos')
Q3.setsToDispBeamLoads=[overallSet]
Q3.vectorScalePointLoads=0.005
Q3.compElLoad='transComponent'

Q4=graphical_reports.LoadCaseDispParameters(loadCaseName='QearthPColsStrL',loadCaseDescr='Q4: earth pressure columns strip load',loadCaseExpr='1.0*QearthPColsStrL',setsToDispLoads=[overallSet],setsToDispDspRot=[overallSet],setsToDispIntForc=[deck,found])
Q4.unitsScaleLoads=1e-3
Q4.unitsScaleDispl=1e3
Q4.unitsDispl='[mm]'
Q4.unitsScaleMom=1e-3
Q4.unitsMom='[m.kN]'
Q4.unitsScaleForc=1e-3
Q4.unitsForc='[kN]'
Q4.setsToDispBeamIntForc=[columnZ,beamX,beamY]
Q4.listBeamIntForc=['My','Mz','Qy','Qz','N']
Q4.cameraParameters= vtk_graphic_base.CameraParameters('XYZPos')
Q4.setsToDispBeamLoads=[overallSet]
Q4.vectorScalePointLoads=0.005
Q4.compElLoad='transComponent'

Q5=graphical_reports.LoadCaseDispParameters(loadCaseName='QearthPColsLinL',loadCaseDescr='Q5: earth pressure columns line load',loadCaseExpr='1.0*QearthPColsLinL',setsToDispLoads=[overallSet],setsToDispDspRot=[overallSet],setsToDispIntForc=[deck,found])
Q5.unitsScaleLoads=1e-3
Q5.unitsScaleDispl=1e3
Q5.unitsDispl='[mm]'
Q5.unitsScaleMom=1e-3
Q5.unitsMom='[m.kN]'
Q5.unitsScaleForc=1e-3
Q5.unitsForc='[kN]'
Q5.setsToDispBeamIntForc=[columnZ,beamX,beamY]
Q5.listBeamIntForc=['My','Mz','Qy','Qz','N']
Q5.cameraParameters= vtk_graphic_base.CameraParameters('XYZPos')
Q5.setsToDispBeamLoads=[overallSet]
Q5.vectorScalePointLoads=0.005
Q5.compElLoad='transComponent'

Q6=graphical_reports.LoadCaseDispParameters(loadCaseName='QearthPColsHrzL',loadCaseDescr='Q6: earth pressure columns line load',loadCaseExpr='1.0*QearthPColsHrzL',setsToDispLoads=[overallSet],setsToDispDspRot=[overallSet],setsToDispIntForc=[deck,found])
Q6.unitsScaleLoads=1e-3
Q6.unitsScaleDispl=1e3
Q6.unitsDispl='[mm]'
Q6.unitsScaleMom=1e-3
Q6.unitsMom='[m.kN]'
Q6.unitsScaleForc=1e-3
Q6.unitsForc='[kN]'
Q6.setsToDispBeamIntForc=[columnZ,beamX,beamY]
Q6.listBeamIntForc=['My','Mz','Qy','Qz','N']
Q6.cameraParameters= vtk_graphic_base.CameraParameters('XYZPos')
Q6.setsToDispBeamLoads=[overallSet]
Q6.vectorScalePointLoads=0.005
Q6.compElLoad='transComponent'
