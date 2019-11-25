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
losInfV1_rg=[gut.def_rg_cooLim(XYZListsTabl,XLosa,YLosligVano1,(zLosInf,zLosInf))]
losInfV2_rg=[gut.def_rg_cooLim(XYZListsTabl,XLosa,YLosligVano2,(zLosInf,zLosInf))]
losInfV3_rg=[gut.def_rg_cooLim(XYZListsTabl,XLosa,YLosligVano3,(zLosInf,zLosInf))]
losInfRP1_rg=[gut.def_rg_cooLim(XYZListsTabl,XLosa,YriostrPil1,(zLosInf,zLosInf))]
losInfRP2_rg=[gut.def_rg_cooLim(XYZListsTabl,XLosa,YriostrPil2,(zLosInf,zLosInf))]
losSupV1_rg=[gut.def_rg_cooLim(XYZListsTabl,XLosa,YLosligVano1,(zLosSup,zLosSup))]
losSupV2_rg=[gut.def_rg_cooLim(XYZListsTabl,XLosa,YLosligVano2,(zLosSup,zLosSup))]
losSupV3_rg=[gut.def_rg_cooLim(XYZListsTabl,XLosa,YLosligVano3,(zLosSup,zLosSup))]
losSupRP1_rg=[gut.def_rg_cooLim(XYZListsTabl,XLosa,YriostrPil1,(zLosSup,zLosSup))]
losSupRP2_rg=[gut.def_rg_cooLim(XYZListsTabl,XLosa,YriostrPil2,(zLosSup,zLosSup))]
aux_rg=gut.def_rg_cooLim(XYZListsTabl,(xAlmasAlig[0],xAlmasAlig[-1]),YriostrPil1,(zLosInf,zLosSup))
diafRP1_rg=aux_rg.extractIncludedIKranges()
aux_rg=gut.def_rg_cooLim(XYZListsTabl,(xAlmasAlig[0],xAlmasAlig[-1]),YriostrPil2,(zLosInf,zLosSup))
diafRP2_rg=aux_rg.extractIncludedIKranges()

def rg_mur(Ycoor,Zcoor=ZmurAlig,Xmur=xAlmasAlig,xyzL=XYZListsTabl):
    rg=list()
    for x in Xmur:
        rg.append(gut.def_rg_cooLim(xyzL,(x,x),Ycoor,Zcoor))
    return rg
murAligV1_rg=rg_mur(YLosligVano1)
murAligV2_rg=rg_mur(YLosligVano2)
murAligV3_rg=rg_mur(YLosligVano3)

xmurRiostr=[xVoladz[0][-1]]+xAlmasAlig+[xVoladz[1][0]]
murRP1_rg=rg_mur(YriostrPil1,Xmur=xmurRiostr)
murRP2_rg=rg_mur(YriostrPil2,Xmur=xmurRiostr)


xmurExtAlig=[xVoladz[0][-1],xVoladz[1][0]]
murExtAligV1_rg=rg_mur(YLosligVano1,Xmur=xmurExtAlig)
murExtAligV2_rg=rg_mur(YLosligVano2,Xmur=xmurExtAlig)
murExtAligV3_rg=rg_mur(YLosligVano3,Xmur=xmurExtAlig)

voladzCentV1_rg=[gut.def_rg_cooLim(XYZListsTabl,XvoladzCentI,YLosligVano1,Zvoladz),gut.def_rg_cooLim(XYZListsTabl,XvoladzCentD,YLosligVano1,Zvoladz)]
voladzCentV2_rg=[gut.def_rg_cooLim(XYZListsTabl,XvoladzCentI,YLosligVano2,Zvoladz),gut.def_rg_cooLim(XYZListsTabl,XvoladzCentD,YLosligVano2,Zvoladz)]
voladzCentV3_rg=[gut.def_rg_cooLim(XYZListsTabl,XvoladzCentI,YLosligVano3,Zvoladz),gut.def_rg_cooLim(XYZListsTabl,XvoladzCentD,YLosligVano3,Zvoladz)]
voladzCentRP1_rg=[gut.def_rg_cooLim(XYZListsTabl,XvoladzCentI,YriostrPil1,Zvoladz),gut.def_rg_cooLim(XYZListsTabl,XvoladzCentD,YriostrPil1,Zvoladz)]
voladzCentRP2_rg=[gut.def_rg_cooLim(XYZListsTabl,XvoladzCentI,YriostrPil2,Zvoladz),gut.def_rg_cooLim(XYZListsTabl,XvoladzCentD,YriostrPil2,Zvoladz)]

