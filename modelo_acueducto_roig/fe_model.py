from model.sets import sets_mng as sUtils
import math
import xc_base
import geom
import xc



def defineArco(pt1,cooC,R,angI,angF):
  mastPoints.append(pt1)
  angM= (angI+angF)/2.0
  pt2= points.newPntFromPos3d(geom.Pos3d(cooC[0]+R*math.cos(angM), cooC[1], cooC[2]+R*math.sin(angM)))
  mastPoints.append(pt2)
  pt3= points.newPntFromPos3d(geom.Pos3d(cooC[0]+R*math.cos(angF), cooC[1], cooC[2]+R*math.sin(angF)))
  l= lines.newCircleArc(pt1.tag,pt2.tag,pt3.tag)
  if(abs(angF-angI)<3):
    l.ndiv= 2
  else:
    l.ndiv= 6
  lineasMastil.getLines.append(l)
  return pt3


model= xc.FEProblem()
preprocessor=  model.getPreprocessor

points= preprocessor.getMultiBlockTopology.getPoints
lines= preprocessor.getMultiBlockTopology.getLines
lineasMastil= preprocessor.getSets.defSet("lineasMastil")

mastPoints= []

# Mast 1
radio= 33
angIni= -math.radians(0.58)
C= [0,0,20]
pt= points.newPntIDPos3d(1, geom.Pos3d( C[0]+radio*math.cos(angIni), C[1], C[2]+radio*math.sin(angIni)) )
pt= defineArco(pt,C,radio,angIni,math.radians(0.0))
pt= defineArco(pt,C,radio,math.radians(0.0),math.radians(12.19))
pt= defineArco(pt,C,radio,math.radians(12.19),math.radians(12.19+3.99))
pt= defineArco(pt,C,radio,math.radians(12.19+3.99),math.radians(12.19+3.99+3.82))
pt= defineArco(pt,C,radio,math.radians(12.19+3.99+3.82),math.radians(12.19+3.99+3.82+1.65))
mastPoints.append(pt)

# Mast 2
angIni= math.pi-math.radians(0.42)
C= [67.1504,0,19.4466]
pt= points.newPntIDPos3d(points.defaultTag, geom.Pos3d( C[0]+radio*math.cos(angIni), C[1], C[2]+radio*math.sin(angIni)) )
pt= defineArco(pt,C,radio,math.pi-math.radians(0.42+0.53),math.pi-math.radians(0.42+0.53+12.19))
pt= defineArco(pt,C,radio,math.pi-math.radians(0.42+0.53+12.19),math.pi-math.radians(0.42+0.53+12.19+9.46))
pt= defineArco(pt,C,radio,math.pi-math.radians(0.42+0.53+12.19+9.46),math.pi-math.radians(0.42+0.53+12.19+9.46+8.65))
pt= defineArco(pt,C,radio,math.pi-math.radians(0.42+0.53+12.19+9.46+8.65),math.pi-math.radians(0.42+0.53+12.19+9.46+8.65+0.87))
mastPoints.append(pt)

# Mast 3
angIni= -math.radians(0.48)
C= [67.1564,0,19.7814]
pt= points.newPntIDPos3d(points.defaultTag, geom.Pos3d( C[0]+radio*math.cos(angIni), C[1], C[2]+radio*math.sin(angIni)) )
pt= defineArco(pt,C,radio,angIni,math.radians(0.0))
pt= defineArco(pt,C,radio,math.radians(0.0),math.radians(18.09))
pt= defineArco(pt,C,radio,math.radians(18.09),math.radians(18.09+11.89))
pt= defineArco(pt,C,radio,math.radians(18.09+11.89),math.radians(18.09+11.89+11.02))
pt= defineArco(pt,C,radio,math.radians(18.09+11.89+11.02),math.radians(18.09+11.89+11.02+10.68))
pt= defineArco(pt,C,radio,math.radians(18.09+11.89+11.02+10.68),math.radians(18.09+11.89+11.02+10.68+0.89))
mastPoints.append(pt)

# Mast 4
angIni= math.pi-math.radians(-0.50)
C= [134.3007,0,19.7911]
pt= points.newPntIDPos3d(points.defaultTag, geom.Pos3d( C[0]+radio*math.cos(angIni), C[1], C[2]+radio*math.sin(angIni)) )
pt= defineArco(pt,C,radio,angIni,math.pi-math.radians(0.0))
pt= defineArco(pt,C,radio,math.pi-math.radians(0.0),math.pi-math.radians(18.08))
pt= defineArco(pt,C,radio,math.pi-math.radians(18.08),math.pi-math.radians(18.08+11.89))
pt= defineArco(pt,C,radio,math.pi-math.radians(18.08+11.89),math.pi-math.radians(18.08+11.89+8.68))
pt= defineArco(pt,C,radio,math.pi-math.radians(18.08+11.89+8.68),math.pi-math.radians(18.08+11.89+8.68+5.03))
pt= defineArco(pt,C,radio,math.pi-math.radians(18.08+11.89+8.68+5.03),math.pi-math.radians(18.08+11.89+8.68+5.03+0.87))
mastPoints.append(pt)
puntosArranqueMastil= 1,12,21,34 # 
puntosAltosMastil= 11,20,33,46 # 

#Pipe
pipePoints= []
pipePoints.append(points.newPntFromPos3d( geom.Pos3d( 21.6001, 0, 20.1625 ) )) # Retenidas estribo izquierdo
pipePoints.append(points.newPntFromPos3d( geom.Pos3d( 24.0001, 0, 20.1259 ) ))
pipePoints.append(points.newPntFromPos3d( geom.Pos3d( 26.4001, 0, 20.0892 ) ))

