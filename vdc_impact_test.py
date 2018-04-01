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
    building_types =    ['wdn', 'rcne', 'sm'] 
    injury_state =      ['injury3', 'fatality']
    damage_state =      ['complete', 'collapse']
    vdc_data = pd.Series(data = ['Aratapur', 'rural', 2182, 1, 1, 453, 5, 5, 2172], 
                         index = ['vdc', 'class', 'pop', 'wdn', 'rcne', 'sm',
                                  'wdn_pop','rcne_pop','sm_pop'])

    #Occupancy Rates
    rows = ['night', 'workday', 'non-workday']
    cols = ['urban', 'rural']
    data = [[0.99, 0.99],
            [0.70, 0.40],
            [0.40, 0.70]]
    occup_rates = pd.DataFrame(data=data, index=rows, columns=cols)
    
    #Fragility Curves
    rows = ['sigma', 'x50']
    cols = damage_state
    data = [[[0.640, 1.547], [0.950, 104.507]], 
            [[0.640, 1.943], [0.510, 23.281]],
            [[0.383, 0.720], [0.210, 0.970]]]
    frames = {}
    for i in range(0, len(data)):
        frames[building_types[i]] = pd.DataFrame(data=data[i], index=rows, columns=cols)
    fragility_curves = pd.Panel(frames)
    fragility_curves.to_frame()
    
    #Human Impact Rates
    rows = injury_state
    cols = damage_state
    data = [[[0.00010, 0.05000], [0.00000, 0.00500]],
            [[0.00010, 0.05000], [0.00000, 0.10000]],
            [[0.00020, 0.05000], [0.00000, 0.05000]]] 
    frames = {}
    for i in range(0, len(data)):
        frames[building_types[i]] = pd.DataFrame(data=data[i], index=rows, columns=cols)
    impact_rates = pd.Panel(frames)
    impact_rates.to_frame()
    
    #Instantiation
    #========================================================================= 
    impacted = ip.VDCImpacts(vdc_data, 0.440522841045, 'night', occup_rates, fragility_curves, impact_rates)
    
     #Test Functions
    #=========================================================================     
    def test_buildingRate(self):
        res = self.impacted.buildingRate('wdn', self.vdc_data)
        self.assertAlmostEqual(round(res,4), 0.00220)
        res = self.impacted.buildingRate('sm', self.vdc_data)
        self.assertAlmostEqual(round(res,3), 0.996)
    
    def test_probOfDamage(self):
        s = pd.Series(data = [0.64,0.95], index=['sigma','x50'])
        res = self.impacted.probabilityOfDamage(0.3,s)
        self.assertAlmostEqual(res, 0.0358465750872893)
        res = self.impacted.probabilityOfDamage(1.0,s)
        self.assertAlmostEqual(res, 0.531939346897124)
        s = pd.Series(data = [0.383,0.21], index=['sigma','x50'])
        res = self.impacted.probabilityOfDamage(0.3,s)
        self.assertAlmostEqual(res, 0.82414207459802)
        res = self.impacted.probabilityOfDamage(1.0,s)
        self.assertAlmostEqual(res, 0.999976972879538)
        res = self.impacted.probabilityOfDamage(500,s)
        self.assertGreaterEqual(res, 0)
        self.assertLessEqual(res, 1)
        res = self.impacted.probabilityOfDamage(-500,s)
        self.assertGreaterEqual(res, 0)
        self.assertLessEqual(res, 1)
        res = self.impacted.probabilityOfDamage('garbage',s)
        self.assertEqual(res, 0)
   
    def test_buildingImpacts(self):
        b_rate = self.impacted.buildingRate('wdn', self.vdc_data)
        res = self.impacted.buildingImpacts(b_rate, 'wdn', 0.440522841045)
        self.assertEquals(len(res), len(self.damage_state))
        self.assertAlmostEqual(res.loc['complete'], 0.000252567314381141)
        self.assertAlmostEqual(res.loc['collapse'], 0.000000449286)
        b_rate = self.impacted.buildingRate('sm', self.vdc_data)
        res = self.impacted.buildingImpacts(b_rate, 'sm', 0.440522841045)
        self.assertAlmostEqual(res.loc['complete'], 0.969185773353955)
        self.assertAlmostEqual(res.loc['collapse'], 0.135874543084081)
        res = self.impacted.buildingImpacts(b_rate, 'sm', 0.1)
        self.assertAlmostEqual(res.loc['complete'], 0.0262462087899565)
        self.assertAlmostEqual(res.loc['collapse'], 0.000796965230788048)
        
    def test_humanImpacts(self):
        b_rate = self.impacted.buildingRate('sm', self.vdc_data)
        b_impact = self.impacted.buildingImpacts(b_rate, 'sm', 0.440522841045)
        res = self.impacted.humanImpacts('sm', 'collapse', b_impact.loc['collapse'])
        self.assertEquals(len(res), len(self.injury_state))
        self.assertEqual(round(res.loc['injury3'], 5), 0.00679)
        self.assertEqual(round(res.loc['fatality'], 5), 0.00679)
        
    def test_vdcImpacts(self):
        res = self.impacted.computeImpacts()
        self.assertEquals(len(res), len(self.injury_state))
        self.assertEqual(res['injury3'], 14)
        self.assertEqual(res['fatality'], 14)


if __name__ == '__main__':
    unittest.main()