voladzExtrV1_rg=[gut.def_rg_cooLim(XYZListsTabl,XvoladzExtrI,YLosligVano1,Zvoladz),gut.def_rg_cooLim(XYZListsTabl,XvoladzExtrD,YLosligVano1,Zvoladz)]
voladzExtrV2_rg=[gut.def_rg_cooLim(XYZListsTabl,XvoladzExtrI,YLosligVano2,Zvoladz),gut.def_rg_cooLim(XYZListsTabl,XvoladzExtrD,YLosligVano2,Zvoladz)]
voladzExtrV3_rg=[gut.def_rg_cooLim(XYZListsTabl,XvoladzExtrI,YLosligVano3,Zvoladz),gut.def_rg_cooLim(XYZListsTabl,XvoladzExtrD,YLosligVano3,Zvoladz)]
voladzExtrRP1_rg=[gut.def_rg_cooLim(XYZListsTabl,XvoladzExtrI,YriostrPil1,Zvoladz),gut.def_rg_cooLim(XYZListsTabl,XvoladzExtrD,YriostrPil1,Zvoladz)]
voladzExtrRP2_rg=[gut.def_rg_cooLim(XYZListsTabl,XvoladzExtrI,YriostrPil2,Zvoladz),gut.def_rg_cooLim(XYZListsTabl,XvoladzExtrD,YriostrPil2,Zvoladz)]

riostrEstr1_rg=[]
riostrEstr1_rg.append(gm.IJKRange((0,0,zListTabl.index(zriostrEstr)),(len(xListTabl)-1,0,zListTabl.index(zriostrEstr))))
riostrEstr2_rg=[]
riostrEstr2_rg.append(gm.IJKRange((0,len(yListTabl)-1,zListTabl.index(zriostrEstr)),(len(xListTabl)-1,len(yListTabl)-1,zListTabl.index(zriostrEstr))))


#Lines generation
riostrEstr1=gridTabl.genLinMultiRegion(lstIJKRange=riostrEstr1_rg,nameSet='riostrEstr1')
riostrEstr2=gridTabl.genLinMultiRegion(lstIJKRange=riostrEstr2_rg,nameSet='riostrEstr2')

#Surfaces generation
losInfV1=gridTabl.genSurfMultiRegion(lstIJKRange=losInfV1_rg,nameSet='losInfV1')
losInfV2=gridTabl.genSurfMultiRegion(lstIJKRange=losInfV2_rg,nameSet='losInfV2')
losInfV3=gridTabl.genSurfMultiRegion(lstIJKRange=losInfV3_rg,nameSet='losInfV3')
losInfRP1=gridTabl.genSurfMultiRegion(lstIJKRange=losInfRP1_rg,nameSet='losInfRP1')
losInfRP2=gridTabl.genSurfMultiRegion(lstIJKRange=losInfRP2_rg,nameSet='losInfRP2')

losSupV1=gridTabl.genSurfMultiRegion(lstIJKRange=losSupV1_rg,nameSet='losSupV1')
losSupV2=gridTabl.genSurfMultiRegion(lstIJKRange=losSupV2_rg,nameSet='losSupV2')
losSupV3=gridTabl.genSurfMultiRegion(lstIJKRange=losSupV3_rg,nameSet='losSupV3')
losSupRP1=gridTabl.genSurfMultiRegion(lstIJKRange=losSupRP1_rg,nameSet='losSupRP1')
losSupRP2=gridTabl.genSurfMultiRegion(lstIJKRange=losSupRP2_rg,nameSet='losSupRP2')


