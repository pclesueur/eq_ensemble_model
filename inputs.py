# -*- coding: utf-8 -*-
"""
Created on Sat Mar 24 21:01:51 2018

@author: plesueur
"""
import pandas as pd

#Constants
#=============================================================================
building_types =    ["wdn", "rcne", "bcf", "bcr", "bm", "sm"] 
injury_state =      ['injury1', 'injury2', 'fatality']
damage_state =      ['moderate', 'extensive', 'complete', 'collapsed']

#VDC Data
#=============================================================================
vdc_data = pd.read_csv('inputs/vdc_data.csv', index_col = 0)


#Fragility Curves
#=============================================================================
rows = ['sigma', 'x50']
cols = damage_state

# follows (building_type, fragility_curve_params, damage_state), 
# must match above array lengths
data = [[[0.640, 0.640, 0.640, 0.640], [0.95, 0.95, 0.95, 0.95]], 
        [[0.640, 0.640, 0.640, 0.640], [0.95, 0.95, 0.95, 0.95]],
        [[0.640, 0.640, 0.640, 0.640], [0.95, 0.95, 0.95, 0.95]],
        [[0.640, 0.640, 0.640, 0.640], [0.95, 0.95, 0.95, 0.95]],
        [[0.640, 0.640, 0.640, 0.640], [0.95, 0.95, 0.95, 0.95]],
        [[0.640, 0.640, 0.640, 0.640], [0.95, 0.95, 0.95, 0.95]]]

frames = {}
for i in range(0, len(data)):
    frames[building_types[i]] = pd.DataFrame(data=data[i], index=rows, columns=cols)
fragility_curves = pd.Panel(frames)

#Human Impact Rates
#=============================================================================
rows = injury_state
cols = damage_state

# follows (building_type, injury_state, damage_state), 
# must match above array lengths
data = [[[0.00030, 0.00100, 0.01000, 0.20000],
         [0.00000, 0.00001, 0.00010, 0.05000],
         [0.00000, 0.00000, 0.00000, 0.05000]],
        [[0.00400, 0.00200, 0.02000, 0.20000],
         [0.00001, 0.00002, 0.00020, 0.05000],
         [0.00000, 0.00000, 0.00000, 0.05000]],
        [[0.00400, 0.00200, 0.02000, 0.20000],
         [0.00001, 0.00002, 0.00020, 0.05000],
         [0.00000, 0.00000, 0.00000, 0.05000]],
        [[0.00400, 0.00200, 0.02000, 0.20000],
         [0.00001, 0.00002, 0.00020, 0.05000],
         [0.00000, 0.00000, 0.00000, 0.05000]],
        [[0.00400, 0.00200, 0.02000, 0.20000],
         [0.00001, 0.00002, 0.00020, 0.05000],
         [0.00000, 0.00000, 0.00000, 0.05000]],
        [[0.00400, 0.00200, 0.02000, 0.20000],
         [0.00001, 0.00002, 0.00020, 0.05000],
         [0.00000, 0.00000, 0.00000, 0.05000]]]

frames = {}
for i in range(0, len(data)):
    frames[building_types[i]] = pd.DataFrame(data=data[i], index=rows, columns=cols)
impact_rates = pd.Panel(frames)
