# -*- coding: utf-8 -*-

import math
from rough_calculations import ng_retaining_wall
import xc_base
import geom
import xc
from materials.aci import ACI_materials
from materials.aci import ACI_limit_state_checking
from materials import typical_materials
from geotechnics import earth_pressure as ep
from geotechnics import FrictionalCohesionalSoil as fcs
from actions import load_cases
from actions import combinations
from actions.earth_pressure import earth_pressure

INCH_2_METER= 0.0254
FEET_2_METER= 0.3048
cover= 55e-3

#Materials
concrete= ACI_materials.c3500
reinfSteel= ACI_materials.A615G60
execfile("./armatures_type.py")

stemBottomWidth= 0.45#Coupe A
footingThickness= 0.50
sectionName= "WT1"
wall= ng_retaining_wall.BasementWall(sectionName,cover,10*INCH_2_METER,10*INCH_2_METER,14*INCH_2_METER,concrete,reinfSteel)
wall.stemHeight= 14.0*FEET_2_METER
wall.bToe= 2.0*FEET_2_METER
wall.bHeel= 2.0*FEET_2_METER
wall.beton= concrete
wall.exigeanceFisuration= 'C'
wall.reinforcement.setArmature(1,D1618_15.getCopy(ACI_limit_state_checking.RebarController('C')))
wall.reinforcement.setArmature(2,A14_15.getCopy(ACI_limit_state_checking.RebarController('C')))
wall.reinforcement.setArmature(3,D1618_15.getCopy(ACI_limit_state_checking.RebarController('C')))
wall.reinforcement.setArmature(4,A10_15.getCopy(ACI_limit_state_checking.RebarController('C')))
wall.reinforcement.setArmature(6,A12_15.getCopy(ACI_limit_state_checking.RebarController('C')))
wall.reinforcement.setArmature(7,A10_15.getCopy(ACI_limit_state_checking.RebarController('C')))
wall.reinforcement.setArmature(8,D1618_15.getCopy(ACI_limit_state_checking.RebarController('B')))
wall.reinforcement.setArmature(11,A14_15.getCopy(ACI_limit_state_checking.RebarController('B')))


wallFEModel= wall.createFEProblem('Basement wall '+sectionName)
preprocessor= wallFEModel.getPreprocessor
nodes= preprocessor.getNodeHandler

#Soil
kS= 64.4285714286e6 #Module de réaction du sol (estimé).
#print 'kS= ', kS/1e6
kX= typical_materials.defElasticMaterial(preprocessor, "kX",kS/10.0)
kY= typical_materials.defElasticMaterial(preprocessor, "kY",kS)
#kY= typical_materials.defElastNoTensMaterial(preprocessor, "kY",kS)
backFillSoilModel= ep.RankineSoil(phi= math.radians(32),rho= 2000) #Characteristic values.
backFillDelta= 0.0#2.0/3.0*backFillSoilModel.phi
hi= [0.65,100.0]
rhoi= [2000,2100]
phii= [math.radians(34),math.radians(28)]
ci= [3e3,7e3]
stratifiedSoil= fcs.StratifiedSoil(hi,rhoi,phii,ci)

foundationSoilModel= stratifiedSoil.getEquivalentSoil(Beff= 2.5,gMPhi= 1.2,gMc= 1.5) #Design values.

#Mesh.
wall.genMesh(nodes,[kX,kY])

#Sets.
totalSet= preprocessor.getSets.getSet("total")


#Actions.
loadCaseManager= load_cases.LoadCaseManager(preprocessor)
loadCaseNames= ['selfWeight','deadLoad','crowdLoad','railLoad','derailmentLoad','quakeLoad']
loadCaseManager.defineSimpleLoadCases(loadCaseNames)

#Self weight.
selfWeight= loadCaseManager.setCurrentLoadCase('selfWeight')
gravity=9.81 #Aceleración de la gravedad (m/s2)
wall.createSelfWeightLoads(rho= 2500,grav= gravity)

