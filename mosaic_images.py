import arcpy
import sys
import traceback

try:
    arcpy.AddMessage('Running mosaic images...')
  
##These are the hard coded paths for testing
    ##This is the path to the vector feature class that shows the footprint of the imagery.  This file needs to contain a field that includeds the name of the imagery.....
    #in_fc = r"_Whatcom_County_1ft_2023_HXIP_Ortho_Tile_Index_WSPS_HARN"
    ##the field name from the featureclass storing the file names.
    #in_field = r"NAME"
    ##this is the folder that is storing all of the image files
    #in_folder = r"I:\Aerial\2023\WashingtonState4BandImages\Whatcom_County"
    ##This is the output file location
    #output_location = r'C:\gTemp\\'
    ##output file name with extension
    #raster_dataset_name_with_extension = 'A1_FUBAR.tif'
    #coordinate_system_for_the_raster = None
    #pixel_type = None
    #cellsize = None
    #number_of_bands = '4'
    #mosaic_method = None
    #mosaic_colormap_mode = None
    
    
    #This is the path to the vector feature class that shows the footprint of the imagery.  This file needs to contain a field that includeds the name of the imagery.....
    in_fc = arcpy.GetParameterAsText(0)
    #the field name from the featureclass storing the file names.
    in_field = arcpy.GetParameterAsText(1)
    #this is the folder that is storing all of the image files
    in_folder = arcpy.GetParameterAsText(2)
    #This is the output file location
    output_location = arcpy.GetParameterAsText(3)
    #output file name with extension
    raster_dataset_name_with_extension = arcpy.GetParameterAsText(4)

    coordinate_system_for_the_raster = arcpy.GetParameterAsText(5)
    if coordinate_system_for_the_raster == '' or coordinate_system_for_the_raster is None:
        coordinate_system_for_the_raster = None    

    pixel_type = arcpy.GetParameterAsText(6)
    if pixel_type == '' or pixel_type is None:
        pixel_type = None    
    
    cellsize = arcpy.GetParameterAsText(7)
    if cellsize == '' or cellsize is None:
        cellsize = None    
    
    number_of_bands = arcpy.GetParameterAsText(8)
    if number_of_bands == '' or  number_of_bands is None:
        number_of_bands = None    
    
    mosaic_method = arcpy.GetParameterAsText(9)
    if mosaic_method == '' or mosaic_method is None:
        mosaic_method = None    
    
    mosaic_colormap_mode = arcpy.GetParameterAsText(10)
    if mosaic_colormap_mode == '' or mosaic_colormap_mode is None:
        mosaic_colormap_mode = None    
    

    fields = [in_field]
    
    in_files = ""
    with arcpy.da.SearchCursor(in_fc, fields) as cursor:
        for row in cursor:
            in_files = in_files + in_folder + '\\' + row[0] + ".tif ; "
    in_files = in_files[:-2]
    arcpy.AddMessage(in_files)
    arcpy.AddMessage('Raster list complete, mosaicing now.  Please stand by - this could take a while.')
    arcpy.MosaicToNewRaster_management(in_files, output_location, raster_dataset_name_with_extension, coordinate_system_for_the_raster,pixel_type, cellsize, number_of_bands,  mosaic_method, mosaic_colormap_mode)
    arcpy.AddMessage('Finished without error...')
except:
    tb = sys.exc_info()[2]
    tbinfo = traceback.format_tb(tb)[0]
    arcpy.AddMessage("PYTHON ERRORS:\nTraceback info:\n" + tbinfo + "\nError Info:\n" + str(sys.exc_info()[1]))
    