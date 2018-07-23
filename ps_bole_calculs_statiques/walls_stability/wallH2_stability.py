# -*- coding: utf-8 -*-
'''
   Wall stability
   Earth pressure computed according to Janssen theory.
'''
from geotechnics import earth_pressure
import math
import scipy.integrate
import xc_base
import geom

gammaSoil= 18 #16 to 22 kN/m3
foundationWidth= 1.22
H= 1.97
B= 2.75
fillPhi= math.radians(30)
delta= 2.0/3.0*fillPhi
k0= 1-math.sin(fillPhi) # earth pressure at rest.
print 'k0= ', k0
x= list()
results5_16= list()
Fv= 0.0 #Friction.
for i in range(0,11):
  stepHeight= H/10.0
  z= i*stepHeight
  k= earth_pressure.k_janssen(k0,delta,B,z)
  sigma_h= k*gammaSoil*z
  fv= sigma_h*math.tan(delta)*stepHeight
  Fv+= fv
  x.append(z)
  results5_16.append(sigma_h)

totalEarthPressure= scipy.integrate.simps(results5_16,x)

earthPressurePolygon=geom.Poligono2d()

for cx,cy in zip(x,results5_16):
  earthPressurePolygon.agregaVertice(geom.Pos2d(cx,cy))

earthPressurePolygon.agregaVertice(geom.Pos2d(x[-1],0.0))
earthPressurePolygon.agregaVertice(geom.Pos2d(0,0))
earthPressurePolygonCentroid= earthPressurePolygon.getCenterOfMass()
earthPressureVector= geom.Vector2d(-totalEarthPressure,-Fv)
earthPressureTail= geom.Pos2d(foundationWidth,H-earthPressurePolygonCentroid.x)
earthPressureSVD= geom.SVD2d(geom.VDesliz2d(earthPressureTail,earthPressureVector))
print 'earthPressureSVD: ', earthPressureSVD

'''
print 'B/H= 0.1', results5_16
'''

# Spandrel wall.
foundationCenter= geom.Pos2d(foundationWidth/2.0,0.0)
spandrelWallPolygon= geom.Poligono2d()
spandrelWallPolygon.agregaVertice(geom.Pos2d(0.0,0.0))
spandrelWallPolygon.agregaVertice(geom.Pos2d(foundationWidth,0.0))
spandrelWallPolygon.agregaVertice(geom.Pos2d(1.05,H))
spandrelWallPolygon.agregaVertice(geom.Pos2d(0.00,H))
spandrelWallPolygonCentroid= spandrelWallPolygon.getCenterOfMass()
spandrelWallPolygonArea= spandrelWallPolygon.getArea()
spandrelWallUnitWeight= 19
spandrelWallPolygonWeight= spandrelWallUnitWeight*spandrelWallPolygonArea
spandrelWallWeightSVD= geom.SVD2d(geom.VDesliz2d(spandrelWallPolygonCentroid,geom.Vector2d(0.0,-spandrelWallPolygonWeight)))
print 'spandrelWallWeightSVD: ', spandrelWallWeightSVD

# backfill weight over the wall.
backfillOverWallPolygon= geom.Poligono2d()
backfillOverWallPolygon.agregaVertice(geom.Pos2d(foundationWidth,0.0))
backfillOverWallPolygon.agregaVertice(geom.Pos2d(foundationWidth,H))
backfillOverWallPolygon.agregaVertice(geom.Pos2d(1.05,H))
backfillOverWallPolygonCentroid= backfillOverWallPolygon.getCenterOfMass()
backfillOverWallPolygonArea= backfillOverWallPolygon.getArea()
backfillOverWallPolygonWeight= gammaSoil*backfillOverWallPolygonArea
backfillOverWallWeightSVD= geom.SVD2d(geom.VDesliz2d(backfillOverWallPolygonCentroid,geom.Vector2d(0.0,-backfillOverWallPolygonWeight)))
print 'backfillOverWallWeightSVD: ', backfillOverWallWeightSVD

# permanent load on top of the wall.
permanentLoadWPosition= geom.Pos2d((0.1+1.05)/2.0,H)
permanentLoadWValue= 71181.4/2.0/1e3/0.9
permanentLoadWSVD= geom.SVD2d(geom.VDesliz2d(permanentLoadWPosition,geom.Vector2d(permanentLoadWValue*math.tan(fillPhi),-permanentLoadWValue)))
print 'permanentLoadWValue: ', permanentLoadWSVD

# permanent load on the backfill.
permanentLoadBPosition= geom.Pos2d(foundationWidth,H/2.0)
permanentLoadBValueH= -k0*15091.4/B/1e3/0.9
permanentLoadBValueV= permanentLoadBValueH*math.tan(delta)
permanentLoadBSVD= geom.SVD2d(geom.VDesliz2d(permanentLoadBPosition,geom.Vector2d(permanentLoadBValueH,permanentLoadBValueV)))
print 'permanentLoadBValue: ', permanentLoadBSVD

# vehicle load on top of the wall.
vehicleLoadWPosition= geom.Pos2d((0.1+1.05)/2.0,H)
vehicleLoadWValue= 36356.6/2.0/1e3
vehicleLoadWSVD= geom.SVD2d(geom.VDesliz2d(vehicleLoadWPosition,geom.Vector2d(vehicleLoadWValue*math.tan(fillPhi),-vehicleLoadWValue)))
print 'vehicleLoadWValue: ', vehicleLoadWSVD

