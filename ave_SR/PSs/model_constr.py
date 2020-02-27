# -*- coding: utf-8 -*-
from model.mesh import finit_el_model as fem
from model.boundary_cond import spring_bound_cond as sprbc
from model.sets import sets_mng as sets
from materials import typical_materials as tm
from actions import loads
from actions import load_cases as lcases
from actions import combinations as cc
from actions.earth_pressure import earth_pressure as ep
from materials.ehe import EHE_materials
from model.geometry import geom_utils as gut
from actions.earth_pressure import earth_pressure as ep


#Ranges for lines and surfaces
pilasInf_rg=[]
pilasInf_rg.append(gm.IJKRange((xList.index(-xPila),yList.index(yPil1),0),(xList.index(-xPila),yList.index(yPil1),zList.index(zInfPilas))))
pilasInf_rg.append(gm.IJKRange((xList.index(xPila),yList.index(yPil1),0),(xList.index(xPila),yList.index(yPil1),zList.index(zInfPilas))))
pilasInf_rg.append(gm.IJKRange((xList.index(-xPila),yList.index(yPil2),0),(xList.index(-xPila),yList.index(yPil2),zList.index(zInfPilas))))
pilasInf_rg.append(gm.IJKRange((xList.index(xPila),yList.index(yPil2),0),(xList.index(xPila),yList.index(yPil2),zList.index(zInfPilas))))
pilasSup_rg=[]
pilasSup_rg.append(gm.IJKRange((xList.index(-xPila),yList.index(yPil1),zList.index(zInfPilas)),(xList.index(-xPila),yList.index(yPil1),zList.index(zLosInf))))
pilasSup_rg.append(gm.IJKRange((xList.index(xPila),yList.index(yPil1),zList.index(zInfPilas)),(xList.index(xPila),yList.index(yPil1),zList.index(zLosInf))))
pilasSup_rg.append(gm.IJKRange((xList.index(-xPila),yList.index(yPil2),zList.index(zInfPilas)),(xList.index(-xPila),yList.index(yPil2),zList.index(zLosInf))))
pilasSup_rg.append(gm.IJKRange((xList.index(xPila),yList.index(yPil2),zList.index(zInfPilas)),(xList.index(xPila),yList.index(yPil2),zList.index(zLosInf))))
losInfV1_rg=[gut.def_rg_cooLim(XYZLists,XLosa,YLosligVano1,(zLosInf,zLosInf))]
losInfV2_rg=[gut.def_rg_cooLim(XYZLists,XLosa,YLosligVano2,(zLosInf,zLosInf))]
losInfV3_rg=[gut.def_rg_cooLim(XYZLists,XLosa,YLosligVano3,(zLosInf,zLosInf))]
losInfRP1_rg=[gut.def_rg_cooLim(XYZLists,XLosa,YriostrPil1,(zLosInf,zLosInf))]
losInfRP2_rg=[gut.def_rg_cooLim(XYZLists,XLosa,YriostrPil2,(zLosInf,zLosInf))]
losSupV1_rg=[gut.def_rg_cooLim(XYZLists,XLosa,YLosligVano1,(zLosSup,zLosSup))]
losSupV2_rg=[gut.def_rg_cooLim(XYZLists,XLosa,YLosligVano2,(zLosSup,zLosSup))]
losSupV3_rg=[gut.def_rg_cooLim(XYZLists,XLosa,YLosligVano3,(zLosSup,zLosSup))]
losSupRP1_rg=[gut.def_rg_cooLim(XYZLists,XLosa,YriostrPil1,(zLosSup,zLosSup))]
losSupRP2_rg=[gut.def_rg_cooLim(XYZLists,XLosa,YriostrPil2,(zLosSup,zLosSup))]
aux_rg=gut.def_rg_cooLim(XYZLists,(-xAlig3,xAlig3),YriostrPil1,(zLosInf,zLosSup))
diafRP1_rg=aux_rg.extractIncludedIKranges()
aux_rg=gut.def_rg_cooLim(XYZLists,(-xAlig3,xAlig3),YriostrPil2,(zLosInf,zLosSup))
diafRP2_rg=aux_rg.extractIncludedIKranges()

def rg_mur(Ycoor,Zcoor=ZmurAlig,Xmur=[-xAlig3,-xAlig2,-xAlig1,0,xAlig1,xAlig2,xAlig3],xyzL=XYZLists):
    rg=list()
    for x in Xmur:
        rg.append(gut.def_rg_cooLim(xyzL,(x,x),Ycoor,Zcoor))
    return rg
murAligV1_rg=rg_mur(YLosligVano1)
murAligV2_rg=rg_mur(YLosligVano2)
murAligV3_rg=rg_mur(YLosligVano3)

xmurRiostr=[-xArranqVoladz,-xAlig3,-xAlig2,-xAlig1,0,xAlig1,xAlig2,xAlig3,xArranqVoladz]
murRP1_rg=rg_mur(YriostrPil1,Xmur=xmurRiostr)
murRP2_rg=rg_mur(YriostrPil2,Xmur=xmurRiostr)


xmurExtAlig=[-xArranqVoladz,xArranqVoladz]
murExtAligV1_rg=rg_mur(YLosligVano1,Xmur=xmurExtAlig)
murExtAligV2_rg=rg_mur(YLosligVano2,Xmur=xmurExtAlig)
murExtAligV3_rg=rg_mur(YLosligVano3,Xmur=xmurExtAlig)

voladzCentV1_rg=[gut.def_rg_cooLim(XYZLists,XvoladzCentI,YLosligVano1,Zvoladz),gut.def_rg_cooLim(XYZLists,XvoladzCentD,YLosligVano1,Zvoladz)]
voladzCentV2_rg=[gut.def_rg_cooLim(XYZLists,XvoladzCentI,YLosligVano2,Zvoladz),gut.def_rg_cooLim(XYZLists,XvoladzCentD,YLosligVano2,Zvoladz)]
voladzCentV3_rg=[gut.def_rg_cooLim(XYZLists,XvoladzCentI,YLosligVano3,Zvoladz),gut.def_rg_cooLim(XYZLists,XvoladzCentD,YLosligVano3,Zvoladz)]
voladzCentRP1_rg=[gut.def_rg_cooLim(XYZLists,XvoladzCentI,YriostrPil1,Zvoladz),gut.def_rg_cooLim(XYZLists,XvoladzCentD,YriostrPil1,Zvoladz)]
voladzCentRP2_rg=[gut.def_rg_cooLim(XYZLists,XvoladzCentI,YriostrPil2,Zvoladz),gut.def_rg_cooLim(XYZLists,XvoladzCentD,YriostrPil2,Zvoladz)]

voladzExtrV1_rg=[gut.def_rg_cooLim(XYZLists,XvoladzExtrI,YLosligVano1,Zvoladz),gut.def_rg_cooLim(XYZLists,XvoladzExtrD,YLosligVano1,Zvoladz)]
voladzExtrV2_rg=[gut.def_rg_cooLim(XYZLists,XvoladzExtrI,YLosligVano2,Zvoladz),gut.def_rg_cooLim(XYZLists,XvoladzExtrD,YLosligVano2,Zvoladz)]
voladzExtrV3_rg=[gut.def_rg_cooLim(XYZLists,XvoladzExtrI,YLosligVano3,Zvoladz),gut.def_rg_cooLim(XYZLists,XvoladzExtrD,YLosligVano3,Zvoladz)]
voladzExtrRP1_rg=[gut.def_rg_cooLim(XYZLists,XvoladzExtrI,YriostrPil1,Zvoladz),gut.def_rg_cooLim(XYZLists,XvoladzExtrD,YriostrPil1,Zvoladz)]
voladzExtrRP2_rg=[gut.def_rg_cooLim(XYZLists,XvoladzExtrI,YriostrPil2,Zvoladz),gut.def_rg_cooLim(XYZLists,XvoladzExtrD,YriostrPil2,Zvoladz)]

riostrEstr1_rg=[]
riostrEstr1_rg.append(gm.IJKRange((0,0,zList.index(zriostrEstr)),(lastXpos,0,zList.index(zriostrEstr))))
riostrEstr2_rg=[]
riostrEstr2_rg.append(gm.IJKRange((0,lastYpos,zList.index(zriostrEstr)),(lastXpos,lastYpos,zList.index(zriostrEstr))))


#Lines generation
pilasInf=gridGeom.genLinMultiRegion(lstIJKRange=pilasInf_rg,nameSet='pilasInf')
pilasSup=gridGeom.genLinMultiRegion(lstIJKRange=pilasSup_rg,nameSet='pilasSup')
riostrEstr1=gridGeom.genLinMultiRegion(lstIJKRange=riostrEstr1_rg,nameSet='riostrEstr1')
riostrEstr2=gridGeom.genLinMultiRegion(lstIJKRange=riostrEstr2_rg,nameSet='riostrEstr2')

#Surfaces generation
losInfV1=gridGeom.genSurfMultiRegion(lstIJKRange=losInfV1_rg,nameSet='losInfV1')
losInfV2=gridGeom.genSurfMultiRegion(lstIJKRange=losInfV2_rg,nameSet='losInfV2')
losInfV3=gridGeom.genSurfMultiRegion(lstIJKRange=losInfV3_rg,nameSet='losInfV3')
losInfRP1=gridGeom.genSurfMultiRegion(lstIJKRange=losInfRP1_rg,nameSet='losInfRP1')
losInfRP2=gridGeom.genSurfMultiRegion(lstIJKRange=losInfRP2_rg,nameSet='losInfRP2')

