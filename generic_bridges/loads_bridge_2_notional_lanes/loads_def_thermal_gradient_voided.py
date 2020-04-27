#Thermal gradient load cases voided slab bridge
GradTcal1=loads.StrainLoadOnShells(name='GradTcal1', xcSet=supTablero,DOFstrain=1,strain=coefDilat*Tfibrsup_cal)
GradTcal2=loads.StrainLoadOnShells(name='GradTcal2', xcSet=murosAll,DOFstrain=0,strain=coefDilat*Tfibrsup_cal/2.0)
GradTfrio1=loads.StrainLoadOnShells(name='GradTfrio1', xcSet=supTablero,DOFstrain=1,strain=coefDilat*Tfibrsup_fria)
GradTfrio2=loads.StrainLoadOnShells(name='GradTfrio2', xcSet=murosAll,DOFstrain=0,strain=coefDilat*Tfibrsup_fria/2.0)

Q33=lcases.LoadCase(preprocessor=prep,name="Q33")
Q33.create()
Q33.addLstLoads([GradTcal1,GradTcal2])

Q34=lcases.LoadCase(preprocessor=prep,name="Q34")
Q34.create()
Q34.addLstLoads([GradTfrio1,GradTfrio2])