murAligV1=gridTabl.genSurfMultiRegion(lstIJKRange=murAligV1_rg,nameSet='murAligV1')
murAligV2=gridTabl.genSurfMultiRegion(lstIJKRange=murAligV2_rg,nameSet='murAligV2')
murAligV3=gridTabl.genSurfMultiRegion(lstIJKRange=murAligV3_rg,nameSet='murAligV3')



murExtAligV1=gridTabl.genSurfMultiRegion(lstIJKRange=murExtAligV1_rg,nameSet='murExtAligV1')
murExtAligV2=gridTabl.genSurfMultiRegion(lstIJKRange=murExtAligV2_rg,nameSet='murExtAligV2')
murExtAligV3=gridTabl.genSurfMultiRegion(lstIJKRange=murExtAligV3_rg,nameSet='murExtAligV3')

murRP1=gridTabl.genSurfMultiRegion(lstIJKRange=murRP1_rg,nameSet='murRP1')
murRP2=gridTabl.genSurfMultiRegion(lstIJKRange=murRP2_rg,nameSet='murRP2')

diafRP1=gridTabl.genSurfMultiRegion(lstIJKRange=diafRP1_rg,nameSet='diafRP1')
diafRP2=gridTabl.genSurfMultiRegion(lstIJKRange=diafRP2_rg,nameSet='diafRP2')

voladzCentV1=gridTabl.genSurfMultiRegion(lstIJKRange=voladzCentV1_rg,nameSet='voladzCentV1')
voladzCentV2=gridTabl.genSurfMultiRegion(lstIJKRange=voladzCentV2_rg,nameSet='voladzCentV2')
voladzCentV3=gridTabl.genSurfMultiRegion(lstIJKRange=voladzCentV3_rg,nameSet='voladzCentV3')
voladzCentRP1=gridTabl.genSurfMultiRegion(lstIJKRange=voladzCentRP1_rg,nameSet='voladzCentRP1')
voladzCentRP2=gridTabl.genSurfMultiRegion(lstIJKRange=voladzCentRP2_rg,nameSet='voladzCentRP2')

voladzExtrV1=gridTabl.genSurfMultiRegion(lstIJKRange=voladzExtrV1_rg,nameSet='voladzExtrV1')
voladzExtrV2=gridTabl.genSurfMultiRegion(lstIJKRange=voladzExtrV2_rg,nameSet='voladzExtrV2')
voladzExtrV3=gridTabl.genSurfMultiRegion(lstIJKRange=voladzExtrV3_rg,nameSet='voladzExtrV3')
voladzExtrRP1=gridTabl.genSurfMultiRegion(lstIJKRange=voladzExtrRP1_rg,nameSet='voladzExtrRP1')
voladzExtrRP2=gridTabl.genSurfMultiRegion(lstIJKRange=voladzExtrRP2_rg,nameSet='voladzExtrRP2')


#                         *** MATERIALS ***
concrete=EHE_materials.HA30
concrProp=tm.MaterialData(name='concrProp',E=concrete.Ecm(),nu=concrete.nuc,rho=concrete.density())

# Isotropic elastic section-material appropiate for plate and shell analysis
losInf_mat=tm.DeckMaterialData(name='losInf_mat',thickness= espLosAlig,material=concrProp)
losInf_mat.setupElasticSection(preprocessor=prep)   #creates the section-material

losSup_mat=tm.DeckMaterialData(name='losSup_mat',thickness= espLosAlig,material=concrProp)
losSup_mat.setupElasticSection(preprocessor=prep)   #creates the section-material

murAlig_mat=tm.DeckMaterialData(name='murAlig_mat',thickness= espEntreAlig,material=concrProp)
murAlig_mat.setupElasticSection(preprocessor=prep)   #creates the section-material

