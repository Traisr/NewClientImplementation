# -*- coding: utf-8 -*-
"""
Created on Fri Dec 04 13:10:36 2015

@author: nwade
"""
import arcpy
import os
ClientFolder = arcpy.GetParameterAsText(0)
ClientName = arcpy.GetParameterAsText(1)
Parcels = arcpy.GetParameterAsText(2)
FileGDB = os.path.join(ClientFolder,ClientName + ".gdb")
FeatureDatasetPath = os.path.join(FileGDB, "BaseLayers")
NewParcels = os.path.join(FeatureDatasetPath,"Parcels")

def createGDB(ClientFolder, ClientName):
    arcpy.management.CreateFileGDB(ClientFolder, ClientName)
    arcpy.management.CreateFeatureDataset(FileGDB,"BaseLayers",Parcels)

def copyParcels(Parcels,FeatureDatasetPath):
    arcpy.CreateFeatureclass_management(FeatureDatasetPath, "Parcels", "POLYGON", r'I:\GIS\Clients\Template and Internal\TemplateGDB.gdb\Template_Feautre_Dataset\Template_Parcels', has_m="DISABLED", has_z="DISABLED", spatial_reference="PROJCS['NAD_1983_StatePlane_Pennsylvania_South_FIPS_3702_Feet',GEOGCS['GCS_North_American_1983',DATUM['D_North_American_1983',SPHEROID['GRS_1980',6378137.0,298.257222101]],PRIMEM['Greenwich',0.0],UNIT['Degree',0.0174532925199433]],PROJECTION['Lambert_Conformal_Conic'],PARAMETER['False_Easting',1968500.0],PARAMETER['False_Northing',0.0],PARAMETER['Central_Meridian',-77.75],PARAMETER['Standard_Parallel_1',39.93333333333333],PARAMETER['Standard_Parallel_2',40.96666666666667],PARAMETER['Latitude_Of_Origin',39.33333333333334],UNIT['Foot_US',0.3048006096012192]];-119214200 -96198500 3048.00609601219;-100000 10000;-100000 10000;3.28083333333333E-03;0.001;0.001;IsHighPrecision")
    arcpy.Append_management(Parcels,NewParcels,"NO_TEST")
def copyStreets
createGDB(ClientFolder, ClientName)
copyParcels(Parcels,FeatureDatasetPath)