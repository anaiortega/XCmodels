# -*- coding: utf-8 -*-
from model.geometry import geom_utils as gut

# grid model definition
gridGeomAbutment= gm.GridModel(prep,xListAbut,yListAbut,zListAbut)

# Grid geometric entities definition (points, lines, surfaces)
# Points' generation
gridGeomAbutment.generatePoints()

#Displacements of the grid points in a range
#syntax: movePointsRange(ijkRange,vDisp)
#        ijkRange: range for the search
#        vDisp: xc vector displacement
if Lvoladzi >0:
    r= gut.def_rg_cooLim(XYZListsAbut,Xaleti,(yVoladz,yVoladz),(zArrVoladz,zArrVoladz))
    gridGeomAbutment.movePointsRange(r,xc.Vector([0.0,0.0,(Hmaxvoladzi-Hminvoladzi)]))
    r= gut.def_rg_cooLim(XYZListsAbut,Xaleti,(yVoladz,yVoladz),(zMur,zMur))
    gridGeomAbutment.movePointsRange(r,xc.Vector([0.0,0.0,(Hmaxvoladzi-Hminvoladzi)/Hmaxvoladzi*hMuret]))

if Lvoladzd >0:
    r= gut.def_rg_cooLim(XYZListsAbut,Xaletd,(yVoladz,yVoladz),(zArrVoladz,zArrVoladz))
    gridGeomAbutment.movePointsRange(r,xc.Vector([0.0,0.0,(Hmaxvoladzd-Hminvoladzd)]))
    r= gut.def_rg_cooLim(XYZListsAbut,Xaletd,(yVoladz,yVoladz),(zMur,zMur))
    gridGeomAbutment.movePointsRange(r,xc.Vector([0.0,0.0,(Hmaxvoladzd-Hminvoladzd)/Hmaxvoladzd*hMuret]))

#Slope (in X direction, Y direction or both) the grid points in a range
#syntax: slopePointsRange(ijkRange,slopeX,xZeroSlope,slopeY,yZeroSlope)
#     ijkRange: range for the search.
#     slopeX: slope in X direction, expressed as deltaZ/deltaX 
#                       (defaults to 0 = no slope applied)
#     xZeroSlope: coordinate X of the "rotation axis".
#     slopeY: slope in Y direction, expressed as deltaZ/deltaY)
#                       (defaults to 0 = no slope applied)
#     yZeroSlope: coordinate Y of the "rotation axis".
if Lvoladzi >0:
    r=gut.def_rg_cooLim(XYZListsAbut,Xmurestr,(yPuntera,yVoladz),(zMur,zAlet))
    gridGeomAbutment.slopePointsRange(ijkRange=r,slopeX=(hMurd-hMuri)/anchoEstr,xZeroSlope=xAletaI)
else:
    r=gut.def_rg_cooLim(XYZListsAbut,Xmurestr,(yPuntera,yVoladz),(zMur,zAlet))
    gridGeomAbutment.slopePointsRange(ijkRange=r,slopeX=(hMuri-hMurd)/anchoEstr,xZeroSlope=xAletaD)
    
if angMuri <>0:
    r=gut.def_rg_cooLim(XYZListsAbut,(xAletaI,xAletaI),(yListAbut[0],yListAbut[-1]),(zListAbut[0],zListAbut[-1]))
    gridGeomAbutment.rotPntsZAxis(ijkRange=r,angle=angMuri,xyRotCent=[xAletaI,yMurEstr])

if angMurd <>0:
    print 'angmd=', angMurd
    r=gut.def_rg_cooLim(XYZListsAbut,(xAletaD,xAletaD),(yListAbut[0],yListAbut[-1]),(zListAbut[0],zListAbut[-1]))
    gridGeomAbutment.rotPntsZAxis(ijkRange=r,angle=angMurd,xyRotCent=[xAletaD,yMurEstr])


#Ranges for lines and surfaces
zap_rg=[gut.def_rg_cooLim(XYZListsAbut,Xmurestr,Yzap,(zZap,zZap))]

murestrZ1_rg=[gut.def_rg_cooLim(XYZListsAbut,Xmurestr,Ymurestr,zZ1)]
murestrZ2_rg=[gut.def_rg_cooLim(XYZListsAbut,Xmurestr,Ymurestr,zZ2mur)]

aletiZ1_rg=[gut.def_rg_cooLim(XYZListsAbut,Xaleti,Yalet,zZ1)]
aletiZ2_rg=[gut.def_rg_cooLim(XYZListsAbut,Xaleti,Yalet,zZ2alet)]
aletiZ3_rg=[gut.def_rg_cooLim(XYZListsAbut,Xaleti,Yalet,zZ3alet)]

aletdZ1_rg=[gut.def_rg_cooLim(XYZListsAbut,Xaletd,Yalet,zZ1)]
aletdZ2_rg=[gut.def_rg_cooLim(XYZListsAbut,Xaletd,Yalet,zZ2alet)]
aletdZ3_rg=[gut.def_rg_cooLim(XYZListsAbut,Xaletd,Yalet,zZ3alet)]

