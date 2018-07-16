
# ***** ACTIONS *****


    # Load acting on one or several points
    # name:       name identifying the load
    # points:     list of points (list of geom.Pos3d(x,y,z)) where 
    #             the load must be applied.
    # loadVector: xc.Vector with the six components of the load: 
    #             xc.Vector([Fx,Fy,Fz,Mx,My,Mz]).
#auxilary fuction
def CoordTrainLoads(xmin,ymin,z):
  xmax=xmin+1.20
  ymax=ymin+2.0
  retval=[geom.Pos3d(xmin,ymin,z),geom.Pos3d(xmin,ymax,z),geom.Pos3d(xmax,ymin,z),geom.Pos3d(xmax,ymax,z)]
  return retval
#
trafQLoadLane1HwSit1a=gm.LoadOnPoints(name='trafQLoadLane1HwSit1a',points=CoordTrainLoads(0.2,yList[YposLane1HwSit1[0]]+0.2,zList[lastZpos]),loadVector=xc.Vector([0,0,-alphQ1hw*Qk1wheel,0,0,0]))
trafQLoadLane2HwSit1a=gm.LoadOnPoints(name='trafQLoadLane2HwSit1a',points=CoordTrainLoads(0.2,yList[YposLane2HwSit1[0]]+0.2,zList[lastZpos]),loadVector=xc.Vector([0,0,-alphQ2hw*Qk2wheel,0,0,0]))
trafQLoadLane1HwSit1b=gm.LoadOnPoints(name='trafQLoadLane1HwSit1b',points=CoordTrainLoads(xList[lastXpos]/2.0-0.6,yList[YposLane1HwSit1[0]]+0.2,zList[lastZpos]),loadVector=xc.Vector([0,0,-alphQ1hw*Qk1wheel,0,0,0]))
trafQLoadLane2HwSit1b=gm.LoadOnPoints(name='trafQLoadLane2HwSit1b',points=CoordTrainLoads(xList[lastXpos]/2.0-0.6,yList[YposLane2HwSit1[0]]+0.2,zList[lastZpos]),loadVector=xc.Vector([0,0,-alphQ2hw*Qk2wheel,0,0,0]))
trafQLoadLane1HwSit2b=gm.LoadOnPoints(name='trafQLoadLane1HwSit2b',points=CoordTrainLoads(xList[lastXpos]/2.0-0.6,yList[YposLane1HwSit2[0]]+0.5,zList[lastZpos]),loadVector=xc.Vector([0,0,-alphQ1hw*Qk1wheel,0,0,0]))
trafQLoadLane2HwSit2a=gm.LoadOnPoints(name='trafQLoadLane2HwSit2a',points=CoordTrainLoads(0.5,yList[YposLane2HwSit2[0]]+0.5,zList[lastZpos]),loadVector=xc.Vector([0,0,-alphQ2hw*Qk2wheel,0,0,0]))
trafQLoadLane1SrSit12a=gm.LoadOnPoints(name='trafQLoadLane1SrSit12a',points=CoordTrainLoads(0.2,yList[YposLane1Sr[0]]+0.2,zList[lastZpos]),loadVector=xc.Vector([0,0,-alphQ1sr*Qk1wheel,0,0,0]))
trafQLoadLane2HwSit2b=gm.LoadOnPoints(name='trafQLoadLane2HwSit2b',points=CoordTrainLoads(xList[lastXpos]/2.0-0.6,yList[YposLane2HwSit2[0]]+0.5,zList[lastZpos]),loadVector=xc.Vector([0,0,-alphQ2hw*Qk2wheel,0,0,0]))
trafQLoadLane1HwSit2a=gm.LoadOnPoints(name='trafQLoadLane1HwSit2a',points=CoordTrainLoads(0.5,yList[YposLane1HwSit2[0]]+0.5,zList[lastZpos]),loadVector=xc.Vector([0,0,-alphQ1hw*Qk1wheel,0,0,0]))
trafQLoadLane1SrSit12b=gm.LoadOnPoints(name='trafQLoadLane1SrSit12b',points=CoordTrainLoads(xList[lastXpos]/2.0-0.6,yList[YposLane1Sr[0]]+0.2,zList[lastZpos]),loadVector=xc.Vector([0,0,-alphQ1sr*Qk1wheel,0,0,0]))

