# USGS

Rasterio is a powerful Python library used for reading a raster image file. Rasterio is dependent on GDAL and georasters library, which use specific Python packages at specific versions. Due to this criterion, anaconda distribution is used for package management and deployment. Georasters work well with python version 3.5 or 3.10. The Python version used for this project is 3.10.4. To setup and use georasters, a virtual environment is created using anaconda command prompt. The order of installation of the python packages are as follows: GDAL, georasters, rasterio, os, uuid, and math.

Follow the below steps for setting up the environment:
<ul>
<li>conda create -n geoEnv python=3.10.4</li>
<li>conda activate geoEnv</li>
<li>conda install -c conda-forge gdal</li>
<li>conda install -c conda-forge rasterio</li>
<li>conda install -c conda-forge georasters</li>
<li>conda install -c jmcmurray os</li>
<li>conda install -c conda-forge r-uuid</li>
<li>conda install -c conda-forge python-markdown-math</li>
<li>conda install flask</li>
</ul>

or 

<ul>
<li>conda create -n geoEnv python=3.10.4</li>
<li>conda install -c conda-forge gdal=3.5.2 rvlib rasterio</li>
<li>pip install git+https://github.com/ozak/georasters flask</li>
<li>conda install -c jmcmurray os</li>
<li>conda install -c conda-forge r-uuid</li>
<li>conda install -c conda-forge python-markdown-math</li>
<li>conda install flask</li>
</ul>

Note: If the scrapper isn't set up then use the below link to download .tif files and place it in the folder along with 'app.py'.
https://prd-tnm.s3.amazonaws.com/index.html?prefix=StagedProducts/Elevation/13/TIFF/current/
