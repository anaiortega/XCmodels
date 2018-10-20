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
G1=graphical_reports.RecordLoadCaseDisp(loadCaseName='G1',loadCaseDescr='G1: Peso propio',loadCaseExpr='1.0*G1',setsToDispLoads=[overallSet],setsToDispDspRot=[overallSet],setsToDispIntForc=[losas_M1M2,hastIzq_M1M2])
G1.unitsScaleLoads=1e-3
G1.unitsScaleDispl=1e3
G1.unitsDispl='[mm]'
G1.unitsScaleMom=1e-3
G1.unitsMom='[m.kN]'
G1.unitsScaleForc=1e-3
G1.unitsForc='[kN]'
G1.viewName="XYZPos"
G1.hCamFct=1

G2a=graphical_reports.RecordLoadCaseDisp(loadCaseName='G2a',loadCaseDescr='G2a: Carga muerta en servicio',loadCaseExpr='1.0*G2a',setsToDispLoads=[overallSet],setsToDispDspRot=[overallSet],setsToDispIntForc=[losas_M1M2,hastIzq_M1M2])
G2a.unitsScaleLoads=1e-3
G2a.unitsScaleDispl=1e3
G2a.unitsDispl='[mm]'
G2a.unitsScaleMom=1e-3
G2a.unitsMom='[m.kN]'
G2a.unitsScaleForc=1e-3
G2a.unitsForc='[kN]'
G2a.viewName="XYZPos"
G2a.hCamFct=1

G2b=graphical_reports.RecordLoadCaseDisp(loadCaseName='G2b',loadCaseDescr='G2b: Carga muerta desbalastado 1',loadCaseExpr='1.0*G2b',setsToDispLoads=[overallSet],setsToDispDspRot=[overallSet],setsToDispIntForc=[losas_M1M2,hastIzq_M1M2])
G2b.unitsScaleLoads=1e-3
G2b.unitsScaleDispl=1e3
G2b.unitsDispl='[mm]'
G2b.unitsScaleMom=1e-3
G2b.unitsMom='[m.kN]'
G2b.unitsScaleForc=1e-3
G2b.unitsForc='[kN]'
G2b.viewName="XYZPos"
G2b.hCamFct=1

G2c=graphical_reports.RecordLoadCaseDisp(loadCaseName='G2c',loadCaseDescr='G2c: Carga muerta desbalastado 2',loadCaseExpr='1.0*G2c',setsToDispLoads=[overallSet],setsToDispDspRot=[overallSet],setsToDispIntForc=[losas_M1M2,hastIzq_M1M2])
G2c.unitsScaleLoads=1e-3
G2c.unitsScaleDispl=1e3
G2c.unitsDispl='[mm]'
G2c.unitsScaleMom=1e-3
G2c.unitsMom='[m.kN]'
G2c.unitsScaleForc=1e-3
G2c.unitsForc='[kN]'
G2c.viewName="XYZPos"
G2c.hCamFct=1

G3=graphical_reports.RecordLoadCaseDisp(loadCaseName='G3',loadCaseDescr='G3: Empuje del terreno',loadCaseExpr='1.0*G3',setsToDispLoads=[overallSet],setsToDispDspRot=[overallSet],setsToDispIntForc=[losas_M1M2,hastIzq_M1M2])
G3.unitsScaleLoads=1e-3
G3.unitsScaleDispl=1e3
G3.unitsDispl='[mm]'
G3.unitsScaleMom=1e-3
G3.unitsMom='[m.kN]'
G3.unitsScaleForc=1e-3
G3.unitsForc='[kN]'
G3.viewName="XYZPos"
G3.hCamFct=1

Q1a=graphical_reports.RecordLoadCaseDisp(loadCaseName='Q1a',loadCaseDescr='Q1a: Tren de cargas posición 1',loadCaseExpr='1.0*Q1a',setsToDispLoads=[overallSet],setsToDispDspRot=[overallSet],setsToDispIntForc=[losas_M1M2,hastIzq_M1M2])
Q1a.unitsScaleLoads=1e-3
Q1a.unitsScaleDispl=1e3
Q1a.unitsDispl='[mm]'
Q1a.unitsScaleMom=1e-3
Q1a.unitsMom='[m.kN]'
Q1a.unitsScaleForc=1e-3
Q1a.unitsForc='[kN]'
Q1a.viewName="XYZPos"
Q1a.hCamFct=1

Q1a_1via=graphical_reports.RecordLoadCaseDisp(loadCaseName='Q1a_1via',loadCaseDescr='Q1a_1via: Tren de cargas posición 1 en sit. desbalastado',loadCaseExpr='1.0*Q1a_1via',setsToDispLoads=[overallSet],setsToDispDspRot=[overallSet],setsToDispIntForc=[losas_M1M2,hastIzq_M1M2])
Q1a_1via.unitsScaleLoads=1e-3
Q1a_1via.unitsScaleDispl=1e3
Q1a_1via.unitsDispl='[mm]'
Q1a_1via.unitsScaleMom=1e-3
Q1a_1via.unitsMom='[m.kN]'
Q1a_1via.unitsScaleForc=1e-3
Q1a_1via.unitsForc='[kN]'
Q1a_1via.viewName="XYZPos"
Q1a_1via.hCamFct=1

