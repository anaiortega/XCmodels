
from __future__ import division
from __future__ import print_function

OKGREEN= '\033[92m'
WARNING= '\033[93m'
FAIL= '\033[91m'
ENDC = '\033[0m'

def checkPlates(studSpacing, plateGeom, infSet, supSet, supportedNodes):
    # Data
    print('Wood material: ', plateGeom.wood.name,' grade:', plateGeom.wood.grade)
    print('plate thickness= ', plateGeom.h*1e3, ' mm')
    print('stud spacing= ', studSpacing, ' m\n')
    ## Bending stiffness
    uYMax= -1e6
    for n in infSet.nodes:
        uY= -n.getDisp[1]
        uYMax= max(uY,uYMax)

    r= studSpacing/uYMax
    print('**** uYMax= ', uYMax*1e3, ' mm (L/'+str(r)+')\n')

    ## Bending strength
    sgMax= -1e6
    for e in supSet.elements:
        e.getResistingForce()
        m1= e.getM1
        sg1= abs(m1/plateGeom.xc_material.sectionProperties.I*plateGeom.h/2)
        sgMax= max(sgMax,sg1)
        m2= e.getM2
        sg2= abs(m2/plateGeom.xc_material.sectionProperties.I*plateGeom.h/2)
        sgMax= max(sgMax,sg2)

    Fb_adj= plateGeom.getFbAdj()
    FbCF= sgMax/Fb_adj
    print('sgMax= ', sgMax/1e6,' MPa')
    print('Fb_adj= ', Fb_adj/1e6,' MPa')
    if(Fb_adj>sgMax):
        print('**** CF= ', FbCF,'OK\n')
    else:
        print(FAIL+'**** CF= '+str(FbCF)+' KO\n'+ENDC)

    ## Shear strength
    tauMax= -1e6
    for e in supSet.elements:
        e.getResistingForce()
        v1= e.getV1
        tau1= abs(v1/plateGeom.xc_material.sectionProperties.A)
        tauMax= max(tauMax,tau1)
        v2= e.getV2
        tau2= abs(v2/plateGeom.xc_material.sectionProperties.A)
        tauMax= max(tauMax,tau2)

    Fv_adj= plateGeom.getFvAdj()
    FvCF= tauMax/Fv_adj
    print('tauMax= ', tauMax/1e6,' MPa')
    print('Fv_adj= ', Fv_adj/1e6,' MPa')
    if(Fv_adj>tauMax):
        print('**** CF= ', FvCF,'OK\n')
    else:
        print(FAIL+'**** CF= '+str(FvCF)+' KO\n'+ENDC)

    ## Compression perpendicular to grain

    ### Reactions
    preprocessor= infSet.getPreprocessor
    preprocessor.getNodeHandler.calculateNodalReactions(False,1e-7)
    RMax= -1e12;
    for n in supportedNodes:
        RMax= max(RMax,n.getReaction[1])
    sgMax= RMax/plateGeom.A()
    Fc_perp= plateGeom.getFc_perpAdj() #Perpendicular to grain
    Fc_perpCF= sgMax/Fc_perp
    print('RMax= ', RMax/1e3, ' kN')
    print('sgMax= ', sgMax/1e6, ' MPa')
    print('Fc_perp= ', Fc_perp/1e6, ' MPa')
    if(Fc_perp>sgMax):
        print('**** CF= ', Fc_perpCF,'OK\n')
    else:
        print(FAIL+'**** CF= '+str(Fc_perpCF)+' KO\n'+ENDC)
