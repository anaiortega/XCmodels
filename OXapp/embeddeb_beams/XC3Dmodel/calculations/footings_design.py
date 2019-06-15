# -*- coding: utf-8 -*-

from __future__ import division
from __future__ import print_function

import math
import csv
from materials.aci import ACI_materials as aci
from scipy.optimize import brentq

class ACIIsolatedFooting(object):
    ''' Design of Isolated Square and Rectangular Footings(ACI 318-14)

    :ivar id: identifier.
    :ivar b: rectangular column dimension in concrete footing design (m).
    :ivar c: rectangular column dimension in concrete footing design (m).
    :ivar concrete: footing concrete.
    :ivar ulsLoads: design loads.
    :ivar phi: shear resistance factor.
    :ivar lamb_da: modification factor for lightweight concrete.
    :ivar q_allow: allowable soil pressure.
    '''
    axialForceIndex= 5
    def __init__(self, id= None, b= 0.5, c= 0.5, concrete= aci.A36M, ulsLoads= None, q= None):
        '''
        Constructor.


        :param b: rectangular column dimension in concrete footing design (m).
        :param c: rectangular column dimension in concrete footing design (m).
        :param ulsLoads: design loads
        '''
        self.id= id
        self.b= b
        self.c= c
        self.concrete= concrete
        self.ulsLoads= ulsLoads
        self.q_allow= q # allowable soil pressure.
        self.phi= 0.75 #shear resistance factor.
        self.lamb_da= 1.0 # normal weight concrete.

    def getFactoredAxialForce(self):
        ''' Return the column to footing factored axial force.'''
        retval= float(self.ulsLoads[0][self.axialForceIndex])
        for l in self.ulsLoads:
            retval= max(retval,float(l[self.axialForceIndex]))
        return retval

    def getVc(self):
        ''' Return shear strength in concrete design for
            two-way shear.'''
        fcklb_inch2= abs(self.concrete.fck*self.concrete.fromPascal) #Pa -> lb/inch2
        return 4.0*self.lamb_da*math.sqrt(fcklb_inch2)*self.concrete.toPascal #lb/inch2 -> Pa
    def hf_func(self, Pu, vc):
        ''' Returns the function to find the root for.'''
        tmp= Pu/self.phi/self.getVc()
        def hf(d):
            return 4.0*d*d+2.0*(self.b+self.c)*d-tmp
        return hf
    
    def computeApproximateFootingDepth(self):
        ''' Find an approximate footing depth.'''
        Pu= self.getFactoredAxialForce()
        vc= self.getVc()
        print('Pu= ', Pu/1e3, ' kN')
        f= self.hf_func(Pu,vc)
        d= brentq(f, 0.0, 100.0, args=())
        return d+4.0*2.54/100.0

    def computeArea(self):
        '''Find required area of footing base.'''
        return self.getServiceAxialForce()/self.q_allow
    
csvFile= open('uls_column_reactions.csv')
reader= csv.reader(csvFile)

b= 16*2.54/100.0 #column dimensions.
c= 16*2.54/100.0
q_allow= 3000.0*47.880208 # Geothecnical exploration page 5

footings= [ACIIsolatedFooting('A1',b,c, aci.A36M), ACIIsolatedFooting('A2',b,c, aci.A36M), ACIIsolatedFooting('A3',b,c, aci.A36M), ACIIsolatedFooting('A4',b,c, aci.A36M), ACIIsolatedFooting('A5',b,c, aci.A36M), ACIIsolatedFooting('B1',b,c, aci.A36M), ACIIsolatedFooting('B2',b,c, aci.A36M), ACIIsolatedFooting('B3',b,c, aci.A36M), ACIIsolatedFooting('B4',b,c, aci.A36M), ACIIsolatedFooting('B5',b,c, aci.A36M), ACIIsolatedFooting('C1',b,c, aci.A36M), ACIIsolatedFooting('C2',b,c, aci.A36M), ACIIsolatedFooting('C3',b,c, aci.A36M), ACIIsolatedFooting('C4',b,c, aci.A36M), ACIIsolatedFooting('C5',b,c, aci.A36M), ACIIsolatedFooting('D1',b,c, aci.A36M), ACIIsolatedFooting('D2',b,c, aci.A36M), ACIIsolatedFooting('D3',b,c, aci.A36M), ACIIsolatedFooting('D4',b,c, aci.A36M), ACIIsolatedFooting('D5',b,c, aci.A36M), ACIIsolatedFooting('G1',b,c, aci.A36M), ACIIsolatedFooting('G2',b,c, aci.A36M), ACIIsolatedFooting('G3',b,c, aci.A36M), ACIIsolatedFooting('G4',b,c, aci.A36M), ACIIsolatedFooting('G5',b,c, aci.A36M), ACIIsolatedFooting('F1',b,c, aci.A36M), ACIIsolatedFooting('F2',b,c, aci.A36M), ACIIsolatedFooting('F3',b,c, aci.A36M), ACIIsolatedFooting('F4',b,c, aci.A36M), ACIIsolatedFooting('F5',b,c, aci.A36M)]

loadDict= dict()
for f in footings:
    loadDict[f.id]= list()
    
#Populate load dictionary.
for row in reader:
    loadDict[row[0]].append(row)

for f in footings:
    f.ulsLoads= loadDict[f.id]
    f.q_allow= q_allow
    print(f.computeApproximateFootingDepth())
    print(f.computeArea())

