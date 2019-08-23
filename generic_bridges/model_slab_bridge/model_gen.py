#             *** GEOMETRIC model (points, lines, surfaces) - SETS***0
FEcase= xc.FEProblem()
preprocessor=FEcase.getPreprocessor
prep=preprocessor   #short name
nodes= prep.getNodeHandler
elements= prep.getElementHandler
elements.dimElem= 3
# Problem type
modelSpace= predefined_spaces.StructuralMechanics3D(nodes) #Defines the
# dimension of the space: nodes by three coordinates (x,y,z) and 
# six DOF for each node (Ux,Uy,Uz,thetaX,thetaY,thetaZ)

# grid model definition (tablero)
gridTabl= gm.GridModel(prep,xListTabl,yListTabl,zListTabl)
# grid model definition (pilas)
gridPil= gm.GridModel(prep,xListPil,yListPil,zListPil)

# Grid geometric entities definition (points, lines, surfaces)
# Points' generation
gridTabl.generatePoints()
gridPil.generatePoints()

#   Surfaces generation (tablero)
#Riostra estribo 1
x=xRiostrEstr[0]
y=yRiostrEstr[0]
z=zLosa[0]
riostrEstr1=gridTabl.genSurfOneXYZRegion(xyzRange=((x[0],y[0],z),(x[-1],y[-1],z)),nameSet='riostrEstr1')
#Riostra estribo 2
x=xRiostrEstr[1]
y=yRiostrEstr[1]
z=zLosa[0]
riostrEstr2=gridTabl.genSurfOneXYZRegion(xyzRange=((x[0],y[0],z),(x[-1],y[-1],z)),nameSet='riostrEstr2')
#Losa
x=xLosa
y=yLosa
z=zLosa[0]
losa=gridTabl.genSurfOneXYZRegion(xyzRange=((x[0],y[0],z),(x[-1],y[-1],z)),nameSet='losa')
#Cartabones
x=xCartab
y=yLosa
z=zLosa[0]
cartabInt=gridTabl.genSurfMultiXYZRegion(lstXYZRange=[((x[0][1],y[0],z),(x[0][-1],y[-1],z)),((x[1][0],y[0],z),(x[1][1],y[-1],z))], nameSet='cartabInt')
cartabExt=gridTabl.genSurfMultiXYZRegion(lstXYZRange=[((x[0][0],y[0],z),(x[0][1],y[-1],z)),((x[1][1],y[0],z),(x[1][-1],y[-1],z))], nameSet='cartabExt')
#Voladizos
x=xVoladz
y=yLosa
z=zLosa[0]
voladzInt=gridTabl.genSurfMultiXYZRegion(lstXYZRange=[((x[0][1],y[0],z),(x[0][-1],y[-1],z)),((x[1][0],y[0],z),(x[1][1],y[-1],z))], nameSet='voladzInt')
voladzExt=gridTabl.genSurfMultiXYZRegion(lstXYZRange=[((x[0][0],y[0],z),(x[0][1],y[-1],z)),((x[1][1],y[0],z),(x[1][-1],y[-1],z))], nameSet='voladzExt')

#Lines generation (Pilas)
x=xPil
y=yPil
z=zPil
#A barlovento
xyzRang=list()
for j in range(len(y)):
    k=j
    i=0
    xyzRang.append([(x[i],y[j],z[k][0]),(x[i],y[j],z[k][-1])])

pilasBarlov=gridPil.genLinMultiXYZRegion(lstXYZRange=xyzRang, nameSet='pilasBarlov')
if len(x)>1:
    xyzRang=list()
    for j in range(len(y)):
        k=j
        for i in range(1,len(x)):
            xyzRang.append([(x[i],y[j],z[k][0]),(x[i],y[j],z[k][-1])])
    pilasSotav=gridPil.genLinMultiXYZRegion(lstXYZRange=xyzRang, nameSet='pilasSotav')
else:
    pilasSotav=None


