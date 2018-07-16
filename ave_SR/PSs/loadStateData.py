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
setsIntF=[allLosas,murAlig,diafRP]
setsBeamIntF=[riostrEstr,pilas]

G1=graphical_reports.RecordLoadCaseDisp(loadCaseName='G1',loadCaseDescr='G1: peso propio',loadCaseExpr='1.0*G1',setsToDispLoads=[overallSet],setsToDispDspRot=[overallSet],setsToDispIntForc=setsIntF)
G1.unitsScaleLoads=1e-3
G1.vectorScaleLoads=0.20
G1.unitsScaleDispl=1e3
G1.unitsDispl='[mm]'
G1.unitsScaleMom=1e-3
G1.unitsMom='[m.kN]'
G1.unitsScaleForc=1e-3
G1.unitsForc='[kN]'
G1.viewName="XYZPos"
G1.hCamFct=1
G1.setsToDispBeamIntForc=setsBeamIntF
G1.listBeamIntForc=['N', 'My', 'Mz', 'Qy', 'Qz']
G1.scaleDispBeamIntForc=[0.001,0.01,0.01]

G2=graphical_reports.RecordLoadCaseDisp(loadCaseName='G2',loadCaseDescr='G2: carga muerta',loadCaseExpr='1.0*G2',setsToDispLoads=[overallSet],setsToDispDspRot=[overallSet],setsToDispIntForc=setsIntF)
G2.unitsScaleLoads=1e-3
G2.vectorScaleLoads=0.20
G2.unitsScaleDispl=1e3
G2.unitsDispl='[mm]'
G2.unitsScaleMom=1e-3
G2.unitsMom='[m.kN]'
G2.unitsScaleForc=1e-3
G2.unitsForc='[kN]'
G2.viewName="XYZPos"
G2.hCamFct=1
G2.setsToDispBeamIntForc=setsBeamIntF
G2.listBeamIntForc=['N', 'My', 'Mz', 'Qy', 'Qz']
G2.scaleDispBeamIntForc=[0.001,0.01,0.01]


G3=graphical_reports.RecordLoadCaseDisp(loadCaseName='G3',loadCaseDescr='G3: Retracción',loadCaseExpr='1.0*G3',setsToDispLoads=[],setsToDispDspRot=[overallSet],setsToDispIntForc=setsIntF)
G3.unitsScaleLoads=1e-3
G3.vectorScaleLoads=0.70
G3.unitsScaleDispl=1e3
G3.unitsDispl='[mm]'
G3.unitsScaleMom=1e-3
G3.unitsMom='[m.kN]'
G3.unitsScaleForc=1e-3
G3.unitsForc='[kN]'
G3.viewName="XYZNeg"
G3.hCamFct=1
G3.setsToDispBeamIntForc=setsBeamIntF
G3.listBeamIntForc=['N', 'My', 'Mz', 'Qy', 'Qz']
G3.scaleDispBeamIntForc=[0.001,0.01,0.01]

Q1a_1=graphical_reports.RecordLoadCaseDisp(loadCaseName='Q1a_1',loadCaseDescr='Q1a_1: tren de cargas, posición A1',loadCaseExpr='1.0*Q1a_1',setsToDispLoads=[overallSet],setsToDispDspRot=[overallSet],setsToDispIntForc=setsIntF)
Q1a_1.unitsScaleLoads=1e-3
Q1a_1.vectorScaleLoads=0.020
Q1a_1.unitsScaleDispl=1e3
Q1a_1.unitsDispl='[mm]'
Q1a_1.unitsScaleMom=1e-3
Q1a_1.unitsMom='[m.kN]'
Q1a_1.unitsScaleForc=1e-3
Q1a_1.unitsForc='[kN]'
Q1a_1.viewName="XYZPos"
Q1a_1.hCamFct=1
Q1a_1.setsToDispBeamIntForc=setsBeamIntF
Q1a_1.listBeamIntForc=['N', 'My', 'Mz', 'Qy', 'Qz']
Q1a_1.scaleDispBeamIntForc=[0.001,0.01,0.01]

