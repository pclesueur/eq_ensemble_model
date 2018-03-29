"""
Created on Tue Mar 27 21:51:57 2018

@author: plesueur
"""

import unittest
import vdc_impacts as ip
import inputs as inpt
import pandas as pd

class TestVDCImpacts(unittest.TestCase):
    '''
    Basic test class
    '''
    
    def test_probOfDamage(self):
        s = pd.Series(data = [0.64,0.95], index=['sigma','x50']) 
        res = ip.probabilityOfDamage(0.3,s)
        self.assertAlmostEqual(res, 0.0358465750872893)
        res = ip.probabilityOfDamage(500,s)
        self.assertGreaterEqual(res, 0)
        self.assertLessEqual(res, 1)
        res = ip.probabilityOfDamage(-500,s)
        self.assertGreaterEqual(res, 0)
        self.assertLessEqual(res, 1)
        res = ip.probabilityOfDamage('garbage',s)
        self.assertEqual(res, 0)
    
    def test_buildingRate(self):
        s = pd.Series(data = [2182, 1, 1, 3, 6, 453, 0], 
                      index=['pop', 'wdn', 'rcne', 'bcf', 'bcr', 'sm', 'bm'])
        res = ip.buildingRate('wdn',s)
        self.assertAlmostEqual(res, 0.0021551724137931)
        res = ip.buildingRate('sm',s)
        self.assertAlmostEqual(res, 0.976293103448276)
    
    def test_buildingPop(self):
        s = pd.Series(data = [2182, 1, 1, 3, 6, 453, 0], 
                      index=['pop', 'wdn', 'rcne', 'bcf', 'bcr', 'sm', 'bm'])
        res = ip.buildingPop(s, 'wdn')
        self.assertAlmostEqual(res, 4.70258620689655)
    
    def test_vdcImpacts(self):
        s = pd.Series(data = [2182, 1, 1, 3, 6, 453, 0], 
                      index=['pop', 'wdn', 'rcne', 'bcf', 'bcr', 'sm', 'bm'])
        res= ip.vdc_impacts(s, 0.3)
        self.assertEquals(len(res), len(inpt.injury_state))
        self.assertTrue(type(res) == type(s))
        
if __name__ == '__main__':
    unittest.main()