#                         *** MATERIALS *** 
concrProp=tm.MaterialData(name='concrProp',E=concrete.Ecm(),nu=concrete.nuc,rho=concrete.density())
# Isotropic elastic section-material appropiate for plate and shell analysis
riostrEstr_mat=tm.DeckMaterialData(name='riostrEstr_mat_mat',thickness= cantoRiostrEstr,material=concrProp)
riostrEstr_mat.setupElasticSection(preprocessor=prep) 
losa_mat=tm.DeckMaterialData(name='losa_mat',thickness= cantoLosa,material=concrProp)
losa_mat.setupElasticSection(preprocessor=prep) 
cartabInt_mat=tm.DeckMaterialData(name='cartabInt_mat',thickness=eCartInt,material=concrProp)
cartabInt_mat.setupElasticSection(preprocessor=prep) 
cartabExt_mat=tm.DeckMaterialData(name='cartabExt_mat',thickness=eCartExt,material=concrProp)
cartabExt_mat.setupElasticSection(preprocessor=prep) 
voladzInt_mat=tm.DeckMaterialData(name='voladzInt_mat',thickness=eVolInt,material=concrProp)
voladzInt_mat.setupElasticSection(preprocessor=prep) 
voladzExt_mat=tm.DeckMaterialData(name='voladzExt_mat',thickness=eVolExt,material=concrProp)
voladzExt_mat.setupElasticSection(preprocessor=prep) 

#Geometric sections
#rectangular sections
from materials.sections import section_properties as sectpr
geomSectPilas=sectpr.RectangularSection(name='geomSectPilas',b=lRectEqPila,h=lRectEqPila)
# Elastic material-section appropiate for 3D beam analysis, including shear
  # deformations.
  # Attributes:
  #   name:         name identifying the section
  #   section:      instance of a class that defines the geometric and
  #                 mechanical characteristiscs
  #                 of a section (e.g: RectangularSection, CircularSection,
  #                 ISection, ...)
  #   material:     instance of a class that defines the elastic modulus,
  #                 shear modulus and mass density of the material

pilas_mat= tm.BeamMaterialData(name= 'pilas_mat', section=geomSectPilas, material=concrProp)
pilas_mat.setupElasticShear3DSection(preprocessor=prep)

# Elastomeric bearings.
from materials import bridge_bearings as bb
neopr=bb.ElastomericBearing(G=Gneopr,a=aNeopr,b=bNeopr,e=hNetoNeopr)
neopr.defineMaterials(prep)

#                         ***FE model - MESH***
# IMPORTANT: it's convenient to generate the mesh of surfaces before meshing
# the lines, otherwise, sets of shells can take also beam elements touched by
# them

pilasBarlov_mesh=fem.LinSetToMesh(linSet=pilasBarlov,matSect=pilas_mat,elemSize=eSize,vDirLAxZ=xc.Vector([0,1,0]),elemType='ElasticBeam3d',dimElemSpace=3,coordTransfType='linear')
if pilasSotav:
    pilasSotav_mesh=fem.LinSetToMesh(linSet=pilasSotav,matSect=pilas_mat,elemSize=eSize,vDirLAxZ=xc.Vector([0,1,0]),elemType='ElasticBeam3d',dimElemSpace=3,coordTransfType='linear')

riostrEstr1_mesh=fem.SurfSetToMesh(surfSet=riostrEstr1,matSect=riostrEstr_mat,elemSize=eSize,elemType='ShellMITC4')
riostrEstr2_mesh=fem.SurfSetToMesh(surfSet=riostrEstr2,matSect=riostrEstr_mat,elemSize=eSize,elemType='ShellMITC4')
losa_mesh=fem.SurfSetToMesh(surfSet=losa,matSect=losa_mat,elemSize=eSize,elemType='ShellMITC4')
cartabInt_mesh=fem.SurfSetToMesh(surfSet=cartabInt,matSect=cartabInt_mat,elemSize=eSize,elemType='ShellMITC4')
cartabExt_mesh=fem.SurfSetToMesh(surfSet=cartabExt,matSect=cartabExt_mat,elemSize=eSize,elemType='ShellMITC4')
voladzExt_mesh=fem.SurfSetToMesh(surfSet=voladzExt,matSect=voladzExt_mat,elemSize=eSize,elemType='ShellMITC4')
voladzInt_mesh=fem.SurfSetToMesh(surfSet=voladzInt,matSect=voladzInt_mat,elemSize=eSize,elemType='ShellMITC4')

allmesh=[riostrEstr1_mesh,riostrEstr2_mesh,losa_mesh,cartabInt_mesh,cartabExt_mesh,voladzInt_mesh,voladzExt_mesh]
fem.multi_mesh(preprocessor=prep,lstMeshSets=allmesh)

pilasBarlov_mesh.generateMesh(prep)
if pilasSotav:
    pilasSotav_mesh.generateMesh(prep)
