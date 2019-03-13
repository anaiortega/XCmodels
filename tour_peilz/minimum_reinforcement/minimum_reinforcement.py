# -*- coding: utf-8 -*-

from __future__ import division
import sys
from materials.sia262 import SIA262_materials
from materials.sia262 import SIA262_limit_state_checking
import math

concrete= SIA262_materials.c30_37
concreteCover= 40e-3
rebarSpacing= 150e-3
deckThickness= 0.40
wallsThickness= 0.30
slabsThickness= 0.30

numberOfRebarsByLayer= 1/0.15

deckAsTraction= SIA262_limit_state_checking.MinReinfAreaUnderTension(concrete,'B',rebarSpacing,deckThickness)
deckTractionBarDiameter= 16e-3
deckTractionBarsArea= math.pi*(deckTractionBarDiameter/2.0)**2*2*numberOfRebarsByLayer
deckAsFlexion= SIA262_limit_state_checking.MinReinfAreaUnderFlexion(concrete,concreteCover,'C',rebarSpacing,deckThickness)
deckFlexionBarDiameter= 16e-3
deckFlexionBarsArea= math.pi*(deckFlexionBarDiameter/2.0)**2*numberOfRebarsByLayer
deckAsFlexion= SIA262_limit_state_checking.MinReinfAreaUnderFlexion(concrete,concreteCover,'C',rebarSpacing,deckThickness)

wallsAsTraction= SIA262_limit_state_checking.MinReinfAreaUnderTension(concrete,'B',rebarSpacing,wallsThickness)
wallsTractionBarDiameter= 14e-3
wallsTractionBarsArea= math.pi*(wallsTractionBarDiameter/2.0)**2*2*numberOfRebarsByLayer
wallsAsFlexion= SIA262_limit_state_checking.MinReinfAreaUnderFlexion(concrete,concreteCover,'C',rebarSpacing,wallsThickness)
wallsFlexionBarDiameter= 14e-3
wallsFlexionBarsArea= math.pi*(wallsFlexionBarDiameter/2.0)**2*numberOfRebarsByLayer
wallsAsFlexion= SIA262_limit_state_checking.MinReinfAreaUnderFlexion(concrete,concreteCover,'C',rebarSpacing,wallsThickness)

slabsAsTraction= SIA262_limit_state_checking.MinReinfAreaUnderTension(concrete,'B',rebarSpacing,slabsThickness)
slabsTractionBarDiameter= 14e-3
slabsTractionBarsArea= math.pi*(slabsTractionBarDiameter/2.0)**2*2*numberOfRebarsByLayer
slabsAsFlexion= SIA262_limit_state_checking.MinReinfAreaUnderFlexion(concrete,concreteCover,'C',rebarSpacing,slabsThickness)
slabsFlexionBarDiameter= 12e-3
slabsFlexionBarsArea= math.pi*(slabsFlexionBarDiameter/2.0)**2*numberOfRebarsByLayer
slabsAsFlexion= SIA262_limit_state_checking.MinReinfAreaUnderFlexion(concrete,concreteCover,'C',rebarSpacing,slabsThickness)


print 'Slabs minimum reinforcement:'
print '    longitudinal: ', slabsAsTraction*1e6, ' mm2'
print '      number of bars: ', 2*numberOfRebarsByLayer
print '      barDiameter: ', slabsTractionBarDiameter*1e3, ' mm'
print '      reinforcement area: ', slabsTractionBarsArea*1e6, ' mm2'
print '      capacity factor: ', slabsAsTraction/slabsTractionBarsArea
#print "    Num. barres par diamêtre: ", SIA262_materials.numBars(slabsAsTraction) 
print '    transverse: ', slabsAsFlexion*1e6, ' mm2'
print '      number of bars: ', numberOfRebarsByLayer
print '      barDiameter: ', slabsFlexionBarDiameter*1e3, ' mm'
print '      reinforcement area: ', slabsFlexionBarsArea*1e6, ' mm2'
print '      capacity factor: ', slabsAsFlexion/slabsFlexionBarsArea
#print "    Num. barres par diamêtre: ", SIA262_materials.numBars(slabsAsFlexion)

print 'Walls minimum reinforcement:'
print '    longitudinal: ', wallsAsTraction*1e6, ' mm2'
print '      number of bars: ', 2*numberOfRebarsByLayer
print '      barDiameter: ', wallsTractionBarDiameter*1e3, ' mm'
print '      reinforcement area: ', wallsTractionBarsArea*1e6, ' mm2'
print '      capacity factor: ', wallsAsTraction/wallsTractionBarsArea
#print "    Num. barres par diamêtre: ", SIA262_materials.numBars(wallsAsTraction) 
print '    transverse: ', wallsAsFlexion*1e6, ' mm2'
print '      number of bars: ', numberOfRebarsByLayer
print '      barDiameter: ', wallsFlexionBarDiameter*1e3, ' mm'
print '      reinforcement area: ', wallsFlexionBarsArea*1e6, ' mm2'
print '      capacity factor: ', wallsAsFlexion/wallsFlexionBarsArea
#print "    Num. barres par diamêtre: ", SIA262_materials.numBars(wallsAsFlexion)

print 'Deck minimum reinforcement:'
print '    longitudinal: ', deckAsTraction*1e6, ' mm2'
print '      number of bars: ', 2*numberOfRebarsByLayer
print '      barDiameter: ', deckTractionBarDiameter*1e3, ' mm'
print '      reinforcement area: ', deckTractionBarsArea*1e6, ' mm2'
print '      capacity factor: ', deckAsTraction/deckTractionBarsArea
#print "    Num. barres par diamêtre: ", SIA262_materials.numBars(deckAsTraction) 
print '    transverse: ', deckAsFlexion*1e6, ' mm2'
print '      number of bars: ', numberOfRebarsByLayer
print '      barDiameter: ', deckFlexionBarDiameter*1e3, ' mm'
print '      reinforcement area: ', deckFlexionBarsArea*1e6, ' mm2'
print '      capacity factor: ', deckAsFlexion/deckFlexionBarsArea
#print "    Num. barres par diamêtre: ", SIA262_materials.numBars(deckAsFlexion)
