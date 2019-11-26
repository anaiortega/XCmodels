# -*- coding: utf-8 -*-
from solution import predefined_solutions


def listVector(v):
    return [v[0],v[1],v[2],v[3],v[4],v[5]]

results=dict()

for lc in resLoadCases_neopr:
    combs=preprocessor.getLoadHandler.getLoadCombinations
    lCase=combs.newLoadCombination('lc'+lc.loadCaseName,lc.loadCaseExpr)
    preprocessor.resetLoadCase()
    combs.addToDomain('lc'+lc.loadCaseName)
    analysis= predefined_solutions.simple_static_linear(FEcase)
    result= analysis.analyze(1)
    combs.removeFromDomain('lc'+lc.loadCaseName)
    #Reactions
    nodes.calculateNodalReactions(False,1e-7)
    #Reacciones nodos arranque pilas y estribo 1
    Rnpil=[listVector(n.getReaction) for n in constrNodesPilas]
    R=n.getReaction
    RnEstr1=[listVector(n.getReaction) for n in constrNodesE1]
    #Tensiones y deformaciones en neoprenos
    neopStrains=list()
    neopStress=list()
    for e in neopsE1:
        mat=[e.getMaterials()[i] for i in range(6)]
        stress=[m.getStress() for m in mat]
        strain=[m.getStrain() for m in mat]
        neopStress.append(stress)
        neopStrains.append(strain)
    results[lc.loadCaseName]={'Rpilas_n1':Rnpil[0],
                              'Rpilas_n2':Rnpil[1],
                              'Rpilas_n3':Rnpil[2],
                              'Rpilas_n4':Rnpil[3],
                              'Restr1_n1':RnEstr1[0],
                              'Restr1_n2':RnEstr1[1],
                              'Restr1_n3':RnEstr1[2],
                              'Restr1_n4':RnEstr1[3],
                              'neoprStress_e1': neopStress[0],
                              'neoprStress_e2': neopStress[1],
                              'neoprStress_e3': neopStress[2],
                              'neoprStress_e4': neopStress[3],
                              'neoprStrain_e1':neopStrains[0],
                              'neoprStrain_e2':neopStrains[1],
                              'neoprStrain_e3':neopStrains[2],
                              'neoprStrain_e4':neopStrains[3]
    }
