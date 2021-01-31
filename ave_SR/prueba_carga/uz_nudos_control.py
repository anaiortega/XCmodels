# -*- coding: utf-8 -*-
import os
from postprocess.xcVtk.FE_model import quick_graphics as QGrph

exec(open('./model_data.py').read()))
exec(open('./loadStateData.py').read()))

#ordered list of load cases (from those defined in ../loadStateData.py
#or redefined lately) to be displayed:

lcs=QGrph.LoadCaseResults(FEcase)
lcs.solve(loadCaseName=Q1.loadCaseName,loadCaseExpr=Q1.loadCaseExpr)

import geom

pPto1=geom.Pos3d(0,0,zList[-1])
pPto2=geom.Pos3d(Lmarco/2.0-5.0,0,zList[-1])
pPto3=geom.Pos3d(Lmarco/2.0,0,zList[-1])
pPto4=geom.Pos3d(Lmarco/2.0+4.0,0,zList[-1])
pPto5=geom.Pos3d(Lmarco,0,zList[-1])

n1=dintel.getNearestNode(pPto1)
n2=dintel.getNearestNode(pPto2)
n3=dintel.getNearestNode(pPto3)
n4=dintel.getNearestNode(pPto4)
n5=dintel.getNearestNode(pPto5)

print 'pto 1: ', 'X=',n1.get3dCoo[0],'Y=',n1.get3dCoo[1], 'Z=',n1.get3dCoo[2], 'uZ=', round(n1.getDisp[2]*1e3,2), '\n'
print 'pto 2: ', 'X=',n2.get3dCoo[0],'Y=',n2.get3dCoo[1], 'Z=',n2.get3dCoo[2], 'uZ=', round(n2.getDisp[2]*1e3,2), '\n'
print 'pto 3: ', 'X=',n3.get3dCoo[0],'Y=',n3.get3dCoo[1], 'Z=',n3.get3dCoo[2], 'uZ=', round(n3.getDisp[2]*1e3,2), '\n'
print 'pto 4: ', 'X=',n4.get3dCoo[0],'Y=',n4.get3dCoo[1], 'Z=',n4.get3dCoo[2], 'uZ=', round(n4.getDisp[2]*1e3,2), '\n'
print 'pto 5: ', 'X=',n5.get3dCoo[0],'Y=',n5.get3dCoo[1], 'Z=',n5.get3dCoo[2], 'uZ=', round(n5.getDisp[2]*1e3,2), '\n'