trafBrakingHwSit1=gm.LoadOnPoints(name='trafBrakingHwSit1',points=[geom.Pos3d(xList[lastXpos]/2.0,(yList[YposLane1HwSit1[0]]+yList[YposLane1HwSit1[1]])/2.0,zList[lastZpos])],loadVector=xc.Vector([brakingQhw,0,0,0,0,0]))
trafBrakingHwSit2=gm.LoadOnPoints(name='trafBrakingHwSit2',points=[geom.Pos3d(xList[lastXpos]/2.0,(yList[YposLane1HwSit2[0]]+yList[YposLane1HwSit2[1]])/2.0,zList[lastZpos])],loadVector=xc.Vector([brakingQhw,0,0,0,0,0]))
trafBrakingSrSit12=gm.LoadOnPoints(name='trafBrakingSrSit12',points=[geom.Pos3d(xList[lastXpos]/2.0,(yList[YposLane1Sr[0]]+yList[YposLane1Sr[1]])/2.0,zList[lastZpos])],loadVector=xc.Vector([brakingQsr,0,0,0,0,0]))
#Exceptional transport
yminTruck=yList[YposAxe]-distTrWheels/2.0+excentr
ymaxTruck=yminTruck+distTrWheels
cWheelsET=[]
for i in range (0,6):
  xw=xminTruck+i*distLnWheels
  cWheelsET.append(geom.Pos3d(xw,yminTruck,zList[lastZpos]))
  cWheelsET.append(geom.Pos3d(xw,ymaxTruck,zList[lastZpos]))

trafExceptTransp=gm.LoadOnPoints(name='trafExceptTransp',points=cWheelsET,loadVector=xc.Vector([0,0,-alphQExcTr*QwheelExcTr,0,0,0]))


    # Earth pressure applied to shell elements
    # Attributes:
    # name:       name identifying the load
    # lstGridRg:   lists of grid ranges to delimit the surfaces to
    #             be loaded
    # earthPressure: instance of the class EarthPressure, with 
    #             the following attributes:
    #               K:Coefficient of pressure
    #               zGround:global Z coordinate of ground level
    #               gammaTerrain: weight density of soil 
    #               zWater: global Z coordinate of groundwater level 
    #                       (if zGroundwater<minimum z of model => there is no groundwater)
    #               gammaWater: weight density of water
    #               vDir: unit vector defining pressures direction
#Earth pressure.
earthPressLoadleftWall= gm.EarthPressureOnSurfaces(name= 'earthPressLoadleftWall', lstGridRg= gm.getIJKRangeListFromSurfaces([leftWall]), earthPressure= ep.EarthPressure(K=KearthPress,zGround=zList[lastZpos]+subbThHw+asphaltTh, gammaSoil=densSoil*grav, zWater=-10.0, gammaWater=densWater*grav, vDir=[1,0,0]))
earthPressLoadrightWall= gm.EarthPressureOnSurfaces(name= 'earthPressLoadrightWall', lstGridRg= gm.getIJKRangeListFromSurfaces([rightWall]), earthPressure= ep.EarthPressure(K=KearthPress,zGround=zList[lastZpos]+subbThHw+asphaltTh, gammaTerrain=densSoil*grav, zWater=-10.0, gammaWater=densWater*grav, vDir=[-1,0,0]))


#ACTIONS
  # Definition of the actions to be combined in design situations for 
  # performing a limit state analysis
  #   inercLoad:     list of inertial loads
  #   unifPressLoad: list of pressures on surfaces
  #   unifVectLoad:  list of uniform loads on shell elements
  #   unifLoadLinRng: list of uniform loads on the lines in a list of grid ranges
  #   pointLoad:     list of point loads
  #   earthPressLoad:list of earth pressure loads
  #   hydrThrustLoad:list of hydrostatic thrust on the walls that delimit a volume
  #   tempGrad:      list of temperature gradient loads