losSupV1=gridGeom.genSurfMultiRegion(lstIJKRange=losSupV1_rg,nameSet='losSupV1')
losSupV2=gridGeom.genSurfMultiRegion(lstIJKRange=losSupV2_rg,nameSet='losSupV2')
losSupV3=gridGeom.genSurfMultiRegion(lstIJKRange=losSupV3_rg,nameSet='losSupV3')
losSupRP1=gridGeom.genSurfMultiRegion(lstIJKRange=losSupRP1_rg,nameSet='losSupRP1')
losSupRP2=gridGeom.genSurfMultiRegion(lstIJKRange=losSupRP2_rg,nameSet='losSupRP2')


murAligV1=gridGeom.genSurfMultiRegion(lstIJKRange=murAligV1_rg,nameSet='murAligV1')
murAligV2=gridGeom.genSurfMultiRegion(lstIJKRange=murAligV2_rg,nameSet='murAligV2')
murAligV3=gridGeom.genSurfMultiRegion(lstIJKRange=murAligV3_rg,nameSet='murAligV3')



murExtAligV1=gridGeom.genSurfMultiRegion(lstIJKRange=murExtAligV1_rg,nameSet='murExtAligV1')
murExtAligV2=gridGeom.genSurfMultiRegion(lstIJKRange=murExtAligV2_rg,nameSet='murExtAligV2')
murExtAligV3=gridGeom.genSurfMultiRegion(lstIJKRange=murExtAligV3_rg,nameSet='murExtAligV3')

murRP1=gridGeom.genSurfMultiRegion(lstIJKRange=murRP1_rg,nameSet='murRP1')
murRP2=gridGeom.genSurfMultiRegion(lstIJKRange=murRP2_rg,nameSet='murRP2')

diafRP1=gridGeom.genSurfMultiRegion(lstIJKRange=diafRP1_rg,nameSet='diafRP1')
diafRP2=gridGeom.genSurfMultiRegion(lstIJKRange=diafRP2_rg,nameSet='diafRP2')

voladzCentV1=gridGeom.genSurfMultiRegion(lstIJKRange=voladzCentV1_rg,nameSet='voladzCentV1')
voladzCentV2=gridGeom.genSurfMultiRegion(lstIJKRange=voladzCentV2_rg,nameSet='voladzCentV2')
voladzCentV3=gridGeom.genSurfMultiRegion(lstIJKRange=voladzCentV3_rg,nameSet='voladzCentV3')
voladzCentRP1=gridGeom.genSurfMultiRegion(lstIJKRange=voladzCentRP1_rg,nameSet='voladzCentRP1')
voladzCentRP2=gridGeom.genSurfMultiRegion(lstIJKRange=voladzCentRP2_rg,nameSet='voladzCentRP2')

voladzExtrV1=gridGeom.genSurfMultiRegion(lstIJKRange=voladzExtrV1_rg,nameSet='voladzExtrV1')
voladzExtrV2=gridGeom.genSurfMultiRegion(lstIJKRange=voladzExtrV2_rg,nameSet='voladzExtrV2')
voladzExtrV3=gridGeom.genSurfMultiRegion(lstIJKRange=voladzExtrV3_rg,nameSet='voladzExtrV3')
voladzExtrRP1=gridGeom.genSurfMultiRegion(lstIJKRange=voladzExtrRP1_rg,nameSet='voladzExtrRP1')
voladzExtrRP2=gridGeom.genSurfMultiRegion(lstIJKRange=voladzExtrRP2_rg,nameSet='voladzExtrRP2')


#                         *** MATERIALS ***
concrete=EHE_materials.HA30
concrData=tm.MaterialData(name='concrData',E=concrete.Ecm(),nu=concrete.nuc,rho=concrete.density())

# Isotropic elastic section-material appropiate for plate and shell analysis
losInf_mat=tm.DeckMaterialData(name='losInf_mat',thickness= espLosAlig,material=concrData)
losInf_mat.setupElasticSection(preprocessor=prep)   #creates the section-material

losSup_mat=tm.DeckMaterialData(name='losSup_mat',thickness= espLosAlig,material=concrData)
losSup_mat.setupElasticSection(preprocessor=prep)   #creates the section-material

murAlig_mat=tm.DeckMaterialData(name='murAlig_mat',thickness= espEntreAlig,material=concrData)
murAlig_mat.setupElasticSection(preprocessor=prep)   #creates the section-material

diafRP_mat=tm.DeckMaterialData(name='diafRP_mat',thickness=espDiafRP ,material=concrData)
diafRP_mat.setupElasticSection(preprocessor=prep)

murExtAlig_mat=tm.DeckMaterialData(name='murExtAlig_mat',thickness=espExtAlig,material=concrData)
murExtAlig_mat.setupElasticSection(preprocessor=prep)   #creates the section-material

voladzCent_mat=tm.DeckMaterialData(name='voladzCent_mat',thickness= espVoladzMax,material=concrData)
voladzCent_mat.setupElasticSection(preprocessor=prep)   #creates the section-material

voladzExtr_mat=tm.DeckMaterialData(name='voladzExtr_mat',thickness= espVoladzMin,material=concrData)
voladzExtr_mat.setupElasticSection(preprocessor=prep)   #creates the section-material


#Geometric sections
#rectangular sections
from materials.sections import section_properties as sectpr
geomSectPilas=sectpr.RectangularSection(name='geomSectPilas',b=lRectEqPila,h=lRectEqPila)
geomSectRiostrEstr=sectpr.RectangularSection(name='geomSectRiostrEstr',b=espRiostrEstr,h=cantoLosa)
# Elastic material-section appropiate for 3D beam analysis, including shear
  # deformations.
  # Attributes:
  #   name:         name identifying the section
  #   section:      instance of a class that defines the geometric and
  #                 mechanical characteristiscs
  #                 of a section (e.g: RectangularSection, CircularSection,
  #                 ISection, ...)
  #   material:     instance of a class that defines the elastic modulus,
  #                 shear modulus and mass density of the material

pilasInf_mat= tm.BeamMaterialData(name= 'pilasInf_mat', section=geomSectPilas, material=concrData)
pilasInf_mat.setupElasticShear3DSection(preprocessor=prep)
pilasSup_mat= tm.BeamMaterialData(name= 'pilasSup_mat', section=geomSectPilas, material=concrData)
pilasSup_mat.setupElasticShear3DSection(preprocessor=prep)
riostrEstr_mat= tm.BeamMaterialData(name= 'riostrEstr_mat', section=geomSectRiostrEstr, material=concrData)
riostrEstr_mat.setupElasticShear3DSection(preprocessor=prep)


#                         ***FE model - MESH***

pilasInf_mesh=fem.LinSetToMesh(linSet=pilasInf,matSect=pilasInf_mat,elemSize=eSize,vDirLAxZ=xc.Vector([0,1,0]),elemType='ElasticBeam3d',dimElemSpace=3,coordTransfType='linear')
#pilasInf_mesh.generateMesh(prep)    # mesh this set of lines

pilasSup_mesh=fem.LinSetToMesh(linSet=pilasSup,matSect=pilasSup_mat,elemSize=eSize,vDirLAxZ=xc.Vector([0,1,0]),elemType='ElasticBeam3d',dimElemSpace=3,coordTransfType='linear')
#pilasSup_mesh.generateMesh(prep)    # mesh this set of lines

riostrEstr1_mesh=fem.LinSetToMesh(linSet=riostrEstr1,matSect=riostrEstr_mat,elemSize=eSize,vDirLAxZ=xc.Vector([0,-1,0]),elemType='ElasticBeam3d',dimElemSpace=3,coordTransfType='linear')
riostrEstr2_mesh=fem.LinSetToMesh(linSet=riostrEstr2,matSect=riostrEstr_mat,elemSize=eSize,vDirLAxZ=xc.Vector([0,-1,0]),elemType='ElasticBeam3d',dimElemSpace=3,coordTransfType='linear')

losInfV1_mesh=fem.SurfSetToMesh(surfSet=losInfV1,matSect=losInf_mat,elemSize=eSize,elemType='ShellMITC4')
losInfV2_mesh=fem.SurfSetToMesh(surfSet=losInfV2,matSect=losInf_mat,elemSize=eSize,elemType='ShellMITC4')
losInfV3_mesh=fem.SurfSetToMesh(surfSet=losInfV3,matSect=losInf_mat,elemSize=eSize,elemType='ShellMITC4')
losInfRP1_mesh=fem.SurfSetToMesh(surfSet=losInfRP1,matSect=losInf_mat,elemSize=eSize,elemType='ShellMITC4')
losInfRP2_mesh=fem.SurfSetToMesh(surfSet=losInfRP2,matSect=losInf_mat,elemSize=eSize,elemType='ShellMITC4')

losSupV1_mesh=fem.SurfSetToMesh(surfSet=losSupV1,matSect=losSup_mat,elemSize=eSize,elemType='ShellMITC4')
losSupV2_mesh=fem.SurfSetToMesh(surfSet=losSupV2,matSect=losSup_mat,elemSize=eSize,elemType='ShellMITC4')
losSupV3_mesh=fem.SurfSetToMesh(surfSet=losSupV3,matSect=losSup_mat,elemSize=eSize,elemType='ShellMITC4')
losSupRP1_mesh=fem.SurfSetToMesh(surfSet=losSupRP1,matSect=losSup_mat,elemSize=eSize,elemType='ShellMITC4')
losSupRP2_mesh=fem.SurfSetToMesh(surfSet=losSupRP2,matSect=losSup_mat,elemSize=eSize,elemType='ShellMITC4')

