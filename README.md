# USGS

Rasterio is a powerful Python library used for reading a raster image file. Rasterio is dependent on GDAL and georasters library, which use specific Python packages at specific versions. Due to this criterion, anaconda distribution is used for package management and deployment. Georasters work well with python version 3.5 or 3.10. The Python version used for this project is 3.10.4. To setup and use georasters, a virtual environment is created using anaconda command prompt. The order of installation of the python packages are as follows: GDAL, georasters, rasterio, os, uuid, and math.

Follow the below steps for setting up the environment:

1.conda create -n geoEnv python=3.9
2.conda activate geoEnv
3.conda install -c conda-forge gdal
4.conda install -c conda-forge rasterio
5.conda install -c conda-forge georasters
6.conda install -c jmcmurray os
7.conda install -c conda-forge r-uuid
8.conda install -c conda-forge python-markdown-math
9.conda install flask

Note: If the scrapper isn't set up then use the below link to download .tif files and place it in the folder along with 'app.py'.
https://prd-tnm.s3.amazonaws.com/index.html?prefix=StagedProducts/Elevation/13/TIFF/current/
