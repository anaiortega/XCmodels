# -*- coding: utf-8 -*-

import math
import os
import xc_base
import geom
import xc
# Macros
#from materials.ehe import auxEHE
from materials.sections.fiber_section import defSimpleRCSection
from materials.sections import section_properties
from postprocess import RC_material_distribution


from materials.aci import ACI_materials

from postprocess import limit_state_data as lsd
from postprocess import element_section_map


concrete= ACI_materials.c3500
reinfSteel= ACI_materials.A615G60
#Define available sections for the elements (spatial distribution of RC sections).
reinfConcreteSectionDistribution= RC_material_distribution.RCMaterialDistribution()
sections= reinfConcreteSectionDistribution.sectionDefinition

#Generic layers (rows of rebars)
n2s150r45=defSimpleRCSection.MainReinfLayer(rebarsDiam=ACI_materials.standard_bars_diameters['#2'],areaRebar= ACI_materials.standard_bars_areas['#2'],rebarsSpacing= 0.150,width=1.0,nominalCover= 0.045)
n2s150r50=defSimpleRCSection.MainReinfLayer(rebarsDiam=ACI_materials.standard_bars_diameters['#2'],areaRebar= ACI_materials.standard_bars_areas['#2'],rebarsSpacing= 0.150,width=1.0,nominalCover=0.050)

n3s150r45=defSimpleRCSection.MainReinfLayer(rebarsDiam=ACI_materials.standard_bars_diameters['#3'],areaRebar= ACI_materials.standard_bars_areas['#3'],rebarsSpacing= 0.150,width=1.0,nominalCover= 0.045)
n3s150r50=defSimpleRCSection.MainReinfLayer(rebarsDiam=ACI_materials.standard_bars_diameters['#3'],areaRebar= ACI_materials.standard_bars_areas['#3'],rebarsSpacing= 0.150,width=1.0,nominalCover=0.050)

n4s150r45=defSimpleRCSection.MainReinfLayer(rebarsDiam=ACI_materials.standard_bars_diameters['#4'],areaRebar= ACI_materials.standard_bars_areas['#4'],rebarsSpacing= 0.150,width=1.0,nominalCover=0.040)
n4s150r50=defSimpleRCSection.MainReinfLayer(rebarsDiam=ACI_materials.standard_bars_diameters['#4'],areaRebar= ACI_materials.standard_bars_areas['#4'],rebarsSpacing= 0.150,width=1.0,nominalCover=0.050)

n5s150r45=defSimpleRCSection.MainReinfLayer(rebarsDiam=ACI_materials.standard_bars_diameters['#5'],areaRebar= ACI_materials.standard_bars_areas['#5'],rebarsSpacing= 0.150,width=1.0,nominalCover= 0.045)
n5s150r50=defSimpleRCSection.MainReinfLayer(rebarsDiam=ACI_materials.standard_bars_diameters['#5'],areaRebar= ACI_materials.standard_bars_areas['#5'],rebarsSpacing= 0.150,width=1.0,nominalCover= 0.050)

n6s150r45=defSimpleRCSection.MainReinfLayer(rebarsDiam=ACI_materials.standard_bars_diameters['#6'],areaRebar= ACI_materials.standard_bars_areas['#6'],rebarsSpacing= 0.150,width=1.0,nominalCover= 0.045)
n6s150r50=defSimpleRCSection.MainReinfLayer(rebarsDiam=ACI_materials.standard_bars_diameters['#6'],areaRebar= ACI_materials.standard_bars_areas['#6'],rebarsSpacing= 0.150,width=1.0,nominalCover= 0.050)

n7s150r45=defSimpleRCSection.MainReinfLayer(rebarsDiam=ACI_materials.standard_bars_diameters['#7'],areaRebar= ACI_materials.standard_bars_areas['#7'],rebarsSpacing= 0.150,width=1.0,nominalCover= 0.045)
n7s150r50=defSimpleRCSection.MainReinfLayer(rebarsDiam=ACI_materials.standard_bars_diameters['#7'],areaRebar= ACI_materials.standard_bars_areas['#7'],rebarsSpacing= 0.150,width=1.0,nominalCover= 0.050)