diafRP_mat=tm.DeckMaterialData(name='diafRP_mat',thickness=espDiafRP ,material=concrProp)
diafRP_mat.setupElasticSection(preprocessor=prep)

murExtAlig_mat=tm.DeckMaterialData(name='murExtAlig_mat',thickness=espExtAlig,material=concrProp)
murExtAlig_mat.setupElasticSection(preprocessor=prep)   #creates the section-material

voladzCent_mat=tm.DeckMaterialData(name='voladzCent_mat',thickness= espVoladzMax,material=concrProp)
voladzCent_mat.setupElasticSection(preprocessor=prep)   #creates the section-material

voladzExtr_mat=tm.DeckMaterialData(name='voladzExtr_mat',thickness= espVoladzMin,material=concrProp)
voladzExtr_mat.setupElasticSection(preprocessor=prep)   #creates the section-material


#Geometric sections
#rectangular sections
from materials.sections import section_properties as sectpr
geomSectRiostrEstr=sectpr.RectangularSection(name='geomSectRiostrEstr',b=cantoRiostrEstr,h=cantoLosa)
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
riostrEstr_mat= tm.BeamMaterialData(name= 'riostrEstr_mat', section=geomSectRiostrEstr, material=concrProp)
riostrEstr_mat.setupElasticShear3DSection(preprocessor=prep)


#                         ***FE model - MESH***
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
#fem.multi_mesh(preprocessor=prep,lstMeshSets=[pilasInf_mesh,pilasSup_mesh])
fem.multi_mesh(preprocessor=prep,lstMeshSets=[riostrEstr1_mesh,riostrEstr2_mesh])
fem.multi_mesh(preprocessor=prep,lstMeshSets=[losInfV1_mesh,losInfV2_mesh,losInfV3_mesh,losInfRP1_mesh,losInfRP2_mesh,losSupV1_mesh,losSupV2_mesh,losSupV3_mesh,losSupRP1_mesh,losSupRP2_mesh])
fem.multi_mesh(preprocessor=prep,lstMeshSets=[murAligV1_mesh,murAligV2_mesh,murAligV3_mesh])
fem.multi_mesh(preprocessor=prep,lstMeshSets=[murExtAligV1_mesh,murExtAligV2_mesh,murExtAligV3_mesh])
fem.multi_mesh(preprocessor=prep,lstMeshSets=[murRP1_mesh,murRP2_mesh])
fem.multi_mesh(preprocessor=prep,lstMeshSets=[diafRP1_mesh,diafRP2_mesh])
fem.multi_mesh(preprocessor=prep,lstMeshSets=[voladzCentV1_mesh,voladzCentV2_mesh,voladzCentV3_mesh,voladzCentRP1_mesh,voladzCentRP2_mesh,voladzExtrV1_mesh,voladzExtrV2_mesh,voladzExtrV3_mesh,voladzExtrRP1_mesh,voladzExtrRP2_mesh])

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
voladzExtr=voladzExtrV1+voladzExtrV2+voladzExtrV3+voladzExtrRP1+voladzExtrRP2
voladzExtr.name='voladzExtr'
voladzCent=voladzCentV1+voladzCentV2+voladzCentV3+voladzCentRP1+voladzCentRP2
voladzCent.name='voladzCent'
riostrEstr=riostrEstr1+riostrEstr2
riostrEstr.name='riostrEstr'
riostrEstr.description='Riostras estribos'


acerIzq_rg=list()
acerIzq_rg.append(gm.IJKRange((0,0,zListTabl.index(zArrVoladz)),(xListTabl.index(xCalzada[0]),len(yListTabl)-1,zListTabl.index(zArrVoladz))))
acerIzq=gridTabl.getSetSurfMultiRegion(lstIJKRange=acerIzq_rg,nameSet='acerIzq')

acerDer_rg=list()
acerDer_rg.append(gm.IJKRange((xListTabl.index(xCalzada[-1]),0,zListTabl.index(zArrVoladz)),(len(xListTabl)-1,len(yListTabl)-1,zListTabl.index(zArrVoladz))))
acerDer=gridTabl.getSetSurfMultiRegion(lstIJKRange=acerDer_rg,nameSet='acerDer')

