# -*- coding: utf-8 -*-
''' Interaction diagram test.
   Home made test. '''
from __future__ import division
# Macros
import xc_base
import geom
import xc

from materials.ehe import EHE_materials
import math
from materials.sia262 import SIA262_materials
from materials.sections.fiber_section import def_simple_RC_section
from materials.sections.fiber_section import section_report as sr
from materials.sections.fiber_section import plotSectionGeometry as pg
from postprocess.reports import graph_material as mg

areaFi6= SIA262_materials.section_barres_courantes[6e-3]
areaFi8= SIA262_materials.section_barres_courantes[8e-3]
areaFi10= SIA262_materials.section_barres_courantes[10e-3]
areaFi12= SIA262_materials.section_barres_courantes[12e-3]
areaFi14= SIA262_materials.section_barres_courantes[14e-3]
areaFi16= SIA262_materials.section_barres_courantes[16e-3]
areaFi18= SIA262_materials.section_barres_courantes[18e-3]
areaFi20= SIA262_materials.section_barres_courantes[20e-3]
areaFi22= SIA262_materials.section_barres_courantes[22e-3]
areaFi26= SIA262_materials.section_barres_courantes[26e-3]
areaFi30= SIA262_materials.section_barres_courantes[30e-3]
areaFi34= SIA262_materials.section_barres_courantes[34e-3]
areaFi40= SIA262_materials.section_barres_courantes[40e-3]

concrete= EHE_materials.HA45
concrete.alfacc=0.85    #concrete fatigue factor (generalmente se toma alfacc=1)
reinfSteel= EHE_materials.B500S

dRebar= 0.15
sccData= def_simple_RC_section.RCRectangularSection()
sccData.name= "sccData"
sccData.sectionDescr= "Prueba."
sccData.fiberSectionParameters.concrType= concrete
sccData.h= 0.5
sccData.b= 1.0
sccData.fiberSectionParameters.reinfSteelType= reinfSteel
negReb=def_simple_RC_section.ReinfRow(rebarsDiam=40e-3,areaRebar= areaFi40,rebarsSpacing=dRebar,width=1.0,nominalCover=0.25-0.19)
sccData.negatvRebarRows= def_simple_RC_section.LongReinfLayers([negReb])
posReb=def_simple_RC_section.ReinfRow(rebarsDiam=6e-3,areaRebar= areaFi6,rebarsSpacing=dRebar,width=1.0,nominalCover=0.25-0.19)
sccData.positvRebarRows= def_simple_RC_section.LongReinfLayers([posReb])

zinf= sccData.h/2.0
zsup= -sccData.h/2.0

prueba= xc.FEProblem()
#prueba.logFileName= "/tmp/borrar.log" # Don't print warnings.
prueba.errFileName= "/tmp/borrar.err" # Don't print errors.

preprocessor= prueba.getPreprocessor
print "divIJ= ", sccData.nDivIJ, "divJK= ", sccData.nDivJK
#sccData.nDivIJ= 100
#sccData.nDivJK= 100
sccData.defRCSection(preprocessor,'d')
si= sr.SectionInfoHASimple(preprocessor,sccData)
si.writeReport('./prueba.tex','./prueba.eps')

Agross= sccData.b*sccData.h
IyGross= 1.0/12.0*sccData.b*sccData.h**3
IzGross= 1.0/12.0*sccData.h*sccData.b**3
n= si.scc.getSteelEquivalenceCoefficient(preprocessor)
AsBarsUp= 6*areaFi40
AsBarsDown= 6*areaFi6
AsTeor= AsBarsUp+AsBarsDown
As= si.areaMainReinforcement
barsUpTeorCenterOfMass= sccData.getNegRowsCGcover()-sccData.h/2.0
barsUpCenterOfMass= sccData.negReinfLayers[0].getCenterOfMass()
#barsUpCenterOfMass= sccData.negReinfLayer.getCenterOfMass()
zBarsUp= barsUpCenterOfMass[1]-si.GH[1]
barsDownTeorCenterOfMass=sccData.h/2.0-sccData.getPosRowsCGcover()
#barsDownTeorCenterOfMass= sccData.h/2.0-sccData.positvRebars.cover
barsDownCenterOfMass= sccData.posReinfLayers[0].getCenterOfMass()
#barsDownCenterOfMass= sccData.posReinfLayer.getCenterOfMass()
zBarsDown= barsDownCenterOfMass[1]-si.GH[1]