murAligV1_mesh=fem.SurfSetToMesh(surfSet=murAligV1,matSect=murAlig_mat,elemSize=eSize,elemType='ShellMITC4')
murAligV2_mesh=fem.SurfSetToMesh(surfSet=murAligV2,matSect=murAlig_mat,elemSize=eSize,elemType='ShellMITC4')
murAligV3_mesh=fem.SurfSetToMesh(surfSet=murAligV3,matSect=murAlig_mat,elemSize=eSize,elemType='ShellMITC4')

murExtAligV1_mesh=fem.SurfSetToMesh(surfSet=murExtAligV1,matSect=murExtAlig_mat,elemSize=eSize,elemType='ShellMITC4')
murExtAligV2_mesh=fem.SurfSetToMesh(surfSet=murExtAligV2,matSect=murExtAlig_mat,elemSize=eSize,elemType='ShellMITC4')
murExtAligV3_mesh=fem.SurfSetToMesh(surfSet=murExtAligV3,matSect=murExtAlig_mat,elemSize=eSize,elemType='ShellMITC4')

murRP1_mesh=fem.SurfSetToMesh(surfSet=murRP1,matSect=murAlig_mat,elemSize=eSize,elemType='ShellMITC4')
murRP2_mesh=fem.SurfSetToMesh(surfSet=murRP2,matSect=murAlig_mat,elemSize=eSize,elemType='ShellMITC4')

diafRP1_mesh=fem.SurfSetToMesh(surfSet=diafRP1,matSect=diafRP_mat,elemSize=eSize,elemType='ShellMITC4')
diafRP2_mesh=fem.SurfSetToMesh(surfSet=diafRP2,matSect=diafRP_mat,elemSize=eSize,elemType='ShellMITC4')

voladzCentV1_mesh=fem.SurfSetToMesh(surfSet=voladzCentV1,matSect=voladzCent_mat,elemSize=eSize,elemType='ShellMITC4')
voladzCentV2_mesh=fem.SurfSetToMesh(surfSet=voladzCentV2,matSect=voladzCent_mat,elemSize=eSize,elemType='ShellMITC4')
voladzCentV3_mesh=fem.SurfSetToMesh(surfSet=voladzCentV3,matSect=voladzCent_mat,elemSize=eSize,elemType='ShellMITC4')
voladzCentRP1_mesh=fem.SurfSetToMesh(surfSet=voladzCentRP1,matSect=voladzCent_mat,elemSize=eSize,elemType='ShellMITC4')
voladzCentRP2_mesh=fem.SurfSetToMesh(surfSet=voladzCentRP2,matSect=voladzCent_mat,elemSize=eSize,elemType='ShellMITC4')

voladzExtrV1_mesh=fem.SurfSetToMesh(surfSet=voladzExtrV1,matSect=voladzExtr_mat,elemSize=eSize,elemType='ShellMITC4')
voladzExtrV2_mesh=fem.SurfSetToMesh(surfSet=voladzExtrV2,matSect=voladzExtr_mat,elemSize=eSize,elemType='ShellMITC4')
voladzExtrV3_mesh=fem.SurfSetToMesh(surfSet=voladzExtrV3,matSect=voladzExtr_mat,elemSize=eSize,elemType='ShellMITC4')
voladzExtrRP1_mesh=fem.SurfSetToMesh(surfSet=voladzExtrRP1,matSect=voladzExtr_mat,elemSize=eSize,elemType='ShellMITC4')
voladzExtrRP2_mesh=fem.SurfSetToMesh(surfSet=voladzExtrRP2,matSect=voladzExtr_mat,elemSize=eSize,elemType='ShellMITC4')


#fem.multi_mesh(preprocessor=prep,lstMeshSets=[pilasInf_mesh,pilasSup_mesh,losInf_mesh,losSup_mesh,murAlig_mesh,murExtAlig_mesh,voladzCent_mesh,voladzExtr_mesh,riostrEstr_mesh,riostrPil_mesh])
fem.multi_mesh(preprocessor=prep,lstMeshSets=[pilasInf_mesh,pilasSup_mesh,riostrEstr1_mesh,riostrEstr2_mesh,losInfV1_mesh,losInfV2_mesh,losInfV3_mesh,losInfRP1_mesh,losInfRP2_mesh,losSupV1_mesh,losSupV2_mesh,losSupV3_mesh,losSupRP1_mesh,losSupRP2_mesh,murAligV1_mesh,murAligV2_mesh,murAligV3_mesh,murExtAligV1_mesh,murExtAligV2_mesh,murExtAligV3_mesh,murRP1_mesh,murRP2_mesh,diafRP1_mesh,diafRP2_mesh,voladzCentV1_mesh,voladzCentV2_mesh,voladzCentV3_mesh,voladzCentRP1_mesh,voladzCentRP2_mesh,voladzExtrV1_mesh,voladzExtrV2_mesh,voladzExtrV3_mesh,voladzExtrRP1_mesh,voladzExtrRP2_mesh])

losInf=losInfV1+losInfV2+losInfV3+losInfRP1+losInfRP2
losSup=losSupV1+losSupV2+losSupV3+losSupRP1+losSupRP2
murAlig=murAligV1+murAligV2+murAligV3
murExtAlig=murExtAligV1+murExtAligV2+murExtAligV3
voladzCent=voladzCentV1+voladzCentV2+voladzCentV3+voladzCentRP1+voladzCentRP2
voladzExtr=voladzExtrV1+voladzExtrV2+voladzExtrV3+voladzExtrRP1+voladzExtrRP2
murRP=murRP1+murRP2
diafRP=diafRP1+diafRP2
diafRP.name='diafRP'
diafRP.description='Diafragmas riostra pilas'

losRP=losInfRP1+losInfRP2+losSupRP1+losSupRP2
losAlig=losInfV1+losInfV2+losInfV3+losSupV1+losSupV2+losSupV3

#Sets for loads
supTablero=losSup+voladzCent+voladzExtr
supTablero.name='supTablero'
supTablero.description='voladizos y tablero losa superior'
losas=losSup+voladzCent+voladzExtr+losInf+losRP
murosAlig=murAlig+murExtAlig
murosAll=murAlig+murExtAlig+murRP1+murRP2
pilas=pilasInf+pilasSup
pilas.name='pilas'
pilas.description='Pilas'
voladzExtr=voladzExtrV1+voladzExtrV2+voladzExtrV3+voladzExtrRP1+voladzExtrRP2
voladzExtr.name='voladzExtr'
voladzCent=voladzCentV1+voladzCentV2+voladzCentV3+voladzCentRP1+voladzCentRP2
voladzCent.name='voladzCent'
riostrEstr=riostrEstr1+riostrEstr2
riostrEstr.name='riostrEstr'
riostrEstr.description='Riostras estribos'


acerIzq_rg=list()
acerIzq_rg.append(gm.IJKRange((0,0,zList.index(zArrVoladz)),(xList.index(-xBordeCalz),lastYpos,zList.index(zArrVoladz))))
acerIzq=gridGeom.getSetSurfMultiRegion(lstIJKRange=acerIzq_rg,nameSet='acerIzq')

acerDer_rg=list()
acerDer_rg.append(gm.IJKRange((xList.index(xBordeCalz),0,zList.index(zArrVoladz)),(lastXpos,lastYpos,zList.index(zArrVoladz))))
acerDer=gridGeom.getSetSurfMultiRegion(lstIJKRange=acerDer_rg,nameSet='acerDer')

aceras=acerIzq+acerDer
aceras.name='aceras'

calzada_rg=gm.IJKRange((xList.index(-xBordeCalz),0,zList.index(zArrVoladz)),(xList.index(xBordeCalz),lastYpos,zList.index(zLosSup))).extractIncludedIJranges()
calzada=gridGeom.getSetSurfMultiRegion(lstIJKRange=calzada_rg,nameSet='calzada')
#Imposta
auxSetPnt1=gridGeom.getSetPntRange(ijkRange=gm.IJKRange((0,0,zList.index(zArrVoladz)),(0,lastYpos,zList.index(zArrVoladz))),setName='auxSetPnt1')
auxSetPnt2=gridGeom.getSetPntRange(ijkRange=gm.IJKRange((lastXpos,0,zList.index(zArrVoladz)),(lastXpos,lastYpos,zList.index(zArrVoladz))),setName='auxSetPnt2')
auxSetPnt=auxSetPnt1+auxSetPnt2
auxSetPnt.name='auxSetPnt'
imposta=sets.get_lines_on_points(setPoints=auxSetPnt,setLinName='imposta',onlyIncluded=True)
barrera_rg=list()
auxSetPnt1=gridGeom.getSetPntRange(ijkRange=gm.IJKRange((xList.index(-xBordeCalz),0,zList.index(zArrVoladz)),(xList.index(-xBordeCalz),lastYpos,zList.index(zArrVoladz))),setName='auxSetPnt1')
auxSetPnt2=gridGeom.getSetPntRange(ijkRange=gm.IJKRange((xList.index(xBordeCalz),0,zList.index(zArrVoladz)),(xList.index(xBordeCalz),lastYpos,zList.index(zArrVoladz))),setName='auxSetPnt2')
auxSetPnt=auxSetPnt1+auxSetPnt2
auxSetPnt.name='auxSetPnt'
barrera=sets.get_lines_on_points(setPoints=auxSetPnt,setLinName='barrera',onlyIncluded=True)
#línea arranque voladizo izquierdo (aplicación W)
arrqVolPnt=gridGeom.getSetPntRange(ijkRange=gm.IJKRange((xList.index(-xArranqVoladz),0,zList.index(zArrVoladz)),(xList.index(-xArranqVoladz),lastYpos,zList.index(zArrVoladz))),setName='arrqVolPnt')
arrqVol=sets.get_lines_on_points(setPoints=arrqVolPnt,setLinName='arrqVol',onlyIncluded=True)

