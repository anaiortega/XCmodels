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
  unitsScaleLoads: factor to apply to loads if we want to change
                 the units (defaults to 1).
  unitsLoads: text to especify the units in which loads are 
                 represented (defaults to 'units:[m,kN]')
  vectorScaleLoads: factor to apply to the vectors length in the 
                 representation of loads (defaults to 1 -> auto-scale).
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
  listIntForc: ordered list of internal forces to be displayed
                 available components: 'N1', 'N2', 'M1', 'M2', 'Q1', 'Q2'
                 (defaults to ['N1', 'N2', 'M1', 'M2', 'Q1', 'Q2'])
  setsToDispIntForc: ordered list of sets of elements to display internal      
                 forces 
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

'''



G1=graphical_reports.RecordLoadCaseDisp(loadCaseName='GselfWeight',loadCaseDescr='G1: Poids propre',loadCaseExpr='1.0*GselfWeight',setsToDispLoads=[overallSet],setsToDispDspRot=[foundDeck,walls],setsToDispIntForc=[foundDeck,walls])
G1.unitsScaleLoads=1e-3
G1.unitsScaleDispl=1e3
G1.unitsDispl='[mm]'
G1.unitsScaleForc=1e-3
G1.unitsScaleMom=1e-3

G2=graphical_reports.RecordLoadCaseDisp(loadCaseName='GdeadLoad',loadCaseDescr='G2: Poids propre non porteur',loadCaseExpr='1.0*GdeadLoad',setsToDispLoads=[overallSet],setsToDispDspRot=[foundDeck,walls],setsToDispIntForc=[foundDeck,walls])
#G2.setToDisplay=foundation
G2.unitsScaleLoads=1e-3
G2.unitsScaleDispl=1e3
G2.unitsDispl='[mm]'
G2.unitsScaleForc=1e-3
G2.unitsScaleMom=1e-3



G3=graphical_reports.RecordLoadCaseDisp(loadCaseName='GearthPress',loadCaseDescr='G3: Poussée des terres',loadCaseExpr='1.0*GearthPress',setsToDispLoads=[overallSet],setsToDispDspRot=[foundDeck,walls],setsToDispIntForc=[foundDeck,walls])
G3.unitsScaleLoads=1e-3
G3.unitsScaleDispl=1e3
G3.unitsDispl='[mm]'
G3.unitsScaleForc=1e-3
G3.unitsScaleMom=1e-3


Q1ayb=graphical_reports.RecordLoadCaseDisp(loadCaseName='QtrafSit1unif',loadCaseDescr='Q1a and Q1b: Modèle de charge 1 . Distribution des charges uniformes',loadCaseExpr='1.0*QtrafSit1unif',setsToDispLoads=[overallSet],setsToDispDspRot=[foundDeck,walls],setsToDispIntForc=[foundDeck,walls])
Q1ayb.unitsScaleLoads=1e-3
Q1ayb.unitsScaleDispl=1e3
Q1ayb.unitsDispl='[mm]'
Q1ayb.unitsScaleForc=1e-3
Q1ayb.unitsScaleMom=1e-3


Q1a=graphical_reports.RecordLoadCaseDisp(loadCaseName='QtrafSit1a',loadCaseDescr='Q1a: Modèle de charge 1 en position Ia',loadCaseExpr='1.0*QtrafSit1a',setsToDispLoads=[overallSet],setsToDispDspRot=[foundDeck,walls],setsToDispIntForc=[foundDeck,walls])
Q1a.unitsScaleLoads=1e-3
Q1a.unitsScaleDispl=1e3
Q1a.unitsDispl='[mm]'
Q1a.unitsScaleForc=1e-3
Q1a.unitsScaleMom=1e-3


Q1b=graphical_reports.RecordLoadCaseDisp(loadCaseName='QtrafSit1b',loadCaseDescr='Q1b:Modèle de charge 1 en position Ib',loadCaseExpr='1.0*QtrafSit1b',setsToDispLoads=[overallSet],setsToDispDspRot=[foundDeck,walls],setsToDispIntForc=[foundDeck,walls])
Q1b.unitsScaleLoads=1e-3
Q1b.unitsScaleDispl=1e3
Q1b.unitsDispl='[mm]'
Q1b.unitsScaleForc=1e-3
Q1b.unitsScaleMom=1e-3

Q2ayb=graphical_reports.RecordLoadCaseDisp(loadCaseName='QtrafSit2unif',loadCaseDescr='Q2a and Q2b: Modèle de charge 2. Distribution des charges uniformes',loadCaseExpr='1.0*QtrafSit2unif',setsToDispLoads=[overallSet],setsToDispDspRot=[foundDeck,walls],setsToDispIntForc=[foundDeck,walls])
Q2ayb.unitsScaleLoads=1e-3
Q2ayb.unitsScaleDispl=1e3
Q2ayb.unitsDispl='[mm]'
Q2ayb.unitsScaleForc=1e-3
Q2ayb.unitsScaleMom=1e-3


Q2a=graphical_reports.RecordLoadCaseDisp(loadCaseName='QtrafSit2a',loadCaseDescr='Q2a: Modèle de charge 1 en position IIa',loadCaseExpr='1.0*QtrafSit2a',setsToDispLoads=[overallSet],setsToDispDspRot=[foundDeck,walls],setsToDispIntForc=[foundDeck,walls])
Q2a.unitsScaleLoads=1e-3
Q2a.unitsScaleDispl=1e3
Q2a.unitsDispl='[mm]'
Q2a.unitsScaleForc=1e-3
Q2a.unitsScaleMom=1e-3


Q2b=graphical_reports.RecordLoadCaseDisp(loadCaseName='QtrafSit2b',loadCaseDescr='Q2b: Modèle de charge 1 en position IIb',loadCaseExpr='1.0*QtrafSit2b',setsToDispLoads=[overallSet],setsToDispDspRot=[foundDeck,walls],setsToDispIntForc=[foundDeck,walls])
Q2b.unitsScaleLoads=1e-3
Q2b.unitsScaleDispl=1e3
Q2b.unitsDispl='[mm]'
Q2b.unitsScaleForc=1e-3
Q2b.unitsScaleMom=1e-3

ELULoadCaseDisp= combContainer.getRecordLoadCaseDisp(combName= 'ELU02',setsToDispLoads=[overallSet],setsToDispDspRot=[],setsToDispIntForc=[leftWall])
ELULoadCaseDisp.unitsScaleLoads=1e-3
ELULoadCaseDisp.unitsScaleDispl=1e3
ELULoadCaseDisp.unitsDispl='[mm]'
ELULoadCaseDisp.unitsScaleForc=1e-3
ELULoadCaseDisp.unitsScaleMom=1e-3
