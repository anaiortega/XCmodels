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
G1=graphical_reports.RecordLoadCaseDisp(loadCaseName='GselfWeight',loadCaseDescr='G1: self weight',loadCaseExpr='1.0*GselfWeight',setsToDispLoads=[shells],setsToDispDspRot=[shells],setsToDispIntForc=[overallSet])
G1.unitsScaleLoads=1e-3
G1.unitsScaleForc=1e-3
G1.unitsScaleMom=1e-3
G1.unitsScaleDispl=1e3
G1.unitsDispl='[mm]'

G2=graphical_reports.RecordLoadCaseDisp(loadCaseName='GdeadLoad',loadCaseDescr='G2: dead load',loadCaseExpr='1.0*GdeadLoad',setsToDispLoads=[shells],setsToDispDspRot=[shells],setsToDispIntForc=[overallSet])
G2.unitsScaleLoads=1e-3
G2.unitsScaleForc=1e-3
G2.unitsScaleMom=1e-3
G2.unitsScaleDispl=1e3
G2.unitsDispl='[mm]'

QA=graphical_reports.RecordLoadCaseDisp(loadCaseName='QliveLoadA',loadCaseDescr='QA: live load A',loadCaseExpr='1.0*QliveLoadA',setsToDispLoads=[shells],setsToDispDspRot=[shells],setsToDispIntForc=[overallSet])
QA.unitsScaleLoads=1e-3
QA.unitsScaleForc=1e-3
QA.unitsScaleMom=1e-3
QA.unitsScaleDispl=1e3
QA.unitsDispl='[mm]'

QB=graphical_reports.RecordLoadCaseDisp(loadCaseName='QliveLoadB',loadCaseDescr='QB: live load B',loadCaseExpr='1.0*QliveLoadB',setsToDispLoads=[shells],setsToDispDspRot=[shells],setsToDispIntForc=[overallSet])
QB.unitsScaleLoads=1e-3
QB.unitsScaleForc=1e-3
QB.unitsScaleMom=1e-3
QB.unitsScaleDispl=1e3
QB.unitsDispl='[mm]'

QF=graphical_reports.RecordLoadCaseDisp(loadCaseName='QfatigueLoad',loadCaseDescr='QF: fatigue load',loadCaseExpr='1.0*QfatigueLoad',setsToDispLoads=[shells],setsToDispDspRot=[shells],setsToDispIntForc=[overallSet])
QF.unitsScaleLoads=1e-3
QF.unitsScaleForc=1e-3
QF.unitsScaleMom=1e-3
QF.unitsScaleDispl=1e3
QF.unitsDispl='[mm]'

QAcc=graphical_reports.RecordLoadCaseDisp(loadCaseName='Qaccidental',loadCaseDescr='QAcc: accidental',loadCaseExpr='1.0*Qaccidental',setsToDispLoads=[shells],setsToDispDspRot=[shells],setsToDispIntForc=[overallSet])
QAcc.unitsScaleLoads=1e-3
QAcc.unitsScaleForc=1e-3
QAcc.unitsScaleMom=1e-3
QAcc.unitsScaleDispl=1e3
QAcc.unitsDispl='[mm]'

# ULS
ULS_A=graphical_reports.RecordLoadCaseDisp(loadCaseName='ULS_A',loadCaseDescr='ULS_A: ultimate limit state A',loadCaseExpr='1.35*GselfWeight+1.35*GdeadLoad+1.5*QliveLoadA',setsToDispLoads=[shells],setsToDispDspRot=[shells],setsToDispIntForc=[overallSet])
ULS_A.unitsScaleLoads=1e-3
ULS_A.unitsScaleForc=1e-3
ULS_A.unitsScaleMom=1e-3
ULS_A.unitsScaleDispl=1e3
ULS_A.unitsDispl='[mm]'

ULS_B=graphical_reports.RecordLoadCaseDisp(loadCaseName='ULS_B',loadCaseDescr='ULS_B: ultimate limit state B',loadCaseExpr='1.35*GselfWeight+1.35*GdeadLoad+1.5*QliveLoadB',setsToDispLoads=[shells],setsToDispDspRot=[shells],setsToDispIntForc=[overallSet])
ULS_B.unitsScaleLoads=1e-3
ULS_B.unitsScaleForc=1e-3
ULS_B.unitsScaleMom=1e-3
ULS_B.unitsScaleDispl=1e3
ULS_B.unitsDispl='[mm]'

ULS_Acc=graphical_reports.RecordLoadCaseDisp(loadCaseName='ULS_Acc',loadCaseDescr='ULS_Acc: ultimate limit state Accidental',loadCaseExpr='1.00*GselfWeight+1.00*GdeadLoad+1.00*Qaccidental',setsToDispLoads=[shells],setsToDispDspRot=[shells],setsToDispIntForc=[overallSet])
ULS_Acc.unitsScaleLoads=1e-3
ULS_Acc.unitsScaleForc=1e-3
ULS_Acc.unitsScaleMom=1e-3
ULS_Acc.unitsScaleDispl=1e3
ULS_Acc.unitsDispl='[mm]'