#    sets vías fictíceas, cargas uniformes tren de cargas (fr: concomitantes con frenado 0.4*q)
def traf_vias_fict(name,xmin,xmax,ymin,ymax,zmin,zmax,qmax=qunifmax,qmin=qunifmin,preprocessor=prep):
    rg=gm.IJKRange((xList.index(xmin),yList.index(ymin),zList.index(zmin)),(xList.index(xmax),yList.index(ymax),zList.index(zmax))).extractIncludedIJranges()
    nmset=name+'_set'
    retval=(gridGeom.getSetSurfMultiRegion(lstIJKRange=rg,nameSet=name+'_set'),
            loads.UniformLoadOnSurfaces(name=name+'_qunifmax',xcSet=preprocessor.getSets.getSet(nmset),loadVector=xc.Vector([0,0,-qmax,0,0,0]),refSystem='Global'),
            loads.UniformLoadOnSurfaces(name=name+'_qunifmin',xcSet=preprocessor.getSets.getSet(nmset),loadVector=xc.Vector([0,0,-qmin,0,0,0]),refSystem='Global'),
            loads.UniformLoadOnSurfaces(name=name+'_frqunifmax',xcSet=preprocessor.getSets.getSet(nmset),loadVector=xc.Vector([0,0,-0.4*qmax,0,0,0]),refSystem='Global'),
            loads.UniformLoadOnSurfaces(name=name+'_frqunifmin',xcSet=preprocessor.getSets.getSet(nmset),loadVector=xc.Vector([0,0,-0.4*qmin,0,0,0]),refSystem='Global')
             )
    return retval

viaExt_vano1_set,viaExt_vano1_qunifmax,viaExt_vano1_qunifmin,viaExt_vano1_qunifmax_fr,viaExt_vano1_qunifmin_fr=traf_vias_fict(name='viaExt_vano1',xmin=xViaFict1,xmax=xBordeCalz,ymin=0,ymax=yPil1,zmin=zArrVoladz,zmax=zLosSup)

viaExt_vano2_set,viaExt_vano2_qunifmax,viaExt_vano2_qunifmin,viaExt_vano2_qunifmax_fr,viaExt_vano2_qunifmin_fr=traf_vias_fict(name='viaExt_vano2',xmin=xViaFict1,xmax=xBordeCalz,ymin=yPil1,ymax=yPil2,zmin=zArrVoladz,zmax=zLosSup)
viaExt_vano3_set,viaExt_vano3_qunifmax,viaExt_vano3_qunifmin,viaExt_vano3_qunifmax_fr,viaExt_vano3_qunifmin_fr=traf_vias_fict(name='viaExt_vano3',xmin=xViaFict1,xmax=xBordeCalz,ymin=yPil2,ymax=yEstr2,zmin=zArrVoladz,zmax=zLosSup)

viaCent_vano1_set,viaCent_vano1_qunifmax,viaCent_vano1_qunifmin,viaCent_vano1_qunifmax_fr,viaCent_vano1_qunifmin_fr=traf_vias_fict(name='viaCent_vano1',xmin=xViaFict2,xmax=xViaFict1,ymin=0,ymax=yPil1,zmin=zLosSup,zmax=zLosSup)
viaCent_vano2_set,viaCent_vano2_qunifmax,viaCent_vano2_qunifmin,viaCent_vano2_qunifmax_fr,viaCent_vano2_qunifmin_fr=traf_vias_fict(name='viaCent_vano2',xmin=xViaFict2,xmax=xViaFict1,ymin=yPil1,ymax=yPil2,zmin=zLosSup,zmax=zLosSup)
viaCent_vano3_set,viaCent_vano3_qunifmax,viaCent_vano3_qunifmin,viaCent_vano3_qunifmax_fr,viaCent_vano3_qunifmin_fr=traf_vias_fict(name='viaCent_vano3',xmin=xViaFict2,xmax=xViaFict1,ymin=yPil2,ymax=yEstr2,zmin=zLosSup,zmax=zLosSup)

viaInt_vano1_set,viaInt_vano1_qunifmax,viaInt_vano1_qunifmin,viaInt_vano1_qunifmax_fr,viaInt_vano1_qunifmin_fr=traf_vias_fict(name='viaInt_vano1',xmin=xViaFict3,xmax=xViaFict2,ymin=0,ymax=yPil1,zmin=zLosSup,zmax=zLosSup)
viaInt_vano2_set,viaInt_vano2_qunifmax,viaInt_vano2_qunifmin,viaInt_vano2_qunifmax_fr,viaInt_vano2_qunifmin_fr=traf_vias_fict(name='viaInt_vano2',xmin=xViaFict3,xmax=xViaFict2,ymin=yPil1,ymax=yPil2,zmin=zLosSup,zmax=zLosSup)
viaInt_vano3_set,viaInt_vano3_qunifmax,viaInt_vano3_qunifmin,viaInt_vano3_qunifmax_fr,viaInt_vano3_qunifmin_fr=traf_vias_fict(name='viaInt_vano3',xmin=xViaFict3,xmax=xViaFict2,ymin=yPil2,ymax=yEstr2,zmin=zLosSup,zmax=zLosSup)

remnt_vano1_set,remnt_vano1_qunifmax,remnt_vano1_qunifmin,remnt_vano1_qunifmax_fr,remnt_vano1_qunifmin_fr=traf_vias_fict(name='remnt_vano1',xmin=-xBordeCalz,xmax=xViaFict3,ymin=0,ymax=yPil1,zmin=zArrVoladz,zmax=zLosSup)
remnt_vano2_set,remnt_vano2_qunifmax,remnt_vano2_qunifmin,remnt_vano2_qunifmax_fr,remnt_vano2_qunifmin_fr=traf_vias_fict(name='remnt_vano2',xmin=-xBordeCalz,xmax=xViaFict3,ymin=yPil1,ymax=yPil2,zmin=zArrVoladz,zmax=zLosSup)
remnt_vano3_set,remnt_vano3_qunifmax,remnt_vano3_qunifmin,remnt_vano3_qunifmax_fr,remnt_vano3_qunifmin_fr=traf_vias_fict(name='remnt_vano3',xmin=-xBordeCalz,xmax=xViaFict3,ymin=yPil2,ymax=yEstr2,zmin=zArrVoladz,zmax=zLosSup)

viaExt=viaExt_vano1_set+viaExt_vano2_set+viaExt_vano3_set
viaCent=viaCent_vano1_set+viaCent_vano2_set+viaCent_vano3_set

#                       ***BOUNDARY CONDITIONS***
# Regions resting on springs (Winkler elastic foundation)
#       wModulus: Winkler modulus of the foundation (springs in Z direction)
#       cRoz:     fraction of the Winkler modulus to apply for friction in
#                 the contact plane (springs in X, Y directions)
#found_wink=sprbc.ElasticFoundation(wModulus=20e7,cRoz=0.2)
#found_wink.generateSprings(xcSet=found)

# Springs (defined by Kx,Ky,Kz) to apply on nodes, points, 3Dpos, ...
# Default values for Kx, Ky, Kz are 0, which means that no spring is
# created in the corresponding direction
#spring_roof=sprbc.SpringBC(name='spring_roof',modelSpace=modelSpace,Kx=1000,Ky=0,Kz=3000)
#a=spring_roof.applyOnNodesIn3Dpos(lst3DPos=[geom.Pos3d(LbeamX/2.0,LbeamY/2.0,LcolumnZ/2.0)])

#List of contrained nodes
constrNodes=list()
#fixed DOF pilas
n_p1=nodes.getDomain.getMesh.getNearestNode(geom.Pos3d(-xPila,yPil1,-hTotPilas))
modelSpace.fixNode('000_000',n_p1.tag)
n_p2=nodes.getDomain.getMesh.getNearestNode(geom.Pos3d(xPila,yPil1,-hTotPilas))
modelSpace.fixNode('000_000',n_p2.tag)
n_p3=nodes.getDomain.getMesh.getNearestNode(geom.Pos3d(-xPila,yPil2,-hTotPilas))
modelSpace.fixNode('000_000',n_p3.tag)
n_p4=nodes.getDomain.getMesh.getNearestNode(geom.Pos3d(xPila,yPil2,-hTotPilas))
modelSpace.fixNode('000_000',n_p4.tag)
constrNodesPilas=[n_p1,n_p2,n_p3,n_p4]

# Elastomeric bearings.
from materials import bridge_bearings as bb
neopr=bb.ElastomericBearing(G=Gneopr,a=aNeopr,b=bNeopr,e=hNetoNeopr)
neopr.defineMaterials(prep)

#estribo 1
constrNodesE1=list()  #constrained nodes ordered from xmin to xmax
neopsE1=list() #elements of abutment1 ordered from xmin to xmax.
               #each element has six materials that reproduce respectively
               #Kx, Ky,Kz, KthetaX,KthetaY,KthetaZ
for xn in xCoordNeopr:
    n2=nodes.getDomain.getMesh.getNearestNode(geom.Pos3d(xn,0,zriostrEstr))
    x,y=n2.getCoo[0],n2.getCoo[1]
    n1=nodes.newNodeXYZ(x,y,zLosInf-hNetoNeopr/2.0)
    modelSpace.setRigidBeamBetweenNodes(n2.tag,n1.tag)
    n0=nodes.newNodeXYZ(x,y,zLosInf-hNetoNeopr/2.0)
    modelSpace.fixNode('000_000',n0.tag)
    constrNodesE1.append(n0)
    elem=neopr.putBetweenNodes(modelSpace,n0.tag,n1.tag)
    neopsE1.append(elem)

