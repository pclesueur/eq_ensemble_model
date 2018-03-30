# -*- coding: utf-8 -*-
"""
Created on Sat Mar 24 09:42:07 2018

@author: plesueur
"""
import pandas as pd
import numpy as np
import inputs as inpt
import vdc_impacts as impacts
import math as math




#vdc_impacts = pd.Series(index = ['a', 'b', 'c']) 
#vdc_impacts['a'] = 1
#print(vdc_impacts)
'''
class Human:
    def __init__(self, height, weight):
        self.height = height
        self.weight = weight
    
    skills = []
    
    def bmi(self):
        return self.height / self.weight
    
    def addSkill(self, skill):
        self.skills.append(skill)
        
    def __mostPrivate(self):
        print('this is private ill kill you')

phil = Human(6, 155)
phil_bmi = phil.bmi()
phil.addSkill('coding')
phil.addSkill('hazard assessment')
print(phil_bmi)
print(phil.skills)
'''



'''
vdc_data = impacts.getVdcData('Atarpur')
result = impacts.vdc_impacts(vdc_data, 5)
#test = impacts.humanImpacts('wdn', 'collapse', )

print(result)

s = pd.Series(data = [0.64,0.95], index=['sigma','x50']) 

print(type(s))

#print(s)
'''


'''
test = impacts.getFragilityCurves('wdn')
print(test)

for dmg_state, curve in test.iteritems():
    print(type(curve))
'''

#impacts.buildingImpacts(0.5,'wdn',0.3)


'''
data = inpt.vdc_data.iloc[0]
print(data['pop'])

print(len(inpt.building_types))
'''

'''
#transpose this, so building types are third axis.
rows = ['injury1', 'injury2', 'fatality']
cols = ['moderate', 'extensive', 'complete', 'collapsed']
data_adb = [[0.00400, 0.00200, 0.02000, 0.20000],
            [0.00001, 0.00002, 0.00020, 0.05000],
            [0.00000, 0.00000, 0.00000, 0.05000]]
data_wdn = [[0.00030, 0.00100, 0.01000, 0.20000],
            [0.00000, 0.00001, 0.00010, 0.05000],
            [0.00000, 0.00000, 0.00000, 0.05000]]

data = {'adb' : pd.DataFrame(data=data_adb, index=rows, columns=cols),
        'wdn' : pd.DataFrame(data=data_wdn, index=rows, columns=cols) }

p = pd.Panel(data)

print(p.loc['adb']['complete'])
'''
'''
a = [[0,1,2],[3,4,5]]
b = [[6,7,8],[9,10,11]]

data = np.array([a,b])
print(data.shape)


p = pd.Panel(data)
'''

"""
atar = inpt.vdc_data.loc['Atarpur'][:]

building_count = atar.loc['wdn']
total_building = sum(atar.loc[inpt.building_types])
rate = building_count / total_building

print(building_count)
print(total_building)
print(rate)
"""

"""
df = pd.read_csv('inputs/vdc_data.csv', index_col = 0)
print(df)
"""



"""
for item in df.loc['Atarpur'][:]:
    print(item)

#fragility curves input
fragility_curves = inpt.fragility_curves

rcne_curves = fragility_curves.loc['rcne'][:]
#print(rcne_curves)

result = {}
for ind, val in rcne_curves.iteritems():
    result[ind] = val

result = pd.Series(result)
#print(result)
 
for dmg_state, val in rcne_curves.iteritems():
    print(val)
"""  

   


#print(test)
#print(test['complete'])
#result = test
#for item in test:
#    result[item]
