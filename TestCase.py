from urllib2 import *
from selenium import webdriver
import sqlite3

PageAddress = 'http://80.191.93.206'

FeaturesHook ='''
window.x = 0 ;

Object.defineProperty(baseAudioContext, "sampleRate", {
    	value: new Proxy(baseAudioContext.sampleRate, {
    		get: function(target, name) {    			
    			window.x++
    			return target[name];
    		}
    	})
    });
'''

GetResults = '''
return window.x;
'''





driver = webdriver.Chrome()

driver.get(PageAddress)


driver.execute_script(FeaturesHook)
time.sleep(5)

Results = driver.execute_script(GetResults)


print Results