#estribo 2    
constrNodesE2=list()  #constrained nodes ordered from xmin to xmax
neopsE2=list() #elements of abutment1 ordered from xmin to xmax.
               #each element has six materials that reproduce respectively
               #Kx, Ky,Kz, KthetaX,KthetaY,KthetaZ
for xn in xCoordNeopr:
    n2=nodes.getDomain.getMesh.getNearestNode(geom.Pos3d(xn,yEstr2,zriostrEstr))
    x,y=n2.getCoo[0],n2.getCoo[1]
    n1=nodes.newNodeXYZ(x,y,zLosInf-hNetoNeopr/2.0)
    modelSpace.setRigidBeamBetweenNodes(n2.tag,n1.tag)
    n0=nodes.newNodeXYZ(x,y,zLosInf-hNetoNeopr/2.0)
    modelSpace.fixNode('000_000',n0.tag)
    constrNodesE2.append(n0)
    elem=neopr.putBetweenNodes(modelSpace,n0.tag,n1.tag)
    neopsE2.append(elem)
    
constrNodes=constrNodesPilas+constrNodesE1+constrNodesE2
    
    


#                       ***ACTIONS***
#overallSet=prep.getSets.getSet('total')
#Inertial load (density*acceleration) applied to the elements in a set
#selfWeight=loads.InertialLoad(name='selfWeight', lstMeshSets=[beamX_mesh,beamY_mesh,columnZ_mesh,deck_mesh,wall_mesh,found_mesh], vAccel=xc.Vector( [0.0,0.0,-grav]))
#selfWeight=loads.InertialLoad(name='selfWeight', lstMeshSets=[beamX_mesh,beamY_mesh,columnZ_mesh,deck_mesh], vAccel=xc.Vector( [0.0,0.0,-grav]))

# Load acting on one or several nodes
#     name:       name identifying the load
#     lstNod:     list of nodes  on which the load is applied
#     loadVector: xc.Vector with the six components of the load: 
#                 xc.Vector([Fx,Fy,Fz,Mx,My,Mz]).
if QCentrif > 0:
    centralNode=sets.get_lstNod_from_lst3DPos(preprocessor=prep,lst3DPos=[geom.Pos3d(0,yList[lastYpos]/2.0,zList[lastZpos])])
    centrif=loads.NodalLoad(name='centrif',lstNod=centralNode,loadVector=xc.Vector([QCentrif,0,0,0,0,0]))

# Uniform loads applied on shell elements
#    name:       name identifying the load
#    xcSet:     set that contains the surfaces
#    loadVector: xc.Vector with the six components of the load: 
#                xc.Vector([Fx,Fy,Fz,Mx,My,Mz]).
#    refSystem: reference system in which loadVector is defined:
#               'Local': element local coordinate system
#               'Global': global coordinate system (defaults to 'Global)

unifLoadPav= loads.UniformLoadOnSurfaces(name= 'unifLoadPav',xcSet=calzada,loadVector=xc.Vector([0,0,-pav_sup,0,0,0]),refSystem='Global')
unifLoadAcera= loads.UniformLoadOnSurfaces(name= 'unifLoadAcera',xcSet=acerIzq,loadVector=xc.Vector([0,0,-Lacera,0,0,0]),refSystem='Global')
qacerI=loads.UniformLoadOnSurfaces(name= 'qacerI',xcSet=acerIzq,loadVector=xc.Vector([0,0,-qunifacera,0,0,0]),refSystem='Global')
qacerD=loads.UniformLoadOnSurfaces(name= 'qacerD',xcSet=acerDer,loadVector=xc.Vector([0,0,-qunifacera,0,0,0]),refSystem='Global')
qfren_viaExt=loads.UniformLoadOnSurfaces(name= 'qfren_viaExt',xcSet=viaExt,loadVector=xc.Vector([0,-Qfrenado/(3*Ltablero),0,0,0,0]),refSystem='Global')
qfren_viaCent=loads.UniformLoadOnSurfaces(name= 'qfren_viaCent',xcSet=viaCent,loadVector=xc.Vector([0,-Qfrenado/(3*Ltablero),0,0,0,0]),refSystem='Global')
if QCentrif >0:
    qderr_viaExt=loads.UniformLoadOnSurfaces(name= 'qderr_viaExt',xcSet=viaExt,loadVector=xc.Vector([Qderrape/(3*Ltablero),0,0,0,0,0]),refSystem='Global')
    qderr_viaCent=loads.UniformLoadOnSurfaces(name= 'qderr_viaCent',xcSet=viaCent,loadVector=xc.Vector([Qderrape/(3*Ltablero),0,0,0,0,0]),refSystem='Global')


PPvoladzExt=loads.UniformLoadOnSurfaces(name= 'PPvoladzExt',xcSet=voladzExtr,loadVector=xc.Vector([0,0,-qPPvolExt,0,0,0]),refSystem='Global')
PPvoladzCent=loads.UniformLoadOnSurfaces(name= 'PPvoladzCent',xcSet=voladzCent,loadVector=xc.Vector([0,0,-qPPvolCent,0,0,0]),refSystem='Global')
PPlosRP=loads.UniformLoadOnSurfaces(name= 'PPlosRP',xcSet=losRP,loadVector=xc.Vector([0,0,-qPPlos,0,0,0]),refSystem='Global')
PPlosAlig=loads.UniformLoadOnSurfaces(name= 'PPlosAlig',xcSet=losAlig,loadVector=xc.Vector([0,0,-qPPlosAlig,0,0,0]),refSystem='Global')

# Earth pressure applied to shell or beam elements
#     Attributes:
#     name:       name identifying the load
#     xcSet:      set that contains the elements to be loaded
#     EarthPressureModel: instance of the class EarthPressureModel, with 
#                 the following attributes:
#                   K:Coefficient of pressure
#                   zGround:global Z coordinate of ground level
#                   gammaSoil: weight density of soil 
#                   zWater: global Z coordinate of groundwater level 
#                   (if zGroundwater<minimum z of model => there is no groundwater)
#                   gammaWater: weight density of water
#     if EarthPressureModel==None no earth thrust is considered
#     vDir: unit xc vector defining pressures direction

#Uniform load on beams
# syntax: UniformLoadOnBeams(name, xcSet, loadVector,refSystem)
#    name:       name identifying the load
#    xcSet:      set that contains the lines
#    loadVector: xc.Vector with the six components of the load: 
#                xc.Vector([Fx,Fy,Fz,Mx,My,Mz]).
#    refSystem: reference system in which loadVector is defined:
#               'Local': element local coordinate system
#               'Global': global coordinate system (defaults to 'Global')


Wpil_barlov_rg=[]
Wpil_barlov_rg.append(gm.IJKRange((xList.index(-xPila),yList.index(yPil1),zList.index(zInfPilAer)),(xList.index(-xPila),yList.index(yPil1),zList.index(zLosInf))))
Wpil_barlov_rg.append(gm.IJKRange((xList.index(-xPila),yList.index(yPil2),zList.index(zInfPilAer)),(xList.index(-xPila),yList.index(yPil2),zList.index(zLosInf))))
Wpil_sotav_rg=[]
Wpil_sotav_rg.append(gm.IJKRange((xList.index(xPila),yList.index(yPil1),zList.index(zInfPilAer)),(xList.index(xPila),yList.index(yPil1),zList.index(zLosInf))))
Wpil_sotav_rg.append(gm.IJKRange((xList.index(xPila),yList.index(yPil2),zList.index(zInfPilAer)),(xList.index(xPila),yList.index(yPil2),zList.index(zLosInf))))
pilBarlov=gridGeom.getSetLinMultiRegion(lstIJKRange=Wpil_barlov_rg,nameSet='pilBarlov')
pilSotav=gridGeom.getSetLinMultiRegion(lstIJKRange=Wpil_sotav_rg,nameSet='pilSotav')

WpilBarlov=loads.UniformLoadOnBeams(name='WpilBarlov', xcSet=pilBarlov,loadVector=xc.Vector([0,qWpilas,0,0,0,0]),refSystem='Local')
WpilSotav=loads.UniformLoadOnBeams(name='WpilSotav', xcSet=pilSotav,loadVector=xc.Vector([0,coef_ocult*qWpilas,0,0,0,0]),refSystem='Local')

PPpilas=loads.UniformLoadOnBeams(name='Wpilas', xcSet=pilas,loadVector=xc.Vector([-Apilas*pespConcr,0,0,0,0,0]),refSystem='Local')
PPriostrEstr=loads.UniformLoadOnBeams(name='PPriostrEstr', xcSet=riostrEstr,loadVector=xc.Vector([0,0,-qlPPriostrEstr,0,0,0]),refSystem='Local')


# Strain on shell elements
#     name:  name identifying the load
#     xcSet: set of elements
#     DOFstrain: degree of freedom to which apply the strain
#     strain: strain (e.g.: alpha x deltaT for thermal expansion)


TunifContr_01=loads.StrainLoadOnShells(name='TunifContr_01', xcSet=losas,DOFstrain=1,strain=coefDilat*Tunif_contr)
TunifContr_02=loads.StrainLoadOnShells(name='TunifContr_02', xcSet=murosAll,DOFstrain=0,strain=coefDilat*Tunif_contr)
TunifDilat_01=loads.StrainLoadOnShells(name='TunifDilat_01', xcSet=losas,DOFstrain=1,strain=coefDilat*Tunif_dilat)
TunifDilat_02=loads.StrainLoadOnShells(name='TunifDilat_02', xcSet=murosAll,DOFstrain=0,strain=coefDilat*Tunif_dilat)
GradTcal1=loads.StrainLoadOnShells(name='GradTcal1', xcSet=supTablero,DOFstrain=1,strain=coefDilat*Tfibrsup_cal)
GradTcal2=loads.StrainLoadOnShells(name='GradTcal2', xcSet=murosAll,DOFstrain=0,strain=coefDilat*Tfibrsup_cal/2.0)
GradTfrio1=loads.StrainLoadOnShells(name='GradTfrio1', xcSet=supTablero,DOFstrain=1,strain=coefDilat*Tfibrsup_fria)
GradTfrio2=loads.StrainLoadOnShells(name='GradTfrio2', xcSet=murosAll,DOFstrain=0,strain=coefDilat*Tfibrsup_fria/2.0)

