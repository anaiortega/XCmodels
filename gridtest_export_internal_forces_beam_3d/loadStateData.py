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
  viewName:  name of the view  that contains the renderer (possible
                 options: "XYZPos", "XPos", "XNeg","YPos", "YNeg",
                 "ZPos", "ZNeg") (defaults to "XYZPos")

'''
G1=graphical_reports.RecordLoadCaseDisp(loadCaseName='GselfWeight',loadCaseDescr='G1: self weight',loadCaseExpr='1.0*GselfWeight',setsToDispLoads=[colsSet],setsToDispDspRot=[colsSet],setsToDispIntForc=[colsSet])
G1.unitsScaleDispl=1e3
G1.unitsDispl='[mm]'
G1.unitsScaleLoads=1e-3
G1.unitsScaleMom=1e-3
Q1=graphical_reports.RecordLoadCaseDisp(loadCaseName='Qwind',loadCaseDescr='Q1: wind',loadCaseExpr='1.0*Qwind',setsToDispLoads=[colsSet],setsToDispDspRot=[colsSet],setsToDispIntForc=[colsSet])
Q1.unitsScaleDispl=1e3
Q1.unitsDispl='[mm]'
Q1.unitsScaleLoads=1e-3
Q1.unitsScaleMom=1e-3
A1=graphical_reports.RecordLoadCaseDisp(loadCaseName='AvehicCrash',loadCaseDescr='A1: vehicle crash',loadCaseExpr='1.0*AvehicCrash',setsToDispLoads=[colsSet],setsToDispDspRot=[colsSet],setsToDispIntForc=[colsSet])
Q1.unitsScaleDispl=1e3
Q1.unitsDispl='[mm]'
Q1.unitsScaleLoads=1e-3
Q1.unitsScaleMom=1e-3

