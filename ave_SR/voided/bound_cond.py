constrNodes=list()
constrNodesPilas=list()
constrNodesE1=list()
constrNodesE2=list()
neopsE1=list() #elements of abutment1 ordered from xmin to xmax.
               #each element has six materials that reproduce respectively
               #Kx, Ky,Kz, KthetaX,KthetaY,KthetaZ
neopsE2=list()
#Empotramiento pilas en tablero
for indy in range(len(yPil)):
    for indx in range(len(xPil)):
        j=gridPil.gridCoo[1].index(yPil[indy])
        i=gridPil.gridCoo[0].index(xPil[indx])
        k=gridPil.gridCoo[2].index(zPil[indy][-1])
        pPil=gridPil.getPntGrid((i,j,k))
        j=gridTabl.gridCoo[1].index(yPil[indy])
        i=gridTabl.gridCoo[0].index(xPil[indx])
        k=gridTabl.gridCoo[2].index(zPil[indy][-1])
        pTabl=gridTabl.getPntGrid((i,j,k))
        nPil=pPil.getNode()
        nTabl=pTabl.getNode()
        for gdl in range(6):
            modelSpace.constraints.newEqualDOF(nPil.tag,nTabl.tag,xc.ID([gdl]))
'''
# Empotramiento base pilas
#for indy in range(len(yPil)):  #25/08/2019 prueba pilotes
for indy in range(1,len(yPil)):
    for indx in range(len(xPil)):
        j=gridPil.gridCoo[1].index(yPil[indy])
        i=gridPil.gridCoo[0].index(xPil[indx])
        k=gridPil.gridCoo[2].index(zPil[indy][0])
        p=gridPil.getPntGrid((i,j,k))
        n=p.getNode()
        modelSpace.fixNode('000_000',n.tag)
        constrNodesPilas.append(n)
'''

# Elastomeric bearings.
from materials import bridge_bearings as bb
neopr=bb.ElastomericBearing(G=Gneopr,a=aNeopr,b=bNeopr,e=hNetoNeopr)
neopr.defineMaterials(prep)

#Neoprenos estribos
#Estribo 1
yn=yEstr[0]
zl=zriostrEstr
if abutment.lower()[0]=='y':
    for xn in xNeopr:
        n3=nodes.getDomain.getMesh.getNearestNode(geom.Pos3d(xn,yn,zl))
        x,y=n3.getCoo[0],n3.getCoo[1]
        n2=nodes.newNodeXYZ(x,y,zl-cantoRiostrEstr/2.-hNetoNeopr/2.0)
        modelSpace.setRigidBeamBetweenNodes(n3.tag,n2.tag)
        n1=nodes.newNodeXYZ(x,y,zl-cantoRiostrEstr/2.-hNetoNeopr/2.0)
        elem=neopr.putBetweenNodes(modelSpace,n1.tag,n2.tag)
        neopsE1.append(elem)
        zneopEstr=zMurEstr
        n0=nodes.getDomain.getMesh.getNearestNode(geom.Pos3d(xn,yMurEstr,zneopEstr))
        modelSpace.setRigidBeamBetweenNodes(n1.tag,n0.tag)
else:
    for xn in xNeopr:
        n2=nodes.getDomain.getMesh.getNearestNode(geom.Pos3d(xn,yn,zl))
        x,y=n2.getCoo[0],n2.getCoo[1]
        n1=nodes.newNodeXYZ(x,y,zl-cantoRiostrEstr/2.-hNetoNeopr/2.0)
        modelSpace.setRigidBeamBetweenNodes(n2.tag,n1.tag)
        n0=nodes.newNodeXYZ(x,y,zl-cantoRiostrEstr/2.-hNetoNeopr/2.0)
        modelSpace.fixNode('000_000',n0.tag)
        constrNodesE1.append(n0)
        elem=neopr.putBetweenNodes(modelSpace,n0.tag,n1.tag)
        neopsE1.append(elem)

#Estribo 2
yn=yEstr[-1]
zl=zriostrEstr
for xn in xNeopr:
    n2=nodes.getDomain.getMesh.getNearestNode(geom.Pos3d(xn,yn,zl))
    x,y=n2.getCoo[0],n2.getCoo[1]
    n1=nodes.newNodeXYZ(x,y,zl-cantoRiostrEstr/2.-hNetoNeopr/2.0)
    modelSpace.setRigidBeamBetweenNodes(n2.tag,n1.tag)
    n0=nodes.newNodeXYZ(x,y,zl-cantoRiostrEstr/2.-hNetoNeopr/2.0)
    modelSpace.fixNode('000_000',n0.tag)
    constrNodesE2.append(n0)
    elem=neopr.putBetweenNodes(modelSpace,n0.tag,n1.tag)
    neopsE2.append(elem)