Ahomog= Agross+n*AsTeor
yCenterOfMassHomogTeor= si.GH[0]
zCenterOfMassHomogTeor= si.GH[1]
IyHomogBarsUpTeor= n*6*math.pi*(20e-3)**4/4.0

IyHomogBarsUp= sccData.negReinfLayers[0].getReinfBars.getIyHomogenizedSection(si.tangConcr)
IyHomogBarsDownTeor= n*6*math.pi*(3e-3)**4/4.0
IyHomogBarsDown= sccData.posReinfLayers[0].getReinfBars.getIyHomogenizedSection(si.tangConcr)
zConcrete= si.GB[1]-si.GH[1]
IyHomog= IyGross+Agross*zConcrete**2+n*(AsBarsUp*zBarsUp**2+AsBarsDown*zBarsDown**2)+IyHomogBarsUpTeor+IyHomogBarsDownTeor

delta= (1-5*dRebar)/2.0
IzHomogBarsUpTeor= n*(6*math.pi*(20e-3)**4/4.0+2*areaFi40*((dRebar/2.0)**2+(dRebar*1.5)**2+(dRebar*2.5)**2))
IzHomogBarsUp= sccData.negReinfLayers[0].getReinfBars.getIzHomogenizedSection(si.tangConcr)
IzHomogBarsDownTeor= n*(6*math.pi*(3e-3)**4/4.0+2*areaFi6*((dRebar/2.0)**2+(dRebar*1.5)**2+(dRebar*2.5)**2))
IzHomogBarsDown= sccData.posReinfLayers[0].getReinfBars.getIzHomogenizedSection(si.tangConcr)
IzHomog= IzGross+IzHomogBarsUpTeor+IzHomogBarsDownTeor

fiberModel= sccData.fs
fibers= fiberModel.getFibers()
Afibers= fibers.getAreaHomogenizedSection(si.tangConcr)
fibersCenterOfMass= fibers.getCenterOfMassHomogenizedSection(si.tangConcr)
yCenterOfMassHomogFibers= fibersCenterOfMass[0]
zCenterOfMassHomogFibers= fibersCenterOfMass[1]
IyFibers= fibers.getIyHomogenizedSection(si.tangConcr)
IzFibers= fibers.getIzHomogenizedSection(si.tangConcr)

class Extrema(object):
  def __init__(self,nmax,nmin,mmax,mmin):
    self.NMax= nmax
    self.NMin= nmin
    self.MMax= mmax
    self.MMin= mmin
  def fromInteractionDiagram(self,diag):
    self.NMax= diag.getXMax
    self.NMin= diag.getXMin
    self.MMax= diag.getYMax
    self.MMin= diag.getYMin
  def __sub__(self, other) :
    return Extrema(self.NMax-other.NMax,self.NMin-other.NMin,self.MMax-other.MMax,self.MMin-other.MMin)
  def __add__(self, other) :
    return Extrema(self.NMax+other.NMax,self.NMin+other.NMin,self.MMax+other.MMax,self.MMin+other.MMin)
  def getRatios(self,other):
    dif= self-other
    ratios= []
    ratios.append(dif.NMax/other.NMax)
    ratios.append(dif.NMin/other.NMin)
    ratios.append(dif.MMax/other.MMax)
    ratios.append(dif.MMin/other.MMin)
    return ratios
  def printRatios(self,other):
    ratios= self.getRatios(other)
    print 'NMax= ', self.NMax/1e3, ' kN NMaxTeor= ', other.NMax/1e3, ' kN ratio[0]= ', ratios[0]
    print 'NMin= ', self.NMin/1e3, ' kM NMinTeor= ', other.NMin/1e3, ' kN ratios[1]= ', ratios[1]
    print 'MMax= ', self.MMax/1e3, ' kM MMaxTeor= ', other.MMax/1e3, ' kM ratios[2]= ', ratios[2]
    print 'MMin= ', self.MMin/1e3, ' kM MMinTeor= ', other.MMin/1e3, ' kM ratios[3]= ', ratios[3]
    

#Test N-My interaction diagram.
diagNMy= sccData.defInteractionDiagramNMy(preprocessor)
extNMy= Extrema(diagNMy.getXMax,diagNMy.getXMin,diagNMy.getYMax,diagNMy.getYMin)
nPos= AsTeor*sccData.fiberSectionParameters.reinfSteelType.fyd()
nNeg= -nPos+(Agross-AsTeor)*sccData.fiberSectionParameters.concrType.fcd()*0.85
extNMyTeor= Extrema(nPos,nNeg,1062.9e3,-1069.8e3) #Numeric values obtained from Fagus program.
ratiosNMy= extNMy.getRatios(extNMyTeor)

