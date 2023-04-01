import argparse
from selenium import webdriver
import time

parser = argparse.ArgumentParser()
parser.add_argument('--list', type=str, required=False)
args = parser.parse_args()

if hasattr(args, 'list') is False:
    print("no arguments  received, exiting")
    exit()

opts = webdriver.ChromeOptions()
#opts.add_argument('headless') #seems not working in headless withouth additional thinkering
prefs = {"download.default_directory" : r"c:\dpreview"}
#example: prefs = {"download.default_directory" : "c:\dpreview"}
opts.add_experimental_option("prefs",prefs)

#add chromedriver excutable path if necessary, like folder path is not in PATH variable
#driver = webdriver.Chrome(executable_path=r"C:\Tools\chromedriver.exe", options=opts)
driver = webdriver.Chrome(options=opts)
driver.get("https://www.dpreview.com/")
#print(driver.title)
time.sleep(10)

with open(args.list, 'r') as list_file:
    for url in list_file:
        try:
            #sec to wait after each download
            waitInSec = 20 if url.endswith('jpg') else 60
            driver.get(url)
            time.sleep(waitInSec)
        except Exception as ex:
            print("failed to download ", url)

#final wait... 
time.sleep(60)
