execfile('../model_gen.py') #FE model generation
allLines=prep.getSets.getSet('total').getLines
'''
for l in allLines:
    print l.getKPoints()[0], ',',l.getKPoints()[1]
'''
for l in slab23.getLines:
    print l.getKPoints()[0], ',',l.getKPoints()[1]
