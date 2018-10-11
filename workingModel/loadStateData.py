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




G1=graphical_reports.RecordLoadCaseDisp(loadCaseName='GselfWeight',loadCaseDescr='G1: self weight',loadCaseExpr='1.0*GselfWeight',setsToDispLoads=[overallSet],setsToDispDspRot=[overallSet],setsToDispIntForc=[])
G1.unitsScaleLoads=1e-3
G1.unitsScaleDispl=1e3
G1.unitsDispl='[mm]'
G1.unitsScaleMom=1e-3
G1.unitsMom='[m.kN]'
G1.unitsScaleForc=1e-3
G1.unitsForc='[kN]'
G1.setsToDispBeamIntForc=[columnZ,beamX,beamY]
G1.listBeamIntForc=['My','Mz','Qy','Qz','N']
G1.viewName="XYZPos"
G1.setsToDispBeamLoads=[beamY]
G1.vectorScalePointLoads=0.005
G1.compElLoad='transComponent'
G1.hCamFct=1

Q1=graphical_reports.RecordLoadCaseDisp(loadCaseName='Qdecks',loadCaseDescr='Q1: uniform load on the decks',loadCaseExpr='1.0*Qdecks',setsToDispLoads=[decks],setsToDispDspRot=[overallSet],setsToDispIntForc=[])
Q1.unitsScaleLoads=1e-3
Q1.unitsScaleDispl=1e3
Q1.unitsDispl='[mm]'
Q1.unitsScaleMom=1e-3
Q1.unitsMom='[m.kN]'
Q1.unitsScaleForc=1e-3
Q1.unitsForc='[kN]'
Q1.setsToDispBeamIntForc=[]
Q1.listBeamIntForc=['My','Mz','Qy','Qz','N']
Q1.viewName="XYZPos"
Q1.setsToDispBeamLoads=[]
Q1.vectorScalePointLoads=0.005
Q1.compElLoad='transComponent'

Q2=graphical_reports.RecordLoadCaseDisp(loadCaseName='QearthPressWall',loadCaseDescr='Q2: earth pressure columns',loadCaseExpr='1.0*QearthPressWall',setsToDispLoads=[wall],setsToDispDspRot=[overallSet],setsToDispIntForc=[])
Q2.unitsScaleLoads=1e-3
Q2.unitsScaleDispl=1e3
Q2.unitsDispl='[mm]'
Q2.unitsScaleMom=1e-3
Q2.unitsMom='[m.kN]'
Q2.unitsScaleForc=1e-3
Q2.unitsForc='[kN]'
Q2.setsToDispBeamIntForc=[columnZ,beamX,beamY]
Q2.listBeamIntForc=['My','Mz','Qy','Qz','N']
Q2.viewName="XYZPos"
Q2.setsToDispBeamLoads=[overallSet]
Q2.vectorScalePointLoads=0.005
Q2.compElLoad='transComponent'


Q3=graphical_reports.RecordLoadCaseDisp(loadCaseName='QearthPressCols',loadCaseDescr='Q3: earth pressure columns',loadCaseExpr='1.0*QearthPressCols',setsToDispLoads=[overallSet],setsToDispDspRot=[decklv2],setsToDispIntForc=[])
Q3.unitsScaleLoads=1e-3
Q3.unitsScaleDispl=1e3
Q3.unitsDispl='[mm]'
Q3.unitsScaleMom=1e-3
Q3.unitsMom='[m.kN]'
Q3.unitsScaleForc=1e-3
Q3.unitsForc='[kN]'
Q3.setsToDispBeamIntForc=[columnZ,beamX,beamY]
Q3.listBeamIntForc=['My','Mz','Qy','Qz','N']
Q3.viewName="XYZPos"
Q3.setsToDispBeamLoads=[overallSet]
Q3.vectorScalePointLoads=0.005
Q3.compElLoad='transComponent'

Q4=graphical_reports.RecordLoadCaseDisp(loadCaseName='QearthPColsStrL',loadCaseDescr='Q4: earth pressure columns strip load',loadCaseExpr='1.0*QearthPColsStrL',setsToDispLoads=[overallSet],setsToDispDspRot=[overallSet],setsToDispIntForc=[])
Q4.unitsScaleLoads=1e-3
Q4.unitsScaleDispl=1e3
Q4.unitsDispl='[mm]'
Q4.unitsScaleMom=1e-3
Q4.unitsMom='[m.kN]'
Q4.unitsScaleForc=1e-3
Q4.unitsForc='[kN]'
Q4.setsToDispBeamIntForc=[columnZ,beamX,beamY]
Q4.listBeamIntForc=['My','Mz','Qy','Qz','N']
Q4.viewName="XYZPos"
Q4.setsToDispBeamLoads=[overallSet]
Q4.vectorScalePointLoads=0.005
Q4.compElLoad='transComponent'

