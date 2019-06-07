# -*- coding: utf-8 -*-

'''In this script we define default data of load cases to be used (or changed)
while displaying loads or results associated to single load cases 
'''
from postprocess.xcVtk import vtk_graphic_base
from postprocess.reports import graphical_reports
from postprocess.xcVtk import vtk_graphic_base
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




'''
G1=graphical_reports.RecordLoadCaseDisp(loadCaseName='GselfWeight',loadCaseDescr='G1: self weight',loadCaseExpr='1.0*GselfWeight',setsToDispLoads=[overallSet],setsToDispDspRot=[overallSet],setsToDispIntForc=[slabs])
G1.unitsScaleLoads=1e-3
G1.unitsScaleDispl=1e3
G1.unitsDispl='[mm]'
G1.unitsScaleMom=1e-3
G1.unitsMom='[m.kN]'
G1.unitsScaleForc=1e-3
G1.unitsForc='[kN]'
G1.setsToDispBeamIntForc=[beams,columns]
G1.listBeamIntForc=['My','Mz','Qy','Qz','N']
G1.cameraParameters= vtk_graphic_base.CameraParameters('XYZPos')
G1.setsToDispBeamLoads=[]
G1.vectorScalePointLoads=0.005
G1.compElLoad='transComponent'

'''
D=graphical_reports.RecordLoadCaseDisp(loadCaseName='DeadL',loadCaseDescr='D: dead load',loadCaseExpr='1.0*DeadL',setsToDispLoads=[overallSet],setsToDispDspRot=[overallSet],setsToDispIntForc=[slabs])
D.unitsScaleLoads=1e-3
D.unitsScaleDispl=1e3
D.unitsDispl='[mm]'
D.unitsScaleMom=1e-3
D.unitsMom='[m.kN]'
D.unitsScaleForc=1e-3
D.unitsForc='[kN]'
D.setsToDispBeamIntForc=[beams,columns]
D.listBeamIntForc=['My','Mz','Qy','Qz','N']
D.cameraParameters= vtk_graphic_base.CameraParameters('XYZPos')
D.setsToDispBeamLoads=[]
D.vectorScalePointLoads=0.005
D.compElLoad='transComponent'


L=graphical_reports.RecordLoadCaseDisp(loadCaseName='LiveL',loadCaseDescr='L: live load',loadCaseExpr='1.0*LiveL',setsToDispLoads=[overallSet],setsToDispDspRot=[overallSet],setsToDispIntForc=[slabs])
L.unitsScaleLoads=1e-3
L.unitsScaleDispl=1e3
L.unitsDispl='[mm]'
L.unitsScaleMom=1e-3
L.unitsMom='[m.kN]'
L.unitsScaleForc=1e-3
L.unitsForc='[kN]'
L.setsToDispBeamIntForc=[beams,columns]
L.listBeamIntForc=['My','Mz','Qy','Qz','N']
L.cameraParameters= vtk_graphic_base.CameraParameters('XYZPos')
L.setsToDispBeamLoads=[]
L.vectorScalePointLoads=0.005
L.compElLoad='transComponent'

S=graphical_reports.RecordLoadCaseDisp(loadCaseName='SnowL',loadCaseDescr='S: snow load',loadCaseExpr='1.0*SnowL',setsToDispLoads=[overallSet],setsToDispDspRot=[overallSet],setsToDispIntForc=[slabs])
S.unitsScaleLoads=1e-3
S.unitsScaleDispl=1e3
S.unitsDispl='[mm]'
S.unitsScaleMom=1e-3
S.unitsMom='[m.kN]'
S.unitsScaleForc=1e-3
S.unitsForc='[kN]'
S.setsToDispBeamIntForc=[beams,columns]
S.listBeamIntForc=['My','Mz','Qy','Qz','N']
S.cameraParameters= vtk_graphic_base.CameraParameters('XYZPos')
S.setsToDispBeamLoads=[]
S.vectorScalePointLoads=0.005
S.compElLoad='transComponent'

