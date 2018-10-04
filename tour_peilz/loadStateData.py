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
G1=graphical_reports.RecordLoadCaseDisp(loadCaseName='selfWeight',loadCaseDescr='G1: self weight',loadCaseExpr='1.0*selfWeight',setsToDispLoads=[shell_elements],setsToDispDspRot=[],setsToDispIntForc=[])
G1.unitsScaleLoads= 1e-3
G1.unitsScaleForc= 1e-3
G1.unitsScaleMom= 1e-3
G1.unitsScaleDispl= 1e3
G1.vectorScaleLoads= 0.1
#G1.viewName= "-X+Y+Z"
G1.unitsDispl='[mm]'

G2=graphical_reports.RecordLoadCaseDisp(loadCaseName='deadLoad',loadCaseDescr='G2: self weight',loadCaseExpr='1.0*deadLoad',setsToDispLoads=[shell_elements],setsToDispDspRot=[shell_elements],setsToDispIntForc=[shell_elements])
G2.unitsScaleLoads= 1e-3
G2.unitsScaleForc= 1e-3
G2.unitsScaleMom= 1e-3
G2.unitsScaleDispl= 1e3
G2.vectorScaleLoads= 0.25
#G2.viewName= "-X+Y+Z"
G2.unitsDispl='[mm]'

G3=graphical_reports.RecordLoadCaseDisp(loadCaseName='earthPressure',loadCaseDescr='G3: earth pressure',loadCaseExpr='1.0*earth_pressure',setsToDispLoads=[shell_elements],setsToDispDspRot=[shell_elements],setsToDispIntForc=[shell_elements])
G3.unitsScaleLoads= 1e-3
G3.unitsScaleForc= 1e-3
G3.unitsScaleMom= 1e-3
G3.unitsScaleDispl= 1e3
G3.vectorScaleLoads= 0.05
#G3.viewName= "-X+Y+Z"
G3.unitsDispl='[mm]'

Q1=graphical_reports.RecordLoadCaseDisp(loadCaseName='pedestrianLoad',loadCaseDescr='Q1: live load A',loadCaseExpr='1.0*pedestrianLoad',setsToDispLoads=[shell_elements],setsToDispDspRot=[],setsToDispIntForc=[])
Q1.unitsScaleLoads= 1e-3
Q1.unitsScaleForc= 1e-3
Q1.unitsScaleMom= 1e-3
Q1.unitsScaleDispl= 1e3
Q1.vectorScaleLoads= 0.2
Q1.viewName= "-X-Y+Z"
Q1.unitsDispl='[mm]'

Q2=graphical_reports.RecordLoadCaseDisp(loadCaseName='singleAxeLoad',loadCaseDescr='Q2: live load B',loadCaseExpr='1.0*singleAxeLoad',setsToDispLoads=[shell_elements],setsToDispDspRot=[],setsToDispIntForc=[])
Q2.unitsScaleLoads= 1e-3
Q2.unitsScaleForc= 1e-3
Q2.unitsScaleMom= 1e-3
Q2.unitsScaleDispl= 1e3
Q2.vectorScaleLoads= 0.05
#Q2.viewName= "-X+Y+Z"
Q2.unitsDispl='[mm]'

Q3=graphical_reports.RecordLoadCaseDisp(loadCaseName='LM1',loadCaseDescr='Q3: earth pressure from rail load',loadCaseExpr='1.0*LM1',setsToDispLoads=[shell_elements],setsToDispDspRot=[],setsToDispIntForc=[])
Q3.unitsScaleLoads= 1e-3
Q3.unitsScaleForc= 1e-3
Q3.unitsScaleMom= 1e-3
Q3.unitsScaleDispl= 1e3
Q3.vectorScaleLoads= 0.3
Q3.viewName= "-X-Y+Z"
Q3.unitsDispl='[mm]'

Q4=graphical_reports.RecordLoadCaseDisp(loadCaseName='nosingLoad',loadCaseDescr='Q4: earth pressure from nosing load',loadCaseExpr='1.0*nosingLoad',setsToDispLoads=[shell_elements],setsToDispDspRot=[],setsToDispIntForc=[])
Q4.unitsScaleLoads= 1e-3
Q4.unitsScaleForc= 1e-3
Q4.unitsScaleMom= 1e-3
Q4.unitsScaleDispl= 1e3
Q4.vectorScaleLoads= 1
Q4.viewName= "-X-Y+Z"
Q4.unitsDispl='[mm]'

Q5=graphical_reports.RecordLoadCaseDisp(loadCaseName='roadTrafficLoad',loadCaseDescr='Q5: earth pressure from road traffic load',loadCaseExpr='1.0*roadTrafficLoad',setsToDispLoads=[shell_elements],setsToDispDspRot=[],setsToDispIntForc=[])
Q5.unitsScaleLoads= 1e-3
Q5.unitsScaleForc= 1e-3
Q5.unitsScaleMom= 1e-3
Q5.unitsScaleDispl= 1e3
Q5.vectorScaleLoads= 0.25
#Q5.viewName= "-X-Y+Z"
Q5.unitsDispl='[mm]'

A1=graphical_reports.RecordLoadCaseDisp(loadCaseName='earthquake',loadCaseDescr='A1: earthquake',loadCaseExpr='1.0*earthquake',setsToDispLoads=[shell_elements],setsToDispDspRot=[shell_elements],setsToDispIntForc=[shell_elements])
A1.unitsScaleLoads= 1e-3
A1.unitsScaleForc= 1e-3
A1.unitsScaleMom= 1e-3
A1.unitsScaleDispl= 1e3
A1.vectorScaleLoads= 0.1
#A1.viewName= "-X+Y+Z"
A1.unitsDispl='[mm]'

lcDisplays= {}
#Quasi-permanent situations.
for key in combContainer.SLS.qp:
    comb= combContainer.SLS.qp[key]
    lcDisplays[key]= comb.getRecordLoadCaseDisp(setsToDispLoads=[shell_elements],setsToDispDspRot=[shell_elements],setsToDispIntForc=[shell_elements])

#Frequent
for key in combContainer.SLS.freq:
    comb= combContainer.SLS.freq[key]
    lcDisplays[key]= comb.getRecordLoadCaseDisp(setsToDispLoads=[shell_elements],setsToDispDspRot=[shell_elements],setsToDispIntForc=[shell_elements])

#Rare
for key in combContainer.SLS.rare:
    comb= combContainer.SLS.rare[key]
    lcDisplays[key]= comb.getRecordLoadCaseDisp(setsToDispLoads=[shell_elements],setsToDispDspRot=[shell_elements],setsToDispIntForc=[shell_elements])

#Permanent and transitory situations.
for key in combContainer.ULS.perm:
    comb= combContainer.ULS.perm[key]
    lcDisplays[key]= comb.getRecordLoadCaseDisp(setsToDispLoads=[shell_elements],setsToDispDspRot=[shell_elements],setsToDispIntForc=[shell_elements])