Retracc_01=loads.StrainLoadOnShells(name='Retracc_01', xcSet=losas,DOFstrain=1,strain=eps_retracc)
Retracc_02=loads.StrainLoadOnShells(name='Retracc_02', xcSet=murosAll,DOFstrain=0,strain=eps_retracc)

TunifContr_01_neopr=loads.StrainLoadOnShells(name='TunifContr_01_neopr', xcSet=losas,DOFstrain=1,strain=coefDilat*Tunif_contr_neopr)
TunifContr_02_neopr=loads.StrainLoadOnShells(name='TunifContr_02_neopr', xcSet=murosAll,DOFstrain=0,strain=coefDilat*Tunif_contr_neopr)
TunifDilat_01_neopr=loads.StrainLoadOnShells(name='TunifDilat_01_neopr', xcSet=losas,DOFstrain=1,strain=coefDilat*Tunif_dilat_neopr)
TunifDilat_02_neopr=loads.StrainLoadOnShells(name='TunifDilat_02_neopr', xcSet=murosAll,DOFstrain=0,strain=coefDilat*Tunif_dilat_neopr)


# Uniform load applied to all the lines (not necessarily defined as lines
# for latter generation of beam elements, they can be lines belonging to 
# surfaces for example) found in the xcSet
# The uniform load is introduced as point loads in the nodes
#     name:   name identifying the load
#     xcSet:  set that contains the lines
#     loadVector: xc.Vector with the six components of the load: 
#                 xc.Vector([Fx,Fy,Fz,Mx,My,Mz]).
unifLoadBarrera=loads.UniformLoadOnLines(name='unifLoadBarrera', xcSet=barrera, loadVector=xc.Vector([0,0,-Lbarrera,0,0,0]))
unifLoadImposta=loads.UniformLoadOnLines(name='unifLoadImposta', xcSet=imposta, loadVector=xc.Vector([0,0,-Limposta,0,0,0]))
unifLoadAntiv=loads.UniformLoadOnLines(name='unifLoadAntiv', xcSet=imposta, loadVector=xc.Vector([0,0,-Lantivand,0,0,0]))
Wtablero=loads.UniformLoadOnLines(name='Wtablero', xcSet=arrqVol, loadVector=xc.Vector([qWTablero,0,0,0,0,0]))
WtableroSCuso=loads.UniformLoadOnLines(name='WtableroSCuso', xcSet=arrqVol, loadVector=xc.Vector([qWTableroSCuso,0,0,0,0,0]))

# Point load distributed over the shell elements in xcSet whose 
# centroids are inside the prism defined by the 2D polygon prismBase
# and one global axis.
# syntax: PointLoadOverShellElems(name, xcSet, loadVector,prismBase,prismAxis,refSystem):
#    name: name identifying the load
#    xcSet: set that contains the shell elements
#    loadVector: xc vector with the six components of the point load:
#                   xc.Vector([Fx,Fy,Fz,Mx,My,Mz]).
#    prismBase: 2D polygon that defines the n-sided base of the prism.
#                   The vertices of the polygon are defined in global 
#                   coordinates in the following way:
#                      - for X-axis-prism: (y,z)
#                      - for Y-axis-prism: (x,z)
#                      - for Z-axis-prism: (x,y)
#    prismAxis: axis of the prism (can be equal to 'X', 'Y', 'Z')
#                   (defaults to 'Z')
#    refSystem:  reference system in which loadVector is defined:
#                   'Local': element local coordinate system
#                   'Global': global coordinate system (defaults to 'Global')

# ---------------------------------------------------------------

# Point loads defined in the object lModel, distributed over the shell 
# elements under the wheels affected by them.

# syntax: VehicleDistrLoad(name,xcSet,loadModel, xCentr,yCentr,hDistr,slopeDistr)
#      name: name identifying the load
#      xcSet: set that contains the shell elements
#      lModel: instance of the class LoadModel with the definition of
#               vehicle of the load model.
#      xCent: global coord. X where to place the centroid of the vehicle
#      yCent: global coord. Y where  to place the centroid of the vehicle
#      hDistr: height considered to distribute each point load with
#               slope slopeDistr 
#      slopeDistr: slope (H/V) through hDistr to distribute the load of 
#               a wheel

#coordenadas auxiliares
xCent_vext=(xViaFict1+xBordeVoladz)/2.
xCent_vcent=(xViaFict1+xViaFict2)/2.
xCent_vint=(xViaFict1+xViaFict3)/2.

yCent_van1=yPil1/2.0
yCent_van2=(yPil1+yPil2)/2.0
yCent_van3=(yPil2+yEstr2)/2.0

yExtr_van1=2
yExtr_van2=yPil1+2

from actions.roadway_trafic import IAP_load_models as slm
from actions.roadway_trafic import load_model_base as lmb
Q1c_vext_v1=lmb.VehicleDistrLoad(name='Q1c_vext_v1',xcSet=supTablero,loadModel=slm.IAP_carril_virt1, xCentr=xCent_vext,yCentr=yCent_van1,hDistr=hDistrQ,slopeDistr=1.0)
Q1c_vext_v2=lmb.VehicleDistrLoad(name='Q1c_vext_v2',xcSet=supTablero,loadModel=slm.IAP_carril_virt1, xCentr=xCent_vext,yCentr=yCent_van2,hDistr=hDistrQ,slopeDistr=1.0)
Q2c_vcent_v1=lmb.VehicleDistrLoad(name='Q2c_vcent_v1',xcSet=supTablero,loadModel=slm.IAP_carril_virt2, xCentr=xCent_vcent,yCentr=yCent_van1,hDistr=hDistrQ,slopeDistr=1.0)
Q2c_vcent_v2=lmb.VehicleDistrLoad(name='Q2c_vcent_v2',xcSet=supTablero,loadModel=slm.IAP_carril_virt2, xCentr=xCent_vcent,yCentr=yCent_van2,hDistr=hDistrQ,slopeDistr=1.0)
Q3c_vint_v1=lmb.VehicleDistrLoad(name='Q3c_vint_v1',xcSet=supTablero,loadModel=slm.IAP_carril_virt3, xCentr=xCent_vint,yCentr=yCent_van1,hDistr=hDistrQ,slopeDistr=1.0)
Q3c_vint_v2=lmb.VehicleDistrLoad(name='Q3c_intt_v2',xcSet=supTablero,loadModel=slm.IAP_carril_virt3, xCentr=xCent_vint,yCentr=yCent_van2,hDistr=hDistrQ,slopeDistr=1.0)
Q1c_vcent_v2=lmb.VehicleDistrLoad(name='Q1c_vcent_v2',xcSet=supTablero,loadModel=slm.IAP_carril_virt1, xCentr=xCent_vcent,yCentr=yCent_van2,hDistr=hDistrQ,slopeDistr=1.0)
Q2c_vint_v2=lmb.VehicleDistrLoad(name='Q2c_vint_v2',xcSet=supTablero,loadModel=slm.IAP_carril_virt2, xCentr=xCent_vint,yCentr=yCent_van2,hDistr=hDistrQ,slopeDistr=1.0)
Q3c_vext_v2=lmb.VehicleDistrLoad(name='Q3c_vext_v2',xcSet=supTablero,loadModel=slm.IAP_carril_virt3, xCentr=xCent_vext,yCentr=yCent_van2,hDistr=hDistrQ,slopeDistr=1.0)

Q1e_vcent_v2=lmb.VehicleDistrLoad(name='Q1e_vcent_v2',xcSet=supTablero,loadModel=slm.IAP_carril_virt1, xCentr=xCent_vcent,yCentr=yExtr_van2,hDistr=hDistrQ,slopeDistr=1.0)
Q2e_vint_v2=lmb.VehicleDistrLoad(name='Q2e_vint_v2',xcSet=supTablero,loadModel=slm.IAP_carril_virt2, xCentr=xCent_vint,yCentr=yExtr_van2,hDistr=hDistrQ,slopeDistr=1.0)
Q3e_vext_v2=lmb.VehicleDistrLoad(name='Q3e_vext_v2',xcSet=supTablero,loadModel=slm.IAP_carril_virt3, xCentr=xCent_vext,yCentr=yExtr_van2,hDistr=hDistrQ,slopeDistr=1.0)

Q1e_vcent_v1=lmb.VehicleDistrLoad(name='Q1e_vcent_v1',xcSet=supTablero,loadModel=slm.IAP_carril_virt1, xCentr=xCent_vcent,yCentr=yExtr_van1,hDistr=hDistrQ,slopeDistr=1.0)
Q2e_vint_v1=lmb.VehicleDistrLoad(name='Q2e_vint_v1',xcSet=supTablero,loadModel=slm.IAP_carril_virt2, xCentr=xCent_vint,yCentr=yExtr_van1,hDistr=hDistrQ,slopeDistr=1.0)
Q3e_vext_v1=lmb.VehicleDistrLoad(name='Q3e_vext_v1',xcSet=supTablero,loadModel=slm.IAP_carril_virt3, xCentr=xCent_vext,yCentr=yExtr_van1,hDistr=hDistrQ,slopeDistr=1.0)