aceras=acerIzq+acerDer
aceras.name='aceras'

calzada_rg=gm.IJKRange((xListTabl.index(xCalzada[0]),0,zListTabl.index(zArrVoladz)),(xListTabl.index(xCalzada[-1]),len(yListTabl)-1,zListTabl.index(zLosSup))).extractIncludedIJranges()
calzada=gridTabl.getSetSurfMultiRegion(lstIJKRange=calzada_rg,nameSet='calzada')
#Imposta
auxSetPnt1=gridTabl.getSetPntRange(ijkRange=gm.IJKRange((0,0,zListTabl.index(zArrVoladz)),(0,len(yListTabl)-1,zListTabl.index(zArrVoladz))),setName='auxSetPnt1')
auxSetPnt2=gridTabl.getSetPntRange(ijkRange=gm.IJKRange((len(xListTabl)-1,0,zListTabl.index(zArrVoladz)),(len(xListTabl)-1,len(yListTabl)-1,zListTabl.index(zArrVoladz))),setName='auxSetPnt2')
auxSetPnt=auxSetPnt1+auxSetPnt2
auxSetPnt.name='auxSetPnt'
imposta=sets.get_lines_on_points(setPoints=auxSetPnt,setLinName='imposta',onlyIncluded=True)
barrera_rg=list()
auxSetPnt1=gridTabl.getSetPntRange(ijkRange=gm.IJKRange((xListTabl.index(xCalzada[0]),0,zListTabl.index(zArrVoladz)),(xListTabl.index(xCalzada[0]),len(yListTabl)-1,zListTabl.index(zArrVoladz))),setName='auxSetPnt1')
auxSetPnt2=gridTabl.getSetPntRange(ijkRange=gm.IJKRange((xListTabl.index(xCalzada[-1]),0,zListTabl.index(zArrVoladz)),(xListTabl.index(xCalzada[-1]),len(yListTabl)-1,zListTabl.index(zArrVoladz))),setName='auxSetPnt2')
auxSetPnt=auxSetPnt1+auxSetPnt2
auxSetPnt.name='auxSetPnt'
barrera=sets.get_lines_on_points(setPoints=auxSetPnt,setLinName='barrera',onlyIncluded=True)
#línea arranque voladizo izquierdo (aplicación W)
arrqVolPnt=gridTabl.getSetPntRange(ijkRange=gm.IJKRange((xListTabl.index(xVoladz[0][-1]),0,zListTabl.index(zArrVoladz)),(xListTabl.index(xVoladz[0][-1]),len(yListTabl)-1,zListTabl.index(zArrVoladz))),setName='arrqVolPnt')
arrqVol=sets.get_lines_on_points(setPoints=arrqVolPnt,setLinName='arrqVol',onlyIncluded=True)

#    sets vías fictíceas, cargas uniformes tren de cargas (fr: concomitantes con frenado 0.4*q)
def traf_vias_fict(name,xmin,xmax,ymin,ymax,zmin,zmax,qmax=qunifmax,qmin=qunifmin,preprocessor=prep):
    rg=gm.IJKRange((xListTabl.index(xmin),yListTabl.index(ymin),zListTabl.index(zmin)),(xListTabl.index(xmax),yListTabl.index(ymax),zListTabl.index(zmax))).extractIncludedIJranges()
    nmset=name+'_set'
    retval=(gridTabl.getSetSurfMultiRegion(lstIJKRange=rg,nameSet=name+'_set'),
            loads.UniformLoadOnSurfaces(name=name+'_qunifmax',xcSet=preprocessor.getSets.getSet(nmset),loadVector=xc.Vector([0,0,-qmax,0,0,0]),refSystem='Global'),
            loads.UniformLoadOnSurfaces(name=name+'_qunifmin',xcSet=preprocessor.getSets.getSet(nmset),loadVector=xc.Vector([0,0,-qmin,0,0,0]),refSystem='Global'),
            loads.UniformLoadOnSurfaces(name=name+'_frqunifmax',xcSet=preprocessor.getSets.getSet(nmset),loadVector=xc.Vector([0,0,-0.4*qmax,0,0,0]),refSystem='Global'),
            loads.UniformLoadOnSurfaces(name=name+'_frqunifmin',xcSet=preprocessor.getSets.getSet(nmset),loadVector=xc.Vector([0,0,-0.4*qmin,0,0,0]),refSystem='Global')
             )
    return retval

