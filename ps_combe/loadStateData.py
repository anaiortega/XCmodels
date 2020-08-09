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
                  forces (defaults to (1.0,1.0,1.0)-> auto-scale)
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

G1=graphical_reports.LoadCaseDispParameters(loadCaseName='GselfWeight',loadCaseDescr='G1: self weight',loadCaseExpr='1.0*GselfWeight',setsToDispLoads=[shells],setsToDispDspRot=[shells],setsToDispIntForc=[shells])
G1.unitsScaleLoads=1e-3
G1.unitsScaleForc=1e-3
G1.unitsScaleMom=1e-3
G1.unitsScaleDispl=1e3
G1.unitsDispl='[mm]'

G2=graphical_reports.LoadCaseDispParameters(loadCaseName='GdeadLoad',loadCaseDescr='G2: dead load',loadCaseExpr='1.0*GdeadLoad',setsToDispLoads=[shells],setsToDispDspRot=[shells],setsToDispIntForc=[shells])
G2.unitsScaleLoads=1e-3
G2.unitsScaleForc=1e-3
G2.unitsScaleMom=1e-3
G2.unitsScaleDispl=1e3
G2.unitsDispl='[mm]'

S=graphical_reports.LoadCaseDispParameters(loadCaseName='GdeadLoad',loadCaseDescr='S: settlement',loadCaseExpr='0.01*GselfWeight+0.01*GdeadLoad',setsToDispLoads=[deckSurfaces],setsToDispDspRot=[deckSurfaces],setsToDispIntForc=[deckSurfaces])
S.unitsScaleLoads=1e-3
S.unitsScaleForc=1e-3
S.unitsScaleMom=1e-3
S.unitsScaleDispl=1e3
S.unitsDispl='[mm]'

S.unitsMom='[m.kN]'
S.unitsForc='[kN]'
S.setsToDispBeamIntForc=[beamLines]
S.listBeamIntForc=['N','Qy','Mz']
S.cameraParameters= vtk_graphic_base.CameraParameters('XYZPos')
S.compElLoad='transComponent'


Q269A_unif= graphical_reports.LoadCaseDispParameters(loadCaseName='liveLoad269_1',loadCaseDescr='SIA 269 load model 1 (mid span)',loadCaseExpr='1.0*liveLoad269_1',setsToDispLoads=[shells],setsToDispDspRot=[shells],setsToDispIntForc=[])
Q269A_unif.unitsScaleLoads=1e-3
Q269A_unif.unitsScaleForc=1e-3
Q269A_unif.unitsScaleMom=1e-3
Q269A_unif.unitsScaleDispl=1e3
Q269A_unif.unitsDispl='[mm]'


Q269A_point= graphical_reports.LoadCaseDispParameters(loadCaseName='liveLoad269_1',loadCaseDescr='SIA 269 load model 1 (mid span)',loadCaseExpr='1.0*liveLoad269_1',setsToDispLoads=[shells],setsToDispDspRot=[shells],setsToDispIntForc=[])
Q269A_point.unitsScaleLoads=1e-3
Q269A_point.unitsScaleForc=1e-3
Q269A_point.unitsScaleMom=1e-3
Q269A_point.unitsScaleDispl=1e3
Q269A_point.unitsDispl='[mm]'

Q269B_unif= graphical_reports.LoadCaseDispParameters(loadCaseName='liveLoad269_2',loadCaseDescr='SIA 269 load model 1 (shear control)',loadCaseExpr='1.0*liveLoad269_2',setsToDispLoads=[shells],setsToDispDspRot=[shells],setsToDispIntForc=[])
Q269B_unif.unitsScaleLoads=1e-3
Q269B_unif.unitsScaleForc=1e-3
Q269B_unif.unitsScaleMom=1e-3
Q269B_unif.unitsScaleDispl=1e3
Q269B_unif.unitsDispl='[mm]'


Q269B_point= graphical_reports.LoadCaseDispParameters(loadCaseName='liveLoad269_2',loadCaseDescr='SIA 269 load model 1 (shear_control)',loadCaseExpr='1.0*liveLoad269_2',setsToDispLoads=[shells],setsToDispDspRot=[shells],setsToDispIntForc=[])
Q269B_point.unitsScaleLoads=1e-3
Q269B_point.unitsScaleForc=1e-3
Q269B_point.unitsScaleMom=1e-3
Q269B_point.unitsScaleDispl=1e3
Q269B_point.unitsDispl='[mm]'

