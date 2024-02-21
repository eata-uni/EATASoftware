import warnings
from GOESutils.GlobalVars import *
from datetime import datetime, timedelta, timezone
import os, time
from IPython.display import display, Image, clear_output
import numpy as np
import GOESutils.GOESplots as gplt
import GOESutils.GOESimport as gimp
import GOESutils.DataBaseUtils as dbu
import GOESutils.NOAAquery as noaa

toDisplay = False
toUpload = True

clear_output(wait=True)
CurrentTime = datetime.now(utcm5)
CurrentTime_str = CurrentTime.strftime('%Y-%m-%d %H:%M:%S %Z')
print("============================================================")
print("Current time is: {}".format(CurrentTime_str))
# gFileList = gimp.GOESfiles("latest", target_product="ABI-L2-MCMIP", download=True)
# f = gFileList.iloc[0]
# RGBdata = gimp.GeoColorData(os.path.join(destination_path,f["file"]))
RGBdata = noaa.GeoColorTif()
figGeo, axGeo = gplt.GeoColorPlot(RGBdata, toSave=True, toDisplay=toDisplay, toUpload=False, dpi=150)
prodFileList = gimp.GOESfiles("latest", target_product=products, to_display=toDisplay, download=True, overwrite=True)
for product in products:
    f = prodFileList[prodFileList["product"]==product].iloc[0]
    FullFileName = os.path.join(destination_path,f["file"])
    data, ProductParams = gimp.ImportingData(FullFileName, product)
    data = gimp.CleaningData(data, product)
    data_re = gimp.interpolate_products(data, product, n=5)
                                                
    print("Working with file: {}".format(os.path.basename(f['file'])))                
    FullImageName = os.path.join(ProductParams["ImagePath"],"Peru",ProductParams["ImageName"])
    if os.path.exists(FullImageName): # If png image exists, it is shown
        print("Image [{}] already exists in [{}]".format(ProductParams["ImageName"],ProductParams["ImagePath"]))
        display(Image(filename=FullImageName)) # , width=540   
    else: # Creating png image
        if not os.path.exists(ProductParams["ImagePath"]):
            print(f"Directory for product {product} does not exist. Creating new one...") 
            os.makedirs(ProductParams["ImagePath"])
        print(f"Image for file {os.path.basename(f['file'])} not found, creating one...")
        figProd = gplt.ProductPlot(data_re, product, axGeo, ProductParams, toSave=True, toDisplay=toDisplay, toUpload=toUpload, dpi=150)

    # # try: # Deleting downloaded product
    # #     os.remove(FullFileName)
    # #     print(f"File '{FullFileName}' has been removed.")
    # # except FileNotFoundError:
    # #     print(f"File '{FullFileName}' not found.")
    # # except Exception as e:
    # #     print(f"An error occurred while deleting the file: {e}")
        
    for dep in gplt.departments:
        gplt.DepartmentPlot(product, dep, RGBdata, data_re, ProductParams, toSave=True, toDisplay=False, toUpload=toUpload)
    if not "DMWV" in product:
        reports = gplt.ReportingEvents(data, product, level="L3", send_comments=toUpload)
        
    print("All the files have been processed.")
    
    
try: # Check if it's time to clear the output
    CurrentTime = datetime.now(utcm5)
    hour, minute, seconds = CurrentTime.hour, CurrentTime.minute, CurrentTime.second
        
    total_remaining_seconds = (5 - (int(minute) % 5)) * 60 - int(seconds)
    remaining_minutes = total_remaining_seconds // 60
    print("Waiting {} minutes for the next file upload".format(remaining_minutes + 2))
    time.sleep((remaining_minutes+2)*60)
except Exception as e:
    print("Elapsed time attempting failed.")