Q1c_vcent_v1=lmb.VehicleDistrLoad(name='Q1c_vcent_v1',xcSet=supTablero,loadModel=slm.IAP_carril_virt1, xCentr=xCent_vcent,yCentr=yCent_van1,hDistr=hDistrQ,slopeDistr=1.0)
Q2c_vint_v1=lmb.VehicleDistrLoad(name='Q2c_vint_v1',xcSet=supTablero,loadModel=slm.IAP_carril_virt2, xCentr=xCent_vint,yCentr=yCent_van1,hDistr=hDistrQ,slopeDistr=1.0)
Q3c_vext_v1=lmb.VehicleDistrLoad(name='Q3c_vext_v1',xcSet=supTablero,loadModel=slm.IAP_carril_virt3, xCentr=xCent_vext,yCentr=yCent_van1,hDistr=hDistrQ,slopeDistr=1.0)

# Carro concomitante con frenado
frQ1c_vext_v1=lmb.VehicleDistrLoad(name='frQ1c_vext_v1',xcSet=supTablero,loadModel=slm.IAP_carril_virt1_fren, xCentr=xCent_vext,yCentr=yCent_van1,hDistr=hDistrQ,slopeDistr=1.0)
frQ1c_vext_v2=lmb.VehicleDistrLoad(name='frQ1c_vext_v2',xcSet=supTablero,loadModel=slm.IAP_carril_virt1_fren, xCentr=xCent_vext,yCentr=yCent_van2,hDistr=hDistrQ,slopeDistr=1.0)
frQ2c_vcent_v1=lmb.VehicleDistrLoad(name='frQ2c_vcent_v1',xcSet=supTablero,loadModel=slm.IAP_carril_virt2_fren, xCentr=xCent_vcent,yCentr=yCent_van1,hDistr=hDistrQ,slopeDistr=1.0)
frQ2c_vcent_v2=lmb.VehicleDistrLoad(name='frQ2c_vcent_v2',xcSet=supTablero,loadModel=slm.IAP_carril_virt2_fren, xCentr=xCent_vcent,yCentr=yCent_van2,hDistr=hDistrQ,slopeDistr=1.0)
frQ3c_vint_v1=lmb.VehicleDistrLoad(name='frQ3c_vint_v1',xcSet=supTablero,loadModel=slm.IAP_carril_virt3_fren, xCentr=xCent_vint,yCentr=yCent_van1,hDistr=hDistrQ,slopeDistr=1.0)
frQ3c_vint_v2=lmb.VehicleDistrLoad(name='frQ3c_intt_v2',xcSet=supTablero,loadModel=slm.IAP_carril_virt3_fren, xCentr=xCent_vint,yCentr=yCent_van2,hDistr=hDistrQ,slopeDistr=1.0)
frQ1c_vcent_v2=lmb.VehicleDistrLoad(name='frQ1c_vcent_v2',xcSet=supTablero,loadModel=slm.IAP_carril_virt1_fren, xCentr=xCent_vcent,yCentr=yCent_van2,hDistr=hDistrQ,slopeDistr=1.0)
frQ2c_vint_v2=lmb.VehicleDistrLoad(name='frQ2c_vint_v2',xcSet=supTablero,loadModel=slm.IAP_carril_virt2_fren, xCentr=xCent_vint,yCentr=yCent_van2,hDistr=hDistrQ,slopeDistr=1.0)
frQ3c_vext_v2=lmb.VehicleDistrLoad(name='frQ3c_vext_v2',xcSet=supTablero,loadModel=slm.IAP_carril_virt3_fren, xCentr=xCent_vext,yCentr=yCent_van2,hDistr=hDistrQ,slopeDistr=1.0)

frQ1e_vcent_v2=lmb.VehicleDistrLoad(name='frQ1e_vcent_v2',xcSet=supTablero,loadModel=slm.IAP_carril_virt1_fren, xCentr=xCent_vcent,yCentr=yExtr_van2,hDistr=hDistrQ,slopeDistr=1.0)
frQ2e_vint_v2=lmb.VehicleDistrLoad(name='frQ2e_vint_v2',xcSet=supTablero,loadModel=slm.IAP_carril_virt2_fren, xCentr=xCent_vint,yCentr=yExtr_van2,hDistr=hDistrQ,slopeDistr=1.0)
frQ3e_vext_v2=lmb.VehicleDistrLoad(name='frQ3e_vext_v2',xcSet=supTablero,loadModel=slm.IAP_carril_virt3_fren, xCentr=xCent_vext,yCentr=yExtr_van2,hDistr=hDistrQ,slopeDistr=1.0)

frQ1e_vcent_v1=lmb.VehicleDistrLoad(name='frQ1e_vcent_v1',xcSet=supTablero,loadModel=slm.IAP_carril_virt1_fren, xCentr=xCent_vcent,yCentr=yExtr_van1,hDistr=hDistrQ,slopeDistr=1.0)
frQ2e_vint_v1=lmb.VehicleDistrLoad(name='frQ2e_vint_v1',xcSet=supTablero,loadModel=slm.IAP_carril_virt2_fren, xCentr=xCent_vint,yCentr=yExtr_van1,hDistr=hDistrQ,slopeDistr=1.0)
frQ3e_vext_v1=lmb.VehicleDistrLoad(name='frQ3e_vext_v1',xcSet=supTablero,loadModel=slm.IAP_carril_virt3_fren, xCentr=xCent_vext,yCentr=yExtr_van1,hDistr=hDistrQ,slopeDistr=1.0)

frQ1c_vcent_v1=lmb.VehicleDistrLoad(name='frQ1c_vcent_v1',xcSet=supTablero,loadModel=slm.IAP_carril_virt1_fren, xCentr=xCent_vcent,yCentr=yCent_van1,hDistr=hDistrQ,slopeDistr=1.0)
frQ2c_vint_v1=lmb.VehicleDistrLoad(name='frQ2c_vint_v1',xcSet=supTablero,loadModel=slm.IAP_carril_virt2_fren, xCentr=xCent_vint,yCentr=yCent_van1,hDistr=hDistrQ,slopeDistr=1.0)
frQ3c_vext_v1=lmb.VehicleDistrLoad(name='frQ3c_vext_v1',xcSet=supTablero,loadModel=slm.IAP_carril_virt3_fren, xCentr=xCent_vext,yCentr=yCent_van1,hDistr=hDistrQ,slopeDistr=1.0)

#    ***LOAD CASES***
#auxiliar lists
qunif_sit1=[viaExt_vano1_qunifmax,viaExt_vano2_qunifmax,viaExt_vano3_qunifmax,qacerD]
qunif_sit2=[
    viaExt_vano1_qunifmax,viaExt_vano2_qunifmax,viaExt_vano3_qunifmax,
    viaCent_vano1_qunifmin,viaCent_vano2_qunifmin,viaCent_vano3_qunifmin,
    viaInt_vano1_qunifmin,viaInt_vano2_qunifmin,viaInt_vano3_qunifmin,
    remnt_vano1_qunifmin,remnt_vano2_qunifmin,remnt_vano3_qunifmin,
    qacerI,qacerD]        
qunif_sit2_fr=[
    viaExt_vano1_qunifmax_fr,viaExt_vano2_qunifmax_fr,viaExt_vano3_qunifmax_fr,
    viaCent_vano1_qunifmin_fr,viaCent_vano2_qunifmin_fr,viaCent_vano3_qunifmin_fr,
    viaInt_vano1_qunifmin_fr,viaInt_vano2_qunifmin_fr,viaInt_vano3_qunifmin_fr,
    remnt_vano1_qunifmin_fr,remnt_vano2_qunifmin_fr,remnt_vano3_qunifmin_fr,
    qacerI,qacerD]        
qunif_sit3=[viaExt_vano2_qunifmin,
viaCent_vano2_qunifmax,
viaInt_vano2_qunifmin,
remnt_vano2_qunifmin
]
qunif_sit4=[
    viaExt_vano1_qunifmin,viaExt_vano2_qunifmin,viaExt_vano3_qunifmin,
    viaCent_vano1_qunifmax,viaCent_vano2_qunifmax,viaCent_vano3_qunifmax,
    viaInt_vano1_qunifmin,viaInt_vano2_qunifmin,viaInt_vano3_qunifmin,
    remnt_vano1_qunifmin,remnt_vano2_qunifmin,remnt_vano3_qunifmin,
    qacerI,qacerD]
qunif_sit4_fr=[
    viaExt_vano1_qunifmin_fr,viaExt_vano2_qunifmin_fr,viaExt_vano3_qunifmin_fr,
    viaCent_vano1_qunifmax_fr,viaCent_vano2_qunifmax_fr,viaCent_vano3_qunifmax_fr,
    viaInt_vano1_qunifmin_fr,viaInt_vano2_qunifmin_fr,viaInt_vano3_qunifmin_fr,
    remnt_vano1_qunifmin_fr,remnt_vano2_qunifmin_fr,remnt_vano3_qunifmin_fr,
    qacerI,qacerD]
  
qunif_sit5=[
    viaExt_vano1_qunifmin,
    viaCent_vano1_qunifmax,
    viaInt_vano1_qunifmin,
    remnt_vano1_qunifmin]


G1=lcases.LoadCase(preprocessor=prep,name="G1",loadPType="default",timeSType="constant_ts")
G1.create()
G1.addLstLoads([PPvoladzExt,PPvoladzCent,PPlosRP,PPlosAlig,PPriostrEstr,PPpilas])


