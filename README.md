# USGS

Rasterio is a powerful Python library used for reading a raster image file. Rasterio is dependent on GDAL and georasters library, which use specific Python packages at specific versions. Due to this criterion, anaconda distribution is used for package management and deployment. Georasters work well with python version 3.5 or 3.10. The Python version used for this project is 3.10.4. To setup and use georasters, a virtual environment is created using anaconda command prompt. The order of installation of the python packages are as follows: GDAL, georasters, rasterio, os, uuid, and math.

Follow the below steps for setting up the environment:

conda create -n geoEnv python=3.9
conda activate geoEnv
conda install -c conda-forge gdal
conda install -c conda-forge rasterio
conda install -c conda-forge georasters
conda install -c jmcmurray os
conda install -c conda-forge r-uuid
conda install -c conda-forge python-markdown-math
conda install flask

Note: If the scrapper isn't set up then use the below link to download .tif files and place it in the folder along with 'app.py'.
https://prd-tnm.s3.amazonaws.com/index.html?prefix=StagedProducts/Elevation/13/TIFF/current/