Q664CraneA_unif= graphical_reports.LoadCaseDispParameters(loadCaseName='liveLoad664Crane_1',loadCaseDescr='Report 664 crane load model (mid span)',loadCaseExpr='1.0*liveLoad664Crane_1',setsToDispLoads=[shells],setsToDispDspRot=[shells],setsToDispIntForc=[shells])
Q664CraneA_unif.unitsScaleLoads=1e-3
Q664CraneA_unif.unitsScaleForc=1e-3
Q664CraneA_unif.unitsScaleMom=1e-3
Q664CraneA_unif.unitsScaleDispl=1e3
Q664CraneA_unif.unitsDispl='[mm]'


Q664CraneA_point= graphical_reports.LoadCaseDispParameters(loadCaseName='liveLoad664Crane_1',loadCaseDescr='Report 664 crane load model (mid span)',loadCaseExpr='1.0*liveLoad664Crane_1',setsToDispLoads=[shells],setsToDispDspRot=[shells],setsToDispIntForc=[shells])
Q664CraneA_point.unitsScaleLoads=1e-3
Q664CraneA_point.unitsScaleForc=1e-3
Q664CraneA_point.unitsScaleMom=1e-3
Q664CraneA_point.unitsScaleDispl=1e3
Q664CraneA_point.unitsDispl='[mm]'

Q664CraneB_unif= graphical_reports.LoadCaseDispParameters(loadCaseName='liveLoad664Crane_2',loadCaseDescr='Report 664 crane load model (mid span)',loadCaseExpr='1.0*liveLoad664Crane_2',setsToDispLoads=[shells],setsToDispDspRot=[shells],setsToDispIntForc=[shells])
Q664CraneB_unif.unitsScaleLoads=1e-3
Q664CraneB_unif.unitsScaleForc=1e-3
Q664CraneB_unif.unitsScaleMom=1e-3
Q664CraneB_unif.unitsScaleDispl=1e3
Q664CraneB_unif.unitsDispl='[mm]'


Q664CraneB_point= graphical_reports.LoadCaseDispParameters(loadCaseName='liveLoad664Crane_2',loadCaseDescr='Report 664 crane load model (end span)',loadCaseExpr='1.0*liveLoad664Crane_2',setsToDispLoads=[shells],setsToDispDspRot=[shells],setsToDispIntForc=[shells])
Q664CraneB_point.unitsScaleLoads=1e-3
Q664CraneB_point.unitsScaleForc=1e-3
Q664CraneB_point.unitsScaleMom=1e-3
Q664CraneB_point.unitsScaleDispl=1e3
Q664CraneB_point.unitsDispl='[mm]'

Q664Det1A_point= graphical_reports.LoadCaseDispParameters(loadCaseName='liveLoad664Det1_1',loadCaseDescr='Report 664 DET1 load model (mid span)',loadCaseExpr='1.0*liveLoad664Det1_1',setsToDispLoads=[shells],setsToDispDspRot=[shells],setsToDispIntForc=[shells])
Q664Det1A_point.unitsScaleLoads=1e-3
Q664Det1A_point.unitsScaleForc=1e-3
Q664Det1A_point.unitsScaleMom=1e-3
Q664Det1A_point.unitsScaleDispl=1e3
Q664Det1A_point.unitsDispl='[mm]'

Q664Det1B_point= graphical_reports.LoadCaseDispParameters(loadCaseName='liveLoad664Det1_2',loadCaseDescr='Report 664 DET1 load model (end span)',loadCaseExpr='1.0*liveLoad664Det1_2',setsToDispLoads=[shells],setsToDispDspRot=[shells],setsToDispIntForc=[shells])
Q664Det1B_point.unitsScaleLoads=1e-3
Q664Det1B_point.unitsScaleForc=1e-3
Q664Det1B_point.unitsScaleMom=1e-3
Q664Det1B_point.unitsScaleDispl=1e3
Q664Det1B_point.unitsDispl='[mm]'

Q664Det2A_point= graphical_reports.LoadCaseDispParameters(loadCaseName='liveLoad664Det2_1',loadCaseDescr='Report 664 DET2 load model (mid span)',loadCaseExpr='1.0*liveLoad664Det2_1',setsToDispLoads=[shells],setsToDispDspRot=[shells],setsToDispIntForc=[shells])
Q664Det2A_point.unitsScaleLoads=1e-3
Q664Det2A_point.unitsScaleForc=1e-3
Q664Det2A_point.unitsScaleMom=1e-3
Q664Det2A_point.unitsScaleDispl=1e3
Q664Det2A_point.unitsDispl='[mm]'

