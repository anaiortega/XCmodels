
execfile('../model_gen.py') #FE model generation

from postprocess.xcVtk.CAD_model import vtk_CAD_graphic
defDisplay= vtk_CAD_graphic.RecordDefDisplayCAD()
#defDisplay.displayBlocks(setToDisplay=overallSet,caption= 'Model grid')
'''
defDisplay.displayBlocks(setToDisplay=columns,caption= columns.description)
defDisplay.displayBlocks(setToDisplay=columns,caption= beams.description)
defDisplay.displayBlocks(setToDisplay=columns,caption= slabs_H.description)
defDisplay.displayBlocks(setToDisplay=columns,caption= slabs_L.description)
'''
#defDisplay.displayBlocks(setToDisplay=lnL3+lnL4+lnL5+lnL6+lnL7+lnL8+lnL9+lnL10+lnL11+lnL12+lnL13,caption= 'Model grid')
#defDisplay.displayBlocks(setToDisplay=lnE1A+lnE1B+lnE1C+lnEC1C+lnEC1B,caption= 'Model grid')

defDisplay.displayBlocks(setToDisplay=lnL3+lnL4+lnL5+lnL6+lnL7+lnL8+lnL9+lnL10+lnL11+lnL12+lnL13+lnE1A+lnE1B+lnE1C+lnEC1C+lnEC1B,caption= 'Model grid')

#defDisplay.displayBlocks(setToDisplay=lnE1A+lnE1B+lnE1C+lnEC1B,caption= 'Model grid')
#defDisplay.displayBlocks(setToDisplay=columns+lnL3+lnW1A+lnW1B+lnW1C+lnWC1A+lnWC1B+lnWC1C+lnN1B+lnN1C,caption= 'Model grid')
#defDisplay.displayBlocks(setToDisplay=slab23,caption= 'Model grid')