if Lvoladzi >0:
    voladzi_rg=[gut.def_rg_cooLim(XYZListsAbut,Xaleti,(yZap,yVoladz),zZ3alet)]

if Lvoladzd >0:
    voladzd_rg=[gut.def_rg_cooLim(XYZListsAbut,Xaletd,(yZap,yVoladz),zZ3alet)]
#Surfaces generation
zap=gridGeomAbutment.genSurfMultiRegion(lstIJKRange=zap_rg,nameSet='zap')
murestrZ1=gridGeomAbutment.genSurfMultiRegion(lstIJKRange=murestrZ1_rg,nameSet='murestrZ1')
murestrZ2=gridGeomAbutment.genSurfMultiRegion(lstIJKRange=murestrZ2_rg,nameSet='murestrZ2')

aletiZ1=gridGeomAbutment.genSurfMultiRegion(lstIJKRange=aletiZ1_rg,nameSet='aletiZ1')
aletiZ2=gridGeomAbutment.genSurfMultiRegion(lstIJKRange=aletiZ2_rg,nameSet='aletiZ2')
aletiZ3=gridGeomAbutment.genSurfMultiRegion(lstIJKRange=aletiZ3_rg,nameSet='aletiZ3')

aletdZ1=gridGeomAbutment.genSurfMultiRegion(lstIJKRange=aletdZ1_rg,nameSet='aletdZ1')
aletdZ2=gridGeomAbutment.genSurfMultiRegion(lstIJKRange=aletdZ2_rg,nameSet='aletdZ2')
aletdZ3=gridGeomAbutment.genSurfMultiRegion(lstIJKRange=aletdZ3_rg,nameSet='aletdZ3')

if Lvoladzi >0:
    voladzi=gridGeomAbutment.genSurfMultiRegion(lstIJKRange=voladzi_rg,nameSet='voladzi')
if Lvoladzd >0:
    voladzd=gridGeomAbutment.genSurfMultiRegion(lstIJKRange=voladzd_rg,nameSet='voladzd')


#                         *** MATERIALS ***
concrete=EHE_materials.HA30
concrData=tm.MaterialData(name='concrData',E=concrete.Ecm(),nu=concrete.nuc,rho=concrete.density())

# Isotropic elastic section-material appropiate for plate and shell analysis
zap_mat=tm.DeckMaterialData(name='zap_mat',thickness= cantoZap,material=concrData)
zap_mat.setupElasticSection(preprocessor=prep)   #creates the section-material

murestr_mat=tm.DeckMaterialData(name='murestr_mat',thickness=espMurEstr,material=concrData)
murestr_mat.setupElasticSection(preprocessor=prep)   #creates the section-material

aletiZ1_mat=tm.DeckMaterialData(name='aletiZ1_mat',thickness=espAletiZ1,material=concrData)
aletiZ1_mat.setupElasticSection(preprocessor=prep)
aletiZ2_mat=tm.DeckMaterialData(name='aletiZ2_mat',thickness=espAletiZ2,material=concrData)
aletiZ2_mat.setupElasticSection(preprocessor=prep)
aletiZ3_mat=tm.DeckMaterialData(name='aletiZ3_mat',thickness=espAletiZ3,material=concrData)
aletiZ3_mat.setupElasticSection(preprocessor=prep)

aletdZ1_mat=tm.DeckMaterialData(name='aletdZ1_mat',thickness=espAletdZ1,material=concrData)
aletdZ1_mat.setupElasticSection(preprocessor=prep)
aletdZ2_mat=tm.DeckMaterialData(name='aletdZ2_mat',thickness=espAletdZ2,material=concrData)
aletdZ2_mat.setupElasticSection(preprocessor=prep)
aletdZ3_mat=tm.DeckMaterialData(name='aletdZ3_mat',thickness=espAletdZ3,material=concrData)
aletdZ3_mat.setupElasticSection(preprocessor=prep)


#                         ***FE model - MESH***


zap_mesh=fem.SurfSetToMesh(surfSet=zap,matSect=zap_mat,elemSize=eSizeAbut,elemType='ShellMITC4')

murestrZ1_mesh=fem.SurfSetToMesh(surfSet=murestrZ1,matSect=murestr_mat,elemSize=eSizeAbut,elemType='ShellMITC4')
murestrZ2_mesh=fem.SurfSetToMesh(surfSet=murestrZ2,matSect=murestr_mat,elemSize=eSizeAbut,elemType='ShellMITC4')

aletiZ1_mesh=fem.SurfSetToMesh(surfSet=aletiZ1,matSect=aletiZ1_mat,elemSize=eSizeAbut,elemType='ShellMITC4')
aletiZ2_mesh=fem.SurfSetToMesh(surfSet=aletiZ2,matSect=aletiZ2_mat,elemSize=eSizeAbut,elemType='ShellMITC4')
aletiZ3_mesh=fem.SurfSetToMesh(surfSet=aletiZ3,matSect=aletiZ3_mat,elemSize=eSizeAbut,elemType='ShellMITC4')