G2=lcases.LoadCase(preprocessor=prep,name="G2")
G2.create()
G2.addLstLoads([unifLoadPav,unifLoadAcera,unifLoadBarrera,unifLoadImposta,unifLoadAntiv])

G3=lcases.LoadCase(preprocessor=prep,name="G3")
G3.create()
G3.addLstLoads([Retracc_01,Retracc_02])

#Sobrecargas de uso
Q1a_1=lcases.LoadCase(preprocessor=prep,name="Q1a_1")
Q1a_1.create()
Q1a_1.addLstLoads(qunif_sit1+[Q1c_vext_v1])

Q1a_2=lcases.LoadCase(preprocessor=prep,name="Q1a_2")
Q1a_2.create()
Q1a_2.addLstLoads(qunif_sit1+[Q1c_vext_v2])

Q1b_1=lcases.LoadCase(preprocessor=prep,name="Q1b_1")
Q1b_1.create()
Q1b_1.addLstLoads(qunif_sit2+[Q1c_vext_v1,Q2c_vcent_v1,Q3c_vint_v1])

Q1b_2=lcases.LoadCase(preprocessor=prep,name="Q1b_2")
Q1b_2.create()
if QCentrif >0:
    Q1b_2.addLstLoads(qunif_sit2+[Q1c_vext_v2,Q2c_vcent_v2,Q3c_vint_v2,centrif])
else:
    Q1b_2.addLstLoads(qunif_sit2+[Q1c_vext_v2,Q2c_vcent_v2,Q3c_vint_v2])

Q1c=lcases.LoadCase(preprocessor=prep,name="Q1c")
Q1c.create()
Q1c.addLstLoads(qunif_sit3+[Q1c_vcent_v2,Q2c_vint_v2,Q3c_vext_v2])

Q1d=lcases.LoadCase(preprocessor=prep,name="Q1d")
Q1d.create()
Q1d.addLstLoads(qunif_sit4+[Q1e_vcent_v2,Q2e_vint_v2,Q3e_vext_v2])

Q1e=lcases.LoadCase(preprocessor=prep,name="Q1e")
Q1e.create()
Q1e.addLstLoads(qunif_sit4+[Q1e_vcent_v1,Q2e_vint_v1,Q3e_vext_v1])

Q1f=lcases.LoadCase(preprocessor=prep,name="Q1f")
Q1f.create()
Q1f.addLstLoads(qunif_sit5+[Q3c_vext_v1,Q1c_vcent_v1,Q2c_vint_v1])

Q1b_fren=lcases.LoadCase(preprocessor=prep,name="Q1b_fren")
Q1b_fren.create()
if QCentrif > 0:
    Q1b_fren.addLstLoads(qunif_sit2_fr+[frQ1c_vext_v1,frQ2c_vcent_v1,frQ3c_vint_v1,qfren_viaExt,qderr_viaExt,centrif])
else:
    Q1b_fren.addLstLoads(qunif_sit2_fr+[frQ1c_vext_v1,frQ2c_vcent_v1,frQ3c_vint_v1,qfren_viaExt])

Q1e_fren=lcases.LoadCase(preprocessor=prep,name="Q1e_fren")
Q1e_fren.create()
if QCentrif > 0:
    Q1e_fren.addLstLoads(qunif_sit4_fr+[frQ1e_vcent_v1,frQ2e_vint_v1,frQ3e_vext_v1,qfren_viaCent,qderr_viaCent,centrif])
else:
    Q1e_fren.addLstLoads(qunif_sit4_fr+[frQ1e_vcent_v1,frQ2e_vint_v1,frQ3e_vext_v1,qfren_viaCent])

Q1d_fren=lcases.LoadCase(preprocessor=prep,name="Q1d_fren")
Q1d_fren.create()
if QCentrif > 0:
    Q1d_fren.addLstLoads(qunif_sit4_fr+[frQ1e_vcent_v2,frQ2e_vint_v2,frQ3e_vext_v2,qfren_viaCent,qderr_viaCent,centrif])
else:
    Q1d_fren.addLstLoads(qunif_sit4_fr+[frQ1e_vcent_v2,frQ2e_vint_v2,frQ3e_vext_v2,qfren_viaCent])
    
Q2_1=lcases.LoadCase(preprocessor=prep,name="Q2_1")
Q2_1.create()
Q2_1.addLstLoads([WpilBarlov,WpilSotav,Wtablero])

Q2_2=lcases.LoadCase(preprocessor=prep,name="Q2_2")
Q2_2.create()
Q2_2.addLstLoads([WpilBarlov,WpilSotav,WtableroSCuso])

Q3_1=lcases.LoadCase(preprocessor=prep,name="Q3_1")
Q3_1.create()
Q3_1.addLstLoads([TunifContr_01,TunifContr_02])

Q3_2=lcases.LoadCase(preprocessor=prep,name="Q3_2")
Q3_2.create()
Q3_2.addLstLoads([TunifDilat_01,TunifDilat_02])

Q3_3=lcases.LoadCase(preprocessor=prep,name="Q3_3")
Q3_3.create()
Q3_3.addLstLoads([GradTcal1,GradTcal2])

Q3_4=lcases.LoadCase(preprocessor=prep,name="Q3_4")
Q3_4.create()
Q3_4.addLstLoads([GradTfrio1,GradTfrio2])

Q3_1_neopr=lcases.LoadCase(preprocessor=prep,name="Q3_1_neopr")
Q3_1_neopr.create()
Q3_1_neopr.addLstLoads([TunifContr_01_neopr,TunifContr_02_neopr])

Q3_2_neopr=lcases.LoadCase(preprocessor=prep,name="Q3_2_neopr")
Q3_2_neopr.create()
Q3_2_neopr.addLstLoads([TunifDilat_01_neopr,TunifDilat_02_neopr])

#    ***LIMIT STATE COMBINATIONS***
combContainer= cc.CombContainer()  #Container of load combinations
# COMBINATIONS OF ACTIONS FOR SERVICEABILITY LIMIT STATES
    # name:        name to identify the combination
    # rare:        combination for a rare design situation
    # freq:        combination for a frequent design situation
    # qp:          combination for a quasi-permanent design situation
    # earthquake:  combination for a seismic design situation
#Characteristic combinations.
#combContainer.SLS.rare.add('ELSR01', '1.0*GselfWeight')
#Frequent combinations.
#combContainer.SLS.freq.add('ELSF01', '1.0*GselfWeight+1.0*Qdeck+1.0*QearthPressWall')
#Quasi permanent combinations.
#combContainer.SLS.qp.add('ELSQP01', '1.0*GselfWeight+1.0*Qdeck')

# COMBINATIONS OF ACTIONS FOR ULTIMATE LIMIT STATES
    # name:        name to identify the combination
    # perm:        combination for a persistent or transient design situation
    # acc:         combination for a accidental design situation
    # fatigue:     combination for a fatigue design situation
    # earthquake:  combination for a seismic design situation
#Persistent and transitory situations.
combContainer.ULS.perm.add('ELU01', '10*G1')


#Fatigue.
# Combinations' names must be:
#        - ELUF0: unloaded structure (permanent loads)
#        - ELUF1: fatigue load in position 1.
#combContainer.ULS.fatigue.add('ELUF0','1.00*GselfWeight+1.0*Qdeck')
#combContainer.ULS.fatigue.add('ELUF1','1.00*GselfWeight+1.0*QearthPressWall')



pilasInf.description='Pilas, zona inferior'
pilasInf.color=cfg.colors['brown04']
pilasSup.description='Pilas, zona superior'
pilasSup.color=cfg.colors['brown01']
pilas.description='Pilas'
pilas.color=cfg.colors['brown03']
losInf.description='Losa aligerada, cordón inferior'
losInf.color=cfg.colors['purple03']
losSup.description='Losa aligerada, cordón superior'
losSup.color=cfg.colors['purple01']
murAlig.description='Losa aligerada, nervios'
murAlig.name='murAlig'
murAlig.color=cfg.colors['orange02']
murExtAlig.description='Losa aligerada, almas borde'
murExtAlig.color=cfg.colors['yellow02']
voladzCent.description='Voladizo, zona central'
voladzCent.color=cfg.colors['brown01']
voladzExtr.description='Voladizo, zona de borde'
voladzExtr.color=cfg.colors['brown02']
supTablero.description='Losa tablero, cordón superior y voladizos'
supTablero.color=cfg.colors['yellow02']
total=prep.getSets.getSet('total')
tablero=losInf+losSup+murAlig+murExtAlig+murRP+diafRP
tablero.name='Tablero'
tablero.description='Tablero'
tablero.color=cfg.colors['purple01']
allLosas=losInf+losSup+voladzCent+voladzExtr
allLosas.name='allLosas'
allLosas.description='Losa tablero, cordones superior e inferior y voladizos'

overallSet=pilasInf+pilasSup+riostrEstr1+riostrEstr2+losInfV1+losInfV2+losInfV3+losInfRP1+losInfRP2+losSupV1+losSupV2+losSupV3+losSupRP1+losSupRP2+murAligV1+murAligV2+murAligV3+murExtAligV1+murExtAligV2+murExtAligV3+murRP1+murRP2+diafRP1+diafRP2+voladzCentV1+voladzCentV2+voladzCentV3+voladzCentRP1+voladzCentRP2+voladzExtrV1+voladzExtrV2+voladzExtrV3+voladzExtrRP1+voladzExtrRP2
overallSet.description='Estructura'
overallSet.name='overallSet'
overallSet.color=cfg.colors['purple01']
'''
nodesTot=total.nodes
for n in nodesTot:
    if n.isFree:
        print 'node ',n.tag, ' is free'
'''