#Test N-Mz interaction diagram.
diagNMz= sccData.defInteractionDiagramNMz(preprocessor)
extNMz= Extrema(diagNMz.getXMax,diagNMz.getXMin,diagNMz.getYMax,diagNMz.getYMin)
extNMzTeor= Extrema(nPos,nNeg,1623.8e3,-1623.8e3) #Numeric values obtained from Fagus program.
ratiosNMz= extNMz.getRatios(extNMzTeor)


# epsilon= -2.0e-3 # Maximal compression in concrete.
# p1= geom.Pos3d(epsilon,sccData.b/2.0,zsup)
# p2= geom.Pos3d(epsilon,-sccData.b/2.0,zsup)
# p3= geom.Pos3d(epsilon,sccData.b/2.0,zinf)
# epsVector= xc.DeformationPlane(p1,p2,p3)
# fiberModel.setTrialDeformationPlane(epsVector)
# for f in fibers:
#   force= f.getForce()
#   area= f.getArea()
#   stress= force/area
#   strain= f.getStrain()
#   print 'tag= ', f.tag, " force= ", force/1e3, " kN ", " stress= ", stress/1e6, 'MPa. strain= ', strain
# epsNFibers= fiberModel.getSectionDeformationByName('defN')
# NMinFibers= fiberModel.getStressResultantComponent("N")
# MzFibers= fiberModel.getStressResultantComponent("Mz")
# MyFibers= fiberModel.getStressResultantComponent("My")
# #print "NMinFibers= ", NMinFibers #, MzFibers, MyFibers


ratio0= (Agross-si.AB)/Agross
ratio1= (IyGross-si.IyB)/IyGross
ratio2= (IzGross-si.IzB)/IzGross
ratio3= (AsTeor-As)/AsTeor
ratio4= (barsUpTeorCenterOfMass-barsUpCenterOfMass[1])/barsUpTeorCenterOfMass
ratio5= (barsDownTeorCenterOfMass-barsDownCenterOfMass[1])/barsDownTeorCenterOfMass
ratio10= (Ahomog-si.AH)/Ahomog
ratio11A= (IyHomogBarsUpTeor-IyHomogBarsUp)/IyHomogBarsUpTeor
ratio11B= (IyHomogBarsDownTeor-IyHomogBarsDown)/IyHomogBarsDownTeor
ratio11= (IyHomog-si.IyH)/IyHomog
ratio12A= (IzHomogBarsUpTeor-IzHomogBarsUp)/IzHomogBarsUpTeor
ratio12B= (IzHomogBarsDownTeor-IzHomogBarsDown)/IzHomogBarsDownTeor
ratio12= (IzHomog-si.IzH)/IzHomog
ratio20= (Ahomog-Afibers)/Ahomog
ratio21= (IyHomog-IyFibers)/IyHomog
ratio22= (IzHomog-IzFibers)/IzHomog
ratio23= (yCenterOfMassHomogTeor-yCenterOfMassHomogFibers)
ratio24= (zCenterOfMassHomogTeor-zCenterOfMassHomogFibers)/zCenterOfMassHomogTeor
ratio30= ratiosNMy[0]
ratio31= ratiosNMy[1]
ratio32= ratiosNMy[2]
ratio33= ratiosNMy[3]
ratio40= ratiosNMz[0]
ratio41= ratiosNMz[1]
ratio42= ratiosNMz[2]
ratio43= ratiosNMz[3]