Q664Det2B_point= graphical_reports.LoadCaseDispParameters(loadCaseName='liveLoad664Det2_2',loadCaseDescr='Report 664 DET2 load model (end span)',loadCaseExpr='1.0*liveLoad664Det2_2',setsToDispLoads=[shells],setsToDispDspRot=[shells],setsToDispIntForc=[shells])
Q664Det2B_point.unitsScaleLoads=1e-3
Q664Det2B_point.unitsScaleForc=1e-3
Q664Det2B_point.unitsScaleMom=1e-3
Q664Det2B_point.unitsScaleDispl=1e3
Q664Det2B_point.unitsDispl='[mm]'

T= graphical_reports.LoadCaseDispParameters(loadCaseName='temperature',loadCaseDescr='Température',loadCaseExpr='1.0*temperature',setsToDispLoads=[shells],setsToDispDspRot=[shells],setsToDispIntForc=[shells])
T.unitsScaleLoads=1e-3
T.unitsScaleDispl=1e3
T.unitsDispl='[mm]'
T.unitsScaleForc=1e-3
T.unitsScaleMom=1e-3

T.unitsMom='[m.kN]'
T.unitsForc='[kN]'
T.setsToDispBeamIntForc=[beams]
T.listBeamIntForc=['My','Mz','Qy','Qz','N']
T.cameraParameters= vtk_graphic_base.CameraParameters('XYZPos')
T.compElLoad='transComponent'


tempDown= graphical_reports.LoadCaseDispParameters(loadCaseName='TmpDown',loadCaseDescr='Température -20',loadCaseExpr='1.0*GselfWeight+1.0*GdeadLoad+1.5*temp_down',setsToDispLoads=[],setsToDispDspRot=[deckSurfaces],setsToDispIntForc=[deckSurfaces])
tempDown.unitsScaleLoads=1e-3
tempDown.unitsScaleDispl=1e3
tempDown.unitsDispl='[mm]'
tempDown.unitsScaleForc=1e-3
tempDown.unitsScaleMom=1e-3

tempDown.unitsMom='[m.kN]'
tempDown.unitsForc='[kN]'
tempDown.setsToDispBeamIntForc=[beamLines]
tempDown.listBeamIntForc=['N','Qy','Mz']
tempDown.cameraParameters= vtk_graphic_base.CameraParameters('XYZPos')
tempDown.compElLoad='transComponent'


tempUp= graphical_reports.LoadCaseDispParameters(loadCaseName='TmpUp',loadCaseDescr='Température +20',loadCaseExpr='1.0*GselfWeight+1.0*GdeadLoad+1.5*temp_up',setsToDispLoads=[],setsToDispDspRot=[deckSurfaces],setsToDispIntForc=[deckSurfaces])
tempUp.unitsScaleLoads=1e-3
tempUp.unitsScaleDispl=1e3
tempUp.unitsDispl='[mm]'
tempUp.unitsScaleForc=1e-3
tempUp.unitsScaleMom=1e-3

tempUp.unitsMom='[m.kN]'
tempUp.unitsForc='[kN]'
tempUp.setsToDispBeamIntForc=[beamLines]
tempUp.listBeamIntForc=['N','Qy','Mz']
tempUp.cameraParameters= vtk_graphic_base.CameraParameters('XYZPos')
tempUp.compElLoad='transComponent'


brake1= graphical_reports.LoadCaseDispParameters(loadCaseName='Brake',loadCaseDescr='Brake disp.',loadCaseExpr='1.0*GselfWeight+1.0*GdeadLoad+0.75*liveLoad269_1+1.5*temp_up',setsToDispLoads=[],setsToDispDspRot=[deckSurfaces],setsToDispIntForc=[])
brake1.unitsScaleLoads=1e-3
brake1.unitsScaleDispl=1e3
brake1.unitsDispl='[mm]'
brake1.unitsScaleForc=1e-3
brake1.unitsScaleMom=1e-3

brake1.unitsMom='[m.kN]'
brake1.unitsForc='[kN]'
brake1.setsToDispBeamIntForc=[]
brake1.listBeamIntForc=['N','Qy','Mz']
brake1.cameraParameters= vtk_graphic_base.CameraParameters('XYZPos')
brake1.compElLoad='transComponent'


brake2= graphical_reports.LoadCaseDispParameters(loadCaseName='Brake',loadCaseDescr='Brake disp.',loadCaseExpr='1.0*GselfWeight+1.0*GdeadLoad+1.0*liveLoad269_1+0.6*temp_up',setsToDispLoads=[],setsToDispDspRot=[deckSurfaces],setsToDispIntForc=[])
brake2.unitsScaleLoads=1e-3
brake2.unitsScaleDispl=1e3
brake2.unitsDispl='[mm]'
brake2.unitsScaleForc=1e-3
brake2.unitsScaleMom=1e-3