#Dead load.
#  Dead load. Earth self weight.
gSoil= backFillSoilModel.rho*gravity
frontFillDepth= 1.0
deadLoad= loadCaseManager.setCurrentLoadCase('deadLoad')
wall.createDeadLoad(heelFillDepth= wall.stemHeight,toeFillDepth= frontFillDepth,rho= backFillSoilModel.rho, grav= gravity)

#  Dead load. Earth pressure.
Ka= backFillSoilModel.Ka()
zGroundBackFill= 0.0 #Back fill
backFillPressureModel=  earth_pressure.EarthPressureModel( zGround= zGroundBackFill, zBottomSoils=[-10],KSoils= [Ka],gammaSoils= [gSoil], zWater= -1e3, gammaWater= 1000*gravity)
wall.createBackFillPressures(backFillPressureModel, Delta= backFillDelta)
zGroundFrontFill= zGroundBackFill-wall.stemHeight+frontFillDepth #Front fill
frontFillPressureModel=  earth_pressure.EarthPressureModel(zGround= zGroundFrontFill, zBottomSoils=[-10],KSoils= [Ka], gammaSoils= [gSoil], zWater= -1e3, gammaWater= 1000*gravity)
wall.createFrontFillPressures(frontFillPressureModel)

#Live load. Crowd loading.
crowdLoad= loadCaseManager.setCurrentLoadCase('crowdLoad')
crowdEarthPressure= earth_pressure.StripLoadOnBackfill(qLoad= 4e3,zLoad= 0.0, distWall= 2.5/2.0, stripWidth= 2.5)
wall.createPressuresFromLoadOnBackFill(crowdEarthPressure, Delta= backFillDelta)
wall.createLoadOnTopOfStem(xc.Vector([-3e3,0.0,3.6e3]))

#Live load. Rail traffic load.
distRailCLWall= 4.12 #Distance from the center line of the rail track to the wall.  
railLoad= loadCaseManager.setCurrentLoadCase('railLoad')
railLoadEarthPressure= earth_pressure.StripLoadOnBackfill(qLoad= 62.5e3,zLoad= -0.6, distWall= distRailCLWall, stripWidth= 2.0)
wall.createPressuresFromLoadOnBackFill(railLoadEarthPressure, Delta= backFillDelta)
#Nosing load
fNosingLoad= 60e3
nosingLoadLength= 1.8+(distRailCLWall-1.0)
nosingLoadSurface= nosingLoadLength*2.0
qNosingLoad= fNosingLoad/nosingLoadLength
print 'qNosingLoad= ', qNosingLoad
#CentrifugalLoad.
v= 40/3.6 #Speed.
R= 71 #Rayon (m)
qZk=  v*v*62.5e3/R/9.81
print 'qZk= ', qZk
horizontalLoad= earth_pressure.HorizontalLoadOnBackfill(backFillSoilModel.phi,qLoad= qZk+qNosingLoad,zLoad= -0.6, distWall= distRailCLWall, widthLoadArea= 2.0)
wall.createEarthPressureLoadOnStem(horizontalLoad)

#Accidental actions. Derailment
derailmentLoad= loadCaseManager.setCurrentLoadCase('derailmentLoad')
derailmentLoaddEarthPressure= earth_pressure.StripLoadOnBackfill(qLoad= 62.5e3,zLoad= -0.6, distWall= 3.12, stripWidth= 2.0)
wall.createPressuresFromLoadOnBackFill(derailmentLoaddEarthPressure, Delta= backFillDelta)

#Accidental actions. Quake
quakeLoad= loadCaseManager.setCurrentLoadCase('quakeLoad')
kh=  0.067957866123
kv=  0.0339789330615
Aq= wall.getMononobeOkabeDryOverpressure(backFillSoilModel,kv,kh)
print 'Aq= ',Aq
quakeEarthPressure= earth_pressure.UniformLoadOnStem(Aq)
wall.createEarthPressureLoadOnStem(quakeEarthPressure, Delta= backFillDelta)

#Load combinations
combContainer= combinations.CombContainer()