n8s150r45=defSimpleRCSection.MainReinfLayer(rebarsDiam=ACI_materials.standard_bars_diameters['#8'],areaRebar= ACI_materials.standard_bars_areas['#8'],rebarsSpacing= 0.150,width=1.0,nominalCover= 0.045)
n8s150r50=defSimpleRCSection.MainReinfLayer(rebarsDiam=ACI_materials.standard_bars_diameters['#8'],areaRebar= ACI_materials.standard_bars_areas['#8'],rebarsSpacing= 0.150,width=1.0,nominalCover= 0.050)

n9s150r45=defSimpleRCSection.MainReinfLayer(rebarsDiam=ACI_materials.standard_bars_diameters['#9'],areaRebar= ACI_materials.standard_bars_areas['#9'],rebarsSpacing= 0.150,width=1.0,nominalCover= 0.045)
n9s150r50=defSimpleRCSection.MainReinfLayer(rebarsDiam=ACI_materials.standard_bars_diameters['#9'],areaRebar= ACI_materials.standard_bars_areas['#9'],rebarsSpacing= 0.150,width=1.0,nominalCover=0.050)

n10s150r45=defSimpleRCSection.MainReinfLayer(rebarsDiam=ACI_materials.standard_bars_diameters['#10'],areaRebar= ACI_materials.standard_bars_areas['#10'],rebarsSpacing= 0.150,width=1.0,nominalCover= 0.045)
n10s150r50=defSimpleRCSection.MainReinfLayer(rebarsDiam=ACI_materials.standard_bars_diameters['#10'],areaRebar= ACI_materials.standard_bars_areas['#10'],rebarsSpacing= 0.150,width=1.0,nominalCover= 0.050)

n2s300r45=defSimpleRCSection.MainReinfLayer(rebarsDiam=ACI_materials.standard_bars_diameters['#2'],areaRebar= ACI_materials.standard_bars_areas['#2'],rebarsSpacing= 0.300,width=1.0,nominalCover= 0.045)
n2s300r50=defSimpleRCSection.MainReinfLayer(rebarsDiam=ACI_materials.standard_bars_diameters['#2'],areaRebar= ACI_materials.standard_bars_areas['#2'],rebarsSpacing= 0.300,width=1.0,nominalCover=0.050)

n3s300r45=defSimpleRCSection.MainReinfLayer(rebarsDiam=ACI_materials.standard_bars_diameters['#3'],areaRebar= ACI_materials.standard_bars_areas['#3'],rebarsSpacing= 0.300,width=1.0,nominalCover= 0.045)
n3s300r50=defSimpleRCSection.MainReinfLayer(rebarsDiam=ACI_materials.standard_bars_diameters['#3'],areaRebar= ACI_materials.standard_bars_areas['#3'],rebarsSpacing= 0.300,width=1.0,nominalCover=0.050)

n4s300r45=defSimpleRCSection.MainReinfLayer(rebarsDiam=ACI_materials.standard_bars_diameters['#4'],areaRebar= ACI_materials.standard_bars_areas['#4'],rebarsSpacing= 0.300,width=1.0,nominalCover=0.040)
n4s300r50=defSimpleRCSection.MainReinfLayer(rebarsDiam=ACI_materials.standard_bars_diameters['#4'],areaRebar= ACI_materials.standard_bars_areas['#4'],rebarsSpacing= 0.300,width=1.0,nominalCover=0.050)

n5s300r45=defSimpleRCSection.MainReinfLayer(rebarsDiam=ACI_materials.standard_bars_diameters['#5'],areaRebar= ACI_materials.standard_bars_areas['#5'],rebarsSpacing= 0.300,width=1.0,nominalCover= 0.045)
n5s300r50=defSimpleRCSection.MainReinfLayer(rebarsDiam=ACI_materials.standard_bars_diameters['#5'],areaRebar= ACI_materials.standard_bars_areas['#5'],rebarsSpacing= 0.300,width=1.0,nominalCover= 0.050)

n6s300r45=defSimpleRCSection.MainReinfLayer(rebarsDiam=ACI_materials.standard_bars_diameters['#6'],areaRebar= ACI_materials.standard_bars_areas['#6'],rebarsSpacing= 0.300,width=1.0,nominalCover= 0.045)
n6s300r50=defSimpleRCSection.MainReinfLayer(rebarsDiam=ACI_materials.standard_bars_diameters['#6'],areaRebar= ACI_materials.standard_bars_areas['#6'],rebarsSpacing= 0.300,width=1.0,nominalCover= 0.050)

