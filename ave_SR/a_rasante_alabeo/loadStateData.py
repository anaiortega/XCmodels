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
  cameraParameters: parameters that define the position and orientation of the
                 camera (defaults to "XYZPos")
  
  cameraParametersBeams: parameters that define the position and orientation of the
                 camera for beam elements displays (defaults to "XYZPos")
  
'''

Q1a=graphical_reports.LoadCaseDispParameters(loadCaseName='Q1a',loadCaseDescr='Q1a: Tren de cargas centrado en ambas vías',loadCaseExpr='1.0*Q1a',setsToDispLoads=[marco],setsToDispDspRot=[dintel],setsToDispIntForc=[])
Q1a.unitsScaleLoads=1e-3
Q1a.unitsScaleDispl=1e3
Q1a.unitsDispl='[mm]'
Q1a.unitsScaleMom=1e-3
Q1a.unitsMom='[m.kN]'
Q1a.unitsScaleForc=1e-3
Q1a.unitsForc='[kN]'
Q1a.cameraParameters= vtk_graphic_base.CameraParameters('ZPos')


Q1a1via=graphical_reports.LoadCaseDispParameters(loadCaseName='Q1a1via',loadCaseDescr='Q1a1via: Tren de cargas centrado en una sola vía',loadCaseExpr='1.0*Q1a1via',setsToDispLoads=[marco],setsToDispDspRot=[dintel],setsToDispIntForc=[])
Q1a1via.unitsScaleLoads=1e-3
Q1a1via.unitsScaleDispl=1e3
Q1a1via.unitsDispl='[mm]'
Q1a1via.unitsScaleMom=1e-3
Q1a1via.unitsMom='[m.kN]'
Q1a1via.unitsScaleForc=1e-3
Q1a1via.unitsForc='[kN]'
Q1a1via.cameraParameters= vtk_graphic_base.CameraParameters('ZPos')


Q1a_alabTot=graphical_reports.LoadCaseDispParameters(loadCaseName='Q1a_alabTot',loadCaseDescr='Q1a_alabTot: Cargas permanentes + tren de cargas centrado en ambas vías',loadCaseExpr='1.0*G1+1.0*G2a+1.0*G3+1.0*Q1a',setsToDispLoads=[marco],setsToDispDspRot=[dintel],setsToDispIntForc=[])
Q1a_alabTot.unitsScaleLoads=1e-3
Q1a_alabTot.unitsScaleDispl=1e3
Q1a_alabTot.unitsDispl='[mm]'
Q1a_alabTot.unitsScaleMom=1e-3
Q1a_alabTot.unitsMom='[m.kN]'
Q1a_alabTot.unitsScaleForc=1e-3
Q1a_alabTot.unitsForc='[kN]'
Q1a_alabTot.cameraParameters= vtk_graphic_base.CameraParameters('ZPos')


Q1a1via_alabTot=graphical_reports.LoadCaseDispParameters(loadCaseName='Q1a1via_alabTot',loadCaseDescr='Q1a1via_alabTot: Cargas permanentes + tren de cargas centrado en una sola vía',loadCaseExpr='1.0*G1+1.0*G2a+1.0*G3+1.0*Q1a1via',setsToDispLoads=[marco],setsToDispDspRot=[dintel],setsToDispIntForc=[])
Q1a1via_alabTot.unitsScaleLoads=1e-3
Q1a1via_alabTot.unitsScaleDispl=1e3
Q1a1via_alabTot.unitsDispl='[mm]'
Q1a1via_alabTot.unitsScaleMom=1e-3
Q1a1via_alabTot.unitsMom='[m.kN]'
Q1a1via_alabTot.unitsScaleForc=1e-3
Q1a1via_alabTot.unitsForc='[kN]'
Q1a1via_alabTot.cameraParameters= vtk_graphic_base.CameraParameters('ZPos')