viaExt_vano1_set,viaExt_vano1_qunifmax,viaExt_vano1_qunifmin,viaExt_vano1_qunifmax_fr,viaExt_vano1_qunifmin_fr=traf_vias_fict(name='viaExt_vano1',xmin=xViaFict[0][0],xmax=xViaFict[0][-1],ymin=0,ymax=yPil1,zmin=zArrVoladz,zmax=zLosSup)

viaExt_vano2_set,viaExt_vano2_qunifmax,viaExt_vano2_qunifmin,viaExt_vano2_qunifmax_fr,viaExt_vano2_qunifmin_fr=traf_vias_fict(name='viaExt_vano2',xmin=xViaFict[0][0],xmax=xViaFict[0][-1],ymin=yPil1,ymax=yPil2,zmin=zArrVoladz,zmax=zLosSup)

viaExt_vano3_set,viaExt_vano3_qunifmax,viaExt_vano3_qunifmin,viaExt_vano3_qunifmax_fr,viaExt_vano3_qunifmin_fr=traf_vias_fict(name='viaExt_vano3',xmin=xViaFict[0][0],xmax=xViaFict[0][1],ymin=yPil2,ymax=yEstr[-1],zmin=zArrVoladz,zmax=zLosSup)



viaCent_vano1_set,viaCent_vano1_qunifmax,viaCent_vano1_qunifmin,viaCent_vano1_qunifmax_fr,viaCent_vano1_qunifmin_fr=traf_vias_fict(name='viaCent_vano1',xmin=xViaFict[1][0],xmax=xViaFict[1][-1],ymin=0,ymax=yPil1,zmin=zLosSup,zmax=zLosSup)

viaCent_vano2_set,viaCent_vano2_qunifmax,viaCent_vano2_qunifmin,viaCent_vano2_qunifmax_fr,viaCent_vano2_qunifmin_fr=traf_vias_fict(name='viaCent_vano2',xmin=xViaFict[1][0],xmax=xViaFict[1][-1],ymin=yPil1,ymax=yPil2,zmin=zLosSup,zmax=zLosSup)

viaCent_vano3_set,viaCent_vano3_qunifmax,viaCent_vano3_qunifmin,viaCent_vano3_qunifmax_fr,viaCent_vano3_qunifmin_fr=traf_vias_fict(name='viaCent_vano3',xmin=xViaFict[1][0],xmax=xViaFict[1][-1],ymin=yPil2,ymax=yEstr[-1],zmin=zLosSup,zmax=zLosSup)



viaInt_vano1_set,viaInt_vano1_qunifmax,viaInt_vano1_qunifmin,viaInt_vano1_qunifmax_fr,viaInt_vano1_qunifmin_fr=traf_vias_fict(name='viaInt_vano1',xmin=xViaFict[2][0],xmax=xViaFict[2][-1],ymin=0,ymax=yPil1,zmin=zLosSup,zmax=zLosSup)

viaInt_vano2_set,viaInt_vano2_qunifmax,viaInt_vano2_qunifmin,viaInt_vano2_qunifmax_fr,viaInt_vano2_qunifmin_fr=traf_vias_fict(name='viaInt_vano2',xmin=xViaFict[2][0],xmax=xViaFict[2][-1],ymin=yPil1,ymax=yPil2,zmin=zLosSup,zmax=zLosSup)