n7s300r45=defSimpleRCSection.MainReinfLayer(rebarsDiam=ACI_materials.standard_bars_diameters['#7'],areaRebar= ACI_materials.standard_bars_areas['#7'],rebarsSpacing= 0.300,width=1.0,nominalCover= 0.045)
n7s300r50=defSimpleRCSection.MainReinfLayer(rebarsDiam=ACI_materials.standard_bars_diameters['#7'],areaRebar= ACI_materials.standard_bars_areas['#7'],rebarsSpacing= 0.300,width=1.0,nominalCover= 0.050)

n8s300r45=defSimpleRCSection.MainReinfLayer(rebarsDiam=ACI_materials.standard_bars_diameters['#8'],areaRebar= ACI_materials.standard_bars_areas['#8'],rebarsSpacing= 0.300,width=1.0,nominalCover= 0.045)
n8s300r50=defSimpleRCSection.MainReinfLayer(rebarsDiam=ACI_materials.standard_bars_diameters['#8'],areaRebar= ACI_materials.standard_bars_areas['#8'],rebarsSpacing= 0.300,width=1.0,nominalCover= 0.050)

n9s300r45=defSimpleRCSection.MainReinfLayer(rebarsDiam=ACI_materials.standard_bars_diameters['#9'],areaRebar= ACI_materials.standard_bars_areas['#9'],rebarsSpacing= 0.300,width=1.0,nominalCover= 0.045)
n9s300r50=defSimpleRCSection.MainReinfLayer(rebarsDiam=ACI_materials.standard_bars_diameters['#9'],areaRebar= ACI_materials.standard_bars_areas['#9'],rebarsSpacing= 0.300,width=1.0,nominalCover=0.050)

n10s300r45=defSimpleRCSection.MainReinfLayer(rebarsDiam=ACI_materials.standard_bars_diameters['#10'],areaRebar= ACI_materials.standard_bars_areas['#10'],rebarsSpacing= 0.300,width=1.0,nominalCover= 0.045)
n10s300r50=defSimpleRCSection.MainReinfLayer(rebarsDiam=ACI_materials.standard_bars_diameters['#10'],areaRebar= ACI_materials.standard_bars_areas['#10'],rebarsSpacing= 0.300,width=1.0,nominalCover= 0.050)

