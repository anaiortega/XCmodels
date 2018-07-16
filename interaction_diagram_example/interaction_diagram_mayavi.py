# -*- coding: utf-8 -*-
''' display a 3D interaction diagram.'''
from __future__ import division
# Macros
import xc_base
import geom
import xcGnuGts
import xc

from materials.ehe import EHE_materials
from postprocess.reports import graph_material as mg

# Coeficientes de seguridad.
gammac= 1.5 # Partial safety factor for concrete strength.
gammas= 1.15 # Partial safety factor for steel strength.

width= 0.2 # Section width (m).
depth= 0.4 # Section depth (m).
cover= 0.05 # Concrete cover (m).
diam= 16e-3 # Diámetro de las barras expresado en metros.
areaFi16= 2.01e-4 # Área de las barras expresado en metros cuadrados.


prueba= xc.FEProblem()
preprocessor=  prueba.getPreprocessor
# Definimos materiales
concr=EHE_materials.HA25
concr.alfacc=0.85    #f_maxd= 0.85*fcd coeficiente de fatiga del hormigón (generalmente alfacc=1)
concreteDiagram= concr.defDiagD(preprocessor)
Ec= concreteDiagram.getTangent
reinfSteel= EHE_materials.B500S
steelDiagram= reinfSteel.defDiagD(preprocessor)
Es= steelDiagram.getTangent

geomRCSection= preprocessor.getMaterialHandler.newSectionGeometry("geomRCSection")
regiones= geomRCSection.getRegions
concrete= regiones.newQuadRegion(concr.nmbDiagD)
concrete.nDivIJ= 10
concrete.nDivJK= 10
concrete.pMin= geom.Pos2d(-depth/2.0,-width/2.0)
concrete.pMax= geom.Pos2d(depth/2.0,width/2.0)
reinforcement= geomRCSection.getReinfLayers
reinforcementInf= reinforcement.newStraightReinfLayer(reinfSteel.nmbDiagD)
reinforcementInf.numReinfBars= 2
reinforcementInf.barArea= areaFi16
reinforcementInf.p1= geom.Pos2d(cover-depth/2.0,cover-width/2.0) # Bottom reinforcement.
reinforcementInf.p2= geom.Pos2d(cover-depth/2.0,width/2.0-cover)
reinforcementSup= reinforcement.newStraightReinfLayer(reinfSteel.nmbDiagD)
reinforcementSup.numReinfBars= 2
reinforcementSup.barArea= areaFi16
reinforcementSup.p1= geom.Pos2d(depth/2.0-cover,cover-width/2.0) # Top reinforcement.
reinforcementSup.p2= geom.Pos2d(depth/2.0-cover,width/2.0-cover)

materiales= preprocessor.getMaterialHandler
secHA= materiales.newMaterial("fiber_section_3d","secHA")
fiberSectionRepr= secHA.getFiberSectionRepr()
fiberSectionRepr.setGeomNamed("geomRCSection")
secHA.setupFibers()
fibers= secHA.getFibers()

param= xc.InteractionDiagramParameters()
param.concreteTag= concr.matTagD
param.reinforcementTag= reinfSteel.matTagD
diagIntsecHA= materiales.calcInteractionDiagram("secHA",param)

mayaviGraphic= mg.InteractionDiagram3DGraphic(diagIntsecHA)

mayaviGraphic.show()

