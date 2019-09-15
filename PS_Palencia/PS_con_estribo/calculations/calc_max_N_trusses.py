# -*- coding: utf-8 -*-
from postprocess import limit_state_data as lsd

execfile("../model_gen.py") #FE model generation
execfile("../env_config_deck.py")
setCalc=ties

intForcCombFileName=cfg.intForcPath+'intForce_ULS_normalStressesResistance.csv'

etags,combs,intForc=lsd.readIntForcesFile(intForcCombFileName,setCalc)
f=open('./pp.py',"w")
setName=setCalc.name
for el in etags:
    #init max. axial internal forces
    maxNsect1=-1e10
    maxNsect2=-1e10
#    el.setProp('maxNsect1',-1e10)
#    el.setProp('maxNsect2',-1e10)
    elIntF=intForc[el]
    for ind in range(len(combs)):
        Nsect1=elIntF[2*ind].N
        Nsect2=elIntF[2*ind+1].N
        print 'idSection1=', elIntF[2*ind].idSection
        print 'idSection2=', elIntF[2*ind+1].idSection
        print 'Nsect1=',Nsect1,' Nsect2=',Nsect2
        if Nsect1>maxNsect1:
            maxNsect1=Nsect1
            maxCmbsect1=elIntF[2*ind].idComb
        if Nsect2>maxNsect2:
            maxNsect2=Nsect2
            maxCmbsect2=elIntF[2*ind+1].idComb
    print 'el=',el,  ' maxNsect1=',maxNsect1, ' maxCmbsect1=',maxCmbsect1 
    print 'el=',el,  ' maxNsect2=',maxNsect2, ' maxCmbsect2=',maxCmbsect2
    strBase1='preprocessor.getElementHandler.getElement('+str(el)+').setProp("maxAxialForceSect1",AxialForceControlVars('
    strBase2='preprocessor.getElementHandler.getElement('+str(el)+').setProp("maxAxialForceSect2",AxialForceControlVars('
    
    strSect1=strBase1+'idSection= "' + setName + 'Sects1"' + ', combName= "' + maxCmbsect1  +'", N= ' + str(Nsect1) + ')) \n'
    strSect2=strBase2+ 'idSection= "'  + setName + 'Sects2"' + ', combName= "' + maxCmbsect2  +'", N= ' + str(Nsect2) + ')) \n'
    f.write(strSect1) 
    f.write(strSect2) 
f.close()
    