viaInt_vano3_set,viaInt_vano3_qunifmax,viaInt_vano3_qunifmin,viaInt_vano3_qunifmax_fr,viaInt_vano3_qunifmin_fr=traf_vias_fict(name='viaInt_vano3',xmin=xViaFict[2][0],xmax=xViaFict[2][-1],ymin=yPil2,ymax=yEstr[-1],zmin=zLosSup,zmax=zLosSup)



remnt_vano1_set,remnt_vano1_qunifmax,remnt_vano1_qunifmin,remnt_vano1_qunifmax_fr,remnt_vano1_qunifmin_fr=traf_vias_fict(name='remnt_vano1',xmin=xViaFict[-1][0],xmax=xViaFict[-1][-1],ymin=0,ymax=yPil1,zmin=zArrVoladz,zmax=zLosSup)

remnt_vano2_set,remnt_vano2_qunifmax,remnt_vano2_qunifmin,remnt_vano2_qunifmax_fr,remnt_vano2_qunifmin_fr=traf_vias_fict(name='remnt_vano2',xmin=xViaFict[-1][0],xmax=xViaFict[-1][-1],ymin=yPil1,ymax=yPil2,zmin=zArrVoladz,zmax=zLosSup)

remnt_vano3_set,remnt_vano3_qunifmax,remnt_vano3_qunifmin,remnt_vano3_qunifmax_fr,remnt_vano3_qunifmin_fr=traf_vias_fict(name='remnt_vano3',xmin=xViaFict[-1][0],xmax=xViaFict[-1][-1],ymin=yPil2,ymax=yEstr[-1],zmin=zArrVoladz,zmax=zLosSup)

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
'''***
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
    n2=nodes.getDomain.getMesh.getNearestNode(geom.Pos3d(xn,yEstr[-1],zriostrEstr))
    x,y=n2.getCoo[0],n2.getCoo[1]
    n1=nodes.newNodeXYZ(x,y,zLosInf-hNetoNeopr/2.0)
    modelSpace.setRigidBeamBetweenNodes(n2.tag,n1.tag)
    n0=nodes.newNodeXYZ(x,y,zLosInf-hNetoNeopr/2.0)
    modelSpace.fixNode('000_000',n0.tag)
    constrNodesE2.append(n0)
    elem=neopr.putBetweenNodes(modelSpace,n0.tag,n1.tag)
    neopsE2.append(elem)
#constrNodes=constrNodesPilas+constrNodesE1+constrNodesE2
constrNodes=constrNodesE1+constrNodesE2    
***'''    

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

#overallSet=pilasInf+pilasSup+riostrEstr1+riostrEstr2+losInfV1+losInfV2+losInfV3+losInfRP1+losInfRP2+losSupV1+losSupV2+losSupV3+losSupRP1+losSupRP2+murAligV1+murAligV2+murAligV3+murExtAligV1+murExtAligV2+murExtAligV3+murRP1+murRP2+diafRP1+diafRP2+voladzCentV1+voladzCentV2+voladzCentV3+voladzCentRP1+voladzCentRP2+voladzExtrV1+voladzExtrV2+voladzExtrV3+voladzExtrRP1+voladzExtrRP2
overallSet=riostrEstr1+riostrEstr2+losInfV1+losInfV2+losInfV3+losInfRP1+losInfRP2+losSupV1+losSupV2+losSupV3+losSupRP1+losSupRP2+murAligV1+murAligV2+murAligV3+murExtAligV1+murExtAligV2+murExtAligV3+murRP1+murRP2+diafRP1+diafRP2+voladzCentV1+voladzCentV2+voladzCentV3+voladzCentRP1+voladzCentRP2+voladzExtrV1+voladzExtrV2+voladzExtrV3+voladzExtrRP1+voladzExtrRP2
overallSet.description='Estructura'
overallSet.name='overallSet'
overallSet.color=cfg.colors['purple01']
'''
nodesTot=total.nodes
for n in nodesTot:
    if n.isFree:
        print 'node ',n.tag, ' is free'
'''


