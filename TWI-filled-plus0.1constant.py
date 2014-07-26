"""
TWI-filled-plus0.1constant.py
Topographic Wetness Index 
2013-11-12
Jeffrey Wolf (EEB); G. Andrew Fricker (GEOG)
UCLA

This script was written to be used as a tool in ArcGIS.  This python script can be imported to create a TWI tool.  Inputs are the workspace and the input DEM, output is the TWI layer
We chose to fill all sinks due to some small sinks in a lidar redived DEM.  We also add a small constant to the denominator to avoid dividng by zero.  

The original script was based off the arcpy script written by Prasad Pathak.
http://arcscripts.esri.com/details.asp?dbid=16750

This revised script converts the terrain slope in degrees to radians
This script also uses the default settings for the flow accumulation raster
however different methods to calculate flow accumulation can dramtically change the results of the TWI

"""

import arcpy, math


if __name__ == '__main__':
	arcpy.CheckOutExtension("Spatial")
	
	# Define workspace and set input and output files
	arcpy.env.workspace = arcpy.GetParameterAsText(0)
	inDEM = arcpy.GetParameterAsText(1)
	outTWI = arcpy.GetParameterAsText(2)

	# Intermediates
	arcpy.AddMessage("Filling DEM.\n")
	DEM_filled = arcpy.sa.Fill(inDEM)
	
	arcpy.AddMessage("Creating flow direction.\n")
	outFlowDirection = arcpy.sa.FlowDirection(DEM_filled, "FORCE")
	
	
	arcpy.AddMessage("Creating flow accumulation.\n")
	#outFlowAccumulation = arcpy.sa.FlowAccumulation(outFlowDirection, "", "FLOAT") + 1 
	outFlowAccumulation = arcpy.sa.FlowAccumulation(outFlowDirection, "", "INTEGER") + 1 
	
	arcpy.AddMessage("Creating slope.\n")
	slope = arcpy.sa.Slope(DEM_filled)
	

	arcpy.AddMessage("Converting slope in degrees to slope in radians")
	# 2Pi radians = 360 degrees
	# Pi radians = 180 degrees
	# conversion: Pi radians/180 degress
	slope_radians = slope * math.pi/180.0
	
	# Output
	arcpy.AddMessage("Creating TWI\n")
	TWI = arcpy.sa.Ln(outFlowAccumulation / (arcpy.sa.Tan(slope_radians)+.01))
	TWI.save(outTWI)
	arcpy.AddMessage("Saved TWI. Done.")
	
