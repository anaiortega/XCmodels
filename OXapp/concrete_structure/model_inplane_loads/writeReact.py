# -*- coding: utf-8 -*-

execfile('./model_gen.py')
def get_max_min_mean_react(lstNod,esize,Lwall):
    '''Return the maximum and minimum reactions (X Y directions) of the nodes
    in the list. Also return the mean reaction in X Y directions'''
    (maxRx,minRx,totalRx)=(0,0,0)
    (maxRy,minRy,totalRy)=(0,0,0)
    for n in lstNod:
        R=n.getReaction
        Rx=R[0]
        Ry=R[1]
        totalRx+=abs(Rx)
        totalRy+=abs(Ry)
        if Rx>maxRx:
            maxRx=Rx
        elif Rx<minRx:
            minRx=Rx
        if Ry>maxRy:
            maxRy=Ry
        elif Ry<minRy:
            minRy=Ry
    maxRx/=esize  #N/m
    minRx/=esize  #N/m
    maxRy/=esize  #N/m
    minRy/=esize  #N/m
    meanRx=totalRx/Lwall
    meanRy=totalRx/Lwall
    return (round(maxRx*1e-3,2),
            round(minRx*1e-3,2),
            round(meanRx*1e-3,2),
            round(maxRy*1e-3,2),
            round(minRy*1e-3,2),
            round(meanRy*1e-3,2))

def print_res(lcName,esize,EastW_L,WestW_L,NorthW_L,SouthW_L):
    print lcName
    R_EastW=get_max_min_mean_react(EastW_nod,esize,EastW_L)
    R_WestW=get_max_min_mean_react(WestW_nod,esize,WestW_L)
    R_NorthW=get_max_min_mean_react(NorthW_nod,esize,NorthW_L)
    R_SouthW=get_max_min_mean_react(SouthW_nod,esize,SouthW_L)
    print 'East wall',R_EastW
    print 'West wall',R_WestW
    print 'North wall', R_NorthW
    print 'South wall', R_SouthW

    
esize=0.5
EastW_L=ySW-yNW-(yStair2_2-yStair2_1)
WestW_L=ySW-yNW
NorthW_L=xWW-xEW-(xStair1-xGridA)
SouthW_L=xWW-xEW
loadHand.addToDomain(Wind_EW.name)
analysis= predefined_solutions.simple_static_linear(FEcase)
result= analysis.analyze(1)
preprocessor.getNodeHandler.calculateNodalReactions(True,1e-7)
print_res(Wind_EW.name)
loadHand.removeFromDomain(Wind_EW.name,esize,EastW_L,WestW_L,NorthW_L,SouthW_L)
        
loadHand.addToDomain(Wind_NS.name)
analysis= predefined_solutions.simple_static_linear(FEcase)
result= analysis.analyze(1)
preprocessor.getNodeHandler.calculateNodalReactions(True,1e-7)
print_res(Wind_NS.name)
loadHand.removeFromDomain(Wind_NS.name,esize,EastW_L,WestW_L,NorthW_L,SouthW_L)
        
loadHand.addToDomain(Wind_WE.name)
analysis= predefined_solutions.simple_static_linear(FEcase)
result= analysis.analyze(1)
preprocessor.getNodeHandler.calculateNodalReactions(True,1e-7)
print_res(Wind_WE.name)
loadHand.removeFromDomain(Wind_WE.name,esize,EastW_L,WestW_L,NorthW_L,SouthW_L)
        
loadHand.addToDomain(Wind_SN.name)
analysis= predefined_solutions.simple_static_linear(FEcase)
result= analysis.analyze(1)
preprocessor.getNodeHandler.calculateNodalReactions(True,1e-7)
print_res(Wind_SN.name)
loadHand.removeFromDomain(Wind_SN.name,esize,EastW_L,WestW_L,NorthW_L,SouthW_L)
        

