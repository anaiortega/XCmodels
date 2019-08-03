import os
import xc_base
import geom
import xc
import math
from model import predefined_spaces
from model.geometry import grid_model as gm
from model.mesh import finit_el_model as fem
from model.boundary_cond import spring_bound_cond as sprbc
from model.sets import sets_mng as sets
from materials import typical_materials as tm
from materials.ec2 import EC2_materials
from materials.ehe import EHE_materials

execfile('data_test_sect04.py')

eSize= 0.1     #length of elements

#             *** GEOMETRIC model (points, lines, surfaces) - SETS ***
FEcase= xc.FEProblem()
preprocessor=FEcase.getPreprocessor
prep=preprocessor   #short name
nodes= prep.getNodeHandler
elements= prep.getElementHandler
elements.dimElem= 3 # Dimension of element space
# Problem type
modelSpace= predefined_spaces.StructuralMechanics3D(nodes) #Defines the 
#dimension of the space: nodes by three coordinates (x,y,z) and 
#six DOF for each node (Ux,Uy,Uz,thetaX,thetaY,thetaZ)

beamSet=prep.getSets.defSet('beamSet')
# points
points=prep.getMultiBlockTopology.getPoints
pnt1=points.newPntIDPos3d(1,geom.Pos3d(0,0,0)) #start point
pnt2=points.newPntIDPos3d(2,geom.Pos3d(Lbeam,0,0)) #end point
beamSet.getPoints.append(pnt1)
beamSet.getPoints.append(pnt2)

#lines
lines= prep.getMultiBlockTopology.getLines
lines.defaultTag=1
ln1=lines.newLine(1,2)
beamSet.getLines.append(ln1)

#materials
concrete=EC2_materials.C30 #concrete according to EC2 fck=33 MPa
reinfSteel=EC2_materials.S450C #reinforcing steel according to EC2 fyk=450 MPa
concrete=EHE_materials.HA30 #concrete according to EC2 fck=33 MPa

concrdat=tm.MaterialData(name='concrdat',E=concrete.Ecm(),nu=0.2,rho=2500)

#Geometric sections
#rectangular sections
from materials.sections import section_properties as sectpr
geomSectBeam=sectpr.RectangularSection(name='geomSectBeam',b=width,h=depth)

# Elastic material-section appropiate for 3D beam analysis, including shear
  # deformations.
beam_mat= tm.BeamMaterialData(name= 'beam_mat', section=geomSectBeam, material=concrdat)
beam_mat.setupElasticShear3DSection(preprocessor=prep)

#                         ***FE model - MESH***

beam_mesh=fem.LinSetToMesh(linSet=beamSet,matSect=beam_mat,elemSize=eSize,vDirLAxZ=xc.Vector([0,-1,0]),elemType='ElasticBeam3d',dimElemSpace=3,coordTransfType='linear')
beam_mesh.generateMesh(prep)    # mesh this set of lines

#                       ***BOUNDARY CONDITIONS***
n1=pnt1.getNode()
modelSpace.fixNode('FFF_FFF',n1.tag)
n2=pnt2.getNode()
modelSpace.fixNode('FFF_FFF',n2.tag)

#                       ***ACTIONS***
from actions import loads
#Uniform load on beams
totalLoadBeam=loads.UniformLoadOnBeams(name='totalLoadBeam', xcSet=beamSet, loadVector=fUnif,refSystem='Global')
halfLoadBeam=loads.UniformLoadOnBeams(name='halfLoadBeam', xcSet=beamSet, loadVector=fUnif*0.5,refSystem='Global')

#    ***LOAD CASES***
from actions import load_cases as lcases
lcase01=lcases.LoadCase(preprocessor=prep,name="lcase01",loadPType="default",timeSType="constant_ts")
lcase01.create()
lcase01.addLstLoads([totalLoadBeam])

lcase02=lcases.LoadCase(preprocessor=prep,name="lcase02",loadPType="default",timeSType="constant_ts")
lcase02.create()
lcase02.addLstLoads([halfLoadBeam])


from postprocess.xcVtk.FE_model import quick_graphics as QGrph


#    ***LIMIT STATE COMBINATIONS***
from actions import combinations as cc
combContainer= cc.CombContainer()  #Container of load combinations
#Frequent combinations.
combContainer.SLS.freq.add('ELSF01', '1.0*lcase01')
combContainer.SLS.freq.add('ELSF02', '1.0*lcase02')

# Reinforced concrete sections
from materials.sections.fiber_section import defSimpleRCSection
beamRCsect=defSimpleRCSection.RecordRCSlabBeamSection(name='beamRCsect',sectionDescr='beam',concrType=concrete, reinfSteelType=reinfSteel,width=width,depth=depth,elemSetName='beamSet')
mainBottReinf=defSimpleRCSection.MainReinfLayer(rebarsDiam=fiBott,areaRebar=math.pi*fiBott**2/4.,width=width,nominalCover=cover)
mainBottReinf.nRebars=nmbBarsBott
beamRCsect.dir1NegatvRebarRows=[mainBottReinf]
beamRCsect.dir2NegatvRebarRows=[mainBottReinf]

#Assigning of sections
from postprocess import RC_material_distribution
from postprocess import element_section_map

# Reinforced concrete material distribution over the elements of the FE model.
# Concrete of type concrete01 with no tension branch
reinfConcreteSectionDistribution= RC_material_distribution.RCMaterialDistribution()
sections= reinfConcreteSectionDistribution.sectionDefinition #sections container
beamRCsect.creaTwoSections()
sections.append(beamRCsect)
#Generation of the distribution of material extended to the elements of the
#FE model, assigning to each element the section-group that corresponds to it
elset=prep.getSets.getSet(beamRCsect.elemSetName)
reinfConcreteSectionDistribution.assign(elemSet=elset.elements,setRCSects=beamRCsect)
reinfConcreteSectionDistribution.dump()

#Calculation of internal forces
from postprocess import limit_state_data as lsd
lsd.LimitStateData.internal_forces_results_directory= './'
reinfConcreteSections= RC_material_distribution.loadRCMaterialDistribution()
loadCombinations= prep.getLoadHandler.getLoadCombinations
ls=lsd.freqLoadsCrackControl
ls.saveAll(FEcase,combContainer,beamSet)