Q1a_2=graphical_reports.RecordLoadCaseDisp(loadCaseName='Q1a_2',loadCaseDescr='Q1a_2: tren de cargas, posición A2',loadCaseExpr='1.0*Q1a_2',setsToDispLoads=[overallSet],setsToDispDspRot=[overallSet],setsToDispIntForc=setsIntF)
Q1a_2.unitsScaleLoads=1e-3
Q1a_2.vectorScaleLoads=0.020
Q1a_2.unitsScaleDispl=1e3
Q1a_2.unitsDispl='[mm]'
Q1a_2.unitsScaleMom=1e-3
Q1a_2.unitsMom='[m.kN]'
Q1a_2.unitsScaleForc=1e-3
Q1a_2.unitsForc='[kN]'
Q1a_2.viewName="XYZPos"
Q1a_2.hCamFct=1
Q1a_2.setsToDispBeamIntForc=setsBeamIntF
Q1a_2.listBeamIntForc=['N', 'My', 'Mz', 'Qy', 'Qz']
Q1a_2.scaleDispBeamIntForc=[0.001,0.01,0.01]

Q1b_1=graphical_reports.RecordLoadCaseDisp(loadCaseName='Q1b_1',loadCaseDescr='Q1b_1: tren de cargas, posición B1',loadCaseExpr='1.0*Q1b_1',setsToDispLoads=[overallSet],setsToDispDspRot=[overallSet],setsToDispIntForc=setsIntF)
Q1b_1.unitsScaleLoads=1e-3
Q1b_1.vectorScaleLoads=0.020
Q1b_1.unitsScaleDispl=1e3
Q1b_1.unitsDispl='[mm]'
Q1b_1.unitsScaleMom=1e-3
Q1b_1.unitsMom='[m.kN]'
Q1b_1.unitsScaleForc=1e-3
Q1b_1.unitsForc='[kN]'
Q1b_1.viewName="XYZPos"
Q1b_1.hCamFct=1
Q1b_1.setsToDispBeamIntForc=setsBeamIntF
Q1b_1.listBeamIntForc=['N', 'My', 'Mz', 'Qy', 'Qz']
Q1b_1.scaleDispBeamIntForc=[0.001,0.01,0.01]

Q1b_2=graphical_reports.RecordLoadCaseDisp(loadCaseName='Q1b_2',loadCaseDescr='Q1b_2: tren de cargas, posición B2',loadCaseExpr='1.0*Q1b_2',setsToDispLoads=[overallSet],setsToDispDspRot=[overallSet],setsToDispIntForc=setsIntF)
Q1b_2.unitsScaleLoads=1e-3
Q1b_2.vectorScaleLoads=0.020
Q1b_2.unitsScaleDispl=1e3
Q1b_2.unitsDispl='[mm]'
Q1b_2.unitsScaleMom=1e-3
Q1b_2.unitsMom='[m.kN]'
Q1b_2.unitsScaleForc=1e-3
Q1b_2.unitsForc='[kN]'
Q1b_2.viewName="XYZPos"
Q1b_2.hCamFct=1
Q1b_2.setsToDispBeamIntForc=setsBeamIntF
Q1b_2.listBeamIntForc=['N', 'My', 'Mz', 'Qy', 'Qz']
Q1b_2.scaleDispBeamIntForc=[0.001,0.01,0.01]

Q1c=graphical_reports.RecordLoadCaseDisp(loadCaseName='Q1c',loadCaseDescr='Q1c: tren de cargas, posición C',loadCaseExpr='1.0*Q1c',setsToDispLoads=[overallSet],setsToDispDspRot=[overallSet],setsToDispIntForc=setsIntF)
Q1c.unitsScaleLoads=1e-3
Q1c.vectorScaleLoads=0.020
Q1c.unitsScaleDispl=1e3
Q1c.unitsDispl='[mm]'
Q1c.unitsScaleMom=1e-3
Q1c.unitsMom='[m.kN]'
Q1c.unitsScaleForc=1e-3
Q1c.unitsForc='[kN]'
Q1c.viewName="XYZPos"
Q1c.hCamFct=1
Q1c.setsToDispBeamIntForc=setsBeamIntF
Q1c.listBeamIntForc=['N', 'My', 'Mz', 'Qy', 'Qz']
Q1c.scaleDispBeamIntForc=[0.001,0.01,0.01]

