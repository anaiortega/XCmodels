# -*- coding: utf-8 -*-

import xc_base
import loadCombinations
from loadCombinationUtils import sia260
from loadCombinationUtils import utils
from miscUtils import LogMessages as lmsg

lcg= sia260.controlCombGenerator

combination_factors= lcg.actionWeighting['SIA260']
G1= lcg.insert('SIA260','permanentes',loadCombinations.Action('G1', 'Self weight'),'permanent','permanentes')
G2= lcg.insert('SIA260','permanentes',loadCombinations.Action('G2', 'Dead load'),'permanent','permanentes')
G3= lcg.insert('SIA260','permanentes_nc',loadCombinations.Action('G3', 'Earth pressure'),'poussee_terres','terres')
Q1= lcg.insert('SIA260','variables',loadCombinations.Action('Q1', 'Trafic non motorisé.'),'categorie_G','variables')
Q2= lcg.insert('SIA260','variables',loadCombinations.Action('Q2', 'Véhicules entretien.'),'categorie_G','variables')
Q2.getRelaciones.agregaIncompatible('Q1')
Q3= lcg.insert('SIA260','variables',loadCombinations.Action('Q3', 'LM1'),'voie_normale_load_model_1','variables')
Q4= lcg.insert('SIA260','variables',loadCombinations.Action('Q4', 'Nosing load.'),'voie_normale_load_model_1','variables')
Q4.getRelaciones.agregaMaestra('Q3')
A1= lcg.insert('SIA260','accidentales',loadCombinations.Action('A1', 'Earthquake.'),'accidentales','accidentales')


lcg.genera()

combULS= lcg.getLoadCombinations.getULSTransientCombinations
conta= 0
for comb in combULS:
    print 'ELU_'+str(conta)+'= ', comb.name
    conta+=1
