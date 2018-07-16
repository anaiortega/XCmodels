#Linear bearings. Coordinates imported from FreeCAD model 
#short side
freecad_points_ss=[[39719.0585938,13598.6582031,0.0],[39726.2617188,13596.6875,0.0],[39739.640625,13593.7138672,0.0],[39754.6914062,13592.0419922,0.0],[39771.0429688,13590.7412109,0.0],[39785.5351562,13590.7412109,0.0],[39806.7148438,13591.2988281,0.0],[39829.7539062,13591.6708984,0.0],[39851.8671875,13592.4140625,0.0],[39873.4179688,13592.5996094,0.0],[39886.0546875,13592.9707031,0.0],[39902.03125,13595.7578125,0.0],[39907.7929688,13597.6162109,0.0],[39911.3242188,13598.7314453,0.0]]

#long side
freecad_points_ls=[[39671.0390625,13517.5419922,0.0],[39677.9140625,13522.9296875,0.0],[39689.0625,13529.0615234,0.0],[39701.5117188,13535.5644531,0.0],[39717.6757812,13540.953125,0.0],[39733.8398438,13543.9257812,0.0],[39746.8476562,13544.6689453,0.0],[39771.0,13543.9257812,0.0],[39795.5273438,13544.296875,0.0],[39812.671875,13543.6523438,0.0],[39831.9609375,13543.6523438,0.0],[39852.6132812,13542.7441406,0.0],[39870.9921875,13543.1982422,0.0],[39895.5039062,13542.0634766,0.0],[39913.8867188,13541.3828125,0.0],[39924.5507812,13540.7021484,0.0],[39936.125,13537.5253906,0.0],[39947.4726562,13531.3974609,0.0],[39955.6445312,13524.5888672,0.0],[39959.5,13518.2353516,0.0]]

#transformation from FreeCAD points to model coordinates
shortSide_coord=[[-(i[1]-13599)/10.,(i[0]-39667)/10.] for i in freecad_points_ss]
longSide_coord=[[-(i[1]-13599)/10.,(i[0]-39667)/10.] for i in freecad_points_ls]

mesh= FEcase.getDomain.getMesh
constraints=prep.getBoundaryCondHandler
#Constraint uz=0 in short side linear bearing.
for coo in shortSide_coord:
    n=mesh.getNearestNode(geom.Pos3d(coo[0],coo[1],0))
    constraints.newSPConstraint(n.tag,2,0.0) #uz=0 
#Constraint uz=0 in long side linear bearing.
for coo in longSide_coord:
    n=mesh.getNearestNode(geom.Pos3d(coo[0],coo[1],0))
    constraints.newSPConstraint(n.tag,2,0.0) #uz=0 

# Constraint uy=0 in the left linear side
r=gm.IJKRange((0,0,0),(lastXpos,0,0))
pt_left=gridDeck.getSetPntRange(r,'pt_left')
for pt in pt_left.getPoints:
    n=pt.getNode()
    constraints.newSPConstraint(n.tag,1,0.0) #uy=0
