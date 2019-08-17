# -*- coding: utf-8 -*-
from solution import predefined_solutions


def listVector(v):
    return [v[0],v[1],v[2],v[3],v[4],v[5]]

results=dict()

for lc in resLoadCases_neopr:
    results[lc.loadCaseName]={}
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
    if len(constrNodesPilas)>0:
        Rnpil=[listVector(n.getReaction) for n in constrNodesPilas]
#    R=n.getReaction
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
    for i in range(len(constrNodesE1)):
        results[lc.loadCaseName]['Restr1_n'+str(i+1)]=RnEstr1[i]
    for i in range(len(neopsE1)):
        results[lc.loadCaseName]['neoprStress_e'+str(i+1)]=neopStress[i]
        results[lc.loadCaseName]['neoprStrain_e'+str(i+1)]=neopStrains[i]
    if len(constrNodesPilas)>0:
        for i in range(len(constrNodesPilas)):
            results[lc.loadCaseName]['Rpilas_n'+str(i+1)]=Rnpil[i]