Q1d=graphical_reports.RecordLoadCaseDisp(loadCaseName='Q1d',loadCaseDescr='Q1d: tren de cargas, posición D',loadCaseExpr='1.0*Q1d',setsToDispLoads=[overallSet],setsToDispDspRot=[overallSet],setsToDispIntForc=setsIntF)
Q1d.unitsScaleLoads=1e-3
Q1d.vectorScaleLoads=0.020
Q1d.unitsScaleDispl=1e3
Q1d.unitsDispl='[mm]'
Q1d.unitsScaleMom=1e-3
Q1d.unitsMom='[m.kN]'
Q1d.unitsScaleForc=1e-3
Q1d.unitsForc='[kN]'
Q1d.viewName="XYZPos"
Q1d.hCamFct=1
Q1d.setsToDispBeamIntForc=setsBeamIntF
Q1d.listBeamIntForc=['N', 'My', 'Mz', 'Qy', 'Qz']
Q1d.scaleDispBeamIntForc=[0.001,0.01,0.01]

Q1e=graphical_reports.RecordLoadCaseDisp(loadCaseName='Q1e',loadCaseDescr='Q1e: tren de cargas, posición E',loadCaseExpr='1.0*Q1e',setsToDispLoads=[overallSet],setsToDispDspRot=[overallSet],setsToDispIntForc=setsIntF)
Q1e.unitsScaleLoads=1e-3
Q1e.vectorScaleLoads=0.020
Q1e.unitsScaleDispl=1e3
Q1e.unitsDispl='[mm]'
Q1e.unitsScaleMom=1e-3
Q1e.unitsMom='[m.kN]'
Q1e.unitsScaleForc=1e-3
Q1e.unitsForc='[kN]'
Q1e.viewName="XYZPos"
Q1e.hCamFct=1
Q1e.setsToDispBeamIntForc=setsBeamIntF
Q1e.listBeamIntForc=['N', 'My', 'Mz', 'Qy', 'Qz']
Q1e.scaleDispBeamIntForc=[0.001,0.01,0.01]

Q1f=graphical_reports.RecordLoadCaseDisp(loadCaseName='Q1f',loadCaseDescr='Q1f: tren de cargas, posición F',loadCaseExpr='1.0*Q1f',setsToDispLoads=[overallSet],setsToDispDspRot=[overallSet],setsToDispIntForc=setsIntF)
Q1f.unitsScaleLoads=1e-3
Q1f.vectorScaleLoads=0.020
Q1f.unitsScaleDispl=1e3
Q1f.unitsDispl='[mm]'
Q1f.unitsScaleMom=1e-3
Q1f.unitsMom='[m.kN]'
Q1f.unitsScaleForc=1e-3
Q1f.unitsForc='[kN]'
Q1f.viewName="XYZPos"
Q1f.hCamFct=1
Q1f.setsToDispBeamIntForc=setsBeamIntF
Q1f.listBeamIntForc=['N', 'My', 'Mz', 'Qy', 'Qz']
Q1f.scaleDispBeamIntForc=[0.001,0.01,0.01]