sectA1= defSimpleRCSection.RecordRCSlabBeamSection(name='A1_sections',sectionDescr="A1 footing sections.",concrType=concrete, reinfSteelType=reinfSteel,depth=0.5008)
sectA2= defSimpleRCSection.RecordRCSlabBeamSection(name='A2_sections',sectionDescr="A2 footing sections.",concrType=concrete, reinfSteelType=reinfSteel,depth=0.5008)
sectA3= defSimpleRCSection.RecordRCSlabBeamSection(name='A3_sections',sectionDescr="A3 footing sections.",concrType=concrete, reinfSteelType=reinfSteel,depth=0.5008)
sectA4= defSimpleRCSection.RecordRCSlabBeamSection(name='A4_sections',sectionDescr="A4 footing sections.",concrType=concrete, reinfSteelType=reinfSteel,depth=0.5008)
sectA5= defSimpleRCSection.RecordRCSlabBeamSection(name='A5_sections',sectionDescr="A5 footing sections.",concrType=concrete, reinfSteelType=reinfSteel,depth=0.5008)
sectB1= defSimpleRCSection.RecordRCSlabBeamSection(name='B1_sections',sectionDescr="B1 footing sections.",concrType=concrete, reinfSteelType=reinfSteel,depth=0.5008)
sectB2= defSimpleRCSection.RecordRCSlabBeamSection(name='B2_sections',sectionDescr="B2 footing sections.",concrType=concrete, reinfSteelType=reinfSteel,depth=0.5008)
sectB3= defSimpleRCSection.RecordRCSlabBeamSection(name='B3_sections',sectionDescr="B3 footing sections.",concrType=concrete, reinfSteelType=reinfSteel,depth=0.5008)
sectB4= defSimpleRCSection.RecordRCSlabBeamSection(name='B4_sections',sectionDescr="B4 footing sections.",concrType=concrete, reinfSteelType=reinfSteel,depth=0.5008)
sectB5= defSimpleRCSection.RecordRCSlabBeamSection(name='B5_sections',sectionDescr="B5 footing sections.",concrType=concrete, reinfSteelType=reinfSteel,depth=0.5008)
sectC1= defSimpleRCSection.RecordRCSlabBeamSection(name='C1_sections',sectionDescr="C1 footing sections.",concrType=concrete, reinfSteelType=reinfSteel,depth=0.635)
sectC2= defSimpleRCSection.RecordRCSlabBeamSection(name='C2_sections',sectionDescr="C2 footing sections.",concrType=concrete, reinfSteelType=reinfSteel,depth=0.635)
sectC3= defSimpleRCSection.RecordRCSlabBeamSection(name='C3_sections',sectionDescr="C3 footing sections.",concrType=concrete, reinfSteelType=reinfSteel,depth=0.635)
sectC4= defSimpleRCSection.RecordRCSlabBeamSection(name='C4_sections',sectionDescr="C4 footing sections.",concrType=concrete, reinfSteelType=reinfSteel,depth=0.635)
sectC5= defSimpleRCSection.RecordRCSlabBeamSection(name='C5_sections',sectionDescr="C5 footing sections.",concrType=concrete, reinfSteelType=reinfSteel,depth=0.635)
sectD1= defSimpleRCSection.RecordRCSlabBeamSection(name='D1_sections',sectionDescr="D1 footing sections.",concrType=concrete, reinfSteelType=reinfSteel,depth=0.635)
sectD2= defSimpleRCSection.RecordRCSlabBeamSection(name='D2_sections',sectionDescr="D2 footing sections.",concrType=concrete, reinfSteelType=reinfSteel,depth=0.635)
sectD3= defSimpleRCSection.RecordRCSlabBeamSection(name='D3_sections',sectionDescr="D3 footing sections.",concrType=concrete, reinfSteelType=reinfSteel,depth=0.635)
sectD4= defSimpleRCSection.RecordRCSlabBeamSection(name='D4_sections',sectionDescr="D4 footing sections.",concrType=concrete, reinfSteelType=reinfSteel,depth=0.635)
sectD5= defSimpleRCSection.RecordRCSlabBeamSection(name='D5_sections',sectionDescr="D5 footing sections.",concrType=concrete, reinfSteelType=reinfSteel,depth=0.635)
sectG1= defSimpleRCSection.RecordRCSlabBeamSection(name='G1_sections',sectionDescr="G1 footing sections.",concrType=concrete, reinfSteelType=reinfSteel,depth=0.635)
sectG2= defSimpleRCSection.RecordRCSlabBeamSection(name='G2_sections',sectionDescr="G2 footing sections.",concrType=concrete, reinfSteelType=reinfSteel,depth=0.635)
sectG3= defSimpleRCSection.RecordRCSlabBeamSection(name='G3_sections',sectionDescr="G3 footing sections.",concrType=concrete, reinfSteelType=reinfSteel,depth=0.635)
sectG4= defSimpleRCSection.RecordRCSlabBeamSection(name='G4_sections',sectionDescr="G4 footing sections.",concrType=concrete, reinfSteelType=reinfSteel,depth=0.635)
sectG5= defSimpleRCSection.RecordRCSlabBeamSection(name='G5_sections',sectionDescr="G5 footing sections.",concrType=concrete, reinfSteelType=reinfSteel,depth=0.635)
sectF1= defSimpleRCSection.RecordRCSlabBeamSection(name='F1_sections',sectionDescr="F1 footing sections.",concrType=concrete, reinfSteelType=reinfSteel,depth=0.635)
sectF2= defSimpleRCSection.RecordRCSlabBeamSection(name='F2_sections',sectionDescr="F2 footing sections.",concrType=concrete, reinfSteelType=reinfSteel,depth=0.635)
sectF3= defSimpleRCSection.RecordRCSlabBeamSection(name='F3_sections',sectionDescr="F3 footing sections.",concrType=concrete, reinfSteelType=reinfSteel,depth=0.635)
sectF4= defSimpleRCSection.RecordRCSlabBeamSection(name='F4_sections',sectionDescr="F4 footing sections.",concrType=concrete, reinfSteelType=reinfSteel,depth=0.635)
sectF5= defSimpleRCSection.RecordRCSlabBeamSection(name='F5_sections',sectionDescr="F5 footing sections.",concrType=concrete, reinfSteelType=reinfSteel,depth=0.635)

