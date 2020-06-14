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
    centralNode=sets.get_lstNod_from_lst3DPos(preprocessor=prep,lst3DPos=[geom.Pos3d(0,yList[len(yListTabl)-1]/2.0,zList[len(zListTabl)-1])])
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
pilBarlov=gridPil.getSetLinMultiRegion(lstIJKRange=Wpil_barlov_rg,setName='pilBarlov')
pilSotav=gridPil.getSetLinMultiRegion(lstIJKRange=Wpil_sotav_rg,setName='pilSotav')

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
xCent_vext=(xViaFict[0][0]+xViaFict[0][-1])/2.
xCent_vcent=(xViaFict[1][0]+xViaFict[1][-1])/2.
xCent_vint=(xViaFict[2][0]+xViaFict[2][-1])/2.

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
