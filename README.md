# DP Review Crawlers

#### studio_image_crawler.py
file to automatically download DP Review Studio comparision tool. It is using file dump list from [ReclusiveEagle's DPReview-Studio-Archive](https://github.com/ReclusiveEagle/DPReview-Studio-Archive) repositoy (URL Dump folder). 

###### requires:
<ul>
<li>python 3</li>
<li>selenium</li>
<li>chromdriver tested with Chrome version 11.0.5563.147</li>
</ul>

usage example: 
```ps
python3 studio_image_crawler.py --list 'D:\Projects\Misc\DPReview-Studio-Archive\URL Dump\Olympus RAW Day light.txt'
```

**Note** change the file according to your environmnet:
executable path of chromium webdriver if necessary
waits seconds



