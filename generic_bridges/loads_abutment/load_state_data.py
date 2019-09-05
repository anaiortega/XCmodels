# -*- coding: utf-8 -*-
#Earth pressures
G4=graphical_reports.RecordLoadCaseDisp(loadCaseName='G4',loadCaseDescr='G4: empuje del relleno',loadCaseExpr='1.0*G4',setsToDispLoads=[overallSet],setsToDispDspRot=[overallSet],setsToDispIntForc=[])

Q4=graphical_reports.RecordLoadCaseDisp(loadCaseName='Q4',loadCaseDescr='Q4: sobrecarga sobre relleno trasdós',loadCaseExpr='1.0*Q4',setsToDispLoads=[overallSet],setsToDispDspRot=[overallSet],setsToDispIntForc=[])

LSDabut=[G4,Q4]
for lc in LSDabut:
    lc.unitsScaleLoads=1e-3
    lc.unitsScaleDispl=1e3
    lc.unitsDispl='[mm]'
    lc.unitsScaleMom=1e-3
    lc.unitsMom='[m.kN]'
    lc.unitsScaleForc=1e-3
    lc.unitsForc='[kN]'
    lc.cameraParameters= vtk_graphic_base.CameraParameters('XYZPos')

