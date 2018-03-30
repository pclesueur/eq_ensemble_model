"""
Created on Tue Mar 27 21:51:57 2018

@author: plesueur
"""

import unittest
import vdc_impacts as ip
import pandas as pd

class TestVDCImpacts(unittest.TestCase):
    '''
    Basic test class
    '''
    #Test Input Data
    #=========================================================================
    building_types =    ['wdn', 'rcne', 'bcf'] 
    injury_state =      ['injury2', 'fatality']
    damage_state =      ['complete', 'collapsed']
    vdc_data = pd.Series(data = ['Aratapur', 2182, 1, 1, 3], 
                         index = ['vdc', 'pop', 'wdn', 'rcne', 'bcf'])

    #Fragility Curves
    rows = ['sigma', 'x50']
    cols = damage_state
    data = [[[0.640, 0.640], [0.95, 0.95]], 
            [[0.640, 0.640], [0.95, 0.95]],
            [[0.640, 0.640], [0.95, 0.95]]]
    frames = {}
    for i in range(0, len(data)):
        frames[building_types[i]] = pd.DataFrame(data=data[i], index=rows, columns=cols)
    fragility_curves = pd.Panel(frames)
    
    #Human Impact Rates
    rows = injury_state
    cols = damage_state
    data = [[[0.00030, 0.00100],
             [0.00000, 0.00001]],
            [[0.00400, 0.00200],
             [0.00001, 0.00002]],
            [[0.00400, 0.00200],
             [0.00001, 0.00002]]] 
    frames = {}
    for i in range(0, len(data)):
        frames[building_types[i]] = pd.DataFrame(data=data[i], index=rows, columns=cols)
    impact_rates = pd.Panel(frames)
    
    #Instantiation
    #========================================================================= 
    impacted = ip.VDCImpacts(vdc_data, 0.3, fragility_curves, impact_rates)
    
     #Test Functions
    #=========================================================================     
    def test_buildingRate(self):
        res = self.impacted.buildingRate('wdn', self.vdc_data)
        self.assertEqual(res, 0.2)
        res = self.impacted.buildingRate('bcf', self.vdc_data)
        self.assertEqual(res, 0.6)
    
    def test_probOfDamage(self):
        s = pd.Series(data = [0.64,0.95], index=['sigma','x50'])
        res = self.impacted.probabilityOfDamage(0.3,s)
        self.assertAlmostEqual(res, 0.0358465750872893)
        res = self.impacted.probabilityOfDamage(500,s)
        self.assertGreaterEqual(res, 0)
        self.assertLessEqual(res, 1)
        res = self.impacted.probabilityOfDamage(-500,s)
        self.assertGreaterEqual(res, 0)
        self.assertLessEqual(res, 1)
        res = self.impacted.probabilityOfDamage('garbage',s)
        self.assertEqual(res, 0)
   
    def test_vdcImpacts(self):
        res = self.impacted.computeImpacts()
        self.assertEquals(len(res), len(self.injury_state)) 

if __name__ == '__main__':
    unittest.main()