import geom

def getType4BeamPoints(offset):
  return [(offset+23.0,0.0,0.0),(offset+23.0,10.0,0.0),(offset+6.0,14.0,0.0),(offset+6.0,52.0,0.0),(offset+6+19+10,55.0,0.0),(offset+6+19+10,65.0,0.0),(offset-64.5,65,0.0),(offset-64.5,59.0,0.0),(offset-6,52,0.0),(offset-6.0,14.0,0.0),(offset-23.0,10.0,0.0),(offset-23.0,0.0,0.0),(offset-2.5,0.0,0.0),(offset-2.5,3.0,0.0),(offset+2.5,3.0,0.0),(offset+2.5,0.0,0.0),(offset+23,0.0,0.0)]

def getType5BeamPoints(offset):
  return [(offset+23.0,0.0,0.0),(offset+23.0,10.0,0.0),(offset+6.0,14.0,0.0),(offset+6.0,52.0,0.0),(offset+64.5,59.0,0.0),(offset+64.5,65.0,0.0),(offset-6-19-10,65,0.0),(offset-6-19-10,55.0,0.0),(offset-6,52,0.0),(offset-6.0,14.0,0.0),(offset-23.0,10.0,0.0),(offset-23.0,0.0,0.0),(offset-2.5,0.0,0.0),(offset-2.5,3.0,0.0),(offset+2.5,3.0,0.0),(offset+2.5,0.0,0.0),(offset+23,0.0,0.0)]

def getType6BeamPoints(offset):
    return [(offset+23.0,0.0,0.0),(offset+23.0,10.0,0.0),(offset+6.0,14.0,0.0),(offset+6.0,52.0,0.0),(offset+64.5,59.0,0.0),(offset+64.5,65.0,0.0),(offset-64.5,65,0.0),(offset-64.5,59.0,0.0),(offset-6,52,0.0),(offset-6.0,14.0,0.0),(offset-23.0,10.0,0.0),(offset-23.0,0.0,0.0),(offset+23,0.0,0.0)]

t4= getType4BeamPoints(0.0)

t5= getType5BeamPoints(0.0)

t6= getType6BeamPoints(0.0)

txt4= 'polT4= geom.Polygon2d('
for p in t4:
  txt4+= 'geom.Pos2d('+str(p[0]/100.0)+','+str(p[1]/100.0)+'), '

txt5= 'polT5= geom.Polygon2d(['
for p in t5:
  txt5+= 'geom.Pos2d('+str(p[0]/100.0)+','+str(p[1]/100.0)+'), '

txt6= 'polT6= geom.Polygon2d(['
for p in t6:
  txt6+= 'geom.Pos2d('+str(p[0]/100.0)+','+str(p[1]/100.0)+'), '

print txt4
print txt5
print txt6
