# -*- coding: utf-8 -*-

'''In this script we define default data of load cases to be used (or changed)
while displaying loads or results associated to single load cases 
'''
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
  viewName:  name of the view  that contains the renderer (available standard 
                 views: "XYZPos", "XYZNeg", "XPos", "XNeg","YPos", "YNeg",
                 "ZPos", "ZNeg", "+X+Y+Z", "+X+Y-Z", "+X-Y+Z", "+X-Y-Z", 
                 "-X+Y+Z", "-X+Y-Z", 
                 "-X-Y+Z", "-X-Y-Z")  (defaults to "XYZPos")
  hCamFct:   factor that applies to the height of the camera position 
                 in order to change perspective of isometric views 
                 (defaults to 1, usual values 0.1 to 10)
  viewNameBeams: name of the view  for beam elements displays (defaults to "XYZPos")
  hCamFctBeams:  factor that applies to the height of the camera position for
                 beam displays (defaults to 1)
'''

G1=graphical_reports.RecordLoadCaseDisp(loadCaseName='GselfWeight',loadCaseDescr='G1: self weight',loadCaseExpr='1.0*GselfWeight',setsToDispLoads=[shells],setsToDispDspRot=[shells],setsToDispIntForc=[shells])
G1.unitsScaleLoads=1e-3
G1.unitsScaleForc=1e-3
G1.unitsScaleMom=1e-3
G1.unitsScaleDispl=1e3
G1.unitsDispl='[mm]'
G1.vectorScaleLoads= .25

G2=graphical_reports.RecordLoadCaseDisp(loadCaseName='GdeadLoad',loadCaseDescr='G2: dead load',loadCaseExpr='1.0*GdeadLoad',setsToDispLoads=[shells],setsToDispDspRot=[shells],setsToDispIntForc=[shells])
G2.unitsScaleLoads=1e-3
G2.unitsScaleForc=1e-3
G2.unitsScaleMom=1e-3
G2.unitsScaleDispl=1e3
G2.unitsDispl='[mm]'
G2.vectorScaleLoads= .1

S=graphical_reports.RecordLoadCaseDisp(loadCaseName='GdeadLoad',loadCaseDescr='S: settlement',loadCaseExpr='0.01*GselfWeight+0.01*GdeadLoad',setsToDispLoads=[deckSurfaces],setsToDispDspRot=[deckSurfaces],setsToDispIntForc=[deckSurfaces])
S.unitsScaleLoads=1e-3
S.unitsScaleForc=1e-3
S.unitsScaleMom=1e-3
S.unitsScaleDispl=1e3
S.unitsDispl='[mm]'
S.vectorScaleLoads= .1

S.unitsMom='[m.kN]'
S.unitsForc='[kN]'
S.setsToDispBeamIntForc=[beamLines]
S.listBeamIntForc=['N','Qy','Mz']
S.scaleDispBeamIntForc=(0.02,0.05,-0.05)
S.viewName="XYZPos"
S.compElLoad='transComponent'
S.hCamFct=1

Q269A_unif= graphical_reports.RecordLoadCaseDisp(loadCaseName='liveLoad269_1',loadCaseDescr='SIA 269 load model 1 (mid span)',loadCaseExpr='1.0*liveLoad269_1',setsToDispLoads=[shells],setsToDispDspRot=[shells],setsToDispIntForc=[])
Q269A_unif.vectorScaleLoads= 1.0
Q269A_unif.unitsScaleLoads=1e-3
Q269A_unif.unitsScaleForc=1e-3
Q269A_unif.unitsScaleMom=1e-3
Q269A_unif.unitsScaleDispl=1e3
Q269A_unif.unitsDispl='[mm]'


Q269A_point= graphical_reports.RecordLoadCaseDisp(loadCaseName='liveLoad269_1',loadCaseDescr='SIA 269 load model 1 (mid span)',loadCaseExpr='1.0*liveLoad269_1',setsToDispLoads=[shells],setsToDispDspRot=[shells],setsToDispIntForc=[])
Q269A_point.vectorScaleLoads= 0.05
Q269A_point.unitsScaleLoads=1e-3
Q269A_point.unitsScaleForc=1e-3
Q269A_point.unitsScaleMom=1e-3
Q269A_point.unitsScaleDispl=1e3
Q269A_point.unitsDispl='[mm]'

Q269B_unif= graphical_reports.RecordLoadCaseDisp(loadCaseName='liveLoad269_2',loadCaseDescr='SIA 269 load model 1 (shear control)',loadCaseExpr='1.0*liveLoad269_2',setsToDispLoads=[shells],setsToDispDspRot=[shells],setsToDispIntForc=[])
Q269B_unif.vectorScaleLoads= 1.0
Q269B_unif.unitsScaleLoads=1e-3
Q269B_unif.unitsScaleForc=1e-3
Q269B_unif.unitsScaleMom=1e-3
Q269B_unif.unitsScaleDispl=1e3
Q269B_unif.unitsDispl='[mm]'


Q269B_point= graphical_reports.RecordLoadCaseDisp(loadCaseName='liveLoad269_2',loadCaseDescr='SIA 269 load model 1 (shear_control)',loadCaseExpr='1.0*liveLoad269_2',setsToDispLoads=[shells],setsToDispDspRot=[shells],setsToDispIntForc=[])
Q269B_point.vectorScaleLoads= 0.05
Q269B_point.unitsScaleLoads=1e-3
Q269B_point.unitsScaleForc=1e-3
Q269B_point.unitsScaleMom=1e-3
Q269B_point.unitsScaleDispl=1e3
Q269B_point.unitsDispl='[mm]'

Q664CraneA_unif= graphical_reports.RecordLoadCaseDisp(loadCaseName='liveLoad664Crane_1',loadCaseDescr='Report 664 crane load model (mid span)',loadCaseExpr='1.0*liveLoad664Crane_1',setsToDispLoads=[shells],setsToDispDspRot=[shells],setsToDispIntForc=[shells])
Q664CraneA_unif.vectorScaleLoads= 1.0
Q664CraneA_unif.unitsScaleLoads=1e-3
Q664CraneA_unif.unitsScaleForc=1e-3
Q664CraneA_unif.unitsScaleMom=1e-3
Q664CraneA_unif.unitsScaleDispl=1e3
Q664CraneA_unif.unitsDispl='[mm]'


Q664CraneA_point= graphical_reports.RecordLoadCaseDisp(loadCaseName='liveLoad664Crane_1',loadCaseDescr='Report 664 crane load model (mid span)',loadCaseExpr='1.0*liveLoad664Crane_1',setsToDispLoads=[shells],setsToDispDspRot=[shells],setsToDispIntForc=[shells])
Q664CraneA_point.vectorScaleLoads= 0.05
Q664CraneA_point.unitsScaleLoads=1e-3
Q664CraneA_point.unitsScaleForc=1e-3
Q664CraneA_point.unitsScaleMom=1e-3
Q664CraneA_point.unitsScaleDispl=1e3
Q664CraneA_point.unitsDispl='[mm]'

Q664CraneB_unif= graphical_reports.RecordLoadCaseDisp(loadCaseName='liveLoad664Crane_2',loadCaseDescr='Report 664 crane load model (mid span)',loadCaseExpr='1.0*liveLoad664Crane_2',setsToDispLoads=[shells],setsToDispDspRot=[shells],setsToDispIntForc=[shells])
Q664CraneB_unif.vectorScaleLoads= 1.0
Q664CraneB_unif.unitsScaleLoads=1e-3
Q664CraneB_unif.unitsScaleForc=1e-3
Q664CraneB_unif.unitsScaleMom=1e-3
Q664CraneB_unif.unitsScaleDispl=1e3
Q664CraneB_unif.unitsDispl='[mm]'


Q664CraneB_point= graphical_reports.RecordLoadCaseDisp(loadCaseName='liveLoad664Crane_2',loadCaseDescr='Report 664 crane load model (end span)',loadCaseExpr='1.0*liveLoad664Crane_2',setsToDispLoads=[shells],setsToDispDspRot=[shells],setsToDispIntForc=[shells])
Q664CraneB_point.vectorScaleLoads= 0.05
Q664CraneB_point.unitsScaleLoads=1e-3
Q664CraneB_point.unitsScaleForc=1e-3
Q664CraneB_point.unitsScaleMom=1e-3
Q664CraneB_point.unitsScaleDispl=1e3
Q664CraneB_point.unitsDispl='[mm]'

Q664Det1A_point= graphical_reports.RecordLoadCaseDisp(loadCaseName='liveLoad664Det1_1',loadCaseDescr='Report 664 DET1 load model (mid span)',loadCaseExpr='1.0*liveLoad664Det1_1',setsToDispLoads=[shells],setsToDispDspRot=[shells],setsToDispIntForc=[shells])
Q664Det1A_point.vectorScaleLoads= 0.05
Q664Det1A_point.unitsScaleLoads=1e-3
Q664Det1A_point.unitsScaleForc=1e-3
Q664Det1A_point.unitsScaleMom=1e-3
Q664Det1A_point.unitsScaleDispl=1e3
Q664Det1A_point.unitsDispl='[mm]'

Q664Det1B_point= graphical_reports.RecordLoadCaseDisp(loadCaseName='liveLoad664Det1_2',loadCaseDescr='Report 664 DET1 load model (end span)',loadCaseExpr='1.0*liveLoad664Det1_2',setsToDispLoads=[shells],setsToDispDspRot=[shells],setsToDispIntForc=[shells])
Q664Det1B_point.vectorScaleLoads= 0.05
Q664Det1B_point.unitsScaleLoads=1e-3
Q664Det1B_point.unitsScaleForc=1e-3
Q664Det1B_point.unitsScaleMom=1e-3
Q664Det1B_point.unitsScaleDispl=1e3
Q664Det1B_point.unitsDispl='[mm]'

Q664Det2A_point= graphical_reports.RecordLoadCaseDisp(loadCaseName='liveLoad664Det2_1',loadCaseDescr='Report 664 DET2 load model (mid span)',loadCaseExpr='1.0*liveLoad664Det2_1',setsToDispLoads=[shells],setsToDispDspRot=[shells],setsToDispIntForc=[shells])
Q664Det2A_point.vectorScaleLoads= 0.05
Q664Det2A_point.unitsScaleLoads=1e-3
Q664Det2A_point.unitsScaleForc=1e-3
Q664Det2A_point.unitsScaleMom=1e-3
Q664Det2A_point.unitsScaleDispl=1e3
Q664Det2A_point.unitsDispl='[mm]'

Q664Det2B_point= graphical_reports.RecordLoadCaseDisp(loadCaseName='liveLoad664Det2_2',loadCaseDescr='Report 664 DET2 load model (end span)',loadCaseExpr='1.0*liveLoad664Det2_2',setsToDispLoads=[shells],setsToDispDspRot=[shells],setsToDispIntForc=[shells])
Q664Det2B_point.vectorScaleLoads= 0.05
Q664Det2B_point.unitsScaleLoads=1e-3
Q664Det2B_point.unitsScaleForc=1e-3
Q664Det2B_point.unitsScaleMom=1e-3
Q664Det2B_point.unitsScaleDispl=1e3
Q664Det2B_point.unitsDispl='[mm]'

T= graphical_reports.RecordLoadCaseDisp(loadCaseName='temperature',loadCaseDescr='Température',loadCaseExpr='1.0*temperature',setsToDispLoads=[shells],setsToDispDspRot=[shells],setsToDispIntForc=[shells])
T.unitsScaleLoads=1e-3
T.vectorScaleLoads=0.1
T.unitsScaleDispl=1e3
T.unitsDispl='[mm]'
T.unitsScaleForc=1e-3
T.unitsScaleMom=1e-3

T.unitsMom='[m.kN]'
T.unitsForc='[kN]'
T.setsToDispBeamIntForc=[beams]
T.listBeamIntForc=['My','Mz','Qy','Qz','N']
T.scaleDispBeamIntForc=(1,0.5,1)
T.viewName="XYZPos"
T.compElLoad='transComponent'
T.hCamFct=1

tempDown= graphical_reports.RecordLoadCaseDisp(loadCaseName='TmpDown',loadCaseDescr='Température -20',loadCaseExpr='1.0*GselfWeight+1.0*GdeadLoad+1.5*temp_down',setsToDispLoads=[],setsToDispDspRot=[deckSurfaces],setsToDispIntForc=[deckSurfaces])
tempDown.unitsScaleLoads=1e-3
tempDown.vectorScaleLoads=0.1
tempDown.unitsScaleDispl=1e3
tempDown.unitsDispl='[mm]'
tempDown.unitsScaleForc=1e-3
tempDown.unitsScaleMom=1e-3

tempDown.unitsMom='[m.kN]'
tempDown.unitsForc='[kN]'
tempDown.setsToDispBeamIntForc=[beamLines]
tempDown.listBeamIntForc=['N','Qy','Mz']
tempDown.scaleDispBeamIntForc=(0.02,0.05,-0.05)
tempDown.viewName="XYZPos"
tempDown.compElLoad='transComponent'
tempDown.hCamFct=1

tempUp= graphical_reports.RecordLoadCaseDisp(loadCaseName='TmpUp',loadCaseDescr='Température +20',loadCaseExpr='1.0*GselfWeight+1.0*GdeadLoad+1.5*temp_up',setsToDispLoads=[],setsToDispDspRot=[deckSurfaces],setsToDispIntForc=[deckSurfaces])
tempUp.unitsScaleLoads=1e-3
tempUp.vectorScaleLoads=0.1
tempUp.unitsScaleDispl=1e3
tempUp.unitsDispl='[mm]'
tempUp.unitsScaleForc=1e-3
tempUp.unitsScaleMom=1e-3

tempUp.unitsMom='[m.kN]'
tempUp.unitsForc='[kN]'
tempUp.setsToDispBeamIntForc=[beamLines]
tempUp.listBeamIntForc=['N','Qy','Mz']
tempUp.scaleDispBeamIntForc=(0.02,0.05,-0.05)
tempUp.viewName="XYZPos"
tempUp.compElLoad='transComponent'
tempUp.hCamFct=1

brake1= graphical_reports.RecordLoadCaseDisp(loadCaseName='Brake',loadCaseDescr='Brake disp.',loadCaseExpr='1.0*GselfWeight+1.0*GdeadLoad+0.75*liveLoad269_1+1.5*temp_up',setsToDispLoads=[],setsToDispDspRot=[deckSurfaces],setsToDispIntForc=[])
brake1.unitsScaleLoads=1e-3
brake1.vectorScaleLoads=0.1
brake1.unitsScaleDispl=1e3
brake1.unitsDispl='[mm]'
brake1.unitsScaleForc=1e-3
brake1.unitsScaleMom=1e-3

brake1.unitsMom='[m.kN]'
brake1.unitsForc='[kN]'
brake1.setsToDispBeamIntForc=[]
brake1.listBeamIntForc=['N','Qy','Mz']
brake1.scaleDispBeamIntForc=(0.02,0.05,-0.05)
brake1.viewName="XYZPos"
brake1.compElLoad='transComponent'
brake1.hCamFct=1

brake2= graphical_reports.RecordLoadCaseDisp(loadCaseName='Brake',loadCaseDescr='Brake disp.',loadCaseExpr='1.0*GselfWeight+1.0*GdeadLoad+1.0*liveLoad269_1+0.6*temp_up',setsToDispLoads=[],setsToDispDspRot=[deckSurfaces],setsToDispIntForc=[])
brake2.unitsScaleLoads=1e-3
brake2.vectorScaleLoads=0.1
brake2.unitsScaleDispl=1e3
brake2.unitsDispl='[mm]'
brake2.unitsScaleForc=1e-3
brake2.unitsScaleMom=1e-3

brake2.unitsMom='[m.kN]'
brake2.unitsForc='[kN]'
brake2.setsToDispBeamIntForc=[]
brake2.listBeamIntForc=['N','Qy','Mz']
brake2.scaleDispBeamIntForc=(0.02,0.05,-0.05)
brake2.viewName="XYZPos"
brake2.compElLoad='transComponent'
brake2.hCamFct=1

ELU01= graphical_reports.RecordLoadCaseDisp(loadCaseName='ELU01',loadCaseDescr='SIA 269 LM1 A',loadCaseExpr='1.2*GselfWeight+1.2*GdeadLoad+1.5*liveLoad269_1',setsToDispLoads=[],setsToDispDspRot=[deckSurfaces],setsToDispIntForc=[deckSurfaces])
ELU01.unitsScaleLoads=1e-3
ELU01.vectorScaleLoads=0.1
ELU01.unitsScaleDispl=1e3
ELU01.unitsDispl='[mm]'
ELU01.unitsScaleForc=1e-3
ELU01.unitsScaleMom=1e-3

ELU01.unitsMom='[m.kN]'
ELU01.unitsForc='[kN]'
ELU01.setsToDispBeamIntForc=[beamLines]
ELU01.listBeamIntForc=['N','Qy','Mz']
ELU01.scaleDispBeamIntForc=(0.02,0.05,-0.05)
ELU01.viewName="XYZPos"
ELU01.compElLoad='transComponent'
ELU01.hCamFct=1

ELU02= graphical_reports.RecordLoadCaseDisp(loadCaseName='ELU02',loadCaseDescr='SIA 269 LM1 B',loadCaseExpr='1.2*GselfWeight+1.2*GdeadLoad+1.5*liveLoad269_2',setsToDispLoads=[],setsToDispDspRot=[],setsToDispIntForc=[])
ELU02.unitsScaleLoads=1e-3
ELU02.vectorScaleLoads=0.1
ELU02.unitsScaleDispl=1e3
ELU02.unitsDispl='[mm]'
ELU02.unitsScaleForc=1e-3
ELU02.unitsScaleMom=1e-3

ELU02.unitsMom='[m.kN]'
ELU02.unitsForc='[kN]'
ELU02.setsToDispBeamIntForc=[beamLines]
ELU02.listBeamIntForc=['N','Qy','Mz']
ELU02.scaleDispBeamIntForc=(0.02,0.05,-0.05)
ELU02.viewName="XYZPos"
ELU02.compElLoad='transComponent'
ELU02.hCamFct=1

ELU03= graphical_reports.RecordLoadCaseDisp(loadCaseName='ELU03',loadCaseDescr='SIA 664 Crane LM1 A',loadCaseExpr='1.2*GselfWeight+1.2*GdeadLoad+1.1*liveLoad664Crane_1',setsToDispLoads=[],setsToDispDspRot=[deckSurfaces],setsToDispIntForc=[deckSurfaces])
ELU03.unitsScaleLoads=1e-3
ELU03.vectorScaleLoads=0.1
ELU03.unitsScaleDispl=1e3
ELU03.unitsDispl='[mm]'
ELU03.unitsScaleForc=1e-3
ELU03.unitsScaleMom=1e-3

ELU03.unitsMom='[m.kN]'
ELU03.unitsForc='[kN]'
ELU03.setsToDispBeamIntForc=[beamLines]
ELU03.listBeamIntForc=['N','Qy','Mz']
ELU03.scaleDispBeamIntForc=(0.02,0.05,-0.05)
ELU03.viewName="XYZPos"
ELU03.compElLoad='transComponent'
ELU03.hCamFct=1

ELU04= graphical_reports.RecordLoadCaseDisp(loadCaseName='ELU04',loadCaseDescr='SIA 664 Crane LM1 B',loadCaseExpr='1.2*GselfWeight+1.2*GdeadLoad+1.1*liveLoad664Crane_2',setsToDispLoads=[],setsToDispDspRot=[],setsToDispIntForc=[])
ELU04.unitsScaleLoads=1e-3
ELU04.vectorScaleLoads=0.1
ELU04.unitsScaleDispl=1e3
ELU04.unitsDispl='[mm]'
ELU04.unitsScaleForc=1e-3
ELU04.unitsScaleMom=1e-3

ELU04.unitsMom='[m.kN]'
ELU04.unitsForc='[kN]'
ELU04.setsToDispBeamIntForc=[beamLines]
ELU04.listBeamIntForc=['N','Qy','Mz']
ELU04.scaleDispBeamIntForc=(0.04,0.05,-0.05)
ELU04.viewName="XYZPos"
ELU04.compElLoad='transComponent'
ELU04.hCamFct=1

ELU05= graphical_reports.RecordLoadCaseDisp(loadCaseName='ELU05',loadCaseDescr='SIA 664 DET1 LM A',loadCaseExpr='1.2*GselfWeight+1.2*GdeadLoad+1.1*liveLoad664Det1_1',setsToDispLoads=[],setsToDispDspRot=[],setsToDispIntForc=[])
ELU05.unitsScaleLoads=1e-3
ELU05.vectorScaleLoads=0.1
ELU05.unitsScaleDispl=1e3
ELU05.unitsDispl='[mm]'
ELU05.unitsScaleForc=1e-3
ELU05.unitsScaleMom=1e-3

ELU05.unitsMom='[m.kN]'
ELU05.unitsForc='[kN]'
ELU05.setsToDispBeamIntForc=[beamLines]
ELU05.listBeamIntForc=['N','Qy','Mz']
ELU05.scaleDispBeamIntForc=(0.02,0.05,-0.05)
ELU05.viewName="XYZPos"
ELU05.compElLoad='transComponent'
ELU05.hCamFct=1

ELU06= graphical_reports.RecordLoadCaseDisp(loadCaseName='ELU06',loadCaseDescr='SIA 664 DET1 LM A',loadCaseExpr='1.2*GselfWeight+1.2*GdeadLoad+1.1*liveLoad664Det1_2',setsToDispLoads=[],setsToDispDspRot=[],setsToDispIntForc=[])
ELU06.unitsScaleLoads=1e-3
ELU06.vectorScaleLoads=0.1
ELU06.unitsScaleDispl=1e3
ELU06.unitsDispl='[mm]'
ELU06.unitsScaleForc=1e-3
ELU06.unitsScaleMom=1e-3

ELU06.unitsMom='[m.kN]'
ELU06.unitsForc='[kN]'
ELU06.setsToDispBeamIntForc=[beamLines]
ELU06.listBeamIntForc=['N','Qy','Mz']
ELU06.scaleDispBeamIntForc=(0.02,0.05,-0.05)
ELU06.viewName="XYZPos"
ELU06.compElLoad='transComponent'
ELU06.hCamFct=1

ELU07= graphical_reports.RecordLoadCaseDisp(loadCaseName='ELU07',loadCaseDescr='SIA 664 DET2 LM A',loadCaseExpr='1.2*GselfWeight+1.2*GdeadLoad+1.1*liveLoad664Det2_1',setsToDispLoads=[],setsToDispDspRot=[],setsToDispIntForc=[])
ELU07.unitsScaleLoads=1e-3
ELU07.vectorScaleLoads=0.1
ELU07.unitsScaleDispl=1e3
ELU07.unitsDispl='[mm]'
ELU07.unitsScaleForc=1e-3
ELU07.unitsScaleMom=1e-3

ELU07.unitsMom='[m.kN]'
ELU07.unitsForc='[kN]'
ELU07.setsToDispBeamIntForc=[beamLines]
ELU07.listBeamIntForc=['N','Qy','Mz']
ELU07.scaleDispBeamIntForc=(0.02,0.05,-0.05)
ELU07.viewName="XYZPos"
ELU07.compElLoad='transComponent'
ELU07.hCamFct=1

ELU08= graphical_reports.RecordLoadCaseDisp(loadCaseName='ELU08',loadCaseDescr='SIA 664 DET2 LM A',loadCaseExpr='1.2*GselfWeight+1.2*GdeadLoad+1.1*liveLoad664Det2_2',setsToDispLoads=[],setsToDispDspRot=[],setsToDispIntForc=[])
ELU08.unitsScaleLoads=1e-3
ELU08.vectorScaleLoads=0.1
ELU08.unitsScaleDispl=1e3
ELU08.unitsDispl='[mm]'
ELU08.unitsScaleForc=1e-3
ELU08.unitsScaleMom=1e-3

ELU08.unitsMom='[m.kN]'
ELU08.unitsForc='[kN]'
ELU08.setsToDispBeamIntForc=[beamLines]
ELU08.listBeamIntForc=['N','Qy','Mz']
ELU08.scaleDispBeamIntForc=(0.02,0.05,-0.05)
ELU08.viewName="XYZPos"
ELU08.compElLoad='transComponent'
ELU08.hCamFct=1

A= graphical_reports.RecordLoadCaseDisp(loadCaseName='A',loadCaseDescr='Earthquake load',loadCaseExpr='1.0*GselfWeight+1.0*GdeadLoad+1.0*eQuake',setsToDispLoads=[],setsToDispDspRot=[shells],setsToDispIntForc=[])
A.unitsScaleLoads=1e-3
A.vectorScaleLoads=0.1
A.unitsScaleDispl=1e3
A.unitsDispl='[mm]'
A.unitsScaleForc=1e-3
A.unitsScaleMom=1e-3

A.unitsMom='[m.kN]'
A.unitsForc='[kN]'
A.setsToDispBeamIntForc=[beamLines]
A.listBeamIntForc=['N','Qy','Mz']
A.scaleDispBeamIntForc=(0.02,0.05,-0.05)
A.viewName="XYZPos"
A.compElLoad='transComponent'
A.hCamFct=1


