# grid model definition (pilas)
gridPil= gm.GridModel(prep,xListPil,yListPil,zListPil)
# Points' generation
gridPil.generatePoints()

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

pilasBarlov=gridPil.genLinMultiXYZRegion(lstXYZRange=xyzRang, setName='pilasBarlov')
if len(x)>1:
    xyzRang=list()
    for j in range(len(y)):
        k=j
        for i in range(1,len(x)):
            xyzRang.append([(x[i],y[j],z[k][0]),(x[i],y[j],z[k][-1])])
    pilasSotav=gridPil.genLinMultiXYZRegion(lstXYZRange=xyzRang, setName='pilasSotav')
else:
    pilasSotav=None

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

#                         ***FE model - MESH***
pilasBarlov_mesh=fem.LinSetToMesh(linSet=pilasBarlov,matSect=pilas_mat,elemSize=eSize,vDirLAxZ=xc.Vector([0,1,0]),elemType='ElasticBeam3d',dimElemSpace=3,coordTransfType='linear')
allmesh+=[pilasBarlov_mesh]
if pilasSotav:
    pilasSotav_mesh=fem.LinSetToMesh(linSet=pilasSotav,matSect=pilas_mat,elemSize=eSize,vDirLAxZ=xc.Vector([0,1,0]),elemType='ElasticBeam3d',dimElemSpace=3,coordTransfType='linear')
pilasBarlov_mesh.generateMesh(prep)
if pilasSotav:
    pilasSotav_mesh.generateMesh(prep)
    allmesh+=[pilasSotav_mesh]
