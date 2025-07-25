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
G1=graphical_reports.LoadCaseDispParameters(loadCaseName='GselfWeight',loadCaseDescr='G1: self weight',loadCaseExpr='1.0*GselfWeight',setsToDispLoads=[bridgeSectionSet],setsToDispDspRot=[bridgeSectionSet],setsToDispIntForc=[])
G1.unitsScaleLoads=1e-3
G1.unitsScaleDispl=1e3
G1.unitsDispl='[mm]'
G1.unitsScaleMom=1e-3
G1.unitsMom='[m.kN]'
G1.unitsScaleForc=1e-3
G1.unitsForc='[kN]'
G1.setsToDispBeamIntForc=[bridgeSectionSet]
G1.listBeamIntForc=['My','Mz','Qy','Qz','N']
G1.cameraParameters= vtk_graphic_base.CameraParameters('ZPos')
G1.setsToDispBeamLoads=[bridgeSectionSet]
G1.vectorScalePointLoads=0.005
G1.compElLoad='transComponent'


G2=graphical_reports.LoadCaseDispParameters(loadCaseName='GdeadLoad',loadCaseDescr='G2: dead load',loadCaseExpr='1.0*GdeadLoad',setsToDispLoads=[bridgeSectionSet],setsToDispDspRot=[bridgeSectionSet],setsToDispIntForc=[])
G2.unitsScaleLoads=1e-3
G2.unitsScaleDispl=1e3
G2.unitsDispl='[mm]'
G2.unitsScaleMom=1e-3
G2.unitsMom='[m.kN]'
G2.unitsScaleForc=1e-3
G2.unitsForc='[kN]'
G2.setsToDispBeamIntForc=[bridgeSectionSet]
G2.listBeamIntForc=['My','Mz','Qy','Qz','N']
G2.cameraParameters= vtk_graphic_base.CameraParameters('ZPos')
G2.setsToDispBeamLoads=[bridgeSectionSet]
G2.vectorScalePointLoads=0.005
G2.compElLoad='transComponent'


Q1=graphical_reports.LoadCaseDispParameters(loadCaseName='vehicleLiveLoad',loadCaseDescr='Q1: vehicle loads',loadCaseExpr='1.0*vehicleLiveLoad',setsToDispLoads=[bridgeSectionSet],setsToDispDspRot=[bridgeSectionSet],setsToDispIntForc=[])
Q1.unitsScaleLoads=1e-3
Q1.unitsScaleDispl=1e3
Q1.unitsDispl='[mm]'
Q1.unitsScaleMom=1e-3
Q1.unitsMom='[m.kN]'
Q1.unitsScaleForc=1e-3
Q1.unitsForc='[kN]'
Q1.setsToDispBeamIntForc=[bridgeSectionSet]
Q1.listBeamIntForc=['My','Mz','Qy','Qz','N']
Q1.cameraParameters= vtk_graphic_base.CameraParameters('ZPos')
Q1.setsToDispBeamLoads=[bridgeSectionSet]
Q1.vectorScalePointLoads=0.025
Q1.compElLoad='transComponent'


Q2=graphical_reports.LoadCaseDispParameters(loadCaseName='truckLiveLoad',loadCaseDescr='Q2: truck loads',loadCaseExpr='1.0*truckLiveLoad',setsToDispLoads=[bridgeSectionSet],setsToDispDspRot=[bridgeSectionSet],setsToDispIntForc=[])
Q2.unitsScaleLoads=1e-3
Q2.unitsScaleDispl=1e3
Q2.unitsDispl='[mm]'
Q2.unitsScaleMom=1e-3
Q2.unitsMom='[m.kN]'
Q2.unitsScaleForc=1e-3
Q2.unitsForc='[kN]'
Q2.setsToDispBeamIntForc=[bridgeSectionSet]
Q2.listBeamIntForc=['My','Mz','Qy','Qz','N']
Q2.cameraParameters= vtk_graphic_base.CameraParameters('ZPos')
Q2.setsToDispBeamLoads=[bridgeSectionSet]
Q2.vectorScalePointLoads=0.025
Q2.compElLoad='transComponent'


Q3=graphical_reports.LoadCaseDispParameters(loadCaseName='pedestrianLiveLoad',loadCaseDescr='Q3: pedestrian load',loadCaseExpr='1.0*pedestrianLiveLoad',setsToDispLoads=[bridgeSectionSet],setsToDispDspRot=[bridgeSectionSet],setsToDispIntForc=[])
Q3.unitsScaleLoads=1e-3
Q3.unitsScaleDispl=1e3
Q3.unitsDispl='[mm]'
Q3.unitsScaleMom=1e-3
Q3.unitsMom='[m.kN]'
Q3.unitsScaleForc=1e-3
Q3.unitsForc='[kN]'
Q3.setsToDispBeamIntForc=[bridgeSectionSet]
Q3.listBeamIntForc=['My','Mz','Qy','Qz','N']
Q3.cameraParameters= vtk_graphic_base.CameraParameters('ZPos')
Q3.setsToDispBeamLoads=[bridgeSectionSet]
Q3.vectorScalePointLoads=0.025
Q3.compElLoad='transComponent'


