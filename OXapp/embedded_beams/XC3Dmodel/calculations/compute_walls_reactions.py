# -*- coding: utf-8 -*-
import os
from postprocess.xcVtk.FE_model import quick_graphics as QGrph
import csv

execfile('../model_gen.py')
execfile('../load_state_data.py')
execfile('../wall_nodes.py')

#ordered list of load cases (from those defined in ../load_state_data.py
#or redefined lately) to be displayed:
loadCases=[D,L,S,W_WE,W_NS]

#End data

csvFileNorth= open("wall_North_reactions.csv", "w")
writerNorth = csv.writer(csvFileNorth)
csvFileSouth= open("wall_South_reactions.csv", "w")
writerSouth = csv.writer(csvFileSouth)
csvFileEast= open("wall_East_reactions.csv", "w")
writerEast = csv.writer(csvFileEast)
csvFileWest= open("wall_West_reactions.csv", "w")
writerWest = csv.writer(csvFileWest)

for lc in loadCases:
    lcs=QGrph.QuickGraphics(FEcase)
    #solve for load case
    lcs.solve(loadCaseName=lc.loadCaseName,loadCaseExpr=lc.loadCaseExpr)
    #Reaction on column bases
    nodes.calculateNodalReactions(False,1e-7)
    for n in wallNorth:
        reac= n.getReaction
        row= [n.tag, lc.loadCaseName, reac[2]]
        writerNorth.writerow(row)
    for n in wallSouth:
        reac= n.getReaction
        row= [n.tag, lc.loadCaseName, reac[2]]
        writerSouth.writerow(row)
    for n in wallEast:
        reac= n.getReaction
        row= [n.tag, lc.loadCaseName, reac[2]]
        writerEast.writerow(row)
    for n in wallWest:
        reac= n.getReaction
        row= [n.tag, lc.loadCaseName, reac[2]]
        writerWest.writerow(row)

csvFileNorth.close()
csvFileSouth.close()
csvFileEast.close()
csvFileWest.close()



            