# vehicle load on the backfill.
vehicleLoadBPosition= geom.Pos2d(foundationWidth,H/2.0)
vehicleLoadBValueH= -k0*43643.4/B/1e3
vehicleLoadBValueV= vehicleLoadBValueH*math.tan(delta)
vehicleLoadBSVD= geom.SVD2d(geom.VDesliz2d(vehicleLoadBPosition,geom.Vector2d(vehicleLoadBValueH,vehicleLoadBValueV)))
print 'vehicleLoadBValue: ', vehicleLoadBSVD

# truck load on top of the wall.
truckLoadWPosition= geom.Pos2d((0.1+1.05)/2.0,H)
truckLoadWValue= 73802.4/2.0/1e3
truckLoadWSVD= geom.SVD2d(geom.VDesliz2d(truckLoadWPosition,geom.Vector2d(truckLoadWValue*math.tan(fillPhi),-truckLoadWValue)))
print 'truckLoadWValue: ', truckLoadWSVD

# truck load on the backfill.
truckLoadBPosition= geom.Pos2d(foundationWidth,H/2.0)
truckLoadBValueH= -k0*86197.6/B/1e3
truckLoadBValueV= truckLoadBValueH*math.tan(delta)
truckLoadBSVD= geom.SVD2d(geom.VDesliz2d(truckLoadBPosition,geom.Vector2d(truckLoadBValueH,truckLoadBValueV)))
print 'truckLoadBValue: ', truckLoadBSVD


selfWeightSVD= spandrelWallWeightSVD+backfillOverWallWeightSVD+permanentLoadWSVD+permanentLoadBSVD

vehicleLoadSVD= vehicleLoadWSVD+vehicleLoadBSVD
truckLoadSVD= truckLoadWSVD+truckLoadBSVD

#pruebaSVD= geom.SVD2d(geom.VDesliz2d(foundationCenter+geom.Vector2d(0,H),geom.Vector2d(1.0,-1.0)))
#pruebaSVD= geom.SVD2d(geom.VDesliz2d(foundationCenter+geom.Vector2d(-1,0),geom.Vector2d(0.0,-1.0)))

def getOverturningSafetyFactor(svd):
    svd= svd.reduceTo(foundationCenter)
    R= svd.getResultant()
    M= svd.getMoment()

    #Overturning safety factor.
    foundationPlane= geom.Recta2d(geom.Pos2d(0.0,0.0), geom.Pos2d(1e3,0.0))
    zml= svd.zeroMomentLine()
    p= foundationPlane.getIntersectionWithLine(zml)[0] # Intersection with
                                                       # foundation plane.
    gammaR= 1.0
    e= p.x-foundationCenter.x
    b= foundationWidth
    bReduced= 2*(b/2.0+e)
    if(e<0):
      F= b/(3*(-e)*gammaR)
    else:
      F= 10
    print 'e= ', e, ' m'
    return F

def getSlidingSafetyFactor(svd):
    svd= svd.reduceTo(foundationCenter)
    R= svd.getResultant()
    V=R.y
    H=R.x
    F= V*math.tan(math.radians(30))/H
    return F

# Resultant.
svdAB= 0.9*selfWeightSVD+1.35*earthPressureSVD
svdAG= 0.8*selfWeightSVD+1.35*earthPressureSVD
svdBB= 0.9*selfWeightSVD+1.35*earthPressureSVD+1.35*vehicleLoadSVD
svdBG= 0.8*selfWeightSVD+1.35*earthPressureSVD+1.35*vehicleLoadSVD
svdC= 1.0*selfWeightSVD+1.0*earthPressureSVD+1.0*truckLoadSVD


Fo= getOverturningSafetyFactor(svdAB)
Fs= getSlidingSafetyFactor(svdAG)
print 'F(svdA,basculement)= ', Fo
print 'F(svdA,glissement)= ', Fs
Fo= getOverturningSafetyFactor(svdBB)
Fs= getSlidingSafetyFactor(svdBG)
print 'F(svdB,basculement)= ', Fo
print 'F(svdB,glissement)= ', Fs
Fo= getOverturningSafetyFactor(svdC)
Fs= getSlidingSafetyFactor(svdC)
print 'F(svdC,basculement)= ', Fo
print 'F(svdC,glissement)= ', Fs

# #Drawing stuff
# import matplotlib.pyplot as plt


# dshs = [10, 5, 100, 5]  # 10 points on, 5 off, 100 on, 5 off
# dshs2 = [30, 5, 10, 5]  # 30 points on, 5 off, 10 on, 5 off

# fig, ax = plt.subplots()
# line5_16, = ax.plot(results5_16, x, '--', linewidth=2, label='earth pressure')
# line5_16.set_dashes(dshs)


# ax.legend(loc='upper right')

# plt.ylim(x[-1],x[0])
# plt.xlabel('$\sigma_h\ (kN/m^2)$')
# plt.ylabel('$z\ (m)$')
# title= 'Distribution of lateral earth pressure over wall H= '+str(H)+' m.'
# plt.title(title)
# plt.show()

