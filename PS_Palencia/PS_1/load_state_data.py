# -*- coding: utf-8 -*-
from postprocess.xcVtk import vtk_graphic_base
from postprocess.reports import graphical_reports

#Dead load cases
G2=graphical_reports.RecordLoadCaseDisp(loadCaseName='G2',loadCaseDescr='G2: carga muerta',loadCaseExpr='1.0*G2',setsToDispLoads=[overallSet],setsToDispDspRot=[overallSet],setsToDispIntForc=[])
#Rheological load cases
G3=graphical_reports.RecordLoadCaseDisp(loadCaseName='G3',loadCaseDescr='G3: acciones reológicas',loadCaseExpr='1.0*G3',setsToDispLoads=[overallSet],setsToDispDspRot=[overallSet],setsToDispIntForc=[])

#Traffic load cases
Q1a1=graphical_reports.RecordLoadCaseDisp(loadCaseName='Q1a1',loadCaseDescr='Q1a1: tren de cargas, posición A1',loadCaseExpr='1.0*Q1a1',setsToDispLoads=[overallSet],setsToDispDspRot=[overallSet],setsToDispIntForc=[])
Q1a2=graphical_reports.RecordLoadCaseDisp(loadCaseName='Q1a2',loadCaseDescr='Q1a2: tren de cargas, posición A2',loadCaseExpr='1.0*Q1a2',setsToDispLoads=[overallSet],setsToDispDspRot=[overallSet],setsToDispIntForc=[])
Q1b1=graphical_reports.RecordLoadCaseDisp(loadCaseName='Q1b1',loadCaseDescr='Q1b1: tren de cargas, posición B1',loadCaseExpr='1.0*Q1b1',setsToDispLoads=[overallSet],setsToDispDspRot=[overallSet],setsToDispIntForc=[])
Q1b2=graphical_reports.RecordLoadCaseDisp(loadCaseName='Q1b2',loadCaseDescr='Q1b2: tren de cargas, posición B2',loadCaseExpr='1.0*Q1b2',setsToDispLoads=[overallSet],setsToDispDspRot=[overallSet],setsToDispIntForc=[])
Q1c=graphical_reports.RecordLoadCaseDisp(loadCaseName='Q1c',loadCaseDescr='Q1c: tren de cargas, posición C',loadCaseExpr='1.0*Q1c',setsToDispLoads=[overallSet],setsToDispDspRot=[overallSet],setsToDispIntForc=[])
Q1d=graphical_reports.RecordLoadCaseDisp(loadCaseName='Q1d',loadCaseDescr='Q1d: tren de cargas, posición D',loadCaseExpr='1.0*Q1d',setsToDispLoads=[overallSet],setsToDispDspRot=[overallSet],setsToDispIntForc=[])
Q1e=graphical_reports.RecordLoadCaseDisp(loadCaseName='Q1e',loadCaseDescr='Q1e: tren de cargas, posición D',loadCaseExpr='1.0*Q1e',setsToDispLoads=[overallSet],setsToDispDspRot=[overallSet],setsToDispIntForc=[])

Q1bFren=graphical_reports.RecordLoadCaseDisp(loadCaseName='Q1bFren',loadCaseDescr='Q1bFren: tren de cargas, posición B1 + frenado',loadCaseExpr='1.0*Q1bFren',setsToDispLoads=[overallSet],setsToDispDspRot=[overallSet],setsToDispIntForc=[])
Q1dFren=graphical_reports.RecordLoadCaseDisp(loadCaseName='Q1dFren',loadCaseDescr='Q1dFren: tren de cargas, posición D + frenado',loadCaseExpr='1.0*Q1dFren',setsToDispLoads=[overallSet],setsToDispDspRot=[overallSet],setsToDispIntForc=[])
Q1eFren=graphical_reports.RecordLoadCaseDisp(loadCaseName='Q1eFren',loadCaseDescr='Q1eFren: tren de cargas, posición D + frenado',loadCaseExpr='1.0*Q1eFren',setsToDispLoads=[overallSet],setsToDispDspRot=[overallSet],setsToDispIntForc=[])

#Thermal load cases
Q31=graphical_reports.RecordLoadCaseDisp(loadCaseName='Q31',loadCaseDescr='Q31: Temperatura uniforme, contracción',loadCaseExpr='1.0*Q31',setsToDispLoads=[overallSet],setsToDispDspRot=[overallSet],setsToDispIntForc=[])
Q32=graphical_reports.RecordLoadCaseDisp(loadCaseName='Q32',loadCaseDescr='Q32: Temperatura uniforme, dilatación',loadCaseExpr='1.0*Q32',setsToDispLoads=[],setsToDispDspRot=[overallSet],setsToDispIntForc=[])
Q31neopr=graphical_reports.RecordLoadCaseDisp(loadCaseName='Q31neopr',loadCaseDescr='Q31neopr: Temperatura uniforme, contracción',loadCaseExpr='1.0*Q31neopr',setsToDispLoads=[overallSet],setsToDispDspRot=[overallSet],setsToDispIntForc=[])
Q32neopr=graphical_reports.RecordLoadCaseDisp(loadCaseName='Q32neopr',loadCaseDescr='Q32neopr: Temperatura uniforme, dilatación',loadCaseExpr='1.0*Q32neopr',setsToDispLoads=[],setsToDispDspRot=[overallSet],setsToDispIntForc=[])


LSD=[G2,G3,Q1a1,Q1a2,Q1b1,Q1b2,Q1c,Q1d,Q1e,Q1bFren,Q1dFren,Q1eFren,Q31,Q32,Q31neopr,Q32neopr]

for lc in LSD:
    lc.unitsScaleLoads=1e-3
    lc.unitsScaleDispl=1e3
    lc.unitsDispl='[mm]'
    lc.unitsScaleMom=1e-3
    lc.unitsMom='[m.kN]'
    lc.unitsScaleForc=1e-3
    lc.unitsForc='[kN]'
    lc.cameraParameters= vtk_graphic_base.CameraParameters('XYZPos')