Q5=graphical_reports.RecordLoadCaseDisp(loadCaseName='QearthPColsLinL',loadCaseDescr='Q5: earth pressure columns line load',loadCaseExpr='1.0*QearthPColsLinL',setsToDispLoads=[overallSet],setsToDispDspRot=[overallSet],setsToDispIntForc=[])
Q5.unitsScaleLoads=1e-3
Q5.unitsScaleDispl=1e3
Q5.unitsDispl='[mm]'
Q5.unitsScaleMom=1e-3
Q5.unitsMom='[m.kN]'
Q5.unitsScaleForc=1e-3
Q5.unitsForc='[kN]'
Q5.setsToDispBeamIntForc=[columnZ,beamX,beamY]
Q5.listBeamIntForc=['My','Mz','Qy','Qz','N']
Q5.viewName="XYZPos"
Q5.setsToDispBeamLoads=[overallSet]
Q5.vectorScalePointLoads=0.005
Q5.compElLoad='transComponent'

Q6=graphical_reports.RecordLoadCaseDisp(loadCaseName='QearthPColsHrzL',loadCaseDescr='Q6: earth pressure columns line load',loadCaseExpr='1.0*QearthPColsHrzL',setsToDispLoads=[overallSet],setsToDispDspRot=[overallSet],setsToDispIntForc=[])
Q6.unitsScaleLoads=1e-3
Q6.unitsScaleDispl=1e3
Q6.unitsDispl='[mm]'
Q6.unitsScaleMom=1e-3
Q6.unitsMom='[m.kN]'
Q6.unitsScaleForc=1e-3
Q6.unitsForc='[kN]'
Q6.setsToDispBeamIntForc=[columnZ,beamX,beamY]
Q6.listBeamIntForc=['My','Mz','Qy','Qz','N']
Q6.viewName="XYZPos"
Q6.setsToDispBeamLoads=[overallSet]
Q6.vectorScalePointLoads=0.005
Q6.compElLoad='transComponent'

Q7=graphical_reports.RecordLoadCaseDisp(loadCaseName='qunifBeams',loadCaseDescr='Q7: uniform load on beams',loadCaseExpr='1.0*qunifBeams',setsToDispLoads=[overallSet],setsToDispDspRot=[overallSet],setsToDispIntForc=[])
Q7.unitsScaleLoads=1e-3
Q7.unitsScaleDispl=1e3
Q7.unitsDispl='[mm]'
Q7.unitsScaleMom=1e-3
Q7.unitsMom='[m.kN]'
Q7.unitsScaleForc=1e-3
Q7.unitsForc='[kN]'
Q7.setsToDispBeamIntForc=[columnZ,beamX,beamY]
Q7.listBeamIntForc=['My','Mz','Qy','Qz','N']
Q7.viewName="XYZPos"
Q7.setsToDispBeamLoads=[overallSet]
Q7.vectorScalePointLoads=0.005
Q7.compElLoad='transComponent'

Q8=graphical_reports.RecordLoadCaseDisp(loadCaseName='qlinDeck',loadCaseDescr='Q8: linear load on deck level 2',loadCaseExpr='1.0*qlinDeck',setsToDispLoads=[decklv2],setsToDispDspRot=[overallSet],setsToDispIntForc=[])
Q8.unitsScaleLoads=1e-3
Q8.unitsScaleDispl=1e3
Q8.unitsDispl='[mm]'
Q8.unitsScaleMom=1e-3
Q8.unitsMom='[m.kN]'
Q8.unitsScaleForc=1e-3
Q8.unitsForc='[kN]'
Q8.setsToDispBeamIntForc=[columnZ,beamX,beamY]
Q8.listBeamIntForc=['My','Mz','Qy','Qz','N']
Q8.viewName="XYZPos"
Q8.vectorScalePointLoads=0.005

