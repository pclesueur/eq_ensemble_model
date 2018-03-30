"""
Main class to compute ensemble model, given a series of eqs.
V1.0
Prepared by: Philip LeSueur
Date: March 30, 2018

"""
  
'''
have one more external python file that get's the inputs and runs the EnsembleModel Class.
     
Class EnsembleModel
    initialize
    get all the data
    'comment that defines model iteration'
    
    def eqImpacts()
        result = dataframe of vdc x impact state
        
        for vdc in vdc
        result = {}, series for each impact_state
        
            for exposure_condition in exposure_conditions
                make cur_vdc_scenerio
                compute impacts
                update results table ()
            
            update results table, dataframe of vdc x impact_state
    
    def exportData()
        export current 3d frame into master csv's, which are (eq x vdc) organized by impact type
        calculate summary values, export summary to 3 master csv's.
    
    def ensembleModel()
        result = 3d data [eq, vdc, impact_state]
        for eq in eqs
            eqImpacts(shaking)
            update results table
    
        export_data
'''


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

