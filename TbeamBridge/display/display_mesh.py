# -*- coding: utf-8 -*-

execfile('../model_data.py')

xcTotalSet= model.getPreprocessor().getSets.getSet('total')
model.displayMesh(xcTotalSet,'Finite element mesh') 