rcSects= dict()

rcSects['A1']= sectA1; rcSects['A2']= sectA2; rcSects['A3']= sectA3; rcSects['A4']= sectA4; rcSects['A5']= sectA5; rcSects['B1']= sectB1; rcSects['B2']= sectB2; rcSects['B3']= sectB3; rcSects['B4']= sectB4; rcSects['B5']= sectB5; rcSects['C1']= sectC1; rcSects['C2']= sectC2; rcSects['C3']= sectC3; rcSects['C4']= sectC4; rcSects['C5']= sectC5; rcSects['D1']= sectD1; rcSects['D2']= sectD2; rcSects['D3']= sectD3; rcSects['D4']= sectD4; rcSects['D5']= sectD5; rcSects['G1']= sectG1; rcSects['G2']= sectG2; rcSects['G3']= sectG3; rcSects['G4']= sectG4; rcSects['G5']= sectG5; rcSects['F1']= sectF1; rcSects['F2']= sectF2; rcSects['F3']= sectF3; rcSects['F4']= sectF4; rcSects['F5']= sectF5

for key in ['A1','A2','B1','B2']:
    rcS= rcSects[key]
    rcS.dir1PositvRebarRows=[n2s300r50]
    rcS.dir1NegatvRebarRows=[n7s300r50]
    rcS.dir2PositvRebarRows=[n2s300r45]
    rcS.dir2NegatvRebarRows=[n7s300r45]

for key in ['A3','A4','A5','B3','B4','B5']:
    rcS= rcSects[key]
    rcS.dir1PositvRebarRows=[n2s300r50]
    rcS.dir1NegatvRebarRows=[n8s300r50]
    rcS.dir2PositvRebarRows=[n2s300r45]
    rcS.dir2NegatvRebarRows=[n8s300r45]

for key in ['C1','D1','G1']:
    rcS= rcSects[key]
    rcS.dir1PositvRebarRows=[n2s300r50]
    rcS.dir1NegatvRebarRows=[n7s150r50]
    rcS.dir2PositvRebarRows=[n2s300r45]
    rcS.dir2NegatvRebarRows=[n7s150r45]

for key in ['C2','C3','C4','C5','D2','D3','D4','D5']:
    rcS= rcSects[key]
    rcS.dir1PositvRebarRows=[n2s300r50]
    rcS.dir1NegatvRebarRows=[n8s300r50]
    rcS.dir2PositvRebarRows=[n2s300r45]
    rcS.dir2NegatvRebarRows=[n8s300r45]

for key in ['G2','G3','G4','G5']:
    rcS= rcSects[key]
    rcS.dir1PositvRebarRows=[n2s300r50]
    rcS.dir1NegatvRebarRows=[n8s300r50]
    rcS.dir2PositvRebarRows=[n2s300r45]
    rcS.dir2NegatvRebarRows=[n8s300r45]

for key in ['F1','F2','F3','F4','F5']:
    rcS= rcSects[key]
    rcS.dir1PositvRebarRows=[n2s300r50]
    rcS.dir1NegatvRebarRows=[n8s300r50]
    rcS.dir2PositvRebarRows=[n2s300r45]
    rcS.dir2NegatvRebarRows=[n8s300r45]


for key in rcSects:
    rcS= rcSects[key]
    rcS.creaTwoSections()
    sections.append(rcS)
    
footingRCSect= defSimpleRCSection.RecordRCSlabBeamSection(name='footingRCSect',sectionDescr="footing.",concrType=concrete, reinfSteelType=reinfSteel,depth=0.50)
#[0]: longitudinal rebars
#[1]: transversal rebars
footingRCSect.dir1PositvRebarRows=[n2s150r50]
footingRCSect.dir1NegatvRebarRows=[n8s150r50]
footingRCSect.dir2PositvRebarRows=[n2s150r45]
footingRCSect.dir2NegatvRebarRows=[n8s150r45]

footingRCSect.creaTwoSections() 
sections.append(footingRCSect)

