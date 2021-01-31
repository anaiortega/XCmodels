# -*- coding: utf-8 -*-

exec(open('../model_data.py').read())

xcTotalSet= model.getPreprocessor().getSets.getSet('total')
model.displayMesh(xcTotalSet,'Finite element mesh') 
