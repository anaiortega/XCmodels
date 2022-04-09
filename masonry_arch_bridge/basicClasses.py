#-*- coding: utf-8 -*-

from __future__ import division
import math
import rough_calculations.masonry_bridge
import sys

class archGeometry(object):
  """
  Arch deometric definition:
   coefPolArch=[f,j,k,r]: Coefficients of polynomial y=fx^4+jx^3+kx^2+rx+u (u=0)
   XRot=[xA,xB,xC,xD]:  X coordinate rotules A,B,C,D [m]
   arcThick: arch thickness [m]
   arcSpan: arch span [m]
  """
  coefPolArch=[0,0,0,0] #[f,j,k,r] coefficients of polynomial y=fx^4+jx^3+kx^2+rx+u (u=0)
  XRot=[0,0,0,0]        #[xA,xB,xC,xD] X coordinates rotules
  arcThick=0            #arch thickness (m)
  arcSpan=15            #arch span [m]
  arcEffL=4             #arch effective length [m]
  def __init__(self,coefPolArch=[0,0,0,0],XRot=[0,0,0,0],arcThick=0,arcSpan=15,arcEffL=4):
    self.coefPolArch=coefPolArch
    self.XRot=XRot
    self.arcThick=arcThick
    self.arcSpan=arcSpan
    self.arcEffL=arcEffL
  def getYRot(self):
    """YRot=[yA,yB,yC,yD]: Y coordinate of rotules A,B,C,D [m]"""
    YRot=[]
    for x in self.XRot:
      YRot.append(rough_calculations.masonry_bridge.yAxis(self.coefPolArch[0],self.coefPolArch[1],self.coefPolArch[2],self.coefPolArch[3],x))
    return YRot
  def getGammaD(self):
    """angle at rotule D """
    x=self.XRot[3]
    return -rough_calculations.masonry_bridge.calcGamma(self.coefPolArch[0],self.coefPolArch[1],self.coefPolArch[2],self.coefPolArch[3],x)
  def getDistxAC(self):
    return self.XRot[2]-self.XRot[0]
  def getDistxBD(self):
    return self.XRot[1]-self.XRot[3]
  def getDistxAB(self):
    return self.XRot[1]-self.XRot[0]
  def getYKeystone(self):
    """Y coordinate in keystone of arch (at arcSpan/2)""" 
    x=self.arcSpan/2
    return rough_calculations.masonry_bridge.yAxis(self.coefPolArch[0],self.coefPolArch[1],self.coefPolArch[2],self.coefPolArch[3],x)


class FillingCharacteristics(object): 
  angPhi= math.radians(30)   #angle de frottement interne
  cohesion= 0                #cohésion
  mp= 0.33 #Correction factor.
  mc= 0.01 #Correction factor.
  alpha= 0.726
  beta= 6.095
  swFill=18e3   #specific weight of filling material [N/m3]
  swSupStr=20e3 #specific weight or superstructure [N/m3]
  fillThick=9  #thickness of filling material in the endpoint of the arch
  eqThickRoad=0.5  #equivalent thickness of road material
  def __init__(self,a= math.radians(30.0),c= 0.0,mp= 0.33,mc= 0.01,alpha= 0.726,beta= 6.095,swFill=18e3,swSupStr=20e3,fillThick=9,eqThickRoad=0.5):
    self.angPhi= a
    self.cohesion= c
    self.mp= mp
    self.mc= mc
    self.alpha=alpha
    self.beta=beta
    self.swFill=swFill
    self.swSupStr=swSupStr
    self.fillThick=fillThick
    self.eqThickRoad=eqThickRoad
  def getKp(self):
    """coefficient de poussée des terres"""
    return pow(math.tan(math.pi/4+self.angPhi/2),2)
  def getKc(self):
    return 2*math.sqrt(self.getKp())

class trafficLoad(object):
    delta= math.radians(30)
    fillThickKeys= 1.5 # Hauteur du remplissage sur la clé de la voûte (m).
    Q= 160000 # Punctual load due to traffic (N).
    qrep= 0.005e6 # Uniform load due to traffic (Pa).
    def __init__(self,delta= math.radians(30),fillThickKeys= 1.5,Q= 160000,qrep= 0.005e6):
        self.delta=delta
        self.fillThickKeys=fillThickKeys
        self.Q=Q
        self.qrep=qrep

