# -*- coding: utf-8 -*-
import os

loadStates= ['LC1_deadLoadBearingStructure','LC2_deadLoadInterior','LC3_deadLoadFacade','LC51_windX','LC101_windY','LC201_snowRoof','LC202_snowAx1_2','LC203_snowAx2_3','LC204_snowAx3_4','LC205_snowAx4_5','LC206_snowAx5_6','LC1326_servRoof','LC1336_servRoof','LC1356_servRoof','LC1366_servRoof','LC10001_serv1','LC10011_serv1','LC10021_serv1','LC10031_serv1','LC10101_servParking','LC10111_servParking','LC10121_servParking','LC10131_servParking']

f=open('pp.txt','w')
for ld in loadStates:
    f.write(ld+"=graphical_reports.RecordLoadCaseDisp(loadCaseName='"+ld+"',loadCaseDescr='"+ld+"',loadCaseExpr='1.0*"+ld+"',setsToDispLoads=[xcTotalSet],setsToDispDspRot=[xcTotalSet],setsToDispIntForc=[shellSet]) \n" +
ld+".unitsScaleLoads=1 \n"+
ld+".vectorScaleLoads=0.2 \n"+
ld+".unitsScaleDispl=1e3 \n"+
ld+".unitsDispl='[mm]' \n"+
ld+".unitsScaleMom=1 \n"+
ld+".unitsMom='[m.kN]' \n"+
ld+".unitsScaleForc=1 \n"+
ld+".unitsForc='[kN]' \n"+
ld+".setsToDispBeamIntForc=[columnsSet] \n"+
ld+".listBeamIntForc=['My','Mz','Qy','Qz','N'] \n"+
ld+".scaleDispBeamIntForc=1.5 \n"+
ld+".viewName='XPos' \n"+
ld+".setsToDispBeamLoads=[columnsSet] \n"+
ld+".vectorScalePointLoads=0.005 \n"+
ld+".compElLoad='transComponent' \n \n"
)
f.close()
