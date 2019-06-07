ft2m=0.3048
in2m=0.0254
# Columns, dimensions X direction
dimWA=20*ft2m
dimAB=26*ft2m
dimBC=20*ft2m+10*in2m
dimCD=39*ft2m+4*in2m
dimDG=25*ft2m+10*in2m
dimGF=28*ft2m
dimFW=23*ft2m

#Columns, dimensions Y direction
dimW1=8.839
dim12=8.306
dim23=8.306
dim34=8.306
dim45=8.306
dim5W=6.096

xCols=[dimWA]
xCols.append(xCols[-1]+dimAB)
xCols.append(xCols[-1]+dimBC)
xCols.append(xCols[-1]+dimCD)
xCols.append(xCols[-1]+dimDG)
xCols.append(xCols[-1]+dimGF)

yCols=[dimW1]
yCols.append(yCols[-1]+dim12)
yCols.append(yCols[-1]+dim23)
yCols.append(yCols[-1]+dim34)
yCols.append(yCols[-1]+dim45)

xWalls=[0,xCols[-1]+dimFW]
yWalls=[0,yCols[-1]+dim5W]

xRamp=[7.828]
yRamp=[16.02]
yStair1=[30.373,33.183]

xStair2Elev=[16.66]
yStair2Elev=[8.875]

#Facades
xFac=[0,xCols[2],xCols[3],53.52]
yFac=[0,10.975,44.77]   

#Wall frames
xWF=[0,xCols[0],xCols[0]+3.5,10.2,10.2+1.6/2.,xCols[1],xCols[2],xCols[3],xFac[-1]-10.2-0.8,xFac[-1]-10.2,xFac[-1]-9.6,xFac[-1]-10.2+4.2,xFac[-1]]


yWF=[0,yCols[0],yCols[0]+2,yCols[3]-4.5,yCols[3],yFac[-1]]


gap=0.2

xGaps=[]
for i in xCols:
    xGaps.append(i-gap/2.)
    xGaps.append(i+gap/2.)
yGaps=[]
for i in yCols:
    yGaps.append(i-gap/2.)
    yGaps.append(i+gap/2.)

#!!!!! Modify according to problem!!!
zCol=3 #!!!!!
zBeamLow=2.75
zBeamHigh=3
zHlwLow=(zCol+zBeamLow)/2.0
zHlwHigh=zCol+0.15

# coordinates in global X,Y,Z axes for the grid generation
xListaux=xCols+xWalls+xRamp+xStair2Elev+xFac+xWF+xGaps+xWalls
xList=[]
for i in xListaux:
    if i not in xList:
        xList.append(i)
xList.sort()
yListaux=yCols+yWalls+yRamp+yStair1+yStair2Elev+yFac+yWF+yGaps
yList=[]
for i in yListaux:
    if i not in yList:
        yList.append(i)
yList.sort()

zList=[0,zBeamLow,zHlwLow,zCol,zHlwHigh]
#auxiliary data
lastXpos=len(xList)-1
lastYpos=len(yList)-1
lastZpos=len(zList)-1

#Beam section
beamWidth=0.4
beamHeight=0.5

#Column section
colXdim=0.5
colYdim=0.3

# precast slabs
slabTh=0.20
#Compressive deck layer


#Weight hollowcore deck 30+5 [Pa]
Whollowdeck=6440
#Dead load facades [N/ml]
DLfac=7352+2035+4876
#Dead load interior wall frames [N/ml]
DLwf=4070+9746

#Live load facades [N/ml]
LLfac=5269+21065
#Live load interior wall frames [N/ml]
LLwf=10538+42130

#Snow load facades [N/ml]
SLfac=15801
#Snow load interior wall frames [N/ml]
SLwf=31603



#unif. live load rooms[Pa]
unifLLrooms=1915
#unif. live load terrace [Pa]
unifLLterrace=4788



