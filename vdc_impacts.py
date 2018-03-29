"""
Main function package to estimate the human impacts in a VDC given a eq scenerio
V1.0
Prepared by: Philip LeSueur
Date: March 26, 2018

"""
#Header
#=============================================================================
import pandas as pd
import inputs as inpt
import math as math


#Variables
#=============================================================================
building_types   =  inpt.building_types


#Getters
#==============================================================================
'''
Input:  VDC [string]
Output: Series of VDC data 
'''
def getVdcData(vdc):
    return inpt.vdc_data.loc[vdc] 

'''
Input:  building_type [string]
Output: Dataframe of std, x50 for damage states
'''
def getFragilityCurves(building_type):
    return inpt.fragility_curves.loc[building_type]


'''
Input:  building_type [string], damage_state [string]
Output: Series of impact_rates 
'''
def getImpactRates(building_type, damage_state):
    return inpt.impact_rates[building_type][damage_state]


#Helpers
#==============================================================================
'''
calculate building rate
Input:  building_type [string], vdc_data [Series]
Output: building rate [float]
'''
def buildingRate(building_type, vdc_data):
    return vdc_data.loc[building_type] / sum(vdc_data.loc[building_types])


'''
calculate proportion of building_type impacted for each damage state
Input:  building_rate [float, 0 to 1], building_type [string], shaking [float]
Output: Series of (damage_state, percent of bldng_type damaged)
'''
def buildingImpacts(building_rate, building_type, shaking):
    fragility_curves = getFragilityCurves(building_type)
    result = {}
    for dmg_state, curve in fragility_curves.iteritems():
        result[dmg_state] = buildingsImpacted(building_rate, shaking, curve)
    result = pd.Series(result)
    return result


'''
calculate proportion of building_type impacted for a damage state
Input:  building_count[float, 0-1], shaking [float], curve_std [float]
Output: proportion of buildings [float]
'''
def buildingsImpacted(building_rate, shaking, curve):
    return building_rate * probabilityOfDamage(shaking, curve)
  

'''
calculate probability of damage. Returns zero if given non-number.
Input:  shaking [float], curve of std and x50 [Series of float]
Output: probability of damage state [float]
'''
def probabilityOfDamage(shaking, curve):
    try:
        float(repr(shaking))
        return 0.5 * (1 + math.erf((math.log(shaking)-math.log(curve.loc['x50']))/
                       (math.sqrt(2)*curve.loc['sigma'])))
    except:
        return 0
  
    
'''
calculate proportion of population in building_type impacted for each injury_type
Input:  building_type [string], damage_state [string], buildings_impacted [float]
Output: Series of (injury_state, impact_probability)
'''
def humanImpacts(building_type, damage_state, buildings_impacted):
    impact_rates = getImpactRates(building_type, damage_state)
    result = {}
    for injury_state, impact_rate  in impact_rates.iteritems():
        result[injury_state] = buildings_impacted * impact_rate
    result = pd.Series(result)    
    return result


'''
calcuate the number of people in each building type
Input:  vdc_data [Series], building_type [string]
Output: people in given building type [int]
'''   
def buildingPop(vdc_data, building_type):
    return vdc_data.loc['pop'] / sum(vdc_data.loc[building_types])


#Main Function
#==============================================================================
'''
calculate impacts in a vdc for a given eq scenerio
input:  vdc [string], shaking [float]
output: Series of (injury_state, number of people impacted)

'''
def vdc_impacts(vdc, shaking):
    vdc_data = getVdcData(vdc)
    result = pd.Series(data = [0,0,0], index = inpt.injury_state) 
    
    for building_type in building_types:
        building_rate = buildingRate(building_type, vdc_data)
        building_impacts = buildingImpacts(building_rate, building_type, shaking)
    
        for damage_state, buildings_impacted in building_impacts.iteritems():
            human_impacts = humanImpacts(building_type, damage_state, buildings_impacted)
            
            for injury_state, impact_probability in human_impacts.iteritems():
                result.loc[injury_state] += (impact_probability * buildingPop(vdc_data, building_type))
              
    return result 
