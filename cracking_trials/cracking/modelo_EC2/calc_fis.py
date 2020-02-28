# -*- coding: utf-8 -*-
#Parameters for tension stiffening of concrete
paramTS= concrete_base.paramTensStiffness(concrMat=concrete,reinfMat=rfSteel,reinfRatio=ro_s_eff,diagType='K')
concrete.tensionStiffparam=paramTS           #parameters for tension stiffening are assigned to concrete

ftdiag=concrete.tensionStiffparam.pointOnsetCracking()['ft']      #stress at the adopted point for concrete onset cracking
Etsdiag=abs(concrete.tensionStiffparam.regresLine()['slope'])
print 'ft=',ftdiag*1e-6
print 'Ets0=', Etsdiag*1e-6

fiber_sets.redefTensStiffConcr(setOfTenStffConcrFibSect=setsRCEl1.concrFibers,ft=ftdiag,Ets=Etsdiag)



# Solve
dom.revertToStart()  #!!!VERY IMPORTANT, don't forget!!!
analysis= predefined_solutions.simple_static_modified_newton(problem)
analOk= analysis.analyze(1)
x= sccEl1.getNeutralAxisDepth()
d=sccEl1.getEffectiveDepth()
h=sccEl1.getLeverArm()

As=setsRCEl1.tensionFibers.getArea(1.0)

#maximum depth of the effective area:
hceff=EC2_limit_state_checking.h_c_eff(depth_tot=h,depht_eff=abs(d),depth_neutral_axis=abs(x))
print 'depth of the effective area: ',hceff,' m'
Aceff=sccEl1.getNetEffectiveConcreteArea(hceff,'reinfSetFbEl1',15.0)
print 'effective concrete tension area: ',Aceff,' m2'
ro_s_eff=As/Aceff      #effective ratio of reinforcement
print 'effective ratio of reinforcement=', ro_s_eff
#maximum crack spacing
srmax=EC2_limit_state_checking.s_r_max(k1=0.8,k2=0.5,k3=3.4,k4=0.425,cover=cover,fiReinf=fiBott,ro_eff=ro_s_eff)
# print 'maximum crack spacing: ',srmax,' m'
#mean strain in the concrete between cracks
eps_cm=concrete.fctm()/concrete.E0()/2.0
#mean strain in the reinforcemen taking into account the effects of tension stiffening
fReinfMax= setsRCEl1.reinfFibers.getFiberWithMaxStrain()
epsSMax= fReinfMax.getMaterial().getStrain() # maximum strain among steel fibers
eps_sm=epsSMax
#crack withs
w_k=srmax*(eps_sm-eps_cm)
print 'crack widths: ',w_k*1e3, ' mm'