#For loads display
QA_unif=graphical_reports.RecordLoadCaseDisp(loadCaseName='QliveLoadA_unif',loadCaseDescr='QA: live load A_unif',loadCaseExpr='1.0*QliveLoadA_unif',setsToDispLoads=[shells],setsToDispDspRot=[shells],setsToDispIntForc=[])
QA_unif.unitsScaleLoads=1e-3
QA_unif.unitsScaleForc=1e-3
QA_unif.unitsScaleMom=1e-3
QA_unif.unitsScaleDispl=1e3
QA_unif.unitsDispl='[mm]'


QB_unif=graphical_reports.RecordLoadCaseDisp(loadCaseName='QliveLoadB_unif',loadCaseDescr='QB: live load B_unif',loadCaseExpr='1.0*QliveLoadB_unif',setsToDispLoads=[shells],setsToDispDspRot=[shells],setsToDispIntForc=[])
QB_unif.unitsScaleLoads=1e-3
QB_unif.unitsScaleForc=1e-3
QB_unif.unitsScaleMom=1e-3
QB_unif.unitsScaleDispl=1e3
QB_unif.unitsDispl='[mm]'

QF_unif=graphical_reports.RecordLoadCaseDisp(loadCaseName='QfatigueLoad_unif',loadCaseDescr='QF: fatigue load_unif',loadCaseExpr='1.0*QfatigueLoad_unif',setsToDispLoads=[shells],setsToDispDspRot=[shells],setsToDispIntForc=[])
QF_unif.unitsScaleLoads=1e-3
QF_unif.unitsScaleForc=1e-3
QF_unif.unitsScaleMom=1e-3
QF_unif.unitsScaleDispl=1e3
QF_unif.unitsDispl='[mm]'


QAcc_unif=graphical_reports.RecordLoadCaseDisp(loadCaseName='Qaccidental_unif',loadCaseDescr='QAcc: accidental_unif',loadCaseExpr='1.0*Qaccidental_unif',setsToDispLoads=[shells],setsToDispDspRot=[shells],setsToDispIntForc=[])
QAcc_unif.unitsScaleLoads=1e-3
QAcc_unif.unitsScaleForc=1e-3
QAcc_unif.unitsScaleMom=1e-3
QAcc_unif.unitsScaleDispl=1e3
QAcc_unif.unitsDispl='[mm]'


QA_point=graphical_reports.RecordLoadCaseDisp(loadCaseName='QliveLoadA_point',loadCaseDescr='QA: live load A_point',loadCaseExpr='1.0*QliveLoadA_point',setsToDispLoads=[shells],setsToDispDspRot=[shells],setsToDispIntForc=[])
QA_point.vectorScaleLoads=2e-2
QA_point.unitsScaleLoads=1e-3
QA_point.unitsScaleForc=1e-3
QA_point.unitsScaleMom=1e-3
QA_point.unitsScaleDispl=1e3
QA_point.unitsDispl='[mm]'

QB_point=graphical_reports.RecordLoadCaseDisp(loadCaseName='QliveLoadB_point',loadCaseDescr='QB: live load B_point',loadCaseExpr='1.0*QliveLoadB_point',setsToDispLoads=[shells],setsToDispDspRot=[shells],setsToDispIntForc=[])
QB_point.vectorScaleLoads=2e-2
QB_point.unitsScaleLoads=1e-3
QB_point.unitsScaleForc=1e-3
QB_point.unitsScaleMom=1e-3
QB_point.unitsScaleDispl=1e3
QB_point.unitsDispl='[mm]'

QF_point=graphical_reports.RecordLoadCaseDisp(loadCaseName='QfatigueLoad_point',loadCaseDescr='QF: fatigue load_point',loadCaseExpr='1.0*QfatigueLoad_point',setsToDispLoads=[shells],setsToDispDspRot=[shells],setsToDispIntForc=[])
QF_point.vectorScaleLoads=2e-2
QF_point.unitsScaleLoads=1e-3
QF_point.unitsScaleForc=1e-3
QF_point.unitsScaleMom=1e-3
QF_point.unitsScaleDispl=1e3
QF_point.unitsDispl='[mm]'

QAcc_point=graphical_reports.RecordLoadCaseDisp(loadCaseName='Qaccidental_point',loadCaseDescr='QAcc: accidental_point',loadCaseExpr='1.0*Qaccidental_point',setsToDispLoads=[shells],setsToDispDspRot=[shells],setsToDispIntForc=[overallSet])
QAcc_point.vectorScaleLoads=2e-2
QAcc_point.unitsScaleLoads=1e-3
QAcc_point.unitsScaleForc=1e-3
QAcc_point.unitsScaleMom=1e-3
QAcc_point.unitsScaleDispl=1e3
QAcc_point.unitsDispl='[mm]'
