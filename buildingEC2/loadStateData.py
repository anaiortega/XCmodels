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
                  forces (defaults to (1.0,1.0,1.0) -> auto-scale)
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
                 "ZPos", "ZNeg", "+X+Y+Z", "+X+Y-Z", "+X-Y+Z", "+X-Y-Z", "-X+Y+Z", "-X+Y-Z", 
                 "-X-Y+Z", "-X-Y-Z")  (defaults to "XYZPos")
  hCamFct:   factor that applies to the height of the camera position 
                 in order to change perspective of isometric views 
                 (defaults to 1, usual values 0.1 to 10)
  viewNameBeams: name of the view  for beam elements displays (defaults to "XYZPos")
  hCamFctBeams:  factor that applies to the height of the camera position for
                 beam displays (defaults to 1)
    
'''
LC1_deadLoadBearingStructure=graphical_reports.RecordLoadCaseDisp(loadCaseName='LC1_deadLoadBearingStructure',loadCaseDescr='LC1: dead load of the bearing structure',loadCaseExpr='1.0*LC1_deadLoadBearingStructure',setsToDispLoads=[xcTotalSet],setsToDispDspRot=[xcTotalSet],setsToDispIntForc=[shellSet]) 
LC1_deadLoadBearingStructure.unitsScaleLoads=1 
LC1_deadLoadBearingStructure.unitsScaleDispl=1e3 
LC1_deadLoadBearingStructure.unitsDispl='[mm]' 
LC1_deadLoadBearingStructure.unitsScaleMom=1 
LC1_deadLoadBearingStructure.unitsMom='[m.kN]' 
LC1_deadLoadBearingStructure.unitsScaleForc=1 
LC1_deadLoadBearingStructure.unitsForc='[kN]' 
LC1_deadLoadBearingStructure.setsToDispBeamIntForc=[columnsSet] 
LC1_deadLoadBearingStructure.listBeamIntForc=['My','Mz','Qy','Qz','N'] 
LC1_deadLoadBearingStructure.viewName='-X-Y+Z' 
LC1_deadLoadBearingStructure.setsToDispBeamLoads=[] 
LC1_deadLoadBearingStructure.vectorScalePointLoads=0.005 
LC1_deadLoadBearingStructure.compElLoad='transComponent' 
LC1_deadLoadBearingStructure.hCamFct=1

LC2_deadLoadInterior=graphical_reports.RecordLoadCaseDisp(loadCaseName='LC2_deadLoadInterior',loadCaseDescr='LC2: dead load of the interior',loadCaseExpr='1.0*LC2_deadLoadInterior',setsToDispLoads=[xcTotalSet],setsToDispDspRot=[xcTotalSet],setsToDispIntForc=[shellSet]) 
LC2_deadLoadInterior.unitsScaleLoads=1 
LC2_deadLoadInterior.unitsScaleDispl=1e3 
LC2_deadLoadInterior.unitsDispl='[mm]' 
LC2_deadLoadInterior.unitsScaleMom=1 
LC2_deadLoadInterior.unitsMom='[m.kN]' 
LC2_deadLoadInterior.unitsScaleForc=1 
LC2_deadLoadInterior.unitsForc='[kN]' 
LC2_deadLoadInterior.setsToDispBeamIntForc=[columnsSet] 
LC2_deadLoadInterior.listBeamIntForc=['My','Mz','Qy','Qz','N'] 
LC2_deadLoadInterior.viewName='-X-Y+Z'  
LC2_deadLoadInterior.setsToDispBeamLoads=[] 
LC2_deadLoadInterior.vectorScalePointLoads=0.005 
LC2_deadLoadInterior.compElLoad='transComponent' 

LC3_deadLoadFacade=graphical_reports.RecordLoadCaseDisp(loadCaseName='LC3_deadLoadFacade',loadCaseDescr='LC3: dead load of the facade',loadCaseExpr='1.0*LC3_deadLoadFacade',setsToDispLoads=[xcTotalSet],setsToDispDspRot=[xcTotalSet],setsToDispIntForc=[shellSet]) 
LC3_deadLoadFacade.unitsScaleLoads=1 
LC3_deadLoadFacade.unitsScaleDispl=1e3 
LC3_deadLoadFacade.unitsDispl='[mm]' 
LC3_deadLoadFacade.unitsScaleMom=1 
LC3_deadLoadFacade.unitsMom='[m.kN]' 
LC3_deadLoadFacade.unitsScaleForc=1 
LC3_deadLoadFacade.unitsForc='[kN]' 
LC3_deadLoadFacade.setsToDispBeamIntForc=[columnsSet] 
LC3_deadLoadFacade.listBeamIntForc=['My','Mz','Qy','Qz','N'] 
LC3_deadLoadFacade.viewName='-X-Y+Z'  
LC3_deadLoadFacade.setsToDispBeamLoads=[] 
LC3_deadLoadFacade.vectorScalePointLoads=0.005 
LC3_deadLoadFacade.compElLoad='transComponent' 
 
LC51_windX=graphical_reports.RecordLoadCaseDisp(loadCaseName='LC51_windX',loadCaseDescr='LC51: wind in global X direction',loadCaseExpr='1.0*LC51_windX',setsToDispLoads=[xcTotalSet],setsToDispDspRot=[xcTotalSet],setsToDispIntForc=[shellSet]) 
LC51_windX.unitsScaleLoads=1 
LC51_windX.unitsScaleDispl=1e3 
LC51_windX.unitsDispl='[mm]' 
LC51_windX.unitsScaleMom=1 
LC51_windX.unitsMom='[m.kN]' 
LC51_windX.unitsScaleForc=1 
LC51_windX.unitsForc='[kN]' 
LC51_windX.setsToDispBeamIntForc=[columnsSet] 
LC51_windX.listBeamIntForc=['My','Mz','Qy','Qz','N'] 
LC51_windX.viewName='-X-Y+Z'  
LC51_windX.setsToDispBeamLoads=[] 
LC51_windX.vectorScalePointLoads=0.005 
LC51_windX.compElLoad='transComponent' 
 
LC101_windY=graphical_reports.RecordLoadCaseDisp(loadCaseName='LC101_windY',loadCaseDescr='LC101: wind in global Y direction',loadCaseExpr='1.0*LC101_windY',setsToDispLoads=[xcTotalSet],setsToDispDspRot=[xcTotalSet],setsToDispIntForc=[shellSet]) 
LC101_windY.unitsScaleLoads=1 
LC101_windY.unitsScaleDispl=1e3 
LC101_windY.unitsDispl='[mm]' 
LC101_windY.unitsScaleMom=1 
LC101_windY.unitsMom='[m.kN]' 
LC101_windY.unitsScaleForc=1 
LC101_windY.unitsForc='[kN]' 
LC101_windY.setsToDispBeamIntForc=[columnsSet] 
LC101_windY.listBeamIntForc=['My','Mz','Qy','Qz','N'] 
LC101_windY.viewName='-X-Y+Z'  
LC101_windY.setsToDispBeamLoads=[] 
LC101_windY.vectorScalePointLoads=0.005 
LC101_windY.compElLoad='transComponent' 
 
LC201_snowRoof=graphical_reports.RecordLoadCaseDisp(loadCaseName='LC201_snowRoof',loadCaseDescr='LC201: snow on the roof',loadCaseExpr='1.0*LC201_snowRoof',setsToDispLoads=[xcTotalSet],setsToDispDspRot=[xcTotalSet],setsToDispIntForc=[shellSet]) 
LC201_snowRoof.unitsScaleLoads=1 
LC201_snowRoof.unitsScaleDispl=1e3 
LC201_snowRoof.unitsDispl='[mm]' 
LC201_snowRoof.unitsScaleMom=1 
LC201_snowRoof.unitsMom='[m.kN]' 
LC201_snowRoof.unitsScaleForc=1 
LC201_snowRoof.unitsForc='[kN]' 
LC201_snowRoof.setsToDispBeamIntForc=[columnsSet] 
LC201_snowRoof.listBeamIntForc=['My','Mz','Qy','Qz','N'] 
LC201_snowRoof.viewName='-X-Y+Z'  
LC201_snowRoof.setsToDispBeamLoads=[] 
LC201_snowRoof.vectorScalePointLoads=0.005 
LC201_snowRoof.compElLoad='transComponent' 
 
LC202_snowAx1_2=graphical_reports.RecordLoadCaseDisp(loadCaseName='LC202_snowAx1_2',loadCaseDescr='LC202: snow on the external area between axes 1 and 2',loadCaseExpr='1.0*LC202_snowAx1_2',setsToDispLoads=[xcTotalSet],setsToDispDspRot=[xcTotalSet],setsToDispIntForc=[shellSet]) 
LC202_snowAx1_2.unitsScaleLoads=1 
LC202_snowAx1_2.unitsScaleDispl=1e3 
LC202_snowAx1_2.unitsDispl='[mm]' 
LC202_snowAx1_2.unitsScaleMom=1 
LC202_snowAx1_2.unitsMom='[m.kN]' 
LC202_snowAx1_2.unitsScaleForc=1 
LC202_snowAx1_2.unitsForc='[kN]' 
LC202_snowAx1_2.setsToDispBeamIntForc=[columnsSet] 
LC202_snowAx1_2.listBeamIntForc=['My','Mz','Qy','Qz','N'] 
LC202_snowAx1_2.viewName='-X-Y+Z'  
LC202_snowAx1_2.setsToDispBeamLoads=[] 
LC202_snowAx1_2.vectorScalePointLoads=0.005 
LC202_snowAx1_2.compElLoad='transComponent' 
 
LC203_snowAx2_3=graphical_reports.RecordLoadCaseDisp(loadCaseName='LC203_snowAx2_3',loadCaseDescr='LC203: snow on the external area between axes 2 and 3',loadCaseExpr='1.0*LC203_snowAx2_3',setsToDispLoads=[xcTotalSet],setsToDispDspRot=[xcTotalSet],setsToDispIntForc=[shellSet]) 
LC203_snowAx2_3.unitsScaleLoads=1 
LC203_snowAx2_3.unitsScaleDispl=1e3 
LC203_snowAx2_3.unitsDispl='[mm]' 
LC203_snowAx2_3.unitsScaleMom=1 
LC203_snowAx2_3.unitsMom='[m.kN]' 
LC203_snowAx2_3.unitsScaleForc=1 
LC203_snowAx2_3.unitsForc='[kN]' 
LC203_snowAx2_3.setsToDispBeamIntForc=[columnsSet] 
LC203_snowAx2_3.listBeamIntForc=['My','Mz','Qy','Qz','N'] 
LC203_snowAx2_3.viewName='-X-Y+Z'  
LC203_snowAx2_3.setsToDispBeamLoads=[] 
LC203_snowAx2_3.vectorScalePointLoads=0.005 
LC203_snowAx2_3.compElLoad='transComponent' 
 
LC204_snowAx3_4=graphical_reports.RecordLoadCaseDisp(loadCaseName='LC204_snowAx3_4',loadCaseDescr='LC204: snow on the external area between axes 3 and 4',loadCaseExpr='1.0*LC204_snowAx3_4',setsToDispLoads=[xcTotalSet],setsToDispDspRot=[xcTotalSet],setsToDispIntForc=[shellSet]) 
LC204_snowAx3_4.unitsScaleLoads=1 
LC204_snowAx3_4.unitsScaleDispl=1e3 
LC204_snowAx3_4.unitsDispl='[mm]' 
LC204_snowAx3_4.unitsScaleMom=1 
LC204_snowAx3_4.unitsMom='[m.kN]' 
LC204_snowAx3_4.unitsScaleForc=1 
LC204_snowAx3_4.unitsForc='[kN]' 
LC204_snowAx3_4.setsToDispBeamIntForc=[columnsSet] 
LC204_snowAx3_4.listBeamIntForc=['My','Mz','Qy','Qz','N'] 
LC204_snowAx3_4.viewName='-X-Y+Z'  
LC204_snowAx3_4.setsToDispBeamLoads=[] 
LC204_snowAx3_4.vectorScalePointLoads=0.005 
LC204_snowAx3_4.compElLoad='transComponent' 
 
LC205_snowAx4_5=graphical_reports.RecordLoadCaseDisp(loadCaseName='LC205_snowAx4_5',loadCaseDescr='LC205: snow on the external area between axes 4 and 5',loadCaseExpr='1.0*LC205_snowAx4_5',setsToDispLoads=[xcTotalSet],setsToDispDspRot=[xcTotalSet],setsToDispIntForc=[shellSet]) 
LC205_snowAx4_5.unitsScaleLoads=1 
LC205_snowAx4_5.unitsScaleDispl=1e3 
LC205_snowAx4_5.unitsDispl='[mm]' 
LC205_snowAx4_5.unitsScaleMom=1 
LC205_snowAx4_5.unitsMom='[m.kN]' 
LC205_snowAx4_5.unitsScaleForc=1 
LC205_snowAx4_5.unitsForc='[kN]' 
LC205_snowAx4_5.setsToDispBeamIntForc=[columnsSet] 
LC205_snowAx4_5.listBeamIntForc=['My','Mz','Qy','Qz','N'] 
LC205_snowAx4_5.viewName='-X-Y+Z'  
LC205_snowAx4_5.setsToDispBeamLoads=[] 
LC205_snowAx4_5.vectorScalePointLoads=0.005 
LC205_snowAx4_5.compElLoad='transComponent' 
 
LC206_snowAx5_6=graphical_reports.RecordLoadCaseDisp(loadCaseName='LC206_snowAx5_6',loadCaseDescr='LC206: snow on the external area between axes 5 and 6',loadCaseExpr='1.0*LC206_snowAx5_6',setsToDispLoads=[xcTotalSet],setsToDispDspRot=[xcTotalSet],setsToDispIntForc=[shellSet]) 
LC206_snowAx5_6.unitsScaleLoads=1 
LC206_snowAx5_6.unitsScaleDispl=1e3 
LC206_snowAx5_6.unitsDispl='[mm]' 
LC206_snowAx5_6.unitsScaleMom=1 
LC206_snowAx5_6.unitsMom='[m.kN]' 
LC206_snowAx5_6.unitsScaleForc=1 
LC206_snowAx5_6.unitsForc='[kN]' 
LC206_snowAx5_6.setsToDispBeamIntForc=[columnsSet] 
LC206_snowAx5_6.listBeamIntForc=['My','Mz','Qy','Qz','N'] 
LC206_snowAx5_6.viewName='-X-Y+Z'  
LC206_snowAx5_6.setsToDispBeamLoads=[] 
LC206_snowAx5_6.vectorScalePointLoads=0.005 
LC206_snowAx5_6.compElLoad='transComponent' 
 
LC1326_servRoof=graphical_reports.RecordLoadCaseDisp(loadCaseName='LC1326_servRoof',loadCaseDescr='LC1326: service load 1 on the roof, arrangement 1',loadCaseExpr='1.0*LC1326_servRoof',setsToDispLoads=[xcTotalSet],setsToDispDspRot=[xcTotalSet],setsToDispIntForc=[shellSet]) 
LC1326_servRoof.unitsScaleLoads=1 
LC1326_servRoof.unitsScaleDispl=1e3 
LC1326_servRoof.unitsDispl='[mm]' 
LC1326_servRoof.unitsScaleMom=1 
LC1326_servRoof.unitsMom='[m.kN]' 
LC1326_servRoof.unitsScaleForc=1 
LC1326_servRoof.unitsForc='[kN]' 
LC1326_servRoof.setsToDispBeamIntForc=[columnsSet] 
LC1326_servRoof.listBeamIntForc=['My','Mz','Qy','Qz','N'] 
LC1326_servRoof.viewName='-X-Y+Z'  
LC1326_servRoof.setsToDispBeamLoads=[] 
LC1326_servRoof.vectorScalePointLoads=0.005 
LC1326_servRoof.compElLoad='transComponent' 
 
LC1336_servRoof=graphical_reports.RecordLoadCaseDisp(loadCaseName='LC1336_servRoof',loadCaseDescr='LC1336: service load 1 on the roof, arrangement 2',loadCaseExpr='1.0*LC1336_servRoof',setsToDispLoads=[xcTotalSet],setsToDispDspRot=[xcTotalSet],setsToDispIntForc=[shellSet]) 
LC1336_servRoof.unitsScaleLoads=1 
LC1336_servRoof.unitsScaleDispl=1e3 
LC1336_servRoof.unitsDispl='[mm]' 
LC1336_servRoof.unitsScaleMom=1 
LC1336_servRoof.unitsMom='[m.kN]' 
LC1336_servRoof.unitsScaleForc=1 
LC1336_servRoof.unitsForc='[kN]' 
LC1336_servRoof.setsToDispBeamIntForc=[columnsSet] 
LC1336_servRoof.listBeamIntForc=['My','Mz','Qy','Qz','N'] 
LC1336_servRoof.viewName='-X-Y+Z'  
LC1336_servRoof.setsToDispBeamLoads=[] 
LC1336_servRoof.vectorScalePointLoads=0.005 
LC1336_servRoof.compElLoad='transComponent' 
 
LC1356_servRoof=graphical_reports.RecordLoadCaseDisp(loadCaseName='LC1356_servRoof',loadCaseDescr='LC1356: service load 1 on the roof, arrangement 3',loadCaseExpr='1.0*LC1356_servRoof',setsToDispLoads=[xcTotalSet],setsToDispDspRot=[xcTotalSet],setsToDispIntForc=[shellSet]) 
LC1356_servRoof.unitsScaleLoads=1 
LC1356_servRoof.unitsScaleDispl=1e3 
LC1356_servRoof.unitsDispl='[mm]' 
LC1356_servRoof.unitsScaleMom=1 
LC1356_servRoof.unitsMom='[m.kN]' 
LC1356_servRoof.unitsScaleForc=1 
LC1356_servRoof.unitsForc='[kN]' 
LC1356_servRoof.setsToDispBeamIntForc=[columnsSet] 
LC1356_servRoof.listBeamIntForc=['My','Mz','Qy','Qz','N'] 
LC1356_servRoof.viewName='-X-Y+Z'  
LC1356_servRoof.setsToDispBeamLoads=[] 
LC1356_servRoof.vectorScalePointLoads=0.005 
LC1356_servRoof.compElLoad='transComponent' 
 
LC1366_servRoof=graphical_reports.RecordLoadCaseDisp(loadCaseName='LC1366_servRoof',loadCaseDescr='LC1366: service load 1 on the roof, arrangement 4',loadCaseExpr='1.0*LC1366_servRoof',setsToDispLoads=[xcTotalSet],setsToDispDspRot=[xcTotalSet],setsToDispIntForc=[shellSet]) 
LC1366_servRoof.unitsScaleLoads=1 
LC1366_servRoof.unitsScaleDispl=1e3 
LC1366_servRoof.unitsDispl='[mm]' 
LC1366_servRoof.unitsScaleMom=1 
LC1366_servRoof.unitsMom='[m.kN]' 
LC1366_servRoof.unitsScaleForc=1 
LC1366_servRoof.unitsForc='[kN]' 
LC1366_servRoof.setsToDispBeamIntForc=[columnsSet] 
LC1366_servRoof.listBeamIntForc=['My','Mz','Qy','Qz','N'] 
LC1366_servRoof.viewName='-X-Y+Z'  
LC1366_servRoof.setsToDispBeamLoads=[] 
LC1366_servRoof.vectorScalePointLoads=0.005 
LC1366_servRoof.compElLoad='transComponent' 
 
LC10001_serv1=graphical_reports.RecordLoadCaseDisp(loadCaseName='LC10001_serv1',loadCaseDescr='LC10001: service load 1 on levels 0 to 5, arrangement 1',loadCaseExpr='1.0*LC10001_serv1',setsToDispLoads=[xcTotalSet],setsToDispDspRot=[xcTotalSet],setsToDispIntForc=[shellSet]) 
LC10001_serv1.unitsScaleLoads=1 
LC10001_serv1.unitsScaleDispl=1e3 
LC10001_serv1.unitsDispl='[mm]' 
LC10001_serv1.unitsScaleMom=1 
LC10001_serv1.unitsMom='[m.kN]' 
LC10001_serv1.unitsScaleForc=1 
LC10001_serv1.unitsForc='[kN]' 
LC10001_serv1.setsToDispBeamIntForc=[columnsSet] 
LC10001_serv1.listBeamIntForc=['My','Mz','Qy','Qz','N'] 
LC10001_serv1.viewName='-X-Y+Z'
LC10001_serv1.hCamFct=0.5
LC10001_serv1.setsToDispBeamLoads=[] 
LC10001_serv1.vectorScalePointLoads=0.005 
LC10001_serv1.compElLoad='transComponent' 
 
LC10011_serv1=graphical_reports.RecordLoadCaseDisp(loadCaseName='LC10011_serv1',loadCaseDescr='LC10011: service load 1 on levels 0 to 5, arrangement 2',loadCaseExpr='1.0*LC10011_serv1',setsToDispLoads=[xcTotalSet],setsToDispDspRot=[xcTotalSet],setsToDispIntForc=[shellSet]) 
LC10011_serv1.unitsScaleLoads=1 
LC10011_serv1.unitsScaleDispl=1e3 
LC10011_serv1.unitsDispl='[mm]' 
LC10011_serv1.unitsScaleMom=1 
LC10011_serv1.unitsMom='[m.kN]' 
LC10011_serv1.unitsScaleForc=1 
LC10011_serv1.unitsForc='[kN]' 
LC10011_serv1.setsToDispBeamIntForc=[columnsSet] 
LC10011_serv1.listBeamIntForc=['My','Mz','Qy','Qz','N'] 
LC10011_serv1.viewName='-X-Y+Z'  
LC10001_serv1.hCamFct=0.5
LC10011_serv1.setsToDispBeamLoads=[] 
LC10011_serv1.vectorScalePointLoads=0.005 
LC10011_serv1.compElLoad='transComponent' 
 
LC10021_serv1=graphical_reports.RecordLoadCaseDisp(loadCaseName='LC10021_serv1',loadCaseDescr='LC10021: service load 1 on levels 0 to 5, arrangement 3',loadCaseExpr='1.0*LC10021_serv1',setsToDispLoads=[xcTotalSet],setsToDispDspRot=[xcTotalSet],setsToDispIntForc=[shellSet]) 
LC10021_serv1.unitsScaleLoads=1 
LC10021_serv1.unitsScaleDispl=1e3 
LC10021_serv1.unitsDispl='[mm]' 
LC10021_serv1.unitsScaleMom=1 
LC10021_serv1.unitsMom='[m.kN]' 
LC10021_serv1.unitsScaleForc=1 
LC10021_serv1.unitsForc='[kN]' 
LC10021_serv1.setsToDispBeamIntForc=[columnsSet] 
LC10021_serv1.listBeamIntForc=['My','Mz','Qy','Qz','N'] 
LC10021_serv1.viewName='-X-Y+Z'  
LC10021_serv1.hCamFct=0.5
LC10021_serv1.setsToDispBeamLoads=[] 
LC10021_serv1.vectorScalePointLoads=0.005 
LC10021_serv1.compElLoad='transComponent' 
 
LC10031_serv1=graphical_reports.RecordLoadCaseDisp(loadCaseName='LC10031_serv1',loadCaseDescr='LC10031: service load 1 on levels 0 to 5, arrangement 4',loadCaseExpr='1.0*LC10031_serv1',setsToDispLoads=[xcTotalSet],setsToDispDspRot=[xcTotalSet],setsToDispIntForc=[shellSet]) 
LC10031_serv1.unitsScaleLoads=1 
LC10031_serv1.unitsScaleDispl=1e3 
LC10031_serv1.unitsDispl='[mm]' 
LC10031_serv1.unitsScaleMom=1 
LC10031_serv1.unitsMom='[m.kN]' 
LC10031_serv1.unitsScaleForc=1 
LC10031_serv1.unitsForc='[kN]' 
LC10031_serv1.setsToDispBeamIntForc=[columnsSet] 
LC10031_serv1.listBeamIntForc=['My','Mz','Qy','Qz','N'] 
LC10031_serv1.viewName='-X-Y+Z'  
LC10031_serv1.hCamFct=0.5
LC10031_serv1.setsToDispBeamLoads=[] 
LC10031_serv1.vectorScalePointLoads=0.005 
LC10031_serv1.compElLoad='transComponent' 
 
LC10101_servParking=graphical_reports.RecordLoadCaseDisp(loadCaseName='LC10101_servParking',loadCaseDescr='LC10101: service load 2 on levels -1 and -2, arrangement 1',loadCaseExpr='1.0*LC10101_servParking',setsToDispLoads=[xcTotalSet],setsToDispDspRot=[xcTotalSet],setsToDispIntForc=[shellSet]) 
LC10101_servParking.unitsScaleLoads=1 
LC10101_servParking.unitsScaleDispl=1e3 
LC10101_servParking.unitsDispl='[mm]' 
LC10101_servParking.unitsScaleMom=1 
LC10101_servParking.unitsMom='[m.kN]' 
LC10101_servParking.unitsScaleForc=1 
LC10101_servParking.unitsForc='[kN]' 
LC10101_servParking.setsToDispBeamIntForc=[columnsSet] 
LC10101_servParking.listBeamIntForc=['My','Mz','Qy','Qz','N'] 
LC10101_servParking.viewName='-X-Y+Z'  
LC10101_servParking.hCamFct=0.5
LC10101_servParking.setsToDispBeamLoads=[] 
LC10101_servParking.vectorScalePointLoads=0.005 
LC10101_servParking.compElLoad='transComponent' 
 
LC10111_servParking=graphical_reports.RecordLoadCaseDisp(loadCaseName='LC10111_servParking',loadCaseDescr='LC10111: service load 2 on levels -1 and -2, arrangement 2',loadCaseExpr='1.0*LC10111_servParking',setsToDispLoads=[xcTotalSet],setsToDispDspRot=[xcTotalSet],setsToDispIntForc=[shellSet]) 
LC10111_servParking.unitsScaleLoads=1 
LC10111_servParking.unitsScaleDispl=1e3 
LC10111_servParking.unitsDispl='[mm]' 
LC10111_servParking.unitsScaleMom=1 
LC10111_servParking.unitsMom='[m.kN]' 
LC10111_servParking.unitsScaleForc=1 
LC10111_servParking.unitsForc='[kN]' 
LC10111_servParking.setsToDispBeamIntForc=[columnsSet] 
LC10111_servParking.listBeamIntForc=['My','Mz','Qy','Qz','N'] 
LC10111_servParking.viewName='-X-Y+Z'  
LC10111_servParking.hCamFct=0.5
LC10111_servParking.setsToDispBeamLoads=[] 
LC10111_servParking.vectorScalePointLoads=0.005 
LC10111_servParking.compElLoad='transComponent' 
 
LC10121_servParking=graphical_reports.RecordLoadCaseDisp(loadCaseName='LC10121_servParking',loadCaseDescr='LC10121: service load 2 on levels -1 and -2, arrangement 3',loadCaseExpr='1.0*LC10121_servParking',setsToDispLoads=[xcTotalSet],setsToDispDspRot=[xcTotalSet],setsToDispIntForc=[shellSet]) 
LC10121_servParking.unitsScaleLoads=1 
LC10121_servParking.unitsScaleDispl=1e3 
LC10121_servParking.unitsDispl='[mm]' 
LC10121_servParking.unitsScaleMom=1 
LC10121_servParking.unitsMom='[m.kN]' 
LC10121_servParking.unitsScaleForc=1 
LC10121_servParking.unitsForc='[kN]' 
LC10121_servParking.setsToDispBeamIntForc=[columnsSet] 
LC10121_servParking.listBeamIntForc=['My','Mz','Qy','Qz','N'] 
LC10121_servParking.viewName='-X-Y+Z'  
LC10121_servParking.hCamFct=0.5
LC10121_servParking.setsToDispBeamLoads=[] 
LC10121_servParking.vectorScalePointLoads=0.005 
LC10121_servParking.compElLoad='transComponent' 
 
LC10131_servParking=graphical_reports.RecordLoadCaseDisp(loadCaseName='LC10131_servParking',loadCaseDescr='LC10131: service load 2 on levels -1 and -2, arrangement 4',loadCaseExpr='1.0*LC10131_servParking',setsToDispLoads=[xcTotalSet],setsToDispDspRot=[xcTotalSet],setsToDispIntForc=[shellSet]) 
LC10131_servParking.unitsScaleLoads=1 
LC10131_servParking.unitsScaleDispl=1e3 
LC10131_servParking.unitsDispl='[mm]' 
LC10131_servParking.unitsScaleMom=1 
LC10131_servParking.unitsMom='[m.kN]' 
LC10131_servParking.unitsScaleForc=1 
LC10131_servParking.unitsForc='[kN]' 
LC10131_servParking.setsToDispBeamIntForc=[columnsSet] 
LC10131_servParking.listBeamIntForc=['My','Mz','Qy','Qz','N'] 
LC10131_servParking.viewName='-X-Y+Z'  
LC10131_servParking.hCamFct=0.5
LC10131_servParking.setsToDispBeamLoads=[] 
LC10131_servParking.vectorScalePointLoads=0.005 
LC10131_servParking.compElLoad='transComponent' 


ELUmaxMy=graphical_reports.RecordLoadCaseDisp(loadCaseName='ELUmaxMy',loadCaseDescr='ELUmaxMy: maximum internal moment My',loadCaseExpr='1.35*LC1_deadLoadBearingStructure+1.35*LC2_deadLoadInterior+1.35*LC3_deadLoadFacade+1.5*LC101_windY+0.75*LC203_snowAx2_3+0.75*LC204_snowAx3_4+0.75*LC205_snowAx4_5+0.75*LC206_snowAx5_6+1.05*LC1356_servRoof+1.05*LC10111_servParking',setsToDispLoads=[xcTotalSet],setsToDispDspRot=[xcTotalSet],setsToDispIntForc=[shellSet])
ELUmaxMy.unitsScaleLoads=1 
ELUmaxMy.unitsScaleDispl=1e3 
ELUmaxMy.unitsDispl='[mm]' 
ELUmaxMy.unitsScaleMom=1 
ELUmaxMy.unitsMom='[m.kN]' 
ELUmaxMy.unitsScaleForc=1 
ELUmaxMy.unitsForc='[kN]' 
ELUmaxMy.setsToDispBeamIntForc=[columnsSet] 
ELUmaxMy.listBeamIntForc=['My','Mz','Qy','Qz','N'] 
ELUmaxMy.viewName='-X-Y+Z'  
ELUmaxMy.hCamFct=1
ELUmaxMy.setsToDispBeamLoads=[] 
ELUmaxMy.vectorScalePointLoads=0.005 
ELUmaxMy.compElLoad='transComponent' 

ELUmaxMz=graphical_reports.RecordLoadCaseDisp(loadCaseName='ELUmaxMz',loadCaseDescr='ELUmaxMz: maximum internal moment Mz',loadCaseExpr='1.35*LC1_deadLoadBearingStructure+1.35*LC2_deadLoadInterior+1.35*LC3_deadLoadFacade+1.5*LC10111_servParking+0.9*LC51_windX+0.75*LC203_snowAx2_3+0.75*LC204_snowAx3_4+0.75*LC205_snowAx4_5+0.75*LC206_snowAx5_6+1.05*LC10011_serv1',setsToDispLoads=[xcTotalSet],setsToDispDspRot=[xcTotalSet],setsToDispIntForc=[shellSet])
ELUmaxMz.unitsScaleLoads=1 
ELUmaxMz.unitsScaleDispl=1e3 
ELUmaxMz.unitsDispl='[mm]' 
ELUmaxMz.unitsScaleMom=1 
ELUmaxMz.unitsMom='[m.kN]' 
ELUmaxMz.unitsScaleForc=1 
ELUmaxMz.unitsForc='[kN]' 
ELUmaxMz.setsToDispBeamIntForc=[columnsSet] 
ELUmaxMz.listBeamIntForc=['My','Mz','Qy','Qz','N'] 
ELUmaxMz.viewName='-X-Y+Z'  
ELUmaxMz.hCamFct=1
ELUmaxMz.setsToDispBeamLoads=[] 
ELUmaxMz.vectorScalePointLoads=0.005 
ELUmaxMz.compElLoad='transComponent' 

ELUmaxVy=graphical_reports.RecordLoadCaseDisp(loadCaseName='ELUmaxVy',loadCaseDescr='ELUmaxVy: maximum internal force Vy',loadCaseExpr='1.35*LC1_deadLoadBearingStructure+1.35*LC2_deadLoadInterior+1.35*LC3_deadLoadFacade+1.5*LC10111_servParking+0.9*LC51_windX+0.75*LC203_snowAx2_3+0.75*LC204_snowAx3_4+0.75*LC205_snowAx4_5+0.75*LC206_snowAx5_6+1.05*LC10011_serv1',setsToDispLoads=[xcTotalSet],setsToDispDspRot=[xcTotalSet],setsToDispIntForc=[shellSet])
ELUmaxVy.unitsScaleLoads=1 
ELUmaxVy.unitsScaleDispl=1e3 
ELUmaxVy.unitsDispl='[mm]' 
ELUmaxVy.unitsScaleMom=1 
ELUmaxVy.unitsMom='[m.kN]' 
ELUmaxVy.unitsScaleForc=1 
ELUmaxVy.unitsForc='[kN]' 
ELUmaxVy.setsToDispBeamIntForc=[columnsSet] 
ELUmaxVy.listBeamIntForc=['My','Mz','Qy','Qz','N'] 
ELUmaxVy.viewName='-X-Y+Z'  
ELUmaxVy.hCamFct=1
ELUmaxVy.setsToDispBeamLoads=[] 
ELUmaxVy.vectorScalePointLoads=0.005 
ELUmaxVy.compElLoad='transComponent' 

ELUmaxVz=graphical_reports.RecordLoadCaseDisp(loadCaseName='ELUmaxVz',loadCaseDescr='ELUmaxVz: maximum internal force Vz',loadCaseExpr='1.35*LC1_deadLoadBearingStructure+1.35*LC2_deadLoadInterior+1.35*LC3_deadLoadFacade+1.5*LC51_windX+1.05*LC10031_serv1+1.05*LC10101_servParking',setsToDispLoads=[xcTotalSet],setsToDispDspRot=[xcTotalSet],setsToDispIntForc=[shellSet])
ELUmaxVz.unitsScaleLoads=1 
ELUmaxVz.unitsScaleDispl=1e3 
ELUmaxVz.unitsDispl='[mm]' 
ELUmaxVz.unitsScaleMom=1 
ELUmaxVz.unitsMom='[m.kN]' 
ELUmaxVz.unitsScaleForc=1 
ELUmaxVz.unitsForc='[kN]' 
ELUmaxVz.setsToDispBeamIntForc=[columnsSet] 
ELUmaxVz.listBeamIntForc=['My','Mz','Qy','Qz','N'] 
ELUmaxVz.viewName='-X-Y+Z'  
ELUmaxVz.hCamFct=1
ELUmaxVz.setsToDispBeamLoads=[] 
ELUmaxVz.vectorScalePointLoads=0.005 
ELUmaxVz.compElLoad='transComponent' 

ELUmaxN=graphical_reports.RecordLoadCaseDisp(loadCaseName='ELUmaxN',loadCaseDescr='ELUmaxN: maximum internal force N',loadCaseExpr='1.35*LC1_deadLoadBearingStructure+1.35*LC2_deadLoadInterior+1.35*LC3_deadLoadFacade+1.5*LC51_windX+0.75*LC202_snowAx1_2+0.75*LC203_snowAx2_3+0.75*LC204_snowAx3_4+0.75*LC205_snowAx4_5',setsToDispLoads=[xcTotalSet],setsToDispDspRot=[xcTotalSet],setsToDispIntForc=[shellSet])
ELUmaxN.unitsScaleLoads=1 
ELUmaxN.unitsScaleDispl=1e3 
ELUmaxN.unitsDispl='[mm]' 
ELUmaxN.unitsScaleMom=1 
ELUmaxN.unitsMom='[m.kN]' 
ELUmaxN.unitsScaleForc=1 
ELUmaxN.unitsForc='[kN]' 
ELUmaxN.setsToDispBeamIntForc=[columnsSet] 
ELUmaxN.listBeamIntForc=['My','Mz','Qy','Qz','N'] 
ELUmaxN.viewName='-X-Y+Z'  
ELUmaxN.hCamFct=1
ELUmaxN.setsToDispBeamLoads=[] 
ELUmaxN.vectorScalePointLoads=0.005 
ELUmaxN.compElLoad='transComponent' 

ELUminMy=graphical_reports.RecordLoadCaseDisp(loadCaseName='ELUminMy',loadCaseDescr='ELUminMy: minimum internal moment My',loadCaseExpr='1.35*LC1_deadLoadBearingStructure+1.35*LC2_deadLoadInterior+1.35*LC3_deadLoadFacade+1.5*LC51_windX+0.75*LC201_snowRoof+1.05*LC1326_servRoof+1.05*LC10031_serv1+1.05*LC10101_servParking',setsToDispLoads=[xcTotalSet],setsToDispDspRot=[xcTotalSet],setsToDispIntForc=[shellSet])
ELUminMy.unitsScaleLoads=1 
ELUminMy.unitsScaleDispl=1e3 
ELUminMy.unitsDispl='[mm]' 
ELUminMy.unitsScaleMom=1 
ELUminMy.unitsMom='[m.kN]' 
ELUminMy.unitsScaleForc=1 
ELUminMy.unitsForc='[kN]' 
ELUminMy.setsToDispBeamIntForc=[columnsSet] 
ELUminMy.listBeamIntForc=['My','Mz','Qy','Qz','N'] 
ELUminMy.viewName='-X-Y+Z'  
ELUminMy.hCamFct=1
ELUminMy.setsToDispBeamLoads=[] 
ELUminMy.vectorScalePointLoads=0.005 
ELUminMy.compElLoad='transComponent' 

ELUminMz=graphical_reports.RecordLoadCaseDisp(loadCaseName='ELUminMz',loadCaseDescr='ELUminMz: minimum internal moment Mz',loadCaseExpr='1.35*LC1_deadLoadBearingStructure+1.35*LC2_deadLoadInterior+1.35*LC3_deadLoadFacade+1.5*LC10121_servParking+0.9*LC101_windY+0.75*LC201_snowRoof+0.75*LC202_snowAx1_2+1.05*LC1326_servRoof+1.5*LC10021_serv1',setsToDispLoads=[xcTotalSet],setsToDispDspRot=[xcTotalSet],setsToDispIntForc=[shellSet])
ELUminMz.unitsScaleLoads=1 
ELUminMz.unitsScaleDispl=1e3 
ELUminMz.unitsDispl='[mm]' 
ELUminMz.unitsScaleMom=1 
ELUminMz.unitsMom='[m.kN]' 
ELUminMz.unitsScaleForc=1 
ELUminMz.unitsForc='[kN]' 
ELUminMz.setsToDispBeamIntForc=[columnsSet] 
ELUminMz.listBeamIntForc=['My','Mz','Qy','Qz','N'] 
ELUminMz.viewName='-X-Y+Z'  
ELUminMz.hCamFct=1
ELUminMz.setsToDispBeamLoads=[] 
ELUminMz.vectorScalePointLoads=0.005 
ELUminMz.compElLoad='transComponent' 

ELUminVy=graphical_reports.RecordLoadCaseDisp(loadCaseName='ELUminVy',loadCaseDescr='ELUminVy: minimum internal force Vy',loadCaseExpr='1.35*LC1_deadLoadBearingStructure+1.35*LC2_deadLoadInterior+1.35*LC3_deadLoadFacade+1.5*LC10121_servParking+0.75*LC201_snowRoof+0.75*LC202_snowAx1_2+1.05*LC1356_servRoof+1.05*LC10021_serv1',setsToDispLoads=[xcTotalSet],setsToDispDspRot=[xcTotalSet],setsToDispIntForc=[shellSet])
ELUminVy.unitsScaleLoads=1 
ELUminVy.unitsScaleDispl=1e3 
ELUminVy.unitsDispl='[mm]' 
ELUminVy.unitsScaleMom=1 
ELUminVy.unitsMom='[m.kN]' 
ELUminVy.unitsScaleForc=1 
ELUminVy.unitsForc='[kN]' 
ELUminVy.setsToDispBeamIntForc=[columnsSet] 
ELUminVy.listBeamIntForc=['My','Mz','Qy','Qz','N'] 
ELUminVy.viewName='-X-Y+Z'  
ELUminVy.hCamFct=1
ELUminVy.setsToDispBeamLoads=[] 
ELUminVy.vectorScalePointLoads=0.005 
ELUminVy.compElLoad='transComponent' 

ELUminVz=graphical_reports.RecordLoadCaseDisp(loadCaseName='ELUminVz',loadCaseDescr='ELUminVz: minimum internal force Vz',loadCaseExpr='1.35*LC1_deadLoadBearingStructure+1.35*LC2_deadLoadInterior+1.35*LC3_deadLoadFacade+1.5*LC101_windY+0.75*LC202_snowAx1_2+0.75*LC203_snowAx2_3+0.75*LC204_snowAx3_4+0.75*LC205_snowAx4_5+0.75*LC206_snowAx5_6+1.05*LC10111_servParking',setsToDispLoads=[xcTotalSet],setsToDispDspRot=[xcTotalSet],setsToDispIntForc=[shellSet])
ELUminVz.unitsScaleLoads=1 
ELUminVz.unitsScaleDispl=1e3 
ELUminVz.unitsDispl='[mm]' 
ELUminVz.unitsScaleMom=1 
ELUminVz.unitsMom='[m.kN]' 
ELUminVz.unitsScaleForc=1 
ELUminVz.unitsForc='[kN]' 
ELUminVz.setsToDispBeamIntForc=[columnsSet] 
ELUminVz.listBeamIntForc=['My','Mz','Qy','Qz','N'] 
ELUminVz.viewName='-X-Y+Z'  
ELUminVz.hCamFct=1
ELUminVz.setsToDispBeamLoads=[] 
ELUminVz.vectorScalePointLoads=0.005 
ELUminVz.compElLoad='transComponent' 

ELUminN=graphical_reports.RecordLoadCaseDisp(loadCaseName='ELUminN',loadCaseDescr='ELUminN: minimum internal force N',loadCaseExpr='1.35*LC1_deadLoadBearingStructure+1.35*LC2_deadLoadInterior+1.35*LC3_deadLoadFacade+1.5*LC10031_serv1+1.5*LC1366_servRoof+0.75*LC201_snowRoof+1.05*LC10121_servParking',setsToDispLoads=[xcTotalSet],setsToDispDspRot=[xcTotalSet],setsToDispIntForc=[shellSet])
ELUminN.unitsScaleLoads=1 
ELUminN.unitsScaleDispl=1e3 
ELUminN.unitsDispl='[mm]' 
ELUminN.unitsScaleMom=1 
ELUminN.unitsMom='[m.kN]' 
ELUminN.unitsScaleForc=1 
ELUminN.unitsForc='[kN]' 
ELUminN.setsToDispBeamIntForc=[columnsSet] 
ELUminN.listBeamIntForc=['My','Mz','Qy','Qz','N'] 
ELUminN.viewName='-X-Y+Z'  
ELUminN.hCamFct=1
ELUminN.setsToDispBeamLoads=[] 
ELUminN.vectorScalePointLoads=0.005 
ELUminN.compElLoad='transComponent' 

