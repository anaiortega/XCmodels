# -*- coding: utf-8 -*-

'''In this script we define default data of load cases to be used (or changed)
while displaying loads or results associated to single load cases 
'''
import graphical_reports_onlyForThisCase as gr
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
  multByElemSizeLoads: boolean value that must be True if we want to 
                 represent the total load on each element 
                 (=load multiplied by element size) and False if we 
                 are going to depict the value of the uniform load 
                 per unit size (defaults to False)
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



G1=gr.LoadCaseDispParameters(loadCaseName='selfWeight',loadCaseDescr='Poids propre',loadCaseExpr='1.0*selfWeight',setsToDispLoads=[shellElements],setsToDispDspRot=[xcTotalSet],setsToDispIntForc=[setDeck])
G1.unitsScaleLoads=1e-3
G1.unitsScaleDispl=1e3
G1.unitsDispl='[mm]'
G1.unitsScaleForc=1e-3
G1.unitsScaleMom=1e-3

G1.unitsMom='[m.kN]'
G1.unitsForc='[kN]'
G1.setsToDispBeamIntForc=[beamElements]
G1.listBeamIntForc=['My','Qz','N']
G1.cameraParameters= vtk_graphic_base.CameraParameters('XYZPos')
G1.compElLoad='transComponent'


G2=gr.LoadCaseDispParameters(loadCaseName='deadLoad',loadCaseDescr='Charge permanente',loadCaseExpr='1.0*deadLoad',setsToDispLoads=[xcTotalSet],setsToDispDspRot=[xcTotalSet],setsToDispIntForc=[setDeck])
G2.unitsScaleLoads=1e-3
G2.unitsScaleDispl=1e3
G2.unitsDispl='[mm]'
G2.unitsScaleForc=1e-3
G2.unitsScaleMom=1e-3

G2.unitsMom='[m.kN]'
G2.unitsForc='[kN]'
G2.setsToDispBeamIntForc=[beamElements]
G2.listBeamIntForc=['My','Qz','N']
G2.cameraParameters= vtk_graphic_base.CameraParameters('XYZPos')
G2.compElLoad='transComponent'


G3=gr.LoadCaseDispParameters(loadCaseName='shrinkage',loadCaseDescr='Retrait',loadCaseExpr='1.0*shrinkage',setsToDispLoads=[xcTotalSet],setsToDispDspRot=[xcTotalSet],setsToDispIntForc=[setDeck])
G3.unitsScaleLoads=1e-3
G3.unitsScaleDispl=1e3
G3.unitsDispl='[mm]'
G3.unitsScaleForc=1e-3
G3.unitsScaleMom=1e-3

G3.unitsMom='[m.kN]'
G3.unitsForc='[kN]'
G3.setsToDispBeamIntForc=[beamElements]
G3.listBeamIntForc=['My','Mz','Qy','Qz','N']
G3.cameraParameters= vtk_graphic_base.CameraParameters('XYZPos')
G3.compElLoad='transComponent'


QA=gr.LoadCaseDispParameters(loadCaseName='liveLoadA',loadCaseDescr='Rassemblement de personnes',loadCaseExpr='1.0*liveLoadA',setsToDispLoads=[xcTotalSet],setsToDispDspRot=[xcTotalSet],setsToDispIntForc=[setDeck])
QA.unitsScaleLoads=1e-3
QA.unitsScaleDispl=1e3
QA.unitsDispl='[mm]'
QA.unitsScaleForc=1e-3
QA.unitsScaleMom=1e-3

QA.unitsMom='[m.kN]'
QA.unitsForc='[kN]'
QA.setsToDispBeamIntForc=[beamElements]
QA.listBeamIntForc=['My','Mz','Qy','Qz','N']
QA.cameraParameters= vtk_graphic_base.CameraParameters('XYZPos')
QA.compElLoad='transComponent'