A1=graphical_reports.LoadCaseDispParameters(loadCaseName='impactLoad',loadCaseDescr='A1: impact load',loadCaseExpr='1.0*impactLoad',setsToDispLoads=[bridgeSectionSet],setsToDispDspRot=[bridgeSectionSet],setsToDispIntForc=[])
A1.unitsScaleLoads=1e-3
A1.unitsScaleDispl=1e3
A1.unitsDispl='[mm]'
A1.unitsScaleMom=1e-3
A1.unitsMom='[m.kN]'
A1.unitsScaleForc=1e-3
A1.unitsForc='[kN]'
A1.setsToDispBeamIntForc=[bridgeSectionSet]
A1.listBeamIntForc=['My','Mz','Qy','Qz','N']
A1.cameraParameters= vtk_graphic_base.CameraParameters('ZPos')
A1.setsToDispBeamLoads=[bridgeSectionSet]
A1.vectorScalePointLoads=0.025
A1.compElLoad='transComponent'



ELUT201=graphical_reports.LoadCaseDispParameters(loadCaseName='ELUT201',loadCaseDescr='ELUT201: vehicle live load',loadCaseExpr='1.35*GselfWeight+1.35*GdeadLoad+1.5*vehicleLiveLoad',setsToDispLoads=[bridgeSectionSet],setsToDispDspRot=[bridgeSectionSet],setsToDispIntForc=[])
ELUT201.unitsScaleLoads=1e-3
ELUT201.unitsScaleDispl=1e3
ELUT201.unitsDispl='[mm]'
ELUT201.unitsScaleMom=1e-3
ELUT201.unitsMom='[m.kN]'
ELUT201.unitsScaleForc=1e-3
ELUT201.unitsForc='[kN]'
ELUT201.setsToDispBeamIntForc=[bridgeSectionSet]
ELUT201.listBeamIntForc=['My','Mz','Qy','Qz','N']
ELUT201.cameraParameters= vtk_graphic_base.CameraParameters('ZPos')
ELUT201.setsToDispBeamLoads=[bridgeSectionSet]
ELUT201.vectorScalePointLoads=0.025
ELUT201.compElLoad='transComponent'


ELUT202=graphical_reports.LoadCaseDispParameters(loadCaseName='ELUT202',loadCaseDescr='ELUT202: pedestrian live load',loadCaseExpr='1.35*GselfWeight+1.35*GdeadLoad+1.5*pedestrianLiveLoad',setsToDispLoads=[bridgeSectionSet],setsToDispDspRot=[bridgeSectionSet],setsToDispIntForc=[])
ELUT202.unitsScaleLoads=1e-3
ELUT202.unitsScaleDispl=1e3
ELUT202.unitsDispl='[mm]'
ELUT202.unitsScaleMom=1e-3
ELUT202.unitsMom='[m.kN]'
ELUT202.unitsScaleForc=1e-3
ELUT202.unitsForc='[kN]'
ELUT202.setsToDispBeamIntForc=[bridgeSectionSet]
ELUT202.listBeamIntForc=['My','Mz','Qy','Qz','N']
ELUT202.cameraParameters= vtk_graphic_base.CameraParameters('ZPos')
ELUT202.setsToDispBeamLoads=[bridgeSectionSet]
ELUT202.vectorScalePointLoads=0.025
ELUT202.compElLoad='transComponent'


AT101=graphical_reports.LoadCaseDispParameters(loadCaseName='AT101',loadCaseDescr='AT101: impact load 1a',loadCaseExpr='0.9*GselfWeight+0.9*GdeadLoad+1.0*truckLiveLoad+1.0*impactLoad',setsToDispLoads=[bridgeSectionSet],setsToDispDspRot=[bridgeSectionSet],setsToDispIntForc=[])
AT101.unitsScaleLoads=1e-3
AT101.unitsScaleDispl=1e3
AT101.unitsDispl='[mm]'
AT101.unitsScaleMom=1e-3
AT101.unitsMom='[m.kN]'
AT101.unitsScaleForc=1e-3
AT101.unitsForc='[kN]'
AT101.setsToDispBeamIntForc=[bridgeSectionSet]
AT101.listBeamIntForc=['My','Mz','Qy','Qz','N']
AT101.cameraParameters= vtk_graphic_base.CameraParameters('ZPos')
AT101.setsToDispBeamLoads=[bridgeSectionSet]
AT101.vectorScalePointLoads=0.025
AT101.compElLoad='transComponent'