class permLoadResult(object):
  """Permanent load resultants"""
  gm= archGeometry()
  fc= FillingCharacteristics()
  def __init__(self,gm,fc):
    self.gm= gm
    self.fc= fc
  def getEta(self):
    """Résultante des charges permanentes sur l'overture active de l'arc (fig. 6.9) [N]"""
    return self.gm.arcEffL*(self.fc.swSupStr*self.fc.eqThickRoad*self.gm.getDistxAB()+self.fc.swFill*(self.fc.fillThick*self.gm.getDistxAB()+rough_calculations.masonry_bridge.aux1(self.gm.coefPolArch[0],self.gm.coefPolArch[1],self.gm.coefPolArch[2],self.gm.coefPolArch[3],self.gm.XRot[1],self.gm.XRot[0])))

  def getEtaW(self):
    return self.gm.arcEffL*(self.fc.swSupStr*self.fc.eqThickRoad*pow(self.gm.getDistxAB(),2)/2+self.fc.swFill*(self.fc.fillThick*pow(self.gm.getDistxAB(),2)/2-self.gm.coefPolArch[0]*pow(self.gm.XRot[1],6)/30-self.gm.coefPolArch[1]*pow(self.gm.XRot[1],5)/20-self.gm.coefPolArch[2]*pow(self.gm.XRot[1],4)/12-self.gm.coefPolArch[3]*pow(self.gm.XRot[1],3)/6-self.gm.coefPolArch[0]*pow(self.gm.XRot[0],6)/6-self.gm.coefPolArch[1]*pow(self.gm.XRot[0],5)/5+self.gm.coefPolArch[0]*pow(self.gm.XRot[0],5)*self.gm.XRot[1]/5-self.gm.coefPolArch[2]*pow(self.gm.XRot[0],4)/4+self.gm.coefPolArch[1]*pow(self.gm.XRot[0],4)*self.gm.XRot[1]/4-self.gm.coefPolArch[3]*pow(self.gm.XRot[0],3)/3+self.gm.coefPolArch[2]*pow(self.gm.XRot[0],3)*self.gm.XRot[1]/3+self.gm.coefPolArch[3]*pow(self.gm.XRot[0],2)*self.gm.XRot[1]/2))

  def getPhi(self):
    """résultante des charges permanentes solicitant la portion d'arc comprise entre les rotules A et C (fig. 6.9) [N]"""
    return self.gm.arcEffL*(self.fc.swSupStr*self.fc.eqThickRoad*self.gm.getDistxAC()+self.fc.swFill*(self.fc.fillThick*self.gm.getDistxAC()+rough_calculations.masonry_bridge.aux1(self.gm.coefPolArch[0],self.gm.coefPolArch[1],self.gm.coefPolArch[2],self.gm.coefPolArch[3],self.gm.XRot[2],self.gm.XRot[0])))

  def getPsi(self):
    """résultante des charges permanentes solicitant la portion d'arc comprise entre les rotules D et B (fig. 6.9) [N] """
    return self.gm.arcEffL*(self.fc.swSupStr*self.fc.eqThickRoad*self.gm.getDistxBD()+self.fc.swFill*(self.fc.fillThick*self.gm.getDistxBD()+rough_calculations.masonry_bridge.aux1(self.gm.coefPolArch[0],self.gm.coefPolArch[1],self.gm.coefPolArch[2],self.gm.coefPolArch[3],self.gm.XRot[1],self.gm.XRot[3])))

  def getPhiS(self):
    """moment de flexion induit par la résultante phi de la charge permanente entre A et C, par rapport à la rotule C (fig. 6.9) [Nm] """
    return self.gm.arcEffL*(self.fc.swSupStr*self.fc.eqThickRoad*pow(self.gm.getDistxAC(),2)/2+self.fc.swFill*(self.fc.fillThick*pow(self.gm.getDistxAC(),2)/2-self.gm.coefPolArch[0]*pow(self.gm.XRot[2],6)/30-self.gm.coefPolArch[1]*pow(self.gm.XRot[2],5)/20-self.gm.coefPolArch[2]*pow(self.gm.XRot[2],4)/12-self.gm.coefPolArch[3]*pow(self.gm.XRot[2],3)/6-self.gm.coefPolArch[0]*pow(self.gm.XRot[0],6)/6-self.gm.coefPolArch[1]*pow(self.gm.XRot[0],5)/5+self.gm.coefPolArch[0]*pow(self.gm.XRot[0],5)*self.gm.XRot[2]/5-self.gm.coefPolArch[2]*pow(self.gm.XRot[0],4)/4+self.gm.coefPolArch[1]*pow(self.gm.XRot[0],4)*self.gm.XRot[2]/4-self.gm.coefPolArch[3]*pow(self.gm.XRot[0],3)/3+self.gm.coefPolArch[2]*pow(self.gm.XRot[0],3)*self.gm.XRot[2]/3+self.gm.coefPolArch[3]*pow(self.gm.XRot[0],2)*self.gm.XRot[2]/2))

  def getPsiT(self):
    """moment de flexion induit par la résultante psi de la charge permanente entre D et B, par rapport à la rotule D (fig. 6.9) [Nm] """
    return self.gm.arcEffL*(self.fc.swSupStr*self.fc.eqThickRoad*pow(self.gm.getDistxBD(),2)/2+self.fc.swFill*(self.fc.fillThick*pow(self.gm.getDistxBD(),2)/2-self.gm.coefPolArch[0]*pow(self.gm.XRot[3],6)/30-self.gm.coefPolArch[1]*pow(self.gm.XRot[3],5)/20-self.gm.coefPolArch[2]*pow(self.gm.XRot[3],4)/12-self.gm.coefPolArch[3]*pow(self.gm.XRot[3],3)/6-self.gm.coefPolArch[0]*pow(self.gm.XRot[1],6)/6-self.gm.coefPolArch[1]*pow(self.gm.XRot[1],5)/5+self.gm.coefPolArch[0]*pow(self.gm.XRot[1],5)*self.gm.XRot[3]/5-self.gm.coefPolArch[2]*pow(self.gm.XRot[1],4)/4+self.gm.coefPolArch[1]*pow(self.gm.XRot[1],4)*self.gm.XRot[3]/4-self.gm.coefPolArch[3]*pow(self.gm.XRot[1],3)/3+self.gm.coefPolArch[2]*pow(self.gm.XRot[1],3)*self.gm.XRot[3]/3+self.gm.coefPolArch[3]*pow(self.gm.XRot[1],2)*self.gm.XRot[3]/2))

  def getR(self):
    """résultant de la poussée laterale entre les rotules B et D [N]"""
    return self.gm.arcEffL*(self.fc.getKp()*self.fc.mp*(self.fc.eqThickRoad*self.fc.swSupStr*(self.gm.getYRot()[3]-self.gm.getYRot()[1])+self.fc.swFill*self.fc.fillThick*(self.gm.getYRot()[3]-self.gm.getYRot()[1])-self.fc.swFill*(self.gm.getYRot()[3]*self.gm.getYRot()[3]/2-self.gm.getYRot()[1]*self.gm.getYRot()[1]/2))+self.fc.cohesion*self.fc.mc*self.fc.getKc()*(self.gm.getYRot()[3]-self.gm.getYRot()[1]))

  def getRzB(self):
    """moment de flexion induit par la résultant de la poussée laterale entre les rotules B et D, par rapport à la rotule B [Nm]"""
    return self.gm.arcEffL*(self.fc.getKp()*self.fc.mp*(self.fc.eqThickRoad*self.fc.swSupStr*(self.gm.getYRot()[3]*self.gm.getYRot()[3]/2-self.gm.getYRot()[1]*self.gm.getYRot()[1]/2-self.gm.getYRot()[1]*(self.gm.getYRot()[3]-self.gm.getYRot()[1])))+self.fc.swFill*(self.fc.fillThick*(self.gm.getYRot()[3]*self.gm.getYRot()[3]/2-self.gm.getYRot()[1]*self.gm.getYRot()[1]/2)-self.fc.fillThick*self.gm.getYRot()[1]*(self.gm.getYRot()[3]-self.gm.getYRot()[1])-pow(self.gm.getYRot()[3],3)/3+pow(self.gm.getYRot()[1],3)/3+self.gm.getYRot()[1]*(self.gm.getYRot()[3]*self.gm.getYRot()[3]/2-self.gm.getYRot()[1]*self.gm.getYRot()[1]/2))+self.fc.cohesion*self.fc.mc*self.fc.getKc()*(self.gm.getYRot()[3]*self.gm.getYRot()[3]/2-self.gm.getYRot()[1]*self.gm.getYRot()[1]/2-self.gm.getYRot()[1]*(self.gm.getYRot()[3]-self.gm.getYRot()[1])))


  def getRzD(self):
    """moment de flexion induit par la résultant de la poussée laterale entre les rotules B et D, par rapport à la rotule D [Nm]"""
    return self.gm.arcEffL*(self.fc.getKp()*self.fc.mp*(self.fc.eqThickRoad*self.fc.swSupStr*(self.gm.getYRot()[3]*(self.gm.getYRot()[3]-self.gm.getYRot()[1])-self.gm.getYRot()[3]*self.gm.getYRot()[3]/2+self.gm.getYRot()[1]*self.gm.getYRot()[1]/2))+self.fc.swFill*(self.fc.fillThick*self.gm.getYRot()[3]*(self.gm.getYRot()[3]-self.gm.getYRot()[1])-self.fc.fillThick*(self.gm.getYRot()[3]*self.gm.getYRot()[3]/2-self.gm.getYRot()[1]*self.gm.getYRot()[1]/2)-self.gm.getYRot()[3]*(self.gm.getYRot()[3]*self.gm.getYRot()[3]/2-self.gm.getYRot()[1]*self.gm.getYRot()[1]/2)+pow(self.gm.getYRot()[3],3)/3-pow(self.gm.getYRot()[1],3)/3)+self.fc.cohesion*self.fc.mc*self.fc.getKc()*(self.gm.getYRot()[3]*(self.gm.getYRot()[3]-self.gm.getYRot()[1])-self.gm.getYRot()[3]*self.gm.getYRot()[3]/2+self.gm.getYRot()[1]*self.gm.getYRot()[1]/2))

