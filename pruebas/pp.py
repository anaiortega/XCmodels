for lp in actLP:
    lIter= lp.loads.getElementalLoadIter
    eLoad= lIter.next()
    eTagsSet= self.setToDisp.getElements.getTags()
    while(eLoad):
        tags= eLoad.elementTags
        for i in range(0,len(tags)):
            eTag= tags[i]
            if eTag in eTagsSet:
                elem= preprocessor.getElementHandler.getElement(eTag)
                dim= elem.getDimension
                if(dim==1):
                    vJ= elem.getJVector3d(True)
                    vK= elem.getKVector3d(True)
                    if(self.component=='axialComponent'):
                        self.vDir= vJ
                        indxDiagram= self.appendDataToDiagram(elem,indxDiagram,eLoad.axialComponent,eLoad.axialComponent)
                    elif(self.component=='transComponent'):
                        self.vDir= vJ
                        indxDiagram= self.appendDataToDiagram(elem,indxDiagram,eLoad.transComponent,eLoad.transComponent)
                    elif(self.component=='transYComponent'):
                        self.vDir= vJ
                        indxDiagram= self.appendDataToDiagram(elem,indxDiagram,eLoad.transYComponent,eLoad.transYComponent)
                    elif(self.component=='transZComponent'):
                        self.vDir= vK
                        indxDiagram= self.appendDataToDiagram(elem,indxDiagram,eLoad.transZComponent,eLoad.transZComponent)
                    elif(self.component=='xyzComponents'):
                        vI= elem.getIVector3d(True)
                        localForce= eLoad.getVector3dLocalForce() # Local components of the force.
                        v= localForce.x*vI+localForce.y*vJ+localForce.z*vK # Global force vector.
                        self.vDir= v.normalized() 
                        value= v.getModulus()
                        indxDiagram= self.appendDataToDiagram(elem,indxDiagram,value,value)
                    else:    
                        lmsg.error("LinearLoadDiagram :'"+self.component+"' unknown.")        
        eLoad= lIter.next()
return indxDiagram
