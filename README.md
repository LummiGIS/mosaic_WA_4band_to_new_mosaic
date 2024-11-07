# mosaic_WA_4band_to_new_mosaic


Participating organization can receive 4-band 6"-imagery for various Washington State Counties.  As a member of the Northwest Indian Fisheries Commission (NWIFC) Lummi (and other participating tribes) can also access these 4-band 6"-images via the NWIFC.

These images are distributed as ~1.5 mile by 2.15 mile TIFF tiles.  While these images can easily be incorporated into an ESRI raster mosaic dataset the raster mosaic dataset is clunky and slow to render even on my GIS specific (and relatively new) computer.  Also, the raster mosaic dataset is not usable in QGIS which offers a more satisfying GIS experience due to its intuitive interface and under-bloated architecture. Furthermore, many of my projects are smaller area projects scattered throughout the Lummi U and A.  A full raster mosaic dataset only complicates and delays GIS project development when only a few mosaic tiles are required for a project.

Individual images tiles can be mosaic'd together using the Esri Mosaic to Raster geoprocessing tool.  This tool does a fine job of mosaicking the raster but you need to either manually enter the tiles into the tool.

The distributed imagery also includes an ESRI shapefile of image footprints and these data include the individual time names.

This mosaic WA 4 Band to new mosaic ArcGIS Pro Scripting tool will take a selection of the shapefile image footprints and automate the mosaic process resulting in a new output raster file for the area of interest.  Simply add the image footprint data to your ArcGIS Pro project, zoom to the area of interest, select the tiles you want to mosaic, and execute the tool.  The selected images will be mosaicked for you automatically with the full accompaniment of the mosaic to new raster input parameters available to you.  

Developed with ArcGIS Pro v3.3 and Wing Pro IDE for Python.
11/7/2024