#Quasi-permanent situations.
combContainer.SLS.qp.add('ELS00', '1.0*selfWeight+1.0*deadLoad+1.0*railLoad')
combContainer.SLS.qp.add('ELS01', '1.0*selfWeight+1.0*deadLoad+1.0*crowdLoad')

#Stability ultimate states. (type 1)
combContainer.ULS.perm.add('SR1A', '1.1*selfWeight+1.35*deadLoad+1.5*crowdLoad')
combContainer.ULS.perm.add('SR1B', '1.1*selfWeight+1.35*deadLoad+1.45*railLoad')
combContainer.ULS.perm.add('SR2', '1.1*selfWeight+1.35*deadLoad')
combContainer.ULS.perm.add('SR3A', '1.1*selfWeight+0.8*deadLoad+1.5*crowdLoad')
combContainer.ULS.perm.add('SR3B', '1.1*selfWeight+0.8*deadLoad+1.45*railLoad')
combContainer.ULS.perm.add('SR4', '1.1*selfWeight+0.8*deadLoad')
combContainer.ULS.perm.add('SR5A', '0.9*selfWeight+1.35*deadLoad+1.5*crowdLoad')
combContainer.ULS.perm.add('SR5B', '0.9*selfWeight+1.35*deadLoad+1.45*railLoad')
combContainer.ULS.perm.add('SR6', '0.9*selfWeight+1.35*deadLoad')
combContainer.ULS.perm.add('SR7A', '0.9*selfWeight+0.8*deadLoad+1.5*crowdLoad')
combContainer.ULS.perm.add('SR7B', '0.9*selfWeight+0.8*deadLoad+1.45*railLoad')
combContainer.ULS.perm.add('SRS1A', '1.0*selfWeight+1.0*deadLoad+0.3*crowdLoad+1.0*derailmentLoad')
combContainer.ULS.perm.add('SRS1B', '1.0*selfWeight+1.0*deadLoad+0.3*crowdLoad+1.0*quakeLoad')
combContainer.ULS.perm.add('SRS1C', '1.0*selfWeight+1.0*deadLoad+1.0*quakeLoad+1.0*derailmentLoad')

#Strenght ultimate states. (type 2).
# Earth pressure at rest so 1.35*K0/Ka= 1.35*0.5/0.33= 2.05 -> 2.0
combContainer.ULS.perm.add('SR9A', '1.35*selfWeight+2.0*deadLoad+1.5*crowdLoad')
combContainer.ULS.perm.add('SR9B', '1.35*selfWeight+2.0*deadLoad+1.45*railLoad')
combContainer.ULS.perm.add('SR10', '1.35*selfWeight+2.0*deadLoad')
combContainer.ULS.perm.add('SR11A', '1.35*selfWeight+0.8*deadLoad+1.5*crowdLoad')
combContainer.ULS.perm.add('SR11B', '1.35*selfWeight+0.8*deadLoad+1.45*railLoad')
combContainer.ULS.perm.add('SR12', '1.35*selfWeight+0.8*deadLoad')
combContainer.ULS.perm.add('SR13A', '0.8*selfWeight+2.0*deadLoad+1.5*crowdLoad')
combContainer.ULS.perm.add('SR13B', '0.8*selfWeight+2.0*deadLoad+1.45*railLoad')
combContainer.ULS.perm.add('SR14', '0.8*selfWeight+2.0*deadLoad')
combContainer.ULS.perm.add('SR15A', '0.8*selfWeight+0.8*deadLoad+1.5*crowdLoad')
combContainer.ULS.perm.add('SR15B', '0.8*selfWeight+0.8*deadLoad+1.45*railLoad')
combContainer.ULS.perm.add('SRS2A', '1.0*selfWeight+1.0*deadLoad+0.3*crowdLoad+1.0*derailmentLoad')
combContainer.ULS.perm.add('SRS2B', '1.0*selfWeight+1.0*deadLoad+0.3*crowdLoad+1.0*quakeLoad')
combContainer.ULS.perm.add('SRS2C', '1.0*selfWeight+1.0*deadLoad+1.0*quakeLoad+1.0*derailmentLoad')
