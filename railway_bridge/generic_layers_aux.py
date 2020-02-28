# -*- coding: utf-8 -*-

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
#Generic layers (rows of rebars). Other instance variables that we can define
#for MainReinfLayers are coverLat and nRebars. If we define nRebars that
#value overrides the rebarsSpacing
fi8s125r30=def_simple_RC_section.MainReinfLayer(rebarsDiam=8e-3,areaRebar= areaFi8,rebarsSpacing=0.125,width=1.0,nominalCover=0.030)
fi8s125r44=def_simple_RC_section.MainReinfLayer(rebarsDiam=8e-3,areaRebar= areaFi8,rebarsSpacing=0.125,width=1.0,nominalCover=0.044)
fi10s200r44=def_simple_RC_section.MainReinfLayer(rebarsDiam=10e-3,areaRebar= areaFi10,rebarsSpacing=0.200,width=1.0,nominalCover=0.044)
fi10s250r42=def_simple_RC_section.MainReinfLayer(rebarsDiam=10e-3,areaRebar= areaFi10,rebarsSpacing=0.250,width=1.0,nominalCover=0.042)
fi12s250r30=def_simple_RC_section.MainReinfLayer(rebarsDiam=12e-3,areaRebar= areaFi12,rebarsSpacing=0.250,width=1.0,nominalCover=0.030)
fi12s250r46=def_simple_RC_section.MainReinfLayer(rebarsDiam=12e-3,areaRebar= areaFi12,rebarsSpacing=0.250,width=1.0,nominalCover=0.046)
fi12s150r35=def_simple_RC_section.MainReinfLayer(rebarsDiam=12e-3,areaRebar= areaFi12,rebarsSpacing=0.150,width=1.0,nominalCover=0.035)
fi14s250r30=def_simple_RC_section.MainReinfLayer(rebarsDiam=14e-3,areaRebar= areaFi14,rebarsSpacing=0.25,width=1.0,nominalCover=0.030)
fi14s125r30=def_simple_RC_section.MainReinfLayer(rebarsDiam=14e-3,areaRebar= areaFi14,rebarsSpacing=0.125,width=1.0,nominalCover=0.030)
fi16s125r30=def_simple_RC_section.MainReinfLayer(rebarsDiam=16e-3,areaRebar= areaFi16,rebarsSpacing=0.125,width=1.0,nominalCover=0.030)
fi16s250r50=def_simple_RC_section.MainReinfLayer(rebarsDiam=16e-3,areaRebar= areaFi16,rebarsSpacing=0.250,width=1.0,nominalCover=0.050)
fi16s150r35=def_simple_RC_section.MainReinfLayer(rebarsDiam=16e-3,areaRebar= areaFi16,rebarsSpacing=0.150,width=1.0,nominalCover=0.035)
fi16s250r56=def_simple_RC_section.MainReinfLayer(rebarsDiam=16e-3,areaRebar= areaFi16,rebarsSpacing=0.250,width=1.0,nominalCover=0.056)
fi18s125r30=def_simple_RC_section.MainReinfLayer(rebarsDiam=18e-3,areaRebar= areaFi18,rebarsSpacing=0.125,width=1.0,nominalCover=0.030)
fi18s125r44=def_simple_RC_section.MainReinfLayer(rebarsDiam=18e-3,areaRebar= areaFi18,rebarsSpacing=0.125,width=1.0,nominalCover=0.044)
fi18s150r35=def_simple_RC_section.MainReinfLayer(rebarsDiam=18e-3,areaRebar= areaFi18,rebarsSpacing=0.150,width=1.0,nominalCover=0.035)
fi20s250r30=def_simple_RC_section.MainReinfLayer(rebarsDiam=20e-3,areaRebar= areaFi20,rebarsSpacing=0.250,width=1.0,nominalCover=0.030)
fi20s150r35=def_simple_RC_section.MainReinfLayer(rebarsDiam=20e-3,areaRebar= areaFi20,rebarsSpacing=0.150,width=1.0,nominalCover=0.035)
fi22s150r35=def_simple_RC_section.MainReinfLayer(rebarsDiam=22e-3,areaRebar= areaFi22,rebarsSpacing=0.150,width=1.0,nominalCover=0.035)
fi20s125r30=def_simple_RC_section.MainReinfLayer(rebarsDiam=20e-3,areaRebar= areaFi20,rebarsSpacing=0.125,width=1.0,nominalCover=0.030)
fi20s125r50=def_simple_RC_section.MainReinfLayer(rebarsDiam=20e-3,areaRebar= areaFi20,rebarsSpacing=0.125,width=1.0,nominalCover=0.050)
fi26s250r30=def_simple_RC_section.MainReinfLayer(rebarsDiam=26e-3,areaRebar= areaFi26,rebarsSpacing=0.250,width=1.0,nominalCover=0.030)
fi26s250r50=def_simple_RC_section.MainReinfLayer(rebarsDiam=26e-3,areaRebar= areaFi26,rebarsSpacing=0.250,width=1.0,nominalCover=0.050)
fi26s150r35=def_simple_RC_section.MainReinfLayer(rebarsDiam=26e-3,areaRebar= areaFi26,rebarsSpacing=0.150,width=1.0,nominalCover=0.035)
