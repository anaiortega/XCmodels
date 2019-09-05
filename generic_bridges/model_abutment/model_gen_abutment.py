# -*- coding: utf-8 -*-
from model.geometry import geom_utils as gut

# grid model definition
gridAbutment= gm.GridModel(prep,xListAbut,yListAbut,zListAbut)

# Grid geometric entities definition (points, lines, surfaces)
# Points' generation
gridAbutment.generatePoints()
#Slope (in X direction, Y direction or both) the grid points in a range
#syntax: slopePointsRange(ijkRange,slopeX,xZeroSlope,slopeY,yZeroSlope)
#     ijkRange: range for the search.
#     slopeX: slope in X direction, expressed as deltaZ/deltaX 
#                       (defaults to 0 = no slope applied)
#     xZeroSlope: coordinate X of the "rotation axis".
#     slopeY: slope in Y direction, expressed as deltaZ/deltaY)
#                       (defaults to 0 = no slope applied)
#     yZeroSlope: coordinate Y of the "rotation axis".
if LaletaIzq>0:
    if pendCoronAletaIzq>0:
        r=gut.def_rg_cooLim(XYZListsAbut,(Xaleti[0],Xaleti[0]),Yaleti,(zArm1,zAletas))
        scale=1-abs(LaletaIzq*pendCoronAletaIzq)/(zAletas-zZapata)
        gridAbutment.scaleCoorZPointsRange(ijkRange=r,zOrig=zZapata,scale=scale)      
    if angAletaIzq <>0:
        r=gut.def_rg_cooLim(XYZListsAbut,(Xaleti[0],Xaleti[0]),(Ymurestr[0],Yzap[1]),(zListAbut[0],zListAbut[-1]))
        gridAbutment.rotPntsZAxis(ijkRange=r,angle=angAletaIzq,xyRotCent=[xAletaI,yMurEstr])
        scale=1-abs(math.tan(math.radians(angAletaIzq))*Lzap/Xzap[0])
        r=gut.def_rg_cooLim(XYZListsAbut,(Xaleti[0],0),(Yzap[0],Yzap[0]),Zzap)
        gridAbutment.scaleCoorXPointsRange(ijkRange=r,xOrig=0,scale=scale) 

if LaletaDer>0:
    if pendCoronAletaDer>0:
        r=gut.def_rg_cooLim(XYZListsAbut,(Xaletd[1],Xaletd[1]),Yaletd,(zArm1,zAletas))
        scale=1-abs(LaletaDer*pendCoronAletaDer)/(zAletas-zZapata)
        gridAbutment.scaleCoorZPointsRange(ijkRange=r,zOrig=zZapata,scale=scale)      
    if angAletaDer <>0:
        r=gut.def_rg_cooLim(XYZListsAbut,(Xaletd[1],Xaletd[1]),(Ymurestr[0],Yzap[1]),(zListAbut[0],zListAbut[-1]))
        gridAbutment.rotPntsZAxis(ijkRange=r,angle=angAletaDer,xyRotCent=[xAletaD,yMurEstr])
        scale=1-abs(math.tan(math.radians(angAletaDer))*Lzap/Xzap[-1])
        r=gut.def_rg_cooLim(XYZListsAbut,(0,Xaletd[-1]),(Yzap[0],Yzap[0]),Zzap)
        gridAbutment.scaleCoorXPointsRange(ijkRange=r,xOrig=0,scale=scale) 


#Ranges for lines and surfaces
zap_rg=[gut.def_rg_cooLim(XYZListsAbut,Xzap,Yzap,Zzap)]

murestrZ1_rg=[gut.def_rg_cooLim(XYZListsAbut,Xmurestr,Ymurestr,zZ1)]
murestrZ2_rg=[gut.def_rg_cooLim(XYZListsAbut,Xmurestr,Ymurestr,zZ2mur)]
murestrZ3_rg=[gut.def_rg_cooLim(XYZListsAbut,Xmurestr,Ymurestr,zZ3mur)]