Q1b_fren=graphical_reports.RecordLoadCaseDisp(loadCaseName='Q1b_fren',loadCaseDescr='Q1b_fren: tren de cargas, posición B1+frenado',loadCaseExpr='1.0*Q1b_fren',setsToDispLoads=[overallSet],setsToDispDspRot=[overallSet],setsToDispIntForc=setsIntF)
Q1b_fren.unitsScaleLoads=1e-3
Q1b_fren.vectorScaleLoads=0.020
Q1b_fren.unitsScaleDispl=1e3
Q1b_fren.unitsDispl='[mm]'
Q1b_fren.unitsScaleMom=1e-3
Q1b_fren.unitsMom='[m.kN]'
Q1b_fren.unitsScaleForc=1e-3
Q1b_fren.unitsForc='[kN]'
Q1b_fren.viewName="XYZPos"
Q1b_fren.hCamFct=1
Q1b_fren.setsToDispBeamIntForc=setsBeamIntF
Q1b_fren.listBeamIntForc=['N', 'My', 'Mz', 'Qy', 'Qz']
Q1b_fren.scaleDispBeamIntForc=[0.001,0.01,0.01]

Q1d_fren=graphical_reports.RecordLoadCaseDisp(loadCaseName='Q1d_fren',loadCaseDescr='Q1d_fren: tren de cargas, posición D+frenado',loadCaseExpr='1.0*Q1d_fren',setsToDispLoads=[overallSet],setsToDispDspRot=[overallSet],setsToDispIntForc=setsIntF)
Q1d_fren.unitsScaleLoads=1e-3
Q1d_fren.vectorScaleLoads=0.020
Q1d_fren.unitsScaleDispl=1e3
Q1d_fren.unitsDispl='[mm]'
Q1d_fren.unitsScaleMom=1e-3
Q1d_fren.unitsMom='[m.kN]'
Q1d_fren.unitsScaleForc=1e-3
Q1d_fren.unitsForc='[kN]'
Q1d_fren.viewName="XYZPos"
Q1d_fren.hCamFct=1
Q1d_fren.setsToDispBeamIntForc=setsBeamIntF
Q1d_fren.listBeamIntForc=['N', 'My', 'Mz', 'Qy', 'Qz']
Q1d_fren.scaleDispBeamIntForc=[0.001,0.01,0.01]

Q1e_fren=graphical_reports.RecordLoadCaseDisp(loadCaseName='Q1e_fren',loadCaseDescr='Q1e_fren: tren de cargas, posición E+frenado',loadCaseExpr='1.0*Q1e_fren',setsToDispLoads=[overallSet],setsToDispDspRot=[overallSet],setsToDispIntForc=setsIntF)
Q1e_fren.unitsScaleLoads=1e-3
Q1e_fren.vectorScaleLoads=0.020
Q1e_fren.unitsScaleDispl=1e3
Q1e_fren.unitsDispl='[mm]'
Q1e_fren.unitsScaleMom=1e-3
Q1e_fren.unitsMom='[m.kN]'
Q1e_fren.unitsScaleForc=1e-3
Q1e_fren.unitsForc='[kN]'
Q1e_fren.viewName="XYZPos"
Q1e_fren.hCamFct=1
Q1e_fren.setsToDispBeamIntForc=setsBeamIntF
Q1e_fren.listBeamIntForc=['N', 'My', 'Mz', 'Qy', 'Qz']
Q1e_fren.scaleDispBeamIntForc=[0.001,0.01,0.01]


Q2_1=graphical_reports.RecordLoadCaseDisp(loadCaseName='Q2_1',loadCaseDescr='Q2_1: viento aislado',loadCaseExpr='1.0*Q2_1',setsToDispLoads=[overallSet],setsToDispDspRot=[overallSet],setsToDispIntForc=setsIntF)
Q2_1.unitsScaleLoads=1e-3
Q2_1.vectorScaleLoads=0.70
Q2_1.unitsScaleDispl=1e3
Q2_1.unitsDispl='[mm]'
Q2_1.unitsScaleMom=1e-3
Q2_1.unitsMom='[m.kN]'
Q2_1.unitsScaleForc=1e-3
Q2_1.unitsForc='[kN]'
Q2_1.viewName="XYZNeg"
Q2_1.hCamFct=1
Q2_1.setsToDispBeamLoads=setsBeamIntF
Q2_1.listBeamIntForc=['N', 'My', 'Mz', 'Qy', 'Qz']
Q2_1.scaleDispBeamIntForc=[0.001,0.01,0.01]