GselfWeight= gm.LoadState('GselfWeight',inercLoad= [selfWeight])
GdeadLoad= gm.LoadState('GdeadLoad',unifPressLoad= [deadLoadAsphalt,deadLoadSubbT1,deadLoadSubbSr,deadLoadSubbHw,deadLoadSubbT2,deadLoadGuardrail])
GearthPress=gm.LoadState('GearthPress',earthPressLoad= [earthPressLoadleftWall,earthPressLoadrightWall])
QtrafSit1a= gm.LoadState('QtrafSit1a',unifPressLoad= [trafLoadSit1Lane1Hw,trafLoadSit1Lane2Hw,trafLoadSit1Lane3Hw,trafLoadSit1RestHw,trafLoadSit12Lane1Sr],pointLoad=[trafQLoadLane1HwSit1a,trafQLoadLane2HwSit1a,trafBrakingHwSit1,trafQLoadLane1SrSit12a,trafBrakingSrSit12])
QtrafSit1b= gm.LoadState('QtrafSit1b',unifPressLoad= [trafLoadSit1Lane1Hw,trafLoadSit1Lane2Hw,trafLoadSit1Lane3Hw,trafLoadSit1RestHw,trafLoadSit12Lane1Sr],pointLoad=[trafQLoadLane1HwSit1b,trafQLoadLane2HwSit1b,trafBrakingHwSit1,trafQLoadLane1SrSit12b,trafBrakingSrSit12])
QtrafSit2a= gm.LoadState('QtrafSit2a',unifPressLoad= [trafLoadSit2Lane1Hw,trafLoadSit2Lane2Hw,trafLoadSit2Lane3Hw,trafLoadSit2RestHw,trafLoadSit12Lane1Sr],pointLoad=[trafQLoadLane1HwSit2a,trafQLoadLane2HwSit2a,trafBrakingHwSit2,trafQLoadLane1SrSit12a,trafBrakingSrSit12])
QtrafSit2b= gm.LoadState('QtrafSit2b',unifPressLoad= [trafLoadSit2Lane1Hw,trafLoadSit2Lane2Hw,trafLoadSit2Lane3Hw,trafLoadSit2RestHw,trafLoadSit12Lane1Sr],pointLoad=[trafQLoadLane1HwSit2b,trafQLoadLane2HwSit2b,trafBrakingHwSit2,trafQLoadLane1SrSit12b,trafBrakingSrSit12]) 

QtrafExcept= gm.LoadState('QtrafExcept',pointLoad=[trafExceptTransp])

QtrafSit1aPoint= gm.LoadState('QtrafSit1aPoint',pointLoad=[trafQLoadLane1HwSit1a])
QtrafSit1bPoint= gm.LoadState('QtrafSit1bPoint',pointLoad=[trafQLoadLane1HwSit1b])
QtrafSit2aPoint= gm.LoadState('QtrafSit2aPoint',pointLoad=[trafQLoadLane1HwSit2a])
QtrafSit2bPoint= gm.LoadState('QtrafSit2bPoint',pointLoad=[trafQLoadLane1HwSit2b]) 

QtrafSit1unif= gm.LoadState('QtrafSit1unif',unifPressLoad= [trafLoadSit1Lane1Hw,trafLoadSit1Lane2Hw,trafLoadSit1Lane3Hw,trafLoadSit1RestHw,trafLoadSit12Lane1Sr]) #defined only for the purpose of displaying
QtrafSit2unif= gm.LoadState('QtrafSit2unif',unifPressLoad= [trafLoadSit2Lane1Hw,trafLoadSit2Lane2Hw,trafLoadSit2Lane3Hw,trafLoadSit2RestHw,trafLoadSit12Lane1Sr]) #defined only for the purpose of displaying

#Dictionary of actions
loadStates= gm.LoadStateMap([GselfWeight,GdeadLoad,GearthPress,QtrafSit1a,QtrafSit1b,QtrafSit2a,QtrafSit2b,QtrafExcept,QtrafSit1aPoint,QtrafSit1bPoint,QtrafSit2aPoint,QtrafSit2bPoint,QtrafSit1unif,QtrafSit2unif])

model.setLoadStates(loadStates)

    # generateLoads(): Apply the loads for each load state and returns the dictionary 
    # [model.dicGeomEnt] with identifiers and the geometric entities (lines and surfaces) 
    # generated
model.generateLoads()


#LOAD COMBINATIONS
combContainer= cc.CombContainer()  #Container of load combinations

# COMBINATIONS OF ACTIONS FOR SERVICEABILITY LIMIT STATES
    # name:        name to identify the combination
    # rare:        combination for a rare design situation
    # freq:        combination for a frequent design situation
    # qp:          combination for a quasi-permanent design situation
    # earthquake:  combination for a seismic design situation