class trafficLoadResult(object):
  """Traffic load resultants"""
  gm= archGeometry()
  tl= trafficLoad()
  def __init__(self,gm,tl):
    self.gm= gm
    self.tl= tl

  def getvQt(self):
    return rough_calculations.masonry_bridge.vQtrans(self.gm.arcEffL,self.tl.delta,self.tl.fillThickKeys)

  def getqtrans(self):
    """Charge de trafic uniformemente [N/m] répartie après diffussion transversale (voir 6-15)"""
    return self.tl.Q/self.getvQt()

  def getlQt(self):
    return rough_calculations.masonry_bridge.lQtrans(self.gm.getDistxAB(),self.tl.delta,self.tl.fillThickKeys)

  def getX(self):
    """Charge de trafic ponctuelle aprés diffusion longitudinale et transversale (voir 6.18) [Pa]"""
    return self.getqtrans()/self.getlQt()

class resistance(object):
  Nadmis=0    #Effort axial admisible [N]
  gm= archGeometry()
  fc= FillingCharacteristics()
  tl=trafficLoad()
  plR= permLoadResult(gm,fc)
  tlR= trafficLoadResult(gm,tl)
  def __init__(self,Nadmis,gm,fc,tl,plR,tlR):
    self.Nadmis=Nadmis
    self.gm= gm
    self.fc= fc
    self.tl= tl
    self.plR= plR
    self.tlR= tlR

  def getMadmis(self):
    """Moment de flexion admis (voir 5.17 et A 7.15) [Nm]"""
    return rough_calculations.masonry_bridge.diagInteraction(self.Nadmis,self.gm.arcThick,self.gm.arcEffL,self.fc.alpha,self.fc.beta)
  def getE(self):
    return rough_calculations.masonry_bridge.calcE6p27(self.tlR.getX(),self.tl.qrep,self.gm.arcSpan,self.gm.getDistxAB(),self.gm.arcEffL,self.tlR.getlQt(),self.gm.getDistxAC(),self.gm.getDistxBD(),self.gm.getYRot()[0],self.gm.getYRot()[1],self.gm.getYRot()[2],self.gm.getYRot()[3],self.gm.XRot[0])
  def getF(self):
    return rough_calculations.masonry_bridge.calcF6p28(self.plR.getR(),self.gm.getDistxAB(),self.gm.getDistxAC(),self.gm.getDistxBD(),self.plR.getEta(),self.plR.getPhiS(),self.plR.getEtaW(),self.plR.getPsiT(),self.getMadmis(),self.getMadmis(),self.getMadmis(),self.plR.getRzB(),self.plR.getRzD(),self.gm.getYRot()[0],self.gm.getYRot()[1],self.gm.getYRot()[2],self.gm.getYRot()[3])
  def getG(self):
    return rough_calculations.masonry_bridge.calcG6p29(self.tlR.getX(),self.tl.qrep,self.gm.arcSpan,self.gm.getDistxAB(),self.gm.arcEffL,self.tlR.getlQt(),self.gm.getDistxAC(),self.gm.getDistxBD(),self.gm.getYRot()[0],self.gm.getYRot()[1],self.gm.getYRot()[2],self.gm.getYRot()[3],self.gm.XRot[0],self.gm.getGammaD())
  def getH(self):
    return rough_calculations.masonry_bridge.calcH6p30(self.gm.getDistxAB(),self.gm.getDistxAC(),self.plR.getEta(),self.plR.getPsi(),self.plR.getPhiS(),self.plR.getEtaW(),self.getMadmis(),self.getMadmis(),self.getMadmis(),self.plR.getRzB(),self.gm.getYRot()[0],self.gm.getYRot()[1],self.gm.getYRot()[2],self.gm.getYRot()[3],self.gm.getGammaD())
  def getSafCoef(self):
    """Safety coefficient - Multiplicateur limite des charges utiles (voir 6.32)"""
    return rough_calculations.masonry_bridge.calcn6p32(self.fc.alpha,self.fc.beta,self.gm.arcThick,self.gm.arcEffL,self.getE(),self.getF(),self.getG(),self.getH())
  def getMinimFunc(self,x):
    self.gm.XRot=x
    return self.getSafCoef()
