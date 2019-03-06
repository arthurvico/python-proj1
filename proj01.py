# -*- coding: utf-8 -*-
"""
Created on Sun Sep  9 15:49:36 2018

@author: arthu
"""

#First python program

#Input the rods
input_rods = input ("Input rods: ")
#Print their Input
input_rods_float = float(input_rods)
input_rods_str = str(inputs_rods_float)
print ("You input "+ input_rods_str + " rods.")
#Convert to meters
meters = input_rods_float * 5.0292
#Convert to feet
feet = meters / 0.3048
#Convert to miles
mile = meters / 1609.34
#Convert to furlongs
furlongs = input_rods_float / 40
#Convert to minutes to walk
minutes_to_walk = mile/3.1*60
#Round all values to 3 decimals
meters = round(meters,3)
feet = round(feet,3)
mile = round(mile,3)
furlongs = round (furlongs,3)
minutes_to_walk = round (minutes_to_walk,3)
#Convert all floats back to string
meters_str = str(meters)
feet_str = str(feet)
mile_str = str(mile)
furlongs_str = str(furlongs)
minutes_to_walk_str = str(minutes_to_walk)
#Print all new calculated values
print ("Conversions")
print ("Meters: "+meters_str)
print ("Feet: "+feet_str)
print ("Miles: "+mile_str)
print ("Furlongs: "+furlongs_str)
print ("Minutes to walk "+ input_rods_str+" rods: "+minutes_to_walk_str)


