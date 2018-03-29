# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

"""
Given an earthquake and exposure condition

import inputs
    **this needs to store all the look up tables, and needs 
    to be stored with result.

def vdc_impacts....
    inputs = getVdcData(vdc);

    result = [fatalities, injury1, injury2]

    For building_type in building_types
        Calculate % complete damage, % collapse, etc.
            a function
        Calculate population, given VDC, building type
            a function that defines how this is calculated
    
        For damage_type in damage_types
            Calculate number of people in damage_type & building_type, (could also be percent of pop)
                pop_per_building * % damaged    
            Calculate injury_types (fatalities, injuries)
                a function, takes building_type, damage_type, population_rate in damaged building type;
            returns array
            update results array                
       End For
    End For

    return result 
 
       
def quake_impacts....
    
    result = [data table of vdc]
    For vdc in vdcs
        vdc_impacts = vdc_impacts(vdc)    
        add impacts to results table
    End For
    
    summarizeAndStore(result)
        function to finalize all data stuff
        
def summarizeAndStore

    take the big table and get key metrics
        function to summarize(result)
    add results, key metrics, and inputs to database.

def nepal_quakes()

    get all input data going

    For quake in quakes
        quake_impacts(quake,...)
    End For

nepal_quakes();
    
"""