#Surfaces generation
zapEstr=gridAbutment.genSurfMultiRegion(lstIJKRange=zap_rg,nameSet='zapEstr')
murestrZ1=gridAbutment.genSurfMultiRegion(lstIJKRange=murestrZ1_rg,nameSet='murestrZ1')
murestrZ2=gridAbutment.genSurfMultiRegion(lstIJKRange=murestrZ2_rg,nameSet='murestrZ2')
murestrZ3=gridAbutment.genSurfMultiRegion(lstIJKRange=murestrZ3_rg,nameSet='murestrZ3')

#                         *** MATERIALS ***
concrete=EHE_materials.HA30
concrData=tm.MaterialData(name='concrData',E=concrete.Ecm(),nu=concrete.nuc,rho=concrete.density())

# Isotropic elastic section-material appropiate for plate and shell analysis
zap_mat=tm.DeckMaterialData(name='zap_mat',thickness= cantoZap,material=concrData)
zap_mat.setupElasticSection(preprocessor=prep)   #creates the section-material

murestr_mat=tm.DeckMaterialData(name='murestr_mat',thickness=espMurEstr,material=concrData)
murestr_mat.setupElasticSection(preprocessor=prep)   #creates the section-material
#                         ***FE model - MESH***
zap_mesh=fem.SurfSetToMesh(surfSet=zapEstr,matSect=zap_mat,elemSize=eSizeAbut,elemType='ShellMITC4')

murestrZ1_mesh=fem.SurfSetToMesh(surfSet=murestrZ1,matSect=murestr_mat,elemSize=eSizeAbut,elemType='ShellMITC4')
murestrZ2_mesh=fem.SurfSetToMesh(surfSet=murestrZ2,matSect=murestr_mat,elemSize=eSizeAbut,elemType='ShellMITC4')
murestrZ3_mesh=fem.SurfSetToMesh(surfSet=murestrZ3,matSect=murestr_mat,elemSize=eSizeAbut,elemType='ShellMITC4')
lstSups=[]

if LaletaIzq>0:
    aletiZ1_rg=[gut.def_rg_cooLim(XYZListsAbut,Xaleti,Yaleti,zZ1)]
    aletiZ2_rg=[gut.def_rg_cooLim(XYZListsAbut,Xaleti,Yaleti,zZ2alet)]
    aletiZ3_rg=[gut.def_rg_cooLim(XYZListsAbut,Xaleti,Yaleti,zZ3alet)]
    aletiZ1=gridAbutment.genSurfMultiRegion(lstIJKRange=aletiZ1_rg,nameSet='aletiZ1')
    aletiZ2=gridAbutment.genSurfMultiRegion(lstIJKRange=aletiZ2_rg,nameSet='aletiZ2')
    aletiZ3=gridAbutment.genSurfMultiRegion(lstIJKRange=aletiZ3_rg,nameSet='aletiZ3')
    aletiZ1_mat=tm.DeckMaterialData(name='aletiZ1_mat',thickness=espAletiZ1,material=concrData)
    aletiZ1_mat.setupElasticSection(preprocessor=prep)
    aletiZ2_mat=tm.DeckMaterialData(name='aletiZ2_mat',thickness=espAletiZ2,material=concrData)
    aletiZ2_mat.setupElasticSection(preprocessor=prep)
    aletiZ3_mat=tm.DeckMaterialData(name='aletiZ3_mat',thickness=espAletiZ3,material=concrData)
    aletiZ3_mat.setupElasticSection(preprocessor=prep)
    aletiZ1_mesh=fem.SurfSetToMesh(surfSet=aletiZ1,matSect=aletiZ1_mat,elemSize=eSizeAbut,elemType='ShellMITC4')
    aletiZ2_mesh=fem.SurfSetToMesh(surfSet=aletiZ2,matSect=aletiZ2_mat,elemSize=eSizeAbut,elemType='ShellMITC4')
    aletiZ3_mesh=fem.SurfSetToMesh(surfSet=aletiZ3,matSect=aletiZ3_mat,elemSize=eSizeAbut,elemType='ShellMITC4')
    lstSups+=[aletiZ3_mesh,aletiZ2_mesh,aletiZ1_mesh]