AT201=graphical_reports.LoadCaseDispParameters(loadCaseName='AT201',loadCaseDescr='AT201: impact load 1a',loadCaseExpr='0.8*GselfWeight+0.8*GdeadLoad+1.0*truckLiveLoad+1.0*impactLoad',setsToDispLoads=[bridgeSectionSet],setsToDispDspRot=[bridgeSectionSet],setsToDispIntForc=[])
AT201.unitsScaleLoads=1e-3
AT201.unitsScaleDispl=1e3
AT201.unitsDispl='[mm]'
AT201.unitsScaleMom=1e-3
AT201.unitsMom='[m.kN]'
AT201.unitsScaleForc=1e-3
AT201.unitsForc='[kN]'
AT201.setsToDispBeamIntForc=[parapetSet,deckSet]
AT201.listBeamIntForc=['My','Mz','Qy','Qz','N']
AT201.cameraParameters= vtk_graphic_base.CameraParameters('ZPos')
AT201.setsToDispBeamLoads=[bridgeSectionSet]
AT201.vectorScalePointLoads=0.025
AT201.compElLoad='transComponent'


AT202=graphical_reports.LoadCaseDispParameters(loadCaseName='AT202',loadCaseDescr='AT202: impact load 1a',loadCaseExpr='1.35*GselfWeight+1.35*GdeadLoad+1.0*truckLiveLoad+1.0*impactLoad',setsToDispLoads=[bridgeSectionSet],setsToDispDspRot=[bridgeSectionSet],setsToDispIntForc=[])
AT202.unitsScaleLoads=1e-3
AT202.unitsScaleDispl=1e3
AT202.unitsDispl='[mm]'
AT202.unitsScaleMom=1e-3
AT202.unitsMom='[m.kN]'
AT202.unitsScaleForc=1e-3
AT202.unitsForc='[kN]'
AT202.setsToDispBeamIntForc=[bridgeSectionSet]
AT202.listBeamIntForc=['My','Mz','Qy','Qz','N']
AT202.cameraParameters= vtk_graphic_base.CameraParameters('ZPos')
AT202.setsToDispBeamLoads=[bridgeSectionSet]
AT202.vectorScalePointLoads=0.025
AT202.compElLoad='transComponent'


ELUT40=graphical_reports.LoadCaseDispParameters(loadCaseName='ELUT40',loadCaseDescr='ELUT40: vehicle live load',loadCaseExpr='1.0*GselfWeight+1.0*GdeadLoad',setsToDispLoads=[bridgeSectionSet],setsToDispDspRot=[bridgeSectionSet],setsToDispIntForc=[])
ELUT40.unitsScaleLoads=1e-3
ELUT40.unitsScaleDispl=1e3
ELUT40.unitsDispl='[mm]'
ELUT40.unitsScaleMom=1e-3
ELUT40.unitsMom='[m.kN]'
ELUT40.unitsScaleForc=1e-3
ELUT40.unitsForc='[kN]'
ELUT40.setsToDispBeamIntForc=[bridgeSectionSet]
ELUT40.listBeamIntForc=['My','Mz','Qy','Qz','N']
ELUT40.cameraParameters= vtk_graphic_base.CameraParameters('ZPos')
ELUT40.setsToDispBeamLoads=[bridgeSectionSet]
ELUT40.vectorScalePointLoads=0.025
ELUT40.compElLoad='transComponent'


ELUT41=graphical_reports.LoadCaseDispParameters(loadCaseName='ELUT41',loadCaseDescr='ELUT41: vehicle live load',loadCaseExpr='1.0*GselfWeight+1.0*GdeadLoad+1.0*vehicleLiveLoad',setsToDispLoads=[bridgeSectionSet],setsToDispDspRot=[bridgeSectionSet],setsToDispIntForc=[])
ELUT41.unitsScaleLoads=1e-3
ELUT41.unitsScaleDispl=1e3
ELUT41.unitsDispl='[mm]'
ELUT41.unitsScaleMom=1e-3
ELUT41.unitsMom='[m.kN]'
ELUT41.unitsScaleForc=1e-3
ELUT41.unitsForc='[kN]'
ELUT41.setsToDispBeamIntForc=[bridgeSectionSet]
ELUT41.listBeamIntForc=['My','Mz','Qy','Qz','N']
ELUT41.cameraParameters= vtk_graphic_base.CameraParameters('ZPos')
ELUT41.setsToDispBeamLoads=[bridgeSectionSet]
ELUT41.vectorScalePointLoads=0.025
ELUT41.compElLoad='transComponent'