pipePoints.append(points.newPntFromPos3d( geom.Pos3d( 37.8007, 0, 16.7840 ) ))

pipePoints.append(points.newPntFromPos3d( geom.Pos3d( 43.6266, 0, 16.7960 ) ))
pipePoints.append(points.newPntFromPos3d( geom.Pos3d( 49.5969, 0, 16.8084 ) ))
pipePoints.append(points.newPntFromPos3d( geom.Pos3d( 55.5651, 0, 16.8207 ) ))

pipePoints.append(points.newPntFromPos3d( geom.Pos3d( 63.2332, 0, 16.8365 ) ))
pipePoints.append(points.newPntFromPos3d( geom.Pos3d( 69.0707, 0, 16.8485 ) )) # Apeo tuberia
pipePoints.append(points.newPntFromPos3d( geom.Pos3d( 71.2733, 0, 16.8531 ) ))
pipePoints.append(points.newPntFromPos3d( geom.Pos3d( 79.3123, 0, 16.8697 ) ))
pipePoints.append(points.newPntFromPos3d( geom.Pos3d( 87.3482, 0, 16.8862 ) ))

pipePoints.append(points.newPntFromPos3d( geom.Pos3d( 97.3564, 0, 16.9069 ) ))

pipePoints.append(points.newPntFromPos3d( geom.Pos3d( 111.6132, 0, 19.5561 ) )) # Retenidas estribo derecho
pipePoints.append(points.newPntFromPos3d( geom.Pos3d( 119.2003, 0, 20.0335 ) ))
pipePoints.append(points.newPntFromPos3d( geom.Pos3d( 125.2004, 0, 20.4143 ) ))
pipePoints.append(points.newPntFromPos3d( geom.Pos3d( 128.7504, 0, 20.6393 ) ))

# Pipe
pipeLines= []
numDivTuberia= 2
for i in range(3,11):
  pipeLines.append(lines.newLine(pipePoints[i].tag,pipePoints[i+1].tag))

lineasTuberia= preprocessor.getSets.defSet("lineasTuberia")
for l in pipeLines:
  l.ndiv= numDivTuberia
  lineasTuberia.getLines.append(l)

pipeFreePoint= 103
pipeFixedPoint= 112
pipeSupportPoint= 108
pipeFixedPoints= pipeFreePoint,pipeFixedPoint,pipeSupportPoint

#Cables
cableLines= []

longMaxElemCable= 1.5
offsetMastIndex= 1
offsetPipeIndex= 1
# Cables
cableLines.append(lines.newLine(pipePoints[2].tag,mastPoints[4].tag))
cableLines.append(lines.newLine(pipePoints[1].tag,mastPoints[6].tag))
cableLines.append(lines.newLine(pipePoints[0].tag,mastPoints[8].tag))


cableLines.append(lines.newLine(mastPoints[5-offsetMastIndex].tag,mastPoints[13].tag))
cableLines.append(lines.newLine(mastPoints[7-offsetMastIndex].tag,mastPoints[15].tag))
cableLines.append(lines.newLine(mastPoints[9-offsetMastIndex].tag,mastPoints[17].tag))


cableLines.append(lines.newLine(mastPoints[13].tag,pipePoints[04].tag))
cableLines.append(lines.newLine(mastPoints[15].tag,pipePoints[05].tag))
cableLines.append(lines.newLine(mastPoints[17].tag,pipePoints[06].tag))


cableLines.append(lines.newLine(pipePoints[11].tag,mastPoints[24].tag))
cableLines.append(lines.newLine(pipePoints[10].tag,mastPoints[26].tag))
cableLines.append(lines.newLine(pipePoints[9].tag,mastPoints[28].tag))
cableLines.append(lines.newLine(pipePoints[07].tag,mastPoints[30].tag))


cableLines.append(lines.newLine(mastPoints[24].tag,mastPoints[37].tag))
cableLines.append(lines.newLine(mastPoints[26].tag,mastPoints[39].tag))
cableLines.append(lines.newLine(mastPoints[28].tag,mastPoints[41].tag))
cableLines.append(lines.newLine(mastPoints[30].tag,mastPoints[43].tag))


cableLines.append(lines.newLine(mastPoints[37].tag,pipePoints[13].tag))
cableLines.append(lines.newLine(mastPoints[39].tag,pipePoints[14].tag))
cableLines.append(lines.newLine(mastPoints[41].tag,pipePoints[15].tag))
cableLines.append(lines.newLine(mastPoints[43].tag,pipePoints[16].tag))

for l in cableLines:
  l.elemSize= longMaxElemCable

cableAnchorPoints= 100,101,102,113,114,115,116

xcTotalSet= preprocessor.getSets.getSet('total')

# \archivo_err{"pp.err"}
# \archivo_log{"pp.log"}


# \incluye{"geom_acueducto.xci"}
# \incluye{"sections_geometry.xci"}

# \incluye{"define_casos_carga.xci"}
# \incluye{"genera_malla.xcm"}

# \incluye{"carga_agua.xci"}
# \incluye{"wind_loadY.xci"}
# \c{\incluye{"incremento_temperatura.xci"}}

# \incluye{"graficos_vtk.xci"}
# \fin{}
# \incluye{"listados.xci"}

# \incluye{"cargas.xci"}
# \incluye{"resuelve_casos.xci"}

