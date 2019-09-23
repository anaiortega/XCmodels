# -*- coding: utf-8 -*-
import os
from postprocess.xcVtk.FE_model import quick_graphics as QGrph
from postprocess.xcVtk import vtk_graphic_base

execfile('../model_gen.py')

lcs=QGrph.LoadCaseResults(feProblem=FEcase,loadCaseName='ULS1',loadCaseExpr='1.2*D+1.6*L+0.5*S')
lcs.solve()

nodes.calculateNodalReactions(True,1e-7)

print 'Node & R$_y$ & R$_z$ \\'
for n in anchorBase.getNodes:
    r=n.getReaction
    print n.tag, ' & ', round(r[1],2),  ' & ', round(r[2],2) , ' \\\\ '
print '\\hline'
for n in anchorTop.getNodes:
    r=n.getReaction
    print n.tag, ' & ', round(r[1],2),  ' & ', round(r[2],2) , ' \\\\ '
    