QB=gr.LoadCaseDispParameters(loadCaseName='liveLoadB',loadCaseDescr="Véhicule d'entrétien",loadCaseExpr='1.0*liveLoadB',setsToDispLoads=[xcTotalSet],setsToDispDspRot=[xcTotalSet],setsToDispIntForc=[setDeck])
QB.unitsScaleLoads=1e-3
QB.unitsScaleDispl=1e3
QB.unitsDispl='[mm]'
QB.unitsScaleForc=1e-3
QB.unitsScaleMom=1e-3

QB.unitsMom='[m.kN]'
QB.unitsForc='[kN]'
QB.setsToDispBeamIntForc=[beamElements]
QB.listBeamIntForc=['My','Mz','Qy','Qz','N']
QB.cameraParameters= vtk_graphic_base.CameraParameters('XYZPos')
QB.compElLoad='transComponent'


T=gr.LoadCaseDispParameters(loadCaseName='temperature',loadCaseDescr='Température',loadCaseExpr='1.0*temperature',setsToDispLoads=[xcTotalSet],setsToDispDspRot=[xcTotalSet],setsToDispIntForc=[setDeck])
T.unitsScaleLoads=1e-3
T.unitsScaleDispl=1e3
T.unitsDispl='[mm]'
T.unitsScaleForc=1e-3
T.unitsScaleMom=1e-3

T.unitsMom='[m.kN]'
T.unitsForc='[kN]'
T.setsToDispBeamIntForc=[beamElements]
T.listBeamIntForc=['My','Mz','Qy','Qz','N']
T.cameraParameters= vtk_graphic_base.CameraParameters('XYZPos')
T.compElLoad='transComponent'



Snow=gr.LoadCaseDispParameters(loadCaseName='snowLoad',loadCaseDescr='Neige',loadCaseExpr='1.0*snowLoad',setsToDispLoads=[xcTotalSet],setsToDispDspRot=[xcTotalSet],setsToDispIntForc=[setDeck])
Snow.unitsScaleLoads=1e-3
Snow.unitsScaleDispl=1e3
Snow.unitsDispl='[mm]'
Snow.unitsScaleForc=1e-3
Snow.unitsScaleMom=1e-3

Snow.unitsMom='[m.kN]'
Snow.unitsForc='[kN]'
Snow.setsToDispBeamIntForc=[beamElements]
Snow.listBeamIntForc=['My','Qz','N']
Snow.cameraParameters= vtk_graphic_base.CameraParameters('XYZPos')
Snow.compElLoad='transComponent'


EQ=gr.LoadCaseDispParameters(loadCaseName='earthquake',loadCaseDescr='Séisme',loadCaseExpr='1.0*earthquake',setsToDispLoads=[xcTotalSet],setsToDispDspRot=[xcTotalSet],setsToDispIntForc=[setDeck])
EQ.unitsScaleLoads=1e-3
EQ.unitsScaleDispl=1e3
EQ.unitsDispl='[mm]'
EQ.unitsScaleForc=1e-3
EQ.unitsScaleMom=1e-3

EQ.unitsMom='[m.kN]'
EQ.unitsForc='[kN]'
EQ.setsToDispBeamIntForc=[beamElements]
EQ.listBeamIntForc=['My','Qz','N']
EQ.cameraParameters= vtk_graphic_base.CameraParameters('XYZPos')
EQ.compElLoad='transComponent'


qperm=gr.LoadCaseDispParameters(loadCaseName='qperm',loadCaseDescr='Charges quasi permanentes',loadCaseExpr='1.0*selfWeight+1.0*deadLoad+1.0*shrinkage',setsToDispLoads=[xcTotalSet],setsToDispDspRot=[xcTotalSet],setsToDispIntForc=[setDeck])
qperm.unitsScaleLoads=1e-3
qperm.unitsScaleDispl=1e3
qperm.unitsDispl='[mm]'
qperm.unitsScaleForc=1e-3
qperm.unitsScaleMom=1e-3

qperm.unitsMom='[m.kN]'
qperm.unitsForc='[kN]'
qperm.setsToDispBeamIntForc=[beamElements]
qperm.listBeamIntForc=['My','Qz','N']
qperm.cameraParameters= vtk_graphic_base.CameraParameters('XYZPos')
qperm.compElLoad='transComponent'

