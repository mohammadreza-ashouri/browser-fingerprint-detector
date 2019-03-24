from urllib2 import *
from selenium import webdriver
import sqlite3

PageAddress = 'http://80.191.93.206'

FeaturesHook ='''
window.x = 0 ;

var origgetextension = MediaDevices.prototype.enumerateDevices;
MediaDevices.prototype.enumerateDevices = function() {
  var r = origgetextension.apply(this, arguments);
  console.log('hoooooooooooooo');
  return r;
};
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