brake2.unitsMom='[m.kN]'
brake2.unitsForc='[kN]'
brake2.setsToDispBeamIntForc=[]
brake2.listBeamIntForc=['N','Qy','Mz']
brake2.cameraParameters= vtk_graphic_base.CameraParameters('XYZPos')
brake2.compElLoad='transComponent'


ELU01= graphical_reports.LoadCaseDispParameters(loadCaseName='ELU01',loadCaseDescr='SIA 269 LM1 A',loadCaseExpr='1.2*GselfWeight+1.2*GdeadLoad+1.5*liveLoad269_1',setsToDispLoads=[],setsToDispDspRot=[deckSurfaces],setsToDispIntForc=[deckSurfaces])
ELU01.unitsScaleLoads=1e-3
ELU01.unitsScaleDispl=1e3
ELU01.unitsDispl='[mm]'
ELU01.unitsScaleForc=1e-3
ELU01.unitsScaleMom=1e-3

ELU01.unitsMom='[m.kN]'
ELU01.unitsForc='[kN]'
ELU01.setsToDispBeamIntForc=[beamLines]
ELU01.listBeamIntForc=['N','Qy','Mz']
ELU01.cameraParameters= vtk_graphic_base.CameraParameters('XYZPos')
ELU01.compElLoad='transComponent'


ELU02= graphical_reports.LoadCaseDispParameters(loadCaseName='ELU02',loadCaseDescr='SIA 269 LM1 B',loadCaseExpr='1.2*GselfWeight+1.2*GdeadLoad+1.5*liveLoad269_2',setsToDispLoads=[],setsToDispDspRot=[],setsToDispIntForc=[])
ELU02.unitsScaleLoads=1e-3
ELU02.unitsScaleDispl=1e3
ELU02.unitsDispl='[mm]'
ELU02.unitsScaleForc=1e-3
ELU02.unitsScaleMom=1e-3

ELU02.unitsMom='[m.kN]'
ELU02.unitsForc='[kN]'
ELU02.setsToDispBeamIntForc=[beamLines]
ELU02.listBeamIntForc=['N','Qy','Mz']
ELU02.cameraParameters= vtk_graphic_base.CameraParameters('XYZPos')
ELU02.compElLoad='transComponent'


ELU03= graphical_reports.LoadCaseDispParameters(loadCaseName='ELU03',loadCaseDescr='SIA 664 Crane LM1 A',loadCaseExpr='1.2*GselfWeight+1.2*GdeadLoad+1.1*liveLoad664Crane_1',setsToDispLoads=[],setsToDispDspRot=[deckSurfaces],setsToDispIntForc=[deckSurfaces])
ELU03.unitsScaleLoads=1e-3
ELU03.unitsScaleDispl=1e3
ELU03.unitsDispl='[mm]'
ELU03.unitsScaleForc=1e-3
ELU03.unitsScaleMom=1e-3

ELU03.unitsMom='[m.kN]'
ELU03.unitsForc='[kN]'
ELU03.setsToDispBeamIntForc=[beamLines]
ELU03.listBeamIntForc=['N','Qy','Mz']
ELU03.cameraParameters= vtk_graphic_base.CameraParameters('XYZPos')
ELU03.compElLoad='transComponent'


ELU04= graphical_reports.LoadCaseDispParameters(loadCaseName='ELU04',loadCaseDescr='SIA 664 Crane LM1 B',loadCaseExpr='1.2*GselfWeight+1.2*GdeadLoad+1.1*liveLoad664Crane_2',setsToDispLoads=[],setsToDispDspRot=[],setsToDispIntForc=[])
ELU04.unitsScaleLoads=1e-3
ELU04.unitsScaleDispl=1e3
ELU04.unitsDispl='[mm]'
ELU04.unitsScaleForc=1e-3
ELU04.unitsScaleMom=1e-3

ELU04.unitsMom='[m.kN]'
ELU04.unitsForc='[kN]'
ELU04.setsToDispBeamIntForc=[beamLines]
ELU04.listBeamIntForc=['N','Qy','Mz']
ELU04.cameraParameters= vtk_graphic_base.CameraParameters('XYZPos')
ELU04.compElLoad='transComponent'