aletdZ1_mesh=fem.SurfSetToMesh(surfSet=aletdZ1,matSect=aletdZ1_mat,elemSize=eSizeAbut,elemType='ShellMITC4')
aletdZ2_mesh=fem.SurfSetToMesh(surfSet=aletdZ2,matSect=aletdZ2_mat,elemSize=eSizeAbut,elemType='ShellMITC4')
aletdZ3_mesh=fem.SurfSetToMesh(surfSet=aletdZ3,matSect=aletdZ3_mat,elemSize=eSizeAbut,elemType='ShellMITC4')

if Lvoladzi >0:
    voladzi_mesh=fem.SurfSetToMesh(surfSet=voladzi,matSect=aletiZ3_mat,elemSize=eSizeAbut,elemType='ShellMITC4')
if Lvoladzd >0:
    voladzd_mesh=fem.SurfSetToMesh(surfSet=voladzd,matSect=aletdZ3_mat,elemSize=eSizeAbut,elemType='ShellMITC4')

lstSups=[zap_mesh,murestrZ1_mesh,murestrZ2_mesh,aletiZ1_mesh,aletiZ2_mesh,aletiZ3_mesh,aletdZ1_mesh,aletdZ2_mesh,aletdZ3_mesh]
if Lvoladzi >0:
    lstSups.append(voladzi_mesh)
if Lvoladzd >0:
    lstSups.append(voladzd_mesh)

fem.multi_mesh(preprocessor=prep,lstMeshSets=lstSups)



#Sets for loading
murestr=murestrZ1+murestrZ2

if Lvoladzi >0:
    aleti=aletiZ1+aletiZ2+aletiZ3+voladzi
else:
    aleti=aletiZ1+aletiZ2+aletiZ3

if Lvoladzd>0:
    aletd=aletdZ1+aletdZ2+aletdZ3+voladzd
else:
    aletd=aletdZ1+aletdZ2+aletdZ3


