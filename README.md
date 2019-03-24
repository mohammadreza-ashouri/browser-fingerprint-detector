## FingerprintingDetector
Python based Application to Detect websites which are running fingerprinting scripts.

### Usage:

```
usage: fingerdetector [-h] [-v] Address

positional arguments:
  Address     Website address to check for fingerprinting scripts e.g.
              http://80.191.93.206

optional arguments:
  -h, --help  show this help message and exit
  -v          increase output verbosity
```
## Required Python Modules (Needed to be installed)
* BeautifulSoup4 - pip install beautifulsoup4
* Selenium WebDriver - pip install selenium

## Other Requirements
* Chrome Webdriver - https://sites.google.com/a/chromium.org/chromedriver/downloads

## Features
### Plugins List
Detection of Attempts to access `navigator.plugins`

### UserAgent
Detection of Attempts to access `navigator.userAgent`

### Language
Detection of Attempts to access `navigator.userAgent`

### Languages
Detection of Attempts to access `navigator.languages`

### CpuClass
Detection of Attempts to access `navigator.cpuClass`

### Geolocation
Detection of Attempts to access `navigator.geolocation`

### Platform
Detection of Attempts to access `navigator.platform`

### Hardware Concurrency
Detection of Attempts to access `navigator.hardwareConcurrency`

### Available Memory
Detection of Attempts to access `navigator.deviceMemory`

### DoNotTrack
Detection of Attempts to access `navigator.doNotTrack`

### appName
Detection of Attempts to access `navigator.appName`

### Connection
Detection of Attempts to access `navigator.connection`

### ColorDepth
Detection of Attempts to access `window.colorDepth`

### Screen Specifications
Detection of Attempts to access `window.height` and `window.width`

### LocalStorage
Detection of Attempts to access `window.localStorage`

### SessionStorage
Detection of Attempts to access `window.sessionStorage`

### IndexedDB
Detection of Attempts to access `window.indexedDB`

### WebRTC
Detection of Attempts to access `window.RTCPeerConnection`

### AudioContext
Detection of Attempts to access `window.AudioContext`

### Canvas Fingerprinting
Detection of Attempts to access `document.createElement('canvas')` and `toDataURL()` simultaneously

