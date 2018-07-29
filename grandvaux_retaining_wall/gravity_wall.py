# -*- coding: utf-8 -*-
'''
   Gravity wall stability
   Earth pressure computed according to Rankine theory.
'''
import math
from geotechnics import earth_pressure
import scipy.integrate
import xc_base
import geom

B= 1.60 #1.35
H= 3.5
fillPhi= math.radians(30)
delta= 2.0/3.0*fillPhi
gammaSoil= 21e3 #16 to 22 kN/m3

# Gravity wall:
#
#       ^ y
#       |
#       |
#          B
#       +------+
#       |      |
#       |      |
#       |      |
#       |      | H
#       |      |
#       |      |
#       |      |
#       +------+  ----> x
#

soil= earth_pressure.RankineSoil(phi= fillPhi, rho= gammaSoil)
k0= 1-math.sin(fillPhi) # earth pressure at rest.
K= k0#soil.Ka()
print 'K= ', K
x= list()
earth_pressure= list()
Fv= 0.0 #Friction.
for i in range(0,11):
  stepHeight= H/10.0
  z= i*stepHeight
  sigma_h= K*gammaSoil*z
  fv= sigma_h*math.tan(delta)*stepHeight
  Fv+= fv
  x.append(z)
  earth_pressure.append(sigma_h)

totalEarthPressure= scipy.integrate.simps(earth_pressure,x)

earthPressurePolygon=geom.Poligono2d()

for cx,cy in zip(x,earth_pressure):
  earthPressurePolygon.agregaVertice(geom.Pos2d(cx,cy))

earthPressurePolygon.agregaVertice(geom.Pos2d(x[-1],0.0))
earthPressurePolygon.agregaVertice(geom.Pos2d(0,0))
earthPressurePolygonCentroid= earthPressurePolygon.getCenterOfMass()
earthPressureVector= geom.Vector2d(-totalEarthPressure,-Fv)
earthPressureTail= geom.Pos2d(B,H-earthPressurePolygonCentroid.x)
earthPressureSVD= geom.SVD2d(geom.VDesliz2d(earthPressureTail,earthPressureVector))
print 'earthPressureSVD: ', earthPressureSVD

# Gravity wall.
foundationCenter= geom.Pos2d(B/2.0,0.0)
gravityWallPolygon= geom.Poligono2d()
gravityWallPolygon.agregaVertice(geom.Pos2d(0.0,0.0))
gravityWallPolygon.agregaVertice(geom.Pos2d(B,0.0))
gravityWallPolygon.agregaVertice(geom.Pos2d(B,H))
gravityWallPolygon.agregaVertice(geom.Pos2d(0.00,H))
gravityWallPolygonCentroid= gravityWallPolygon.getCenterOfMass()
gravityWallPolygonArea= gravityWallPolygon.getArea()
gravityWallUnitWeight= 24e3
gravityWallPolygonWeight= gravityWallUnitWeight*gravityWallPolygonArea
gravityWallWeightSVD= geom.SVD2d(geom.VDesliz2d(gravityWallPolygonCentroid,geom.Vector2d(0.0,-gravityWallPolygonWeight)))
print 'gravityWallWeightSVD: ', gravityWallWeightSVD

# permanent load on the backfill.
traficLoadOnBackfillPosition= geom.Pos2d(B,H/2.0)
traficLoadOnBackfillValueH= -K*5e3
traficLoadOnBackfillValueV= traficLoadOnBackfillValueH*math.tan(delta)
traficLoadOnBackfillSVD= geom.SVD2d(geom.VDesliz2d(traficLoadOnBackfillPosition,geom.Vector2d(traficLoadOnBackfillValueH,traficLoadOnBackfillValueV)))
print 'traficLoadOnBackfillValue: ', traficLoadOnBackfillSVD

selfWeightSVD= gravityWallWeightSVD

def getOverturningSafetyFactor(svd):
    svd= svd.reduceTo(foundationCenter)
    R= svd.getResultant()
    M= svd.getMoment()

    #Overturning safety factor.
    foundationPlane= geom.Line2d(geom.Pos2d(0.0,0.0), geom.Pos2d(1e3,0.0))
    zml= svd.zeroMomentLine()
    p= foundationPlane.getIntersectionWithLine(zml)[0] # Intersection with
                                                       # foundation plane.
    gammaR= 1.0
    e= p.x-foundationCenter.x
    b= B
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
svdBB= 0.9*selfWeightSVD+1.35*earthPressureSVD+1.35*traficLoadOnBackfillSVD
svdBG= 0.8*selfWeightSVD+1.35*earthPressureSVD+1.35*traficLoadOnBackfillSVD


Fo= getOverturningSafetyFactor(svdAB)
Fs= getSlidingSafetyFactor(svdAG)
print 'F(svdA,basculement)= ', Fo
print 'F(svdA,glissement)= ', Fs
Fo= getOverturningSafetyFactor(svdBB)
Fs= getSlidingSafetyFactor(svdBG)
print 'F(svdB,basculement)= ', Fo
print 'F(svdB,glissement)= ', Fs