ELU05= graphical_reports.LoadCaseDispParameters(loadCaseName='ELU05',loadCaseDescr='SIA 664 DET1 LM A',loadCaseExpr='1.2*GselfWeight+1.2*GdeadLoad+1.1*liveLoad664Det1_1',setsToDispLoads=[],setsToDispDspRot=[],setsToDispIntForc=[])
ELU05.unitsScaleLoads=1e-3
ELU05.unitsScaleDispl=1e3
ELU05.unitsDispl='[mm]'
ELU05.unitsScaleForc=1e-3
ELU05.unitsScaleMom=1e-3

ELU05.unitsMom='[m.kN]'
ELU05.unitsForc='[kN]'
ELU05.setsToDispBeamIntForc=[beamLines]
ELU05.listBeamIntForc=['N','Qy','Mz']
ELU05.cameraParameters= vtk_graphic_base.CameraParameters('XYZPos')
ELU05.compElLoad='transComponent'


ELU06= graphical_reports.LoadCaseDispParameters(loadCaseName='ELU06',loadCaseDescr='SIA 664 DET1 LM A',loadCaseExpr='1.2*GselfWeight+1.2*GdeadLoad+1.1*liveLoad664Det1_2',setsToDispLoads=[],setsToDispDspRot=[],setsToDispIntForc=[])
ELU06.unitsScaleLoads=1e-3
ELU06.unitsScaleDispl=1e3
ELU06.unitsDispl='[mm]'
ELU06.unitsScaleForc=1e-3
ELU06.unitsScaleMom=1e-3

ELU06.unitsMom='[m.kN]'
ELU06.unitsForc='[kN]'
ELU06.setsToDispBeamIntForc=[beamLines]
ELU06.listBeamIntForc=['N','Qy','Mz']
ELU06.cameraParameters= vtk_graphic_base.CameraParameters('XYZPos')
ELU06.compElLoad='transComponent'


ELU07= graphical_reports.LoadCaseDispParameters(loadCaseName='ELU07',loadCaseDescr='SIA 664 DET2 LM A',loadCaseExpr='1.2*GselfWeight+1.2*GdeadLoad+1.1*liveLoad664Det2_1',setsToDispLoads=[],setsToDispDspRot=[],setsToDispIntForc=[])
ELU07.unitsScaleLoads=1e-3
ELU07.unitsScaleDispl=1e3
ELU07.unitsDispl='[mm]'
ELU07.unitsScaleForc=1e-3
ELU07.unitsScaleMom=1e-3

ELU07.unitsMom='[m.kN]'
ELU07.unitsForc='[kN]'
ELU07.setsToDispBeamIntForc=[beamLines]
ELU07.listBeamIntForc=['N','Qy','Mz']
ELU07.cameraParameters= vtk_graphic_base.CameraParameters('XYZPos')
ELU07.compElLoad='transComponent'


ELU08= graphical_reports.LoadCaseDispParameters(loadCaseName='ELU08',loadCaseDescr='SIA 664 DET2 LM A',loadCaseExpr='1.2*GselfWeight+1.2*GdeadLoad+1.1*liveLoad664Det2_2',setsToDispLoads=[],setsToDispDspRot=[],setsToDispIntForc=[])
ELU08.unitsScaleLoads=1e-3
ELU08.unitsScaleDispl=1e3
ELU08.unitsDispl='[mm]'
ELU08.unitsScaleForc=1e-3
ELU08.unitsScaleMom=1e-3

ELU08.unitsMom='[m.kN]'
ELU08.unitsForc='[kN]'
ELU08.setsToDispBeamIntForc=[beamLines]
ELU08.listBeamIntForc=['N','Qy','Mz']
ELU08.cameraParameters= vtk_graphic_base.CameraParameters('XYZPos')
ELU08.compElLoad='transComponent'


A= graphical_reports.LoadCaseDispParameters(loadCaseName='A',loadCaseDescr='Earthquake load',loadCaseExpr='1.0*GselfWeight+1.0*GdeadLoad+1.0*eQuake',setsToDispLoads=[],setsToDispDspRot=[shells],setsToDispIntForc=[])
A.unitsScaleLoads=1e-3
A.unitsScaleDispl=1e3
A.unitsDispl='[mm]'
A.unitsScaleForc=1e-3
A.unitsScaleMom=1e-3

A.unitsMom='[m.kN]'
A.unitsForc='[kN]'
A.setsToDispBeamIntForc=[beamLines]
A.listBeamIntForc=['N','Qy','Mz']
A.cameraParameters= vtk_graphic_base.CameraParameters('XYZPos')
A.compElLoad='transComponent'



