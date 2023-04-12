from selenium import webdriver
import time
import io
import requests
from bs4 import BeautifulSoup
PATH ="C:\Program Files (x86)\chromedriver.exe"
driver = webdriver.Chrome(PATH)
from time import sleep
#List contains all the .tiff file names of Ohio to download
list = ["n39w082/", "n39w083/", "n39w084/", "n39w085/", "n40w081/", "n40w082/", "n40w083/", "n40w084/", "n40w085/",
"n41w081/", "n41w082/", "n41w083/", "n41w084/", "n41w085/",
"n42w081/", "n42w082/", "n42w083/", "n42w084/", "n42w085/"]
dictionary = []
for i in range(len(list)):
    page_url ="https://prd-tnm.s3.amazonaws.com/index.html?prefix=StagedProducts/Elevation/13/TIFF/current/"+str(list[i])
    driver.get(page_url)
    sleep(5)
    soup = BeautifulSoup(driver.page_source,'html.parser')
    listing = soup.find('div',id="listing")
    links = []
    for link in listing.findAll("a"):
      href = link.get('href')
      links.append(href)
      tiff_url= links[3]
    r = requests.get(tiff_url, allow_redirects=True)
    open('USGS_13_'+str(list[i].strip('/'))+'.tif', 
                        'wb').write(r.content)
driver.quit()
