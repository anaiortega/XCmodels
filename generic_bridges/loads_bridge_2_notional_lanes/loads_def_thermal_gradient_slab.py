#Thermal gradient load cases slab bridge
Q33=slm.gradient_thermal_LC(lcName='Q33',lstGradThStrnData=
    [imps.gradThermalStrain(elemSet=losa,elThick=cantoLosa,DOF=3,alpha=coefDilat,Ttop=Tfibrsup_fria,Tbottom=0),
     imps.gradThermalStrain(elemSet=cartabInt,elThick=eCartInt,DOF=3,alpha=coefDilat,Ttop=Tfibrsup_fria,Tbottom=0),
     imps.gradThermalStrain(elemSet=cartabExt,elThick=eCartExt,DOF=3,alpha=coefDilat,Ttop=Tfibrsup_fria,Tbottom=0),
     imps.gradThermalStrain(elemSet=voladzInt,elThick=eVolInt,DOF=3,alpha=coefDilat,Ttop=Tfibrsup_fria,Tbottom=0),
     imps.gradThermalStrain(elemSet=voladzExt,elThick=eVolExt,DOF=3,alpha=coefDilat,Ttop=Tfibrsup_fria,Tbottom=0)])
Q34=slm.gradient_thermal_LC(lcName='Q34',lstGradThStrnData=
    [imps.gradThermalStrain(elemSet=losa,elThick=cantoLosa,DOF=3,alpha=coefDilat,Ttop=Tfibrsup_cal,Tbottom=0),
     imps.gradThermalStrain(elemSet=cartabInt,elThick=eCartInt,DOF=3,alpha=coefDilat,Ttop=Tfibrsup_cal,Tbottom=0),
     imps.gradThermalStrain(elemSet=cartabExt,elThick=eCartExt,DOF=3,alpha=coefDilat,Ttop=Tfibrsup_cal,Tbottom=0),
     imps.gradThermalStrain(elemSet=voladzInt,elThick=eVolInt,DOF=3,alpha=coefDilat,Ttop=Tfibrsup_cal,Tbottom=0),
     imps.gradThermalStrain(elemSet=voladzExt,elThick=eVolExt,DOF=3,alpha=coefDilat,Ttop=Tfibrsup_cal,Tbottom=0)])
