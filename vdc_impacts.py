"""
Main class to estimate the human impacts in a VDC given a eq scenerio
V1.0
Prepared by: Philip LeSueur
Date: March 26, 2018

"""
import pandas as pd
import math as math

# Main Class
#==============================================================================
class VDCImpacts:
    '''
    vdc_data [Series] - input vdc_data  
    shaking [float] - magnitude of ground shaking in the scenerio
    fragility_curves [Panel] - (building_types, curve_params, damage_state);
    impact_rates [Series] - impact rates for injury_states and fatalities
    '''
    def __init__(self, vdc_data, shaking, fragility_curves, impact_rates):
        self.data = vdc_data
        self.shaking = shaking
        self.frag_curves = fragility_curves
        self.impct_rates = impact_rates
        self.bldng_types = fragility_curves.axes[0]
        self.injury_states = impact_rates.axes[1]
        self.dmg_states = fragility_curves.axes[2] 
        #TODO: add exposure condition to make a complete scenerio
        #TODO: change from Panel to new thing
        
    
    def buildingRate(self, building_type, vdc_data):
        '''
        calculate building rate
        Input:  building_type [string], vdc_data [Series]
        Output: building rate [float]
        '''
        return vdc_data.loc[building_type] / sum(vdc_data.loc[self.bldng_types])


    def buildingImpacts(self, building_rate, building_type, shaking):
        '''
        calculate proportion of building_type impacted for each damage state
        Input:  building_rate [float, 0 to 1], building_type [string], shaking [float]
        Output: Series of (damage_state, percent of bldng_type damaged)
        '''
        result = pd.Series(index = self.dmg_states) 
        curves = self.frag_curves.loc[building_type]
        for dmg_state, curve in curves.iteritems():
            result[dmg_state] = self.buildingsImpacted(building_rate, shaking, curve)
        return result


    def buildingsImpacted(self, building_rate, shaking, curve): 
        '''
        calculate proportion of building_type impacted for a damage state
        Input:  building_count[float, 0-1], shaking [float], curve_std [float]
        Output: proportion of buildings [float]
        '''
        return building_rate * self.probabilityOfDamage(shaking, curve)
        
    
    def probabilityOfDamage(self, shaking, curve): 
        '''
        calculate probability of damage. Returns zero if given non-number.
        Input:  shaking [float], curve of std and x50 [Series of float]
        Output: probability of damage state [float]
        '''
        try:
            float(repr(shaking))
            return 0.5 * (1 + math.erf((math.log(shaking)-math.log(curve.loc['x50']))/
                           (math.sqrt(2)*curve.loc['sigma'])))
        except:
            return 0
      

    def humanImpacts(self, building_type, damage_state, buildings_impacted):       
        '''
        calculate proportion of population in building_type impacted for each injury_type
        Input:  building_type [string], damage_state [string], buildings_impacted [float]
        Output: Series of (injury_state, impact_probability)
        '''
        impact_rates = self.impct_rates[building_type][damage_state]
        result = pd.Series(index = self.injury_states) 
        for injury_state, impact_rate  in impact_rates.iteritems():
            result[injury_state] = buildings_impacted * impact_rate    
        return result
    
    
    def buildingPop(self, vdc_data):
        '''
        calcuate the number of people in each building type
        Input:  vdc_data [Series]
        Output: people in given building type [int]
        '''   
        return vdc_data.loc['pop'] / sum(vdc_data.loc[self.bldng_types])
        #TODO: factor this out so buildingPop is in vdc_data
    

    def computeImpacts(self):
        '''
        calculate impacts in a vdc for a given eq scenerio
        output: Series of (injury_state, number of people impacted)    
        '''
        result = pd.Series(index = self.injury_states) 
        
        for building_type in self.bldng_types:
            building_rate = self.buildingRate(building_type, self.data)
            building_impacts = self.buildingImpacts(building_rate, building_type, self.shaking)
        
            for damage_state, buildings_impacted in building_impacts.iteritems():
                human_impacts = self.humanImpacts(building_type, damage_state, buildings_impacted)
                
                for injury_state, impact_probability in human_impacts.iteritems():
                    result.loc[injury_state] += (impact_probability * self.buildingPop(self.data))
                  
        return result 
