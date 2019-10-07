
execfile('../model_gen.py') #FE model generation

from postprocess.xcVtk.CAD_model import vtk_CAD_graphic
defDisplay= vtk_CAD_graphic.RecordDefDisplayCAD()
#defDisplay.displayBlocks(xcSet=overallSet,fName= None,caption= 'Model grid')
'''
xcSet=columns
defDisplay.displayBlocks(xcSet=columns,fName= None,caption= xcSet.description)
xcSet=beams
defDisplay.displayBlocks(xcSet=beams,fName= None,caption= xcSet.description)
xcSet=slabs_H
defDisplay.displayBlocks(xcSet=slabs_H,fName= None,caption= xcSet.description)
xcSet=slabs_L
defDisplay.displayBlocks(xcSet=slabs_L,fName= None,caption= xcSet.description)
'''
#defDisplay.displayBlocks(xcSet=lnL3+lnL4+lnL5+lnL6+lnL7+lnL8+lnL9+lnL10+lnL11+lnL12+lnL13,fName= None,caption= 'Model grid')
#defDisplay.displayBlocks(xcSet=lnE1A+lnE1B+lnE1C+lnEC1C+lnEC1B,fName= None,caption= 'Model grid')

defDisplay.displayBlocks(xcSet=lnL3+lnL4+lnL5+lnL6+lnL7+lnL8+lnL9+lnL10+lnL11+lnL12+lnL13+lnE1A+lnE1B+lnE1C+lnEC1C+lnEC1B,fName= None,caption= 'Model grid')

#defDisplay.displayBlocks(xcSet=lnE1A+lnE1B+lnE1C+lnEC1B,fName= None,caption= 'Model grid')
#defDisplay.displayBlocks(xcSet=columns+lnL3+lnW1A+lnW1B+lnW1C+lnWC1A+lnWC1B+lnWC1C+lnN1B+lnN1C,fName= None,caption= 'Model grid')
#defDisplay.displayBlocks(xcSet=slab23,fName= None,caption= 'Model grid')