Q1b=graphical_reports.RecordLoadCaseDisp(loadCaseName='Q1b',loadCaseDescr='Q1b: Tren de cargas posición 2',loadCaseExpr='1.0*Q1b',setsToDispLoads=[overallSet],setsToDispDspRot=[overallSet],setsToDispIntForc=[losas_M1M2,hastIzq_M1M2])
Q1b.unitsScaleLoads=1e-3
Q1b.unitsScaleDispl=1e3
Q1b.unitsDispl='[mm]'
Q1b.unitsScaleMom=1e-3
Q1b.unitsMom='[m.kN]'
Q1b.unitsScaleForc=1e-3
Q1b.unitsForc='[kN]'
Q1b.viewName="+X-Y+Z"
Q1b.hCamFct=1

Q1c=graphical_reports.RecordLoadCaseDisp(loadCaseName='Q1c',loadCaseDescr='Q1c: Tren de cargas posición 3',loadCaseExpr='1.0*Q1c',setsToDispLoads=[overallSet],setsToDispDspRot=[overallSet],setsToDispIntForc=[losas_M1M2,hastIzq_M1M2])
Q1c.unitsScaleLoads=1e-3
Q1c.unitsScaleDispl=1e3
Q1c.unitsDispl='[mm]'
Q1c.unitsScaleMom=1e-3
Q1c.unitsMom='[m.kN]'
Q1c.unitsScaleForc=1e-3
Q1c.unitsForc='[kN]'
Q1c.viewName="+X-Y+Z"
Q1c.hCamFct=1

Q2b=graphical_reports.RecordLoadCaseDisp(loadCaseName='Q2b',loadCaseDescr='Q2b: SC paso fauna y nivel agua',loadCaseExpr='1.0*Q2b',setsToDispLoads=[overallSet],setsToDispDspRot=[overallSet],setsToDispIntForc=[losas_M1M2,hastIzq_M1M2])
Q2b.unitsScaleLoads=1e-3
Q2b.unitsScaleDispl=1e3
Q2b.unitsDispl='[mm]'
Q2b.unitsScaleMom=1e-3
Q2b.unitsMom='[m.kN]'
Q2b.unitsScaleForc=1e-3
Q2b.unitsForc='[kN]'
Q2b.viewName="XYZPos"
Q2b.hCamFct=1

A1a=graphical_reports.RecordLoadCaseDisp(loadCaseName='A1a',loadCaseDescr='A1a: Descarrilamiento situación 1',loadCaseExpr='1.0*A1a',setsToDispLoads=[overallSet],setsToDispDspRot=[overallSet],setsToDispIntForc=[losas_M1M2,hastIzq_M1M2])
A1a.unitsScaleLoads=1e-3
A1a.unitsScaleDispl=1e3
A1a.unitsDispl='[mm]'
A1a.unitsScaleMom=1e-3
A1a.unitsMom='[m.kN]'
A1a.unitsScaleForc=1e-3
A1a.unitsForc='[kN]'
Q1c.viewName="XYZPos"
A1a.hCamFct=1

A1b=graphical_reports.RecordLoadCaseDisp(loadCaseName='A1b',loadCaseDescr='A1b: Descarrilamiento situación 2',loadCaseExpr='1.0*A1b',setsToDispLoads=[overallSet],setsToDispDspRot=[overallSet],setsToDispIntForc=[losas_M1M2,hastIzq_M1M2])
A1b.unitsScaleLoads=1e-3
A1b.unitsScaleDispl=1e3
A1b.unitsDispl='[mm]'
A1b.unitsScaleMom=1e-3
A1b.unitsMom='[m.kN]'
A1b.unitsScaleForc=1e-3
A1b.unitsForc='[kN]'
A1b.viewName="XYZPos"
A1b.hCamFct=1

C1=graphical_reports.RecordLoadCaseDisp(loadCaseName='C1',loadCaseDescr='C1: Empuje del terreno (construcción)',loadCaseExpr='1.0*C1',setsToDispLoads=[overallSet],setsToDispDspRot=[overallSet],setsToDispIntForc=[losas_M1M2,hastIzq_M1M2])
C1.unitsScaleLoads=1e-3
C1.unitsScaleDispl=1e3
C1.unitsDispl='[mm]'
C1.unitsScaleMom=1e-3
C1.unitsMom='[m.kN]'
C1.unitsScaleForc=1e-3
C1.unitsForc='[kN]'
C1.viewName="+X-Y+Z"
C1.hCamFct=1
