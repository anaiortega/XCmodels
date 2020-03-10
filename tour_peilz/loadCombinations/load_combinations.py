# -*- coding: utf-8 -*-

import xc_base
import loadCombinations
from loadCombinationUtils import sia260
from loadCombinationUtils import utils
from misc_utils import log_messages as lmsg

lcg= sia260.controlCombGenerator

combination_factors= lcg.actionWeighting['SIA260']
G1= lcg.insert('SIA260','permanentes',loadCombinations.Action('selfWeight', 'Poids propre'),'permanent','permanentes')
G2= lcg.insert('SIA260','permanentes',loadCombinations.Action('deadLoad', 'Poids propre non porteur'),'permanent','permanentes')
G3= lcg.insert('SIA260','permanentes_nc',loadCombinations.Action('earthPressure', 'Poussée des terres'),'poussee_terres','terres')
Q1= lcg.insert('SIA260','variables',loadCombinations.Action('pedestrianLoad', 'Trafic non motorisé.'),'categorie_G','variables')
Q2= lcg.insert('SIA260','variables',loadCombinations.Action('singleAxeLoad', 'Véhicules entretien.'),'categorie_G','variables')
Q2.getRelaciones.agregaIncompatible('Q1')
Q3= lcg.insert('SIA260','variables',loadCombinations.Action('LM1', 'Pousée des terres due au modèle de charge 1.'),'voie_normale_load_model_1','variables')
Q4= lcg.insert('SIA260','variables',loadCombinations.Action('nosingLoad', 'Force de lacet.'),'voie_normale_load_model_1','variables')
Q4.getRelaciones.agregaMaestra('LM1')
A1= lcg.insert('SIA260','accidentales',loadCombinations.Action('earthquake', 'Séisme.'),'accidentales','accidentales')


lcg.genera()

conta= 0
for comb in lcg.getLoadCombinations.getULSTransientCombinations:
    print 'ULS_'+str(conta)+'= ', comb.name
    conta+=1

conta= 0
for comb in lcg.getLoadCombinations.getSLSCharacteristicCombinations:
    print 'SLSR_'+str(conta)+'= ', comb.name
    conta+=1

conta= 0
for comb in lcg.getLoadCombinations.getSLSFrequentCombinations:
    print 'SLSF_'+str(conta)+'= ', comb.name
    conta+=1

conta= 0
for comb in lcg.getLoadCombinations.getSLSQuasiPermanentCombinations:
    print 'SLSQP_'+str(conta)+'= ', comb.name
    conta+=1

conta= 0
for comb in lcg.getLoadCombinations.getULSAccidentalCombinations:
    print 'ULSA_'+str(conta)+'= ', comb.name
    conta+=1
