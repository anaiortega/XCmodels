#empuje del terreno
soil=ep.EarthPressureModel( zGround=zGround,zBottomSoils=[-100],KSoils=[K0], gammaSoils=[densrell*grav], zWater=-10.0, gammaWater=grav)
qunifTerr=ep.StripLoadOnBackfill(qLoad=qunifTerr, zLoad=zGround,distWall=0, stripWidth=10)
ep_aleti= loads.EarthPressLoad(name= 'ep_aleti', xcSet=aleti,soilData=soil, vDir=xc.Vector([-1,0,0]))
ep_aletd= loads.EarthPressLoad(name= 'ep_aletd', xcSet=aletd,soilData=soil, vDir=xc.Vector([1,0,0]))
ep_murestr= loads.EarthPressLoad(name= 'ep_murestr', xcSet=murestr,soilData=soil, vDir=xc.Vector([0,-1,0]))
rell_zap=loads.UniformLoadOnSurfaces(name= 'rell_zap',xcSet=zapTrasdos,loadVector= xc.Vector([0,0,-grav*densrell*(zGround-zZap-cantoZap/2.)]))

G4=lcases.LoadCase(preprocessor=prep,name="G4",loadPType="default",timeSType="constant_ts")
G4.create()
G4.addLstLoads([ep_aleti,ep_aletd,ep_murestr,rell_zap])

#Sobrecarga sobre relleno trasdós
SCep_zap=loads.UniformLoadOnSurfaces(name= 'rell_zap',xcSet=zapTrasdos,loadVector= xc.Vector([0,0,-qunifTerr]))
SCep_aleti= loads.EarthPressLoad(name= 'SCep_aleti', xcSet=aleti,soilData=None, vDir=xc.Vector([-1,0,0]))
SCep_aleti.stripLoads=[qunifTerr]
SCep_aletd= loads.EarthPressLoad(name= 'SCep_aletd', xcSet=aletd,soilData=None, vDir=xc.Vector([1,0,0]))
SCep_aletd.stripLoads=[qunifTerr]
SCep_murestr= loads.EarthPressLoad(name= 'SCep_murestr', xcSet=murestr,soilData=None, vDir=xc.Vector([0,-1,0]))
SCep_murestr.stripLoads=[qunifTerr]

Q4=lcases.LoadCase(preprocessor=prep,name="Q4",loadPType="default",timeSType="constant_ts")
Q4.create()
Q4.addLstLoads([SCep_aleti,SCep_aletd,SCep_murestr,SCep_zap])