#                       ***BOUNDARY CONDITIONS***
# Regions resting on springs (Winkler elastic foundation)
#       wModulus: Winkler modulus of the foundation (springs in Z direction)
#       cRoz:     fraction of the Winkler modulus to apply for friction in
#                 the contact plane (springs in X, Y directions)
cRoz=0.5
found_wink=sprbc.ElasticFoundation(wModulus=Kbalasto,cRoz=0.2)
found_wink.generateSprings(xcSet=zap)
'''
#                       ***ACTIONS***
#Inertial load (density*acceleration) applied to the elements in a set
selfWeight=loads.InertialLoad(name='selfWeight', lstMeshSets=lstSups, vAccel=xc.Vector( [0.0,0.0,-grav]))

# Peso del relleno sobre la zapata
zapTrasdos_rg=gut.def_rg_cooLim(XYZListsAbut,Xmurestr,(yMurEstr,yZap),(0,0))
zapTrasdos=gridGeomAbutment.getSetSurfOneRegion(ijkRange=zapTrasdos_rg,nameSet='zapTrasdos')
zapTrasdos.fillDownwards()

rell_zap=loads.UniformLoadOnSurfaces(name= 'rell_zap',xcSet=zapTrasdos,loadVector= xc.Vector([0,0,-grav*densrell*(zGround-zZap-cantoZap/2.)]))

SCep_zap=loads.UniformLoadOnSurfaces(name= 'rell_zap',xcSet=zapTrasdos,loadVector= xc.Vector([0,0,-qunifTerr]))

# empuje del terreno
soil=ep.EarthPressureModel( zGround=zGround,zBottomSoils=[-10],KSoils=[K0], gammaSoils=[densrell*grav], zWater=-10.0, gammaWater=grav)
qunifTerr=ep.StripLoadOnBackfill(qLoad=qunifTerr, zLoad=zGround,distWall=0, stripWidth=10)

ep_aleti= loads.EarthPressLoad(name= 'ep_aleti', xcSet=aleti,soilData=soil, vDir=xc.Vector([-1,0,0]))
ep_aletd= loads.EarthPressLoad(name= 'ep_aletd', xcSet=aletd,soilData=soil, vDir=xc.Vector([1,0,0]))
ep_murestr= loads.EarthPressLoad(name= 'ep_murestr', xcSet=murestr,soilData=soil, vDir=xc.Vector([0,-1,0]))

SCep_aleti= loads.EarthPressLoad(name= 'SCep_aleti', xcSet=aleti,soilData=None, vDir=xc.Vector([-1,0,0]))
SCep_aleti.stripLoads=[qunifTerr]
SCep_aletd= loads.EarthPressLoad(name= 'SCep_aletd', xcSet=aletd,soilData=None, vDir=xc.Vector([1,0,0]))
SCep_aletd.stripLoads=[qunifTerr]
SCep_murestr= loads.EarthPressLoad(name= 'SCep_murestr', xcSet=murestr,soilData=None, vDir=xc.Vector([0,-1,0]))
SCep_murestr.stripLoads=[qunifTerr]

#Sobrecarga sobre relleno 
#Puntos apoyos sobre muro estribo (de menor a mayor X)

ptsAp=[gridGeomAbutment.getPntGrid((xListAbut.index(x),yListAbut.index(yMurEstr),zListAbut.index(zMur))) for x in xCoordNeopr]
nodesAp=[p.getNode() for p in ptsAp]
nodesNeop=[nodes.newNodeXYZ(n.getCoo[0],n.getCoo[1]+excNeop,n.getCoo[2]) for n in nodesAp]

for i in range(len(nodesAp)):
    modelSpace.setRigidBeamBetweenNodes(nodesAp[i].tag,nodesNeop[i].tag)

#resLoadCases=[G1,G2,Q1a_1,Q1a_2,Q1b_1,Q1b_2,Q1c,Q1d,Q1e,Q1f,W1,W2,Q1b_fren,Q1e_fren,Q1d_fren]

#Cargas tablero
#G1
G1_n1=loads.NodalLoad('G1_n1',[nodesAp[0]],xc.Vector(React['G1']['Restr1_n1'])*(-1))
G1_n2=loads.NodalLoad('G1_n2',[nodesAp[1]],xc.Vector(React['G1']['Restr1_n2'])*(-1))
G1_n3=loads.NodalLoad('G1_n3',[nodesAp[2]],xc.Vector(React['G1']['Restr1_n3'])*(-1))
G1_n4=loads.NodalLoad('G1_n4',[nodesAp[3]],xc.Vector(React['G1']['Restr1_n4'])*(-1))
G1_loads=[G1_n1,G1_n2,G1_n3,G1_n4]

#G2
G2_n1=loads.NodalLoad('G2_n1',[nodesAp[0]],xc.Vector(React['G2']['Restr1_n1'])*(-1))
G2_n2=loads.NodalLoad('G2_n2',[nodesAp[1]],xc.Vector(React['G2']['Restr1_n2'])*(-1))
G2_n3=loads.NodalLoad('G2_n3',[nodesAp[2]],xc.Vector(React['G2']['Restr1_n3'])*(-1))
G2_n4=loads.NodalLoad('G2_n4',[nodesAp[3]],xc.Vector(React['G2']['Restr1_n4'])*(-1))
G2_loads=[G2_n1,G2_n2,G2_n3,G2_n4]

#Q1a_1
Q1a_1_n1=loads.NodalLoad('Q1a_1_n1',[nodesAp[0]],xc.Vector(React['Q1a_1']['Restr1_n1'])*(-1))
Q1a_1_n2=loads.NodalLoad('Q1a_1_n2',[nodesAp[1]],xc.Vector(React['Q1a_1']['Restr1_n2'])*(-1))
Q1a_1_n3=loads.NodalLoad('Q1a_1_n3',[nodesAp[2]],xc.Vector(React['Q1a_1']['Restr1_n3'])*(-1))
Q1a_1_n4=loads.NodalLoad('Q1a_1_n4',[nodesAp[3]],xc.Vector(React['Q1a_1']['Restr1_n4'])*(-1))
Q1a_1_loads=[Q1a_1_n1,Q1a_1_n2,Q1a_1_n3,Q1a_1_n4]


#Cargas tablero
#G1
G1_n1=loads.NodalLoad('G1_n1',[nodesAp[0]],xc.Vector(React['G1']['Restr1_n1'])*(-1))
G1_n2=loads.NodalLoad('G1_n2',[nodesAp[1]],xc.Vector(React['G1']['Restr1_n2'])*(-1))
G1_n3=loads.NodalLoad('G1_n3',[nodesAp[2]],xc.Vector(React['G1']['Restr1_n3'])*(-1))
G1_n4=loads.NodalLoad('G1_n4',[nodesAp[3]],xc.Vector(React['G1']['Restr1_n4'])*(-1))
G1_loads=[G1_n1,G1_n2,G1_n3,G1_n4]

#G2
G2_n1=loads.NodalLoad('G2_n1',[nodesAp[0]],xc.Vector(React['G2']['Restr1_n1'])*(-1))
G2_n2=loads.NodalLoad('G2_n2',[nodesAp[1]],xc.Vector(React['G2']['Restr1_n2'])*(-1))
G2_n3=loads.NodalLoad('G2_n3',[nodesAp[2]],xc.Vector(React['G2']['Restr1_n3'])*(-1))
G2_n4=loads.NodalLoad('G2_n4',[nodesAp[3]],xc.Vector(React['G2']['Restr1_n4'])*(-1))
G2_loads=[G2_n1,G2_n2,G2_n3,G2_n4]

#Q1a_1
Q1a_1_n1=loads.NodalLoad('Q1a_1_n1',[nodesAp[0]],xc.Vector(React['Q1a_1']['Restr1_n1'])*(-1))
Q1a_1_n2=loads.NodalLoad('Q1a_1_n2',[nodesAp[1]],xc.Vector(React['Q1a_1']['Restr1_n2'])*(-1))
Q1a_1_n3=loads.NodalLoad('Q1a_1_n3',[nodesAp[2]],xc.Vector(React['Q1a_1']['Restr1_n3'])*(-1))
Q1a_1_n4=loads.NodalLoad('Q1a_1_n4',[nodesAp[3]],xc.Vector(React['Q1a_1']['Restr1_n4'])*(-1))
Q1a_1_loads=[Q1a_1_n1,Q1a_1_n2,Q1a_1_n3,Q1a_1_n4]

#Q1a_2
Q1a_2_n1=loads.NodalLoad('Q1a_2_n1',[nodesAp[0]],xc.Vector(React['Q1a_2']['Restr1_n1'])*(-1))
Q1a_2_n2=loads.NodalLoad('Q1a_2_n2',[nodesAp[1]],xc.Vector(React['Q1a_2']['Restr1_n2'])*(-1))
Q1a_2_n3=loads.NodalLoad('Q1a_2_n3',[nodesAp[2]],xc.Vector(React['Q1a_2']['Restr1_n3'])*(-1))
Q1a_2_n4=loads.NodalLoad('Q1a_2_n4',[nodesAp[3]],xc.Vector(React['Q1a_2']['Restr1_n4'])*(-1))
Q1a_2_loads=[Q1a_2_n1,Q1a_2_n2,Q1a_2_n3,Q1a_2_n4]

#Q1b_1
Q1b_1_n1=loads.NodalLoad('Q1b_1_n1',[nodesAp[0]],xc.Vector(React['Q1b_1']['Restr1_n1'])*(-1))
Q1b_1_n2=loads.NodalLoad('Q1b_1_n2',[nodesAp[1]],xc.Vector(React['Q1b_1']['Restr1_n2'])*(-1))
Q1b_1_n3=loads.NodalLoad('Q1b_1_n3',[nodesAp[2]],xc.Vector(React['Q1b_1']['Restr1_n3'])*(-1))
Q1b_1_n4=loads.NodalLoad('Q1b_1_n4',[nodesAp[3]],xc.Vector(React['Q1b_1']['Restr1_n4'])*(-1))
Q1b_1_loads=[Q1b_1_n1,Q1b_1_n2,Q1b_1_n3,Q1b_1_n4]

#Q1b_2
Q1b_2_n1=loads.NodalLoad('Q1b_2_n1',[nodesAp[0]],xc.Vector(React['Q1b_2']['Restr1_n1'])*(-1))
Q1b_2_n2=loads.NodalLoad('Q1b_2_n2',[nodesAp[1]],xc.Vector(React['Q1b_2']['Restr1_n2'])*(-1))
Q1b_2_n3=loads.NodalLoad('Q1b_2_n3',[nodesAp[2]],xc.Vector(React['Q1b_2']['Restr1_n3'])*(-1))
Q1b_2_n4=loads.NodalLoad('Q1b_2_n4',[nodesAp[3]],xc.Vector(React['Q1b_2']['Restr1_n4'])*(-1))
Q1b_2_loads=[Q1b_2_n1,Q1b_2_n2,Q1b_2_n3,Q1b_2_n4]

#Q1c
Q1c_n1=loads.NodalLoad('Q1c_n1',[nodesAp[0]],xc.Vector(React['Q1c']['Restr1_n1'])*(-1))
Q1c_n2=loads.NodalLoad('Q1c_n2',[nodesAp[1]],xc.Vector(React['Q1c']['Restr1_n2'])*(-1))
Q1c_n3=loads.NodalLoad('Q1c_n3',[nodesAp[2]],xc.Vector(React['Q1c']['Restr1_n3'])*(-1))
Q1c_n4=loads.NodalLoad('Q1c_n4',[nodesAp[3]],xc.Vector(React['Q1c']['Restr1_n4'])*(-1))
Q1c_loads=[Q1c_n1,Q1c_n2,Q1c_n3,Q1c_n4]

#Q1d
Q1d_n1=loads.NodalLoad('Q1d_n1',[nodesAp[0]],xc.Vector(React['Q1d']['Restr1_n1'])*(-1))
Q1d_n2=loads.NodalLoad('Q1d_n2',[nodesAp[1]],xc.Vector(React['Q1d']['Restr1_n2'])*(-1))
Q1d_n3=loads.NodalLoad('Q1d_n3',[nodesAp[2]],xc.Vector(React['Q1d']['Restr1_n3'])*(-1))
Q1d_n4=loads.NodalLoad('Q1d_n4',[nodesAp[3]],xc.Vector(React['Q1d']['Restr1_n4'])*(-1))
Q1d_loads=[Q1d_n1,Q1d_n2,Q1d_n3,Q1d_n4]

#Q1e
Q1e_n1=loads.NodalLoad('Q1e_n1',[nodesAp[0]],xc.Vector(React['Q1e']['Restr1_n1'])*(-1))
Q1e_n2=loads.NodalLoad('Q1e_n2',[nodesAp[1]],xc.Vector(React['Q1e']['Restr1_n2'])*(-1))
Q1e_n3=loads.NodalLoad('Q1e_n3',[nodesAp[2]],xc.Vector(React['Q1e']['Restr1_n3'])*(-1))
Q1e_n4=loads.NodalLoad('Q1e_n4',[nodesAp[3]],xc.Vector(React['Q1e']['Restr1_n4'])*(-1))
Q1e_loads=[Q1e_n1,Q1e_n2,Q1e_n3,Q1e_n4]

#Q1f
Q1f_n1=loads.NodalLoad('Q1f_n1',[nodesAp[0]],xc.Vector(React['Q1f']['Restr1_n1'])*(-1))
Q1f_n2=loads.NodalLoad('Q1f_n2',[nodesAp[1]],xc.Vector(React['Q1f']['Restr1_n2'])*(-1))
Q1f_n3=loads.NodalLoad('Q1f_n3',[nodesAp[2]],xc.Vector(React['Q1f']['Restr1_n3'])*(-1))
Q1f_n4=loads.NodalLoad('Q1f_n4',[nodesAp[3]],xc.Vector(React['Q1f']['Restr1_n4'])*(-1))
Q1f_loads=[Q1f_n1,Q1f_n2,Q1f_n3,Q1f_n4]

#Q1b_fren
Q1b_fren_n1=loads.NodalLoad('Q1b_fren_n1',[nodesAp[0]],xc.Vector(React['Q1b_fren']['Restr1_n1'])*(-1))
Q1b_fren_n2=loads.NodalLoad('Q1b_fren_n2',[nodesAp[1]],xc.Vector(React['Q1b_fren']['Restr1_n2'])*(-1))
Q1b_fren_n3=loads.NodalLoad('Q1b_fren_n3',[nodesAp[2]],xc.Vector(React['Q1b_fren']['Restr1_n3'])*(-1))
Q1b_fren_n4=loads.NodalLoad('Q1b_fren_n4',[nodesAp[3]],xc.Vector(React['Q1b_fren']['Restr1_n4'])*(-1))
Q1b_fren_loads=[Q1b_fren_n1,Q1b_fren_n2,Q1b_fren_n3,Q1b_fren_n4]

#Q1e_fren
Q1e_fren_n1=loads.NodalLoad('Q1e_fren_n1',[nodesAp[0]],xc.Vector(React['Q1e_fren']['Restr1_n1'])*(-1))
Q1e_fren_n2=loads.NodalLoad('Q1e_fren_n2',[nodesAp[1]],xc.Vector(React['Q1e_fren']['Restr1_n2'])*(-1))
Q1e_fren_n3=loads.NodalLoad('Q1e_fren_n3',[nodesAp[2]],xc.Vector(React['Q1e_fren']['Restr1_n3'])*(-1))
Q1e_fren_n4=loads.NodalLoad('Q1e_fren_n4',[nodesAp[3]],xc.Vector(React['Q1e_fren']['Restr1_n4'])*(-1))
Q1e_fren_loads=[Q1e_fren_n1,Q1e_fren_n2,Q1e_fren_n3,Q1e_fren_n4]

#Q1d_fren
Q1d_fren_n1=loads.NodalLoad('Q1d_fren_n1',[nodesAp[0]],xc.Vector(React['Q1d_fren']['Restr1_n1'])*(-1))
Q1d_fren_n2=loads.NodalLoad('Q1d_fren_n2',[nodesAp[1]],xc.Vector(React['Q1d_fren']['Restr1_n2'])*(-1))
Q1d_fren_n3=loads.NodalLoad('Q1d_fren_n3',[nodesAp[2]],xc.Vector(React['Q1d_fren']['Restr1_n3'])*(-1))
Q1d_fren_n4=loads.NodalLoad('Q1d_fren_n4',[nodesAp[3]],xc.Vector(React['Q1d_fren']['Restr1_n4'])*(-1))
Q1d_fren_loads=[Q1d_fren_n1,Q1d_fren_n2,Q1d_fren_n3,Q1d_fren_n4]

#Q2_1 (viento)
W1_n1=loads.NodalLoad('W1_n1',[nodesAp[0]],xc.Vector(React['Q2_1']['Restr1_n1'])*(-1))
W1_n2=loads.NodalLoad('W1_n2',[nodesAp[1]],xc.Vector(React['Q2_1']['Restr1_n2'])*(-1))
W1_n3=loads.NodalLoad('W1_n3',[nodesAp[2]],xc.Vector(React['Q2_1']['Restr1_n3'])*(-1))
W1_n4=loads.NodalLoad('W1_n4',[nodesAp[3]],xc.Vector(React['Q2_1']['Restr1_n4'])*(-1))
W1_loads=[W1_n1,W1_n2,W1_n3,W1_n4]

#Q2_2 (viento con sobrecarga de uso)
W2_n1=loads.NodalLoad('W2_n1',[nodesAp[0]],xc.Vector(React['Q2_2']['Restr1_n1'])*(-1))
W2_n2=loads.NodalLoad('W2_n2',[nodesAp[1]],xc.Vector(React['Q2_2']['Restr1_n2'])*(-1))
W2_n3=loads.NodalLoad('W2_n3',[nodesAp[2]],xc.Vector(React['Q2_2']['Restr1_n3'])*(-1))
W2_n4=loads.NodalLoad('W2_n4',[nodesAp[3]],xc.Vector(React['Q2_2']['Restr1_n4'])*(-1))
W2_loads=[W2_n1,W2_n2,W2_n3,W2_n4]

#Q3_1
Q3_1_n1=loads.NodalLoad('Q3_1_n1',[nodesAp[0]],xc.Vector(React['Q3_1']['Restr1_n1'])*(-1))
Q3_1_n2=loads.NodalLoad('Q3_1_n2',[nodesAp[1]],xc.Vector(React['Q3_1']['Restr1_n2'])*(-1))
Q3_1_n3=loads.NodalLoad('Q3_1_n3',[nodesAp[2]],xc.Vector(React['Q3_1']['Restr1_n3'])*(-1))
Q3_1_n4=loads.NodalLoad('Q3_1_n4',[nodesAp[3]],xc.Vector(React['Q3_1']['Restr1_n4'])*(-1))
Q3_1_loads=[Q3_1_n1,Q3_1_n2,Q3_1_n3,Q3_1_n4]

#Q3_2
Q3_2_n1=loads.NodalLoad('Q3_2_n1',[nodesAp[0]],xc.Vector(React['Q3_2']['Restr1_n1'])*(-1))
Q3_2_n2=loads.NodalLoad('Q3_2_n2',[nodesAp[1]],xc.Vector(React['Q3_2']['Restr1_n2'])*(-1))
Q3_2_n3=loads.NodalLoad('Q3_2_n3',[nodesAp[2]],xc.Vector(React['Q3_2']['Restr1_n3'])*(-1))
Q3_2_n4=loads.NodalLoad('Q3_2_n4',[nodesAp[3]],xc.Vector(React['Q3_2']['Restr1_n4'])*(-1))
Q3_2_loads=[Q3_2_n1,Q3_2_n2,Q3_2_n3,Q3_2_n4]

#Q3_3
Q3_3_n1=loads.NodalLoad('Q3_3_n1',[nodesAp[0]],xc.Vector(React['Q3_3']['Restr1_n1'])*(-1))
Q3_3_n2=loads.NodalLoad('Q3_3_n2',[nodesAp[1]],xc.Vector(React['Q3_3']['Restr1_n2'])*(-1))
Q3_3_n3=loads.NodalLoad('Q3_3_n3',[nodesAp[2]],xc.Vector(React['Q3_3']['Restr1_n3'])*(-1))
Q3_3_n4=loads.NodalLoad('Q3_3_n4',[nodesAp[3]],xc.Vector(React['Q3_3']['Restr1_n4'])*(-1))
Q3_3_loads=[Q3_3_n1,Q3_3_n2,Q3_3_n3,Q3_3_n4]

#Q3_4
Q3_4_n1=loads.NodalLoad('Q3_4_n1',[nodesAp[0]],xc.Vector(React['Q3_4']['Restr1_n1'])*(-1))
Q3_4_n2=loads.NodalLoad('Q3_4_n2',[nodesAp[1]],xc.Vector(React['Q3_4']['Restr1_n2'])*(-1))
Q3_4_n3=loads.NodalLoad('Q3_4_n3',[nodesAp[2]],xc.Vector(React['Q3_4']['Restr1_n3'])*(-1))
Q3_4_n4=loads.NodalLoad('Q3_4_n4',[nodesAp[3]],xc.Vector(React['Q3_4']['Restr1_n4'])*(-1))
Q3_4_loads=[Q3_4_n1,Q3_4_n2,Q3_4_n3,Q3_4_n4]

#G3
G3_n1=loads.NodalLoad('G3_n1',[nodesAp[0]],xc.Vector(React['G3']['Restr1_n1'])*(-1))
G3_n2=loads.NodalLoad('G3_n2',[nodesAp[1]],xc.Vector(React['G3']['Restr1_n2'])*(-1))
G3_n3=loads.NodalLoad('G3_n3',[nodesAp[2]],xc.Vector(React['G3']['Restr1_n3'])*(-1))
G3_n4=loads.NodalLoad('G3_n4',[nodesAp[3]],xc.Vector(React['G3']['Restr1_n4'])*(-1))
G3_loads=[G3_n1,G3_n2,G3_n3,G3_n4]

#    ***LOAD CASES***
G1=lcases.LoadCase(preprocessor=prep,name="G1",loadPType="default",timeSType="constant_ts")
G1.create()
G1.addLstLoads([selfWeight]+G1_loads)

G2=lcases.LoadCase(preprocessor=prep,name="G2",loadPType="default",timeSType="constant_ts")
G2.create()
G2.addLstLoads(G2_loads)

G3=lcases.LoadCase(preprocessor=prep,name="G3",loadPType="default",timeSType="constant_ts")
G3.create()
G3.addLstLoads(G3_loads)

#empuje del terreno
G4=lcases.LoadCase(preprocessor=prep,name="G4",loadPType="default",timeSType="constant_ts")
G4.create()
G4.addLstLoads([ep_aleti,ep_aletd,ep_murestr,rell_zap])


Q1a_1=lcases.LoadCase(preprocessor=prep,name="Q1a_1",loadPType="default",timeSType="constant_ts")
Q1a_1.create()
Q1a_1.addLstLoads(Q1a_1_loads)

Q1a_2=lcases.LoadCase(preprocessor=prep,name="Q1a_2",loadPType="default",timeSType="constant_ts")
Q1a_2.create()
Q1a_2.addLstLoads(Q1a_2_loads)

Q1b_1=lcases.LoadCase(preprocessor=prep,name="Q1b_1",loadPType="default",timeSType="constant_ts")
Q1b_1.create()
Q1b_1.addLstLoads(Q1b_1_loads)

Q1b_2=lcases.LoadCase(preprocessor=prep,name="Q1b_2",loadPType="default",timeSType="constant_ts")
Q1b_2.create()
Q1b_2.addLstLoads(Q1b_2_loads)

Q1c=lcases.LoadCase(preprocessor=prep,name="Q1c",loadPType="default",timeSType="constant_ts")
Q1c.create()
Q1c.addLstLoads(Q1c_loads)

Q1d=lcases.LoadCase(preprocessor=prep,name="Q1d",loadPType="default",timeSType="constant_ts")
Q1d.create()
Q1d.addLstLoads(Q1d_loads)

Q1e=lcases.LoadCase(preprocessor=prep,name="Q1e",loadPType="default",timeSType="constant_ts")
Q1e.create()
Q1e.addLstLoads(Q1e_loads)

Q1f=lcases.LoadCase(preprocessor=prep,name="Q1f",loadPType="default",timeSType="constant_ts")
Q1f.create()
Q1f.addLstLoads(Q1f_loads)

Q1b_fren=lcases.LoadCase(preprocessor=prep,name="Q1b_fren",loadPType="default",timeSType="constant_ts")
Q1b_fren.create()
Q1b_fren.addLstLoads(Q1b_fren_loads)

Q1e_fren=lcases.LoadCase(preprocessor=prep,name="Q1e_fren",loadPType="default",timeSType="constant_ts")
Q1e_fren.create()
Q1e_fren.addLstLoads(Q1e_fren_loads)

Q1d_fren=lcases.LoadCase(preprocessor=prep,name="Q1d_fren",loadPType="default",timeSType="constant_ts")
Q1d_fren.create()
Q1d_fren.addLstLoads(Q1d_fren_loads)

Q2_1=lcases.LoadCase(preprocessor=prep,name="Q2_1",loadPType="default",timeSType="constant_ts")
Q2_1.create()
Q2_1.addLstLoads(W1_loads)

Q2_2=lcases.LoadCase(preprocessor=prep,name="Q2_2",loadPType="default",timeSType="constant_ts")
Q2_2.create()
Q2_2.addLstLoads(W2_loads)


Q3_1=lcases.LoadCase(preprocessor=prep,name="Q3_1",loadPType="default",timeSType="constant_ts")
Q3_1.create()
Q3_1.addLstLoads(Q3_1_loads)

Q3_2=lcases.LoadCase(preprocessor=prep,name="Q3_2",loadPType="default",timeSType="constant_ts")
Q3_2.create()
Q3_2.addLstLoads(Q3_2_loads)

Q3_3=lcases.LoadCase(preprocessor=prep,name="Q3_3",loadPType="default",timeSType="constant_ts")
Q3_3.create()
Q3_3.addLstLoads(Q3_3_loads)

Q3_4=lcases.LoadCase(preprocessor=prep,name="Q3_4",loadPType="default",timeSType="constant_ts")
Q3_4.create()
Q3_4.addLstLoads(Q3_4_loads)

#Sobrecarga sobre relleno trasdós
Q4=lcases.LoadCase(preprocessor=prep,name="Q4",loadPType="default",timeSType="constant_ts")
Q4.create()
Q4.addLstLoads([SCep_aleti,SCep_aletd,SCep_murestr,SCep_zap])


overallSet=zap+aleti+aletd+murestr
overallSet.description='Estribo'
overallSet.color=cfg.colors['purple01']

murestr.description='Muro estribo'
murestr.color=cfg.colors['yellow01']

aleti.description='Aleta izquierda'
aleti.color=cfg.colors['purple01']

aletd.description='Aleta derecha'
aletd.color=cfg.colors['blue01']

zap.description='Losa de cimentación.'
zap.color=cfg.colors['brown01']

#shellsToCheck=zap+murestrZ1+murestrZ2+aletiZ1+aletiZ2+aletiZ3+aletdZ1+aletdZ2+aletdZ3
shellsToCheck=zap+aleti+aletd+murestr
shellsToCheck.description='shells'
'''