Q2_2=graphical_reports.RecordLoadCaseDisp(loadCaseName='Q2_2',loadCaseDescr='Q2_2: viento con SC uso',loadCaseExpr='1.0*Q2_2',setsToDispLoads=[overallSet],setsToDispDspRot=[overallSet],setsToDispIntForc=setsIntF)
Q2_2.unitsScaleLoads=1e-3
Q2_2.vectorScaleLoads=0.70
Q2_2.unitsScaleDispl=1e3
Q2_2.unitsDispl='[mm]'
Q2_2.unitsScaleMom=1e-3
Q2_2.unitsMom='[m.kN]'
Q2_2.unitsScaleForc=1e-3
Q2_2.unitsForc='[kN]'
Q2_2.viewName="XYZNeg"
Q2_2.hCamFct=1
Q2_2.setsToDispBeamLoads=setsBeamIntF
Q2_2.listBeamIntForc=['N', 'My', 'Mz', 'Qy', 'Qz']
Q2_2.scaleDispBeamIntForc=[0.001,0.01,0.01]

Q3_1=graphical_reports.RecordLoadCaseDisp(loadCaseName='Q3_1',loadCaseDescr='Q3_1: Temperatura uniforme, contracción',loadCaseExpr='1.0*Q3_1',setsToDispLoads=[],setsToDispDspRot=[overallSet],setsToDispIntForc=setsIntF)
Q3_1.unitsScaleLoads=1e-3
Q3_1.vectorScaleLoads=0.70
Q3_1.unitsScaleDispl=1e3
Q3_1.unitsDispl='[mm]'
Q3_1.unitsScaleMom=1e-3
Q3_1.unitsMom='[m.kN]'
Q3_1.unitsScaleForc=1e-3
Q3_1.unitsForc='[kN]'
Q3_1.viewName="XYZNeg"
Q3_1.hCamFct=1
Q3_1.setsToDispBeamLoads=setsBeamIntF
Q3_1.listBeamIntForc=['N', 'My', 'Mz', 'Qy', 'Qz']
Q3_1.scaleDispBeamIntForc=[0.001,0.01,0.01]

Q3_2=graphical_reports.RecordLoadCaseDisp(loadCaseName='Q3_2',loadCaseDescr='Q3_2: Temperatura uniforme, dilatación',loadCaseExpr='1.0*Q3_2',setsToDispLoads=[],setsToDispDspRot=[overallSet],setsToDispIntForc=setsIntF)
Q3_2.unitsScaleLoads=1e-3
Q3_2.vectorScaleLoads=0.70
Q3_2.unitsScaleDispl=1e3
Q3_2.unitsDispl='[mm]'
Q3_2.unitsScaleMom=1e-3
Q3_2.unitsMom='[m.kN]'
Q3_2.unitsScaleForc=1e-3
Q3_2.unitsForc='[kN]'
Q3_2.viewName="XYZNeg"
Q3_2.hCamFct=1
Q3_2.setsToDispBeamLoads=setsBeamIntF
Q3_2.listBeamIntForc=['N', 'My', 'Mz', 'Qy', 'Qz']
Q3_2.scaleDispBeamIntForc=[0.001,0.01,0.01]

Q3_3=graphical_reports.RecordLoadCaseDisp(loadCaseName='Q3_3',loadCaseDescr='Q3_3: Diferencia temperatura, fibra sup. más caliente',loadCaseExpr='1.0*Q3_3',setsToDispLoads=[],setsToDispDspRot=[overallSet],setsToDispIntForc=setsIntF)
Q3_3.unitsScaleLoads=1e-3
Q3_3.vectorScaleLoads=0.70
Q3_3.unitsScaleDispl=1e3
Q3_3.unitsDispl='[mm]'
Q3_3.unitsScaleMom=1e-3
Q3_3.unitsMom='[m.kN]'
Q3_3.unitsScaleForc=1e-3
Q3_3.unitsForc='[kN]'
Q3_3.viewName="XYZNeg"
Q3_3.hCamFct=1
Q3_3.setsToDispBeamLoads=setsBeamIntF
Q3_3.listBeamIntForc=['N', 'My', 'Mz', 'Qy', 'Qz']
Q3_3.scaleDispBeamIntForc=[0.001,0.01,0.01]

