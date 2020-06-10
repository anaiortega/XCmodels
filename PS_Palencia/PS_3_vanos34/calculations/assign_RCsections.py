# -*- coding: utf-8 -*-
import os
from postprocess import RC_material_distribution
from postprocess import element_section_map

# Reinforced concrete material distribution over the elements of the FE model.
# Concrete of type concrete01 with no tension branch

execfile("../model_gen.py") #FE model generation
execfile("../arm_def.py") #FE model generation

#RC-sections definition file.
execfile(path_model_slab_bridge+"RC_sections_def.py")
if abutment.lower()[0]=='y':
    execfile('../arm_abutment_def.py')
    execfile(path_model_abutment+'RC_sections_def.py')

#list of RC sections (from those whose attributes (materials, geometry, refinforcement, set of elements to which apply, ... are defined in the file 'RC_sections_def.py') that we want to process in order to run different limit-state checkings.
lstOfSectRecords=losaRCSects+cartIntRCSects+cartExtRCSects+volIntRCSects+volExtRCSects+[RestrRCSects]+[pilasRCSects]
if abutment.lower()[0]=='y':
    lstOfSectRecords+=estriboRCSects

reinfConcreteSectionDistribution= RC_material_distribution.RCMaterialDistribution()
sections= reinfConcreteSectionDistribution.sectionDefinition #sections container


#Generation of 2 fiber sections (1 and 2 direction) for each record in list
#lstOfSectRecords. Inclusion of these section-groups in the sections container
for secRec in lstOfSectRecords:
    sections.append(secRec)

########
for sect in lstOfSectRecords:
    print
    print 'section= ',sect.name,' thickness= ',sect.depth
    print 'Aspos1= ', sect.getAspos(0),' Aspos2= ', sect.getAspos(1), ' Asneg1= ', sect.getAsneg(0),' Aspos2= ', sect.getAsneg(1)
    print 'AshearReinfY1=', sect.dir1ShReinfY.getAs(), ' AshearReinfY2=', sect.dir2ShReinfY.getAs(), ' AshearReinfZ1=', sect.dir1ShReinfZ.getAs(), ' AshearReinfZ2=', sect.dir2ShReinfZ.getAs()
    
########
#Generation of the distribution of material extended to the elements of the
#FE model, assigning to each element the section-group that corresponds to it
for secRec in lstOfSectRecords:
    elset=prep.getSets.getSet(secRec.elemSetName)
    reinfConcreteSectionDistribution.assign(elemSet=elset.getElements,setRCSects=secRec)

reinfConcreteSectionDistribution.dump()