#Characteristic combinations.
combContainer.SLS.rare.add('ELSR01', '1.0*GselfWeight+1.0*GdeadLoad+1.0*GearthPress+1.0*QtrafSit1a')
combContainer.SLS.rare.add('ELSR02', '1.0*GselfWeight+1.0*GdeadLoad+1.0*GearthPress+1.0*QtrafSit1b')
combContainer.SLS.rare.add('ELSR03', '1.0*GselfWeight+1.0*GdeadLoad+1.0*GearthPress+1.0*QtrafSit2a')
combContainer.SLS.rare.add('ELSR04', '1.0*GselfWeight+1.0*GdeadLoad+1.0*GearthPress+1.0*QtrafSit2b')
combContainer.SLS.rare.add('ELSR05', '1.0*GselfWeight+1.0*GdeadLoad+1.0*GearthPress+1.0*QtrafExcept')
#Frequent combinations.
combContainer.SLS.freq.add('ELSF01', '1.0*GselfWeight+1.0*GdeadLoad+1.0*GearthPress+0.75*QtrafSit1a')
combContainer.SLS.freq.add('ELSF02', '1.0*GselfWeight+1.0*GdeadLoad+1.0*GearthPress+0.75*QtrafSit1b')
combContainer.SLS.freq.add('ELSF03', '1.0*GselfWeight+1.0*GdeadLoad+1.0*GearthPress+0.75*QtrafSit2a')
combContainer.SLS.freq.add('ELSF04', '1.0*GselfWeight+1.0*GdeadLoad+1.0*GearthPress+0.75*QtrafSit2b')
#Quasi permanent combinations.
combContainer.SLS.qp.add('ELSQP01', '1.0*GselfWeight+1.0*GdeadLoad+1.0*GearthPress')

# COMBINATIONS OF ACTIONS FOR ULTIMATE LIMIT STATES
    # name:        name to identify the combination
    # perm:        combination for a persistent or transient design situation
    # acc:         combination for a accidental design situation
    # fatigue:     combination for a fatigue design situation
    # earthquake:  combination for a seismic design situation
#Persistent and transitory situations.
combContainer.ULS.perm.add('ELUmaxMy', '1.35*GselfWeight+1.35*GdeadLoad+0.8*GearthPress+1.5*QtrafSit1a')
combContainer.ULS.perm.add('ELU02', '0.8*GselfWeight+0.8*GdeadLoad+1.35*GearthPress+1.5*QtrafSit1a')
combContainer.ULS.perm.add('ELU03', '1.35*GselfWeight+1.35*GdeadLoad+0.8*GearthPress+1.5*QtrafSit1b')
combContainer.ULS.perm.add('ELU04', '0.8*GselfWeight+0.8*GdeadLoad+1.35*GearthPress+1.5*QtrafSit1b')
combContainer.ULS.perm.add('ELU05', '1.35*GselfWeight+1.35*GdeadLoad+0.8*GearthPress+1.5*QtrafSit2a')
combContainer.ULS.perm.add('ELU06', '0.8*GselfWeight+0.8*GdeadLoad+1.35*GearthPress+1.5*QtrafSit2a')
combContainer.ULS.perm.add('ELU07', '1.35*GselfWeight+1.35*GdeadLoad+0.8*GearthPress+1.5*QtrafSit2b')
combContainer.ULS.perm.add('ELU08', '0.8*GselfWeight+0.8*GdeadLoad+1.35*GearthPress+1.5*QtrafSit2b')
combContainer.ULS.perm.add('ELU09', '1.35*GselfWeight+1.35*GdeadLoad+0.8*GearthPress+1.5*QtrafExcept')
combContainer.ULS.perm.add('ELU10', '0.8*GselfWeight+0.8*GdeadLoad+1.35*GearthPress+1.5*QtrafExcept')

#Fatigue.
combContainer.ULS.fatigue.add('ELUF0','1.00*GselfWeight+1.0*GdeadLoad+1.0*GearthPress')
combContainer.ULS.fatigue.add('ELUF1','1.00*GselfWeight+1.0*GdeadLoad+1.0*GearthPress + 1.00*QtrafSit1aPoint')
combContainer.ULS.fatigue.add('ELUF1','1.00*GselfWeight+1.0*GdeadLoad+1.0*GearthPress + 1.00*QtrafSit1bPoint')
combContainer.ULS.fatigue.add('ELUF1','1.00*GselfWeight+1.0*GdeadLoad+1.0*GearthPress + 1.00*QtrafSit2aPoint')
combContainer.ULS.fatigue.add('ELUF1','1.00*GselfWeight+1.0*GdeadLoad+1.0*GearthPress + 1.00*QtrafSit2bPoint')



#sets for display

deckSet= model.getSetFromParts('deckSet',['deck'])
deckSet.fillDownwards()

beamSet= model.getSetFromParts('beamSet',['beams'])
beamSet.fillDownwards()

diaphSet= model.getSetFromParts('diaphSet',['diaph'])
beamSet.fillDownwards()