Q3_4=graphical_reports.RecordLoadCaseDisp(loadCaseName='Q3_4',loadCaseDescr='Q3_4: Diferencia temperatura, fibra sup. más fría',loadCaseExpr='1.0*Q3_4',setsToDispLoads=[],setsToDispDspRot=[overallSet],setsToDispIntForc=setsIntF)
Q3_4.unitsScaleLoads=1e-3
Q3_4.vectorScaleLoads=0.70
Q3_4.unitsScaleDispl=1e3
Q3_4.unitsDispl='[mm]'
Q3_4.unitsScaleMom=1e-3
Q3_4.unitsMom='[m.kN]'
Q3_4.unitsScaleForc=1e-3
Q3_4.unitsForc='[kN]'
Q3_4.viewName="XYZNeg"
Q3_4.hCamFct=1
Q3_4.setsToDispBeamLoads=setsBeamIntF
Q3_4.listBeamIntForc=['N', 'My', 'Mz', 'Qy', 'Qz']
Q3_4.scaleDispBeamIntForc=[0.001,0.01,0.01]


Q3_1_neopr=graphical_reports.RecordLoadCaseDisp(loadCaseName='Q3_1_neopr',loadCaseDescr='Q3_1_neopr: Temperatura uniforme, contracción',loadCaseExpr='1.0*Q3_1_neopr',setsToDispLoads=[],setsToDispDspRot=[overallSet],setsToDispIntForc=setsIntF)
Q3_1_neopr.unitsScaleLoads=1e-3
Q3_1_neopr.vectorScaleLoads=0.70
Q3_1_neopr.unitsScaleDispl=1e3
Q3_1_neopr.unitsDispl='[mm]'
Q3_1_neopr.unitsScaleMom=1e-3
Q3_1_neopr.unitsMom='[m.kN]'
Q3_1_neopr.unitsScaleForc=1e-3
Q3_1_neopr.unitsForc='[kN]'
Q3_1_neopr.viewName="XYZNeg"
Q3_1_neopr.hCamFct=1

Q3_2_neopr=graphical_reports.RecordLoadCaseDisp(loadCaseName='Q3_2_neopr',loadCaseDescr='Q3_2_neopr: Temperatura uniforme, dilatación',loadCaseExpr='1.0*Q3_2_neopr',setsToDispLoads=[],setsToDispDspRot=[overallSet],setsToDispIntForc=setsIntF)
Q3_2_neopr.unitsScaleLoads=1e-3
Q3_2_neopr.vectorScaleLoads=0.70
Q3_2_neopr.unitsScaleDispl=1e3
Q3_2_neopr.unitsDispl='[mm]'
Q3_2_neopr.unitsScaleMom=1e-3
Q3_2_neopr.unitsMom='[m.kN]'
Q3_2_neopr.unitsScaleForc=1e-3
Q3_2_neopr.unitsForc='[kN]'
Q3_2_neopr.viewName="XYZNeg"
Q3_2_neopr.hCamFct=1

resLoadCases=[G1,G2,G3,Q1a_1,Q1a_2,Q1b_1,Q1b_2,Q1c,Q1d,Q1e,Q1f,Q1b_fren,Q1e_fren,Q1d_fren,Q2_1,Q2_2,Q3_1,Q3_2,Q3_3,Q3_4]
resLoadCases_neopr=[G1,G2,G3,Q1a_1,Q1a_2,Q1b_1,Q1b_2,Q1c,Q1d,Q1e,Q1f,Q1b_fren,Q1e_fren,Q1d_fren,Q2_1,Q2_2,Q3_1,Q3_2,Q3_3,Q3_4,Q3_1_neopr,Q3_2_neopr]