'''
print "ratio0= ", ratio0
print "IyGrossTeor= ", IyGross, " IyGross= ", si.IyB, "ratio1= ", ratio1
print "IzGrossTeor= ", IzGross, " IzGross= ", si.IzB, "ratio2= ", ratio2
print "As= ", As, " AsTeor= ", AsTeor, "ratio3= ", ratio3
print "barsUpTeorCenterOfMass= ", barsUpTeorCenterOfMass, " barsUpCenterOfMass= ", barsUpCenterOfMass, "ratio4= ", ratio4
print "barsDownTeorCenterOfMass= ", barsDownTeorCenterOfMass, " barsDownCenterOfMass= ", barsDownCenterOfMass, "ratio5= ", ratio5
print "n= ", n, "Ahomog= ", si.AH, " AhomogTeor= ", Ahomog, "ratio10= ", ratio10
print "n= ", n, "IyHomogBarsUp= ", IyHomogBarsUp, " IyHomogBarsUpTeor= ", IyHomogBarsUpTeor, "ratio11A= ", ratio11A
print "n= ", n, "IyHomogBarsDown= ", IyHomogBarsDown, " IyHomogBarsDownTeor= ", IyHomogBarsDownTeor, "ratio11B= ", ratio11B
print "n= ", n, "IyHomog= ", si.IyH, " IyHomogTeor= ", IyHomog, "ratio11= ", ratio11
print "n= ", n, "IzHomogBarsUp= ", IzHomogBarsUp, " IzHomogBarsUpTeor= ", IzHomogBarsUpTeor, "ratio12A= ", ratio12A
print "n= ", n, "IzHomogBarsDown= ", IzHomogBarsDown, " IzHomogBarsDownTeor= ", IzHomogBarsDownTeor, "ratio12A= ", ratio12B
print "n= ", n, "IzHomog= ", si.IzH, " IzHomogTeor= ", IzHomog, "ratio12= ", ratio12
print "n= ", n, "Ahomog= ", Ahomog, " Afibers= ", Afibers, "ratio20= ", ratio20
print "n= ", n, "IyHomog= ", IyFibers, " IyHomogTeor= ", IyHomog, "ratio21= ", ratio21
print "n= ", n, "IzHomog= ", IzFibers, " IzHomogTeor= ", IzHomog, "ratio22= ", ratio22
print "n= ", n, "yCenterOfMassHomogHomog= ", yCenterOfMassHomogFibers, " yCenterOfMassHomogHomogTeor= ", yCenterOfMassHomogTeor, "ratio23= ", ratio23
print "n= ", n, "zCenterOfMassHomogHomog= ", zCenterOfMassHomogFibers, " zCenterOfMassHomogHomogTeor= ", zCenterOfMassHomogTeor, "ratio24= ", ratio24
extNMy.printRatios(extNMyTeor)
extNMz.printRatios(extNMzTeor)
'''
import matplotlib.pyplot as plt
#Steel stress-strain diagram
materialDiagram= sccData.fiberSectionParameters.reinfSteelType.plotDesignStressStrainDiagram(preprocessor)


#mg.plotInteractionDiagram2D(diagNMy)
diagGraphicNMy= mg.InteractionDiagramGraphic('N-My interaction diagram')
diagGraphicNMy.decorations.xLabel= 'My [kNm]'
diagGraphicNMy.decorations.yLabel= 'N [kN]'
diagGraphicNMy.setupGraphic(diagNMy)
diagGraphicNMy.savefig('diagNMy.eps')
diagGraphicNMy.savefig('diagNMy.jpeg')

diagGraphicNMz= mg.InteractionDiagramGraphic('N-Mz interaction diagram')
diagGraphicNMz.decorations.xLabel= 'Mz [kNm]'
diagGraphicNMz.decorations.yLabel= 'N [kN]'
diagGraphicNMz.setupGraphic(diagNMz)
diagGraphicNMz.savefig('diagNMz.eps')
diagGraphicNMz.savefig('diagNMz.jpeg')

'''
'''

import os
fname= os.path.basename(__file__)
if((abs(ratio0)<1e-12) & (abs(ratio1)<1e-12) & (abs(ratio2)<1e-12) & (abs(ratio3)<1e-12) & (abs(ratio4)<1e-12) & (abs(ratio5)<1e-12) & (abs(ratio10)<1e-12) & (abs(ratio11A)<1e-12) & (abs(ratio11B)<1e-12) & (abs(ratio11)<1e-12) & (abs(ratio12A)<1e-12) & (abs(ratio12B)<1e-12) & (abs(ratio12)<1e-12) & (abs(ratio12A)<1e-12) & (abs(ratio12B)<1e-12) & (abs(ratio12)<1e-12) & (abs(ratio20)<1e-12) & (abs(ratio21)<0.01) & (abs(ratio22)<0.01) & (abs(ratio23)<1e-12) & (abs(ratio24)<1e-12) & (abs(ratio30)<0.01)):
# & (abs(ratio31)<0.01 & (abs(ratio32)<0.05) & (abs(ratio33)<0.05) & (abs(ratio41)<0.01) & (abs(ratio42)<0.05) & (abs(ratio43)<0.05)):
  print "test ",fname,": ok."
else:
  print "test ",fname,": ERROR."