Lunif1fl=graphical_reports.RecordLoadCaseDisp(loadCaseName='Live_unif_1floor',loadCaseDescr='Lunif1fl: live uniform load on first floor',loadCaseExpr='1.0*Live_unif_1floor',setsToDispLoads=[overallSet],setsToDispDspRot=[overallSet],setsToDispIntForc=[slabs])
Lunif1fl.unitsScaleLoads=1e-3
Lunif1fl.unitsScaleDispl=1e3
Lunif1fl.unitsDispl='[mm]'
Lunif1fl.unitsScaleMom=1e-3
Lunif1fl.unitsMom='[m.kN]'
Lunif1fl.unitsScaleForc=1e-3
Lunif1fl.unitsForc='[kN]'
Lunif1fl.setsToDispBeamIntForc=[beams,columns]
Lunif1fl.listBeamIntForc=['My','Mz','Qy','Qz','N']
Lunif1fl.cameraParameters= vtk_graphic_base.CameraParameters('XYZPos')
Lunif1fl.setsToDispBeamLoads=[]
Lunif1fl.vectorScalePointLoads=0.005
Lunif1fl.compElLoad='transComponent'

Lstag1fl=graphical_reports.RecordLoadCaseDisp(loadCaseName='Live_stag_1floor',loadCaseDescr='Lstag1fl: live stagged pattern load on first floor',loadCaseExpr='1.0*Live_stag_1floor',setsToDispLoads=[overallSet],setsToDispDspRot=[overallSet],setsToDispIntForc=[slabs])
Lstag1fl.unitsScaleLoads=1e-3
Lstag1fl.unitsScaleDispl=1e3
Lstag1fl.unitsDispl='[mm]'
Lstag1fl.unitsScaleMom=1e-3
Lstag1fl.unitsMom='[m.kN]'
Lstag1fl.unitsScaleForc=1e-3
Lstag1fl.unitsForc='[kN]'
Lstag1fl.setsToDispBeamIntForc=[beams,columns]
Lstag1fl.listBeamIntForc=['My','Mz','Qy','Qz','N']
Lstag1fl.cameraParameters= vtk_graphic_base.CameraParameters('XYZPos')
Lstag1fl.setsToDispBeamLoads=[]
Lstag1fl.vectorScalePointLoads=0.005
Lstag1fl.compElLoad='transComponent'

W_WE=graphical_reports.RecordLoadCaseDisp(loadCaseName='Wind_WE',loadCaseDescr='W_WE: Wind West-East',loadCaseExpr='1.0*Wind_WE',setsToDispLoads=[overallSet],setsToDispDspRot=[overallSet],setsToDispIntForc=[slabs])
W_WE.unitsScaleLoads=1e-3
W_WE.unitsScaleDispl=1e3
W_WE.unitsDispl='[mm]'
W_WE.unitsScaleMom=1e-3
W_WE.unitsMom='[m.kN]'
W_WE.unitsScaleForc=1e-3
W_WE.unitsForc='[kN]'
W_WE.setsToDispBeamIntForc=[beams,columns]
W_WE.listBeamIntForc=['My','Mz','Qy','Qz','N']
W_WE.cameraParameters= vtk_graphic_base.CameraParameters('XYZPos')
W_WE.setsToDispBeamLoads=[]
W_WE.vectorScalePointLoads=0.005
W_WE.compElLoad='transComponent'

W_NS=graphical_reports.RecordLoadCaseDisp(loadCaseName='Wind_NS',loadCaseDescr='W_NS: Wind North-South',loadCaseExpr='1.0*Wind_NS',setsToDispLoads=[overallSet],setsToDispDspRot=[overallSet],setsToDispIntForc=[slabs])
W_NS.unitsScaleLoads=1e-3
W_NS.unitsScaleDispl=1e3
W_NS.unitsDispl='[mm]'
W_NS.unitsScaleMom=1e-3
W_NS.unitsMom='[m.kN]'
W_NS.unitsScaleForc=1e-3
W_NS.unitsForc='[kN]'
W_NS.setsToDispBeamIntForc=[beams,columns]
W_NS.listBeamIntForc=['My','Mz','Qy','Qz','N']
W_NS.cameraParameters= vtk_graphic_base.CameraParameters('XYZPos')
W_NS.setsToDispBeamLoads=[]
W_NS.vectorScalePointLoads=0.005
W_NS.compElLoad='transComponent'
