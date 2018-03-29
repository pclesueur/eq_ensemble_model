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
        vdc_data = ip.getVdcData('Atarpur')
        res = ip.buildingRate('wdn',vdc_data)
        self.assertAlmostEqual(res, 0.0021551724137931)
        res = ip.buildingRate('sm',vdc_data)
        self.assertAlmostEqual(res, 0.976293103448276)
    
    def test_buildingPop(self):
        vdc_data = ip.getVdcData('Atarpur')
        res = ip.buildingPop(vdc_data, 'wdn')
        self.assertAlmostEqual(res, 4.70258620689655)
        
        
        
if __name__ == '__main__':
    unittest.main()