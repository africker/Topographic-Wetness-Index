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
