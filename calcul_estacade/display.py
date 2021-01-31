exec(open('./model_data.py').read())

from postprocess import output_handler

#########################################################
# Graphic stuff.
oh= output_handler.OutputHandler(modelSpace)
## Uncomment to display blocks
#oh.displayBlocks()

## Uncomment to display local axes
oh.displayLocalAxes()

## Uncomment to display strong and weak axes
#oh.displayStrongWeakAxis()

## Uncomment to display the mesh
#oh.displayFEMesh()

## Uncomment to display the vertical displacement
#oh. displayDispRot(itemToDisp='uY')

## Uncomment to display the reactions
#oh.displayReactions()

## Uncomment to display the reactions
#oh.displayIntForcDiag('Mz')

## Uncomment to display the reactions
# oh.displayLoads()

