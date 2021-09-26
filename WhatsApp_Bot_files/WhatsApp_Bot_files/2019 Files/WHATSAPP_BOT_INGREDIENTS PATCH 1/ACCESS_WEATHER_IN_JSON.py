# -*- coding: utf-8 -*-
"""
Created on Thu May  2 09:23:47 2019

@author: chinjooern
"""

# import json library
import json
import urllib
# request url
urlreq = 'http://www.weather.gov.sg/wp-content/themes/wiptheme/js/function_resizer.js'
# get response
response = urllib.request.urlopen(urlreq)
# load as json
jresponse = json.load(response)
print(jresponse)