if LaletaDer>0:
    aletdZ1_rg=[gut.def_rg_cooLim(XYZListsAbut,Xaletd,Yaletd,zZ1)]
    aletdZ2_rg=[gut.def_rg_cooLim(XYZListsAbut,Xaletd,Yaletd,zZ2alet)]
    aletdZ3_rg=[gut.def_rg_cooLim(XYZListsAbut,Xaletd,Yaletd,zZ3alet)]
    aletdZ1=gridAbutment.genSurfMultiRegion(lstIJKRange=aletdZ1_rg,nameSet='aletdZ1')
    aletdZ2=gridAbutment.genSurfMultiRegion(lstIJKRange=aletdZ2_rg,nameSet='aletdZ2')
    aletdZ3=gridAbutment.genSurfMultiRegion(lstIJKRange=aletdZ3_rg,nameSet='aletdZ3')
    aletdZ1_mat=tm.DeckMaterialData(name='aletdZ1_mat',thickness=espAletdZ1,material=concrData)
    aletdZ1_mat.setupElasticSection(preprocessor=prep)
    aletdZ2_mat=tm.DeckMaterialData(name='aletdZ2_mat',thickness=espAletdZ2,material=concrData)
    aletdZ2_mat.setupElasticSection(preprocessor=prep)
    aletdZ3_mat=tm.DeckMaterialData(name='aletdZ3_mat',thickness=espAletdZ3,material=concrData)
    aletdZ3_mat.setupElasticSection(preprocessor=prep)
    aletdZ1_mesh=fem.SurfSetToMesh(surfSet=aletdZ1,matSect=aletdZ1_mat,elemSize=eSizeAbut,elemType='ShellMITC4')
    aletdZ2_mesh=fem.SurfSetToMesh(surfSet=aletdZ2,matSect=aletdZ2_mat,elemSize=eSizeAbut,elemType='ShellMITC4')
    aletdZ3_mesh=fem.SurfSetToMesh(surfSet=aletdZ3,matSect=aletdZ3_mat,elemSize=eSizeAbut,elemType='ShellMITC4')
    lstSups+=[aletdZ3_mesh,aletdZ2_mesh,aletdZ1_mesh]

lstSups+=[zap_mesh,murestrZ1_mesh,murestrZ2_mesh,murestrZ3_mesh]

fem.multi_mesh(preprocessor=prep,lstMeshSets=lstSups)

zapTrasdos_rg=gut.def_rg_cooLim(XYZListsAbut,Xzap,[Yzap[0],Ymurestr[0]],Zzap)
zapTrasdos=gridAbutment.getSetSurfOneRegion(ijkRange=zapTrasdos_rg, nameSet='zapTrasdos')


#Sets for loading
murEstrSet=murestrZ1+murestrZ2+murestrZ3
setsEstribo=[zapEstr,murEstrSet]
if LaletaIzq>0:
    aletIzqSet=aletiZ1+aletiZ2+aletiZ3
    aletIzqSet.name='aletIzqSet'
    aletIzqSet.description='muro lateral izq.'
    setsEstribo+=[aletIzqSet]
if LaletaDer>0:
    aletDerSet=aletdZ1+aletdZ2+aletdZ3
    aletDerSet.name='aletDerSet'
    aletDerSet.description='muro lateral der.'
    setsEstribo+=[aletDerSet]
murEstrSet.name='murEstrSet'
murEstrSet.description='Muro frontal estribo'

    
#                       ***BOUNDARY CONDITIONS***
# Regions resting on springs (Winkler elastic foundation)
#       wModulus: Winkler modulus of the foundation (springs in Z direction)
#       cRoz:     fraction of the Winkler modulus to apply for friction in
#                 the contact plane (springs in X, Y directions)
cRoz=0.5
found_wink=sprbc.ElasticFoundation(wModulus=Kbalasto,cRoz=0.2)
found_wink.generateSprings(xcSet=zapEstr)