Q9=graphical_reports.RecordLoadCaseDisp(loadCaseName='QpntBeams',loadCaseDescr='Q9: point loads on beams',loadCaseExpr='1.0*QpntBeams',setsToDispLoads=[overallSet],setsToDispDspRot=[overallSet],setsToDispIntForc=[])
Q9.unitsScaleLoads=1e-3
Q9.unitsScaleDispl=1e3
Q9.unitsDispl='[mm]'
Q9.unitsScaleMom=1e-3
Q9.unitsMom='[m.kN]'
Q9.unitsScaleForc=1e-3
Q9.unitsForc='[kN]'
Q9.setsToDispBeamIntForc=[columnZ,beamX,beamY]
Q9.listBeamIntForc=['My','Mz','Qy','Qz','N']
Q9.setsToDispBeamLoads=[overallSet]
Q9.viewName="XYZPos"
Q9.vectorScalePointLoads=0.35

Q10=graphical_reports.RecordLoadCaseDisp(loadCaseName='QwheelDeck1',loadCaseDescr='Q10: load of a wheel over deck level 1',loadCaseExpr='1.0*QwheelDeck1',setsToDispLoads=[decklv1],setsToDispDspRot=[overallSet],setsToDispIntForc=[])
Q10.unitsScaleLoads=1e-3
Q10.unitsScaleDispl=1e3
Q10.unitsDispl='[mm]'
Q10.unitsScaleMom=1e-3
Q10.unitsMom='[m.kN]'
Q10.unitsScaleForc=1e-3
Q10.unitsForc='[kN]'
Q10.setsToDispBeamIntForc=[columnZ,beamX,beamY]
Q10.listBeamIntForc=['My','Mz','Qy','Qz','N']
Q10.setsToDispBeamLoads=[overallSet]
Q10.viewName="XYZPos"
Q10.vectorScalePointLoads=0.05

Q11=graphical_reports.RecordLoadCaseDisp(loadCaseName='QvehicleDeck1',loadCaseDescr='Q11: load of a vehicle over deck level 1',loadCaseExpr='1.0*QvehicleDeck1',setsToDispLoads=[overallSet],setsToDispDspRot=[overallSet],setsToDispIntForc=[])
Q11.unitsScaleLoads=1e-3
Q11.unitsScaleDispl=1e3
Q11.unitsDispl='[mm]'
Q11.unitsScaleMom=1e-3
Q11.unitsMom='[m.kN]'
Q11.unitsScaleForc=1e-3
Q11.unitsForc='[kN]'
Q11.setsToDispBeamIntForc=[columnZ,beamX,beamY]
Q11.listBeamIntForc=['My','Mz','Qy','Qz','N']
Q11.setsToDispBeamLoads=[overallSet]
Q11.viewName="XYZPos"
Q11.vectorScalePointLoads=0.05

Comb1=graphical_reports.RecordLoadCaseDisp(loadCaseName='LS1',loadCaseDescr='Comb1: combination 1 ',loadCaseExpr='1.0*LS1',setsToDispLoads=[overallSet],setsToDispDspRot=[overallSet],setsToDispIntForc=[allShells])
Comb1.unitsScaleLoads=1e-3
Comb1.unitsScaleDispl=1e3
Comb1.unitsDispl='[mm]'
Comb1.unitsScaleMom=1e-3
Comb1.unitsMom='[m.kN]'
Comb1.unitsScaleForc=1e-3
Comb1.unitsForc='[kN]'
Comb1.setsToDispBeamIntForc=[allBeams]
Comb1.listBeamIntForc=['My','Mz','Qy','Qz','N']
Comb1.setsToDispBeamLoads=[allBeams]
Comb1.compElLoad='transComponent'
Comb1.viewName="XYZPos"
Comb1.vectorScalePointLoads=0.05

Comb2=graphical_reports.RecordLoadCaseDisp(loadCaseName='LS2',loadCaseDescr='Comb2: combination 2 ',loadCaseExpr='1.0*LS2',setsToDispLoads=[overallSet],setsToDispDspRot=[overallSet],setsToDispIntForc=[allShells])
Comb2.unitsScaleLoads=1e-3
Comb2.unitsScaleDispl=1e3
Comb2.unitsDispl='[mm]'
Comb2.unitsScaleMom=1e-3
Comb2.unitsMom='[m.kN]'
Comb2.unitsScaleForc=1e-3
Comb2.unitsForc='[kN]'
Comb2.setsToDispBeamIntForc=[allBeams]
Comb2.listBeamIntForc=['My','Mz','Qy','Qz','N']
Comb2.setsToDispBeamLoads=[allBeams]
Comb2.compElLoad='transComponent'
Comb2.viewName="XYZPos"
Comb2.vectorScalePointLoads=0.05
