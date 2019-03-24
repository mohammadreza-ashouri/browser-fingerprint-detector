from selenium import webdriver
import collections
import argparse
import re
from urllib2 import *
from bs4 import *
import sqlite3

PageAddress = ''

hrefvalues = []
hrefscripts = []
Linklist = []
FinalResult = collections.defaultdict(dict)
Eventscr = []

def Onchange(evestr):
    try:
        regex = r"""
        (onchange)\s*=(\s*\"\S*\")
        """
        onch = []

        matches = re.finditer(regex, evestr, re.IGNORECASE | re.MULTILINE | re.VERBOSE)
        for matchNum, match in enumerate(matches):
            matchNum = matchNum + 1

            for groupNum in range(0, len(match.groups())):
                groupNum = groupNum + 1
                if groupNum % 2 == 0:
                    onch.append(match.group(groupNum))
        for val in onch:
            stri = str(val)
            stri = stri.replace("\"", "")
            Eventscr.append(stri)
        return onch
    except Exception, e:
        print str(e)
def onClick(evestr):
    try:
        regex = r"""
        (onclick)\s*=(\s*\"\S*\")
        """
        oncl = []

        matches = re.finditer(regex, evestr, re.IGNORECASE | re.MULTILINE | re.VERBOSE)
        for matchNum, match in enumerate(matches):
            matchNum = matchNum + 1

            for groupNum in range(0, len(match.groups())):
                groupNum = groupNum + 1
                if groupNum % 2 == 0:
                    oncl.append(match.group(groupNum))
        for val in oncl:
            stri = str(val)
            stri = stri.replace("\"", "")
            Eventscr.append(stri)
        return oncl
    except Exception, e:
        print str(e)
def onMouseOver(evestr):
    try:
        regex = r"""
        (onmouseover)\s*=(\s*\"\S*\")
        """
        oncl = []

        matches = re.finditer(regex, evestr, re.IGNORECASE | re.MULTILINE | re.VERBOSE)
        for matchNum, match in enumerate(matches):
            matchNum = matchNum + 1

            for groupNum in range(0, len(match.groups())):
                groupNum = groupNum + 1
                if groupNum % 2 == 0:
                    oncl.append(match.group(groupNum))
        for val in oncl:
            stri = str(val)
            stri = stri.replace("\"", "")
            Eventscr.append(stri)
        return oncl
    except Exception, e:
        print str(e)
def onMouseOut(evestr):
    try:
        regex = r"""
        (onmouseout)\s*=(\s*\"\S*\")
        """
        oncl = []

        matches = re.finditer(regex, evestr, re.IGNORECASE | re.MULTILINE | re.VERBOSE)
        for matchNum, match in enumerate(matches):
            matchNum = matchNum + 1

            for groupNum in range(0, len(match.groups())):
                groupNum = groupNum + 1
                if groupNum % 2 == 0:
                    oncl.append(match.group(groupNum))
        for val in oncl:
            stri = str(val)
            stri = stri.replace("\"", "")
            Eventscr.append(stri)
        return oncl
    except Exception, e:
        print str(e)
def onKeydown(evestr):
    try:
        regex = r"""
        (onkeydown)\s*=(\s*\"\S*\")
        """
        oncl = []

        matches = re.finditer(regex, evestr, re.IGNORECASE | re.MULTILINE | re.VERBOSE)
        for matchNum, match in enumerate(matches):
            matchNum = matchNum + 1

            for groupNum in range(0, len(match.groups())):
                groupNum = groupNum + 1
                if groupNum % 2 == 0:
                    oncl.append(match.group(groupNum))
        for val in oncl:
            stri = str(val)
            stri = stri.replace("\"", "")
            Eventscr.append(stri)
        return oncl
    except Exception, e:
        print str(e)
def onLoad(evestr):
    try:
        regex = r"""
        (onload)\s*=(\s*\"\S*\")
        """
        oncl = []

        matches = re.finditer(regex, evestr, re.IGNORECASE | re.MULTILINE | re.VERBOSE)
        for matchNum, match in enumerate(matches):
            matchNum = matchNum + 1

            for groupNum in range(0, len(match.groups())):
                groupNum = groupNum + 1
                if groupNum % 2 == 0:
                    oncl.append(match.group(groupNum))
        for val in oncl:
            stri = str(val)
            stri = stri.replace("\"", "")
            Eventscr.append(stri)
        return oncl
    except Exception, e:
        print str(e)
def onSubmit(evestr):
    try:
        regex = r"""
        (onsubmit)\s*=(\s*\"\S*\")
        """
        oncl = []

        matches = re.finditer(regex, evestr, re.IGNORECASE | re.MULTILINE | re.VERBOSE)
        for matchNum, match in enumerate(matches):
            matchNum = matchNum + 1

            for groupNum in range(0, len(match.groups())):
                groupNum = groupNum + 1
                if groupNum % 2 == 0:
                    oncl.append(match.group(groupNum))
        for val in oncl:
            stri = str(val)
            stri = stri.replace("\"", "")
            Eventscr.append(stri)
        return oncl
    except Exception, e:
        print str(e)

FeaturesHook = '''
window.plugins = 0;
window.useragent = 0;
window.language = 0;
window.languages = 0;
window.cpuclass = 0;
window.platform = 0;
window.doNotTrack = 0;
window.appName = 0;
window.colorDepth = 0;
window.height = 0;
window.width = 0;
window.localstorage = 0;
window.sessionstorage = 0;
window.indexDB = 0;
window.connection = 0;
window.rtc = 0 ;
window.aud = 0;
window.sample = 0;
window.audstate = 0;
window.memory = 0;
window.concurrency = 0;
window.geolocation = 0; 
window.tourl = 0;
window.offsetheight = 0;
window.offsetwidth = 0; 
window.filltext = 0;
window.stroketext = 0;
window.getimagedata = 0;
window.drawarray = 0;
window.glextension = 0;
window.debuginfo = [];

Object.defineProperty(window, "navigator", {
	value: new Proxy(window.navigator, {
    		get: function(target, name) {
    			console.log("navigator property", name, "is read")
			if (name == "plugins") {
				window.plugins++;
			}
			else if (name == "userAgent")
			{
			    window.useragent++;
			}
			else if (name == "language")
    		{
    		    window.language++;
    		}
    		else if (name == "languages")
    		{
    		    window.languages++;
    		}
    		else if (name == "cpuClass")
    		{
                window.cpuclass++;
    		}
    		else if (name == "platform")
    		{
                window.platform++;
    		}
            else if (name == "doNotTrack")
    		{
                window.doNotTrack++;
    		}
            else if (name == "appName")
    		{
                window.appName++;
    		}
    		else if (name == "connection")
    		{
                window.connection++;
    		}
    		else if (name == "deviceMemory")
    		{
                window.memory++;
    		}
    		else if (name == "hardwareConcurrency")
    		{
                window.concurrency++;
    		}
    		else if (name == "geolocation")
    		{
                window.geolocation++;
    		}
    			return target[name];
    		}

	})
});

Object.defineProperty(window, "screen", {
	value: new Proxy(window.screen, {
    		get: function(target, name) {
    			console.log("screen property", name, "is read")
			if (name == "colorDepth") {
				window.colorDepth++;
			}
			else if (name == "height")
			{
			    window.height++;
			}
			else if (name == "width")
			{
			    window.width++;
			}

				return target[name];
    		}
	})
});


Object.defineProperty(window, "localStorage", {
    	value: new Proxy(window.localStorage, {
    		get: function(target, name) {
    			console.log("localStorage property", name, "is read")
    			window.localstorage++
    			return target[name];
    		}
    	})
    });

Object.defineProperty(window, "sessionStorage", {
    	value: new Proxy(window.sessionStorage, {
    		get: function(target, name) {
    			console.log("sessionStorage property", name, "is read")
    			window.sessionstorage++
    			return target[name];
    		}
    	})
    });

Object.defineProperty(window, "indexedDB", {
    	value: new Proxy(window.indexedDB, {
    		get: function(target, name) {
    			console.log("indexedDB property", name, "is read")
    			window.indexDB++
    			return target[name];
    		}
    	})
    });

Object.defineProperty(window, "RTCPeerConnection", {
    	value: new Proxy(window.RTCPeerConnection, {
    		get: function(target, name) {    			
    			window.rtc++
    			return target[name];
    		}
    	})
    });

Object.defineProperty(window, "AudioContext", {
    	value: new Proxy(window.AudioContext, {
    		get: function(target, name) {   			
    			window.aud++
    			return target[name];
    		}
    	})
    });

function findPrototypeProperty(obj, prop) {
    while (!obj.hasOwnProperty(prop)) {
        obj = Object.getPrototypeOf(obj);
    }
    return obj;
}

var property = 'sampleRate';
var proto = findPrototypeProperty(AudioContext.prototype, property);
var desc = Object.getOwnPropertyDescriptor(proto, property);
var getter = desc.get;
desc.get = function() {
    var r = getter.apply(this, arguments);
    window.sample++;
    return r;
};
Object.defineProperty(proto, property, desc);

var stateproto = findPrototypeProperty(AudioContext.prototype, 'state');
var statedesc = Object.getOwnPropertyDescriptor(stateproto, 'state');
var stategetter = statedesc.get;
statedesc.get = function() {
    var r = stategetter.apply(this, arguments);
    window.audstate++;
    return r;
};
Object.defineProperty(stateproto, 'state', statedesc);



var origToDataURL = HTMLCanvasElement.prototype.toDataURL;
HTMLCanvasElement.prototype.toDataURL = function() {
  var r = origToDataURL.apply(this, arguments);
  window.tourl++;
  return r;
  };

var origfilltext = CanvasRenderingContext2D.prototype.fillText;
CanvasRenderingContext2D.prototype.fillText = function() {
  var r = origfilltext.apply(this, arguments);
  window.filltext++;
  return r;
  };

var origstroketext = CanvasRenderingContext2D.prototype.strokeText;
CanvasRenderingContext2D.prototype.strokeText = function() {
  var r = origstroketext.apply(this, arguments);
  window.stroketext++;
  return r;
  };

var origgetimagedata = CanvasRenderingContext2D.prototype.getImageData;
CanvasRenderingContext2D.prototype.getImageData = function() {
  var r = origgetimagedata.apply(this, arguments);
  window.getimagedata++;
  return r;
  };

var origdrawarray = WebGLRenderingContext.prototype.drawArrays;
WebGLRenderingContext.prototype.drawArrays = function() {
  var r = origdrawarray.apply(this, arguments);
  window.drawarray++;
  return r;
  };

var origgetextension = WebGLRenderingContext.prototype.getSupportedExtensions;
WebGLRenderingContext.prototype.getSupportedExtensions = function() {
  var r = origgetextension.apply(this, arguments);
  window.glextension++;
  return r;
  };

var origdebuginfo = WebGLRenderingContext.prototype.getExtension;
WebGLRenderingContext.prototype.getExtension = function() {
  var r = origdebuginfo.apply(this, arguments);

  window.debuginfo.push(arguments);

  return r;
  };

'''
GetResults = '''
return{
plugins: window.plugins,
useragent: window.useragent,
language: window.language,
languages: window.languages,
concurrency: window.concurrency,
cpuclass: window.cpuclass,
platform: window.platform,
DNT: window.doNotTrack,
appname: window.appName,
colorDepth: window.colorDepth,
height: window.height,
width: window.width,
localstorage: window.localstorage,
sessionstorage: window.sessionstorage,
indexdb: window.indexDB,
connection: window.connection,
rtc: window.rtc,
aud: window.aud,
audstate: window.audstate,
sample: window.sample,
memory: window.memory,
geolocation: window.geolocation,
doc: window.doc,
tourl: window.tourl,
offsetheight: window.offsetheight,
offsetwidth: window.offsetwidth,
filltext: window.filltext,
stroketext: window.stroketext,
getimagedata: window.getimagedata,
drawarray: window.drawarray,
getextension: window.glextension,
getdebuginfo: window.debuginfo

}
'''


####
def SourceRetriever(url):
    try:
        return urlopen(url)
    except Exception, e:
        print str(e) + "ridi"
def ClickonButtons(driver):
    try:
        btns = driver.find_elements_by_tag_name("button")
        for button in btns:
            try:
                if button.is_displayed() and button.is_enabled():
                    button.click()
            except Exception, e:
                pass

        inpbuttons = driver.find_elements_by_tag_name("input")
        for inpbutt in inpbuttons:
            if inpbutt.get_attribute("type") == "button":
                try:
                    if inpbutt.is_displayed() and inpbutt.is_enabled():
                        inpbutt.click()
                except Exception, e:
                    pass

    except Exception, e:
        print str(e)
def hrefExtract(driver):
    try:
        lnks = driver.find_elements_by_tag_name("a")
        for link in lnks:
            hrefvalues.append(link.get_attribute("href"))
        for value in hrefvalues:
            if value != None:
                if "javascript:" in value:
                    hrefscripts.append(value)
                else:
                    try:
                        # temp = PageAddress
                        # temp = temp[:4] + 's' + temp[4:]
                        # if  str(value).find(temp) != -1 or str(value).find(PageAddress) != -1:
                        Linklist.append(value)
                    except Exception, e:
                        print str(e)
    except Exception, e:
        print str(e)
def RemoveDuplicates():
    try:
        if PageAddress in Linklist:
            Linklist.remove(PageAddress)
        if PageAddress + "/" in Linklist:
            Linklist.remove(PageAddress + "/")
        if PageAddress + "#" in Linklist:
            Linklist.remove(PageAddress + "#")

        for val in Linklist:
            if val == "":
                Linklist.remove(val)
            if len(val) > len(PageAddress) + 2:
                if val[len(PageAddress) + 1] == "#":
                    Linklist.remove(val)
                elif val[len(PageAddress) + 1] == "/" and val[len(PageAddress) + 2] == "#":
                    Linklist.remove(val)
    except Exception, e:
        print str(e)
def bodyloadExecutor(driver):
    loadexec = '''
    var load_event = document.createEvent('Event');  
	load_event.initEvent('load', false, false);  
	window.dispatchEvent(load_event);
    '''
    try:
        driver.execute_script(loadexec)
    except:
        pass
def surfer(driver):
    if len(Linklist) > 100:
        print "Process of scanning may take a while"
    for address in Linklist:
        print "Working on Link " + str(address)
        try:
            driver.implicitly_wait(3)
            driver.get(address)
            driver.execute_script(FeaturesHook)
        except Exception, e:
            pass

        try:
            driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")

        except Exception, e:
            pass

        AddressSource = SourceRetriever(address)
        bodyloadExecutor(driver)
        ClickonButtons(driver)
        try:
            BeautifulSource = BeautifulSoup(AddressSource, 'html.parser')
            StrSource = BeautifulSource.prettify()
            StrSource = StrSource.replace(" = ", "=")
            StrSource = StrSource.replace("= ", "=")
            StrSource = StrSource.replace(" =", "=")
        except Exception, e:
            print str(e)

        onLoad(StrSource.encode('utf-8').strip())
        Onchange(StrSource.encode('utf-8').strip())
        onClick(StrSource.encode('utf-8').strip())
        onMouseOver(StrSource.encode('utf-8').strip())
        onMouseOut(StrSource.encode('utf-8').strip())
        onKeydown(StrSource.encode('utf-8').strip())
        onSubmit(StrSource.encode('utf-8').strip())

        EventExecutor(driver)
        Eventscr[:] = []
        try:
            res = driver.execute_script(GetResults)
            FinalResult[address]["plugins"] = res["plugins"]
            FinalResult[address]["useragent"] = res["useragent"]
            FinalResult[address]["language"] = res["language"]
            FinalResult[address]["languages"] = res["languages"]
            FinalResult[address]["cpuclass"] = res["cpuclass"]
            FinalResult[address]["platform"] = res["platform"]
            FinalResult[address]["DNT"] = res["DNT"]
            FinalResult[address]["appname"] = res["appname"]
            FinalResult[address]["colorDepth"] = res["colorDepth"]
            FinalResult[address]["height"] = res["height"]
            FinalResult[address]["width"] = res["width"]
            FinalResult[address]["localstorage"] = res["localstorage"]
            FinalResult[address]["sessionstorage"] = res["sessionstorage"]
            FinalResult[address]["indexdb"] = res["indexdb"]
            FinalResult[address]["connection"] = res["connection"]
            FinalResult[address]["rtc"] = res["rtc"]

            audioFunc = res["aud"]
            samplerate = res["sample"]
            audstate = res["audstate"]
            if audioFunc > 0 and samplerate > 0 and audstate > 0:
                FinalResult[address]["aud"] = 1
            else:
                FinalResult[address]["aud"] = 0

            FinalResult[address]["memory"] = res["memory"]
            FinalResult[address]["concurrency"] = res["concurrency"]
            FinalResult[address]["geolocation"] = res["geolocation"]
            tourl = res["tourl"]
            filltext = res["filltext"]
            stroketext = res["stroketext"]
            getimagedata = res["getimagedata"]
            if (tourl > 0 and stroketext > 0) or (getimagedata > 0 and stroketext > 0) or (
                    tourl > 0 and filltext > 0) or (getimagedata > 0 and filltext > 0):
                FinalResult[address]["canvas"] = 1
            else:
                FinalResult[address]["canvas"] = 0
            debugelem = res["getdebuginfo"]
            drawarray = res["drawarray"]
            glextensions = res["getextension"]
            debugcount = 0
            if debugelem != None:
                for i in range(0, len(debugelem)):
                    if debugelem[i][0] == "WEBGL_debug_renderer_info":
                        debugcount += 1
            if (drawarray > 0 and glextensions > 0 and debugcount > 0 and tourl > 0):
                FinalResult[address]["webgl"] = 1
            else:
                FinalResult[address]["webgl"] = 0
            LinksToDatabase(address)
        except Exception, e:
            print str(e)
def EventExecutor(driver):
    if len(Eventscr) > 0:
        try:
            for ev in Eventscr:
                driver.execute_script(ev)
        except Exception, e:
            pass
def IndexToDatabase():
    try:
        db = sqlite3.connect(str(args.output) + ".db")
        cursor = db.cursor()
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS IndexPage(id INTEGER PRIMARY KEY AUTOINCREMENT ,PageAddress TEXT , plugins INTEGER,
                               useragent INTEGER, language INTEGER , languages INTEGER , concurrency INTEGER,
                               cpuclass INTEGER , platform INTEGER , DNT INTEGER , appname INTEGER , colorDepth INTEGER,
                               height INTEGER , width INTEGER , localstorage INTEGER , sessionstorage INTEGER , 
                               indexdb INTEGER,connection INTEGER , rtc INTEGER , aud INTEGER , memory INTEGER , geolocation INTEGER ,
                               canvas INTEGER,webgl INTEGER)
        ''')
        db.commit()
        cursor.execute('''INSERT INTO IndexPage(PageAddress, plugins, useragent, language, languages, concurrency,
                          cpuclass, platform, DNT, appname, colorDepth, height, width, localstorage, sessionstorage, 
                          indexdb, connection, rtc, aud, memory, geolocation, canvas, webgl)
                          VALUES(?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)''',
                       (PageAddress, FinalResult[PageAddress]["plugins"], FinalResult[PageAddress]["useragent"],
                        FinalResult[PageAddress]["language"],
                        FinalResult[PageAddress]["languages"], FinalResult[PageAddress]["concurrency"],
                        FinalResult[PageAddress]["cpuclass"],
                        FinalResult[PageAddress]["platform"], FinalResult[PageAddress]["DNT"],
                        FinalResult[PageAddress]["appname"], FinalResult[PageAddress]["colorDepth"],
                        FinalResult[PageAddress]["height"], FinalResult[PageAddress]["width"],
                        FinalResult[PageAddress]["localstorage"], FinalResult[PageAddress]["sessionstorage"],
                        FinalResult[PageAddress]["indexdb"], FinalResult[PageAddress]["connection"],
                        FinalResult[PageAddress]["rtc"], FinalResult[PageAddress]["aud"],
                        FinalResult[PageAddress]["memory"], FinalResult[PageAddress]["geolocation"],
                        FinalResult[PageAddress]["canvas"], FinalResult[PageAddress]["webgl"]))

        db.commit()
    except Exception as e:
        print str(e)
        db.rollback()

    finally:
        db.close()
def LinksToDatabase(address):
    try:
        db = sqlite3.connect(str(args.output) + ".db")
        cursor = db.cursor()
        cursor.execute('''
                CREATE TABLE IF NOT EXISTS Links(id INTEGER PRIMARY KEY AUTOINCREMENT,PageAddress TEXT , LinkAddress TEXT ,  plugins INTEGER,
                                   useragent INTEGER, language INTEGER , languages INTEGER , concurrency INTEGER,
                                   cpuclass INTEGER , platform INTEGER , DNT INTEGER , appname INTEGER , colorDepth INTEGER,
                                   height INTEGER , width INTEGER , localstorage INTEGER , sessionstorage INTEGER , 
                                   indexdb INTEGER,connection INTEGER , rtc INTEGER , aud INTEGER , memory INTEGER , geolocation INTEGER ,
                                   canvas INTEGER,webgl INTEGER)

        ''')

        db.commit()
        cursor.execute('''INSERT INTO Links(PageAddress, LinkAddress ,plugins, useragent, language, languages, concurrency,
                              cpuclass, platform, DNT, appname, colorDepth, height, width, localstorage, sessionstorage, 
                              indexdb, connection, rtc, aud, memory, geolocation, canvas, webgl)
                              VALUES(?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)''',
                       (PageAddress, address, FinalResult[address]["plugins"], FinalResult[address]["useragent"],
                        FinalResult[address]["language"],
                        FinalResult[address]["languages"], FinalResult[address]["concurrency"],
                        FinalResult[address]["cpuclass"],
                        FinalResult[address]["platform"], FinalResult[address]["DNT"],
                        FinalResult[address]["appname"], FinalResult[address]["colorDepth"],
                        FinalResult[address]["height"], FinalResult[address]["width"],
                        FinalResult[address]["localstorage"], FinalResult[address]["sessionstorage"],
                        FinalResult[address]["indexdb"], FinalResult[address]["connection"],
                        FinalResult[address]["rtc"], FinalResult[address]["aud"],
                        FinalResult[address]["memory"], FinalResult[address]["geolocation"],
                        FinalResult[address]["canvas"], FinalResult[address]["webgl"]))

        db.commit()

    except Exception as e:
        print str(e)
        db.rollback()

    finally:
        db.close()


parser = argparse.ArgumentParser("fingerdetector")
parser.add_argument("-i" , type = str , help = "Address to file to read input from")
parser.add_argument("-a", help="Single Website address to check for fingerprinting scripts e.g. http://80.191.93.206",
                    type=str)
parser.add_argument("-e", help="Perform Exhaustive Search - Performing Scan for Links on Index Page",
                    action="store_true")
parser.add_argument("output", help="Output DataBase Name",
                    type=str)
args = parser.parse_args()

if args.i == None and args.a != None:
    if str(args.a).startswith("http"):
        PageAddress = args.a
    else:
        PageAddress = "http://" + args.a
    PageSource = SourceRetriever(PageAddress)
    try:
        options = webdriver.ChromeOptions()
        options.add_argument('--ignore-certificate-errors')
        driver = webdriver.Chrome(chrome_options=options)
        driver.get(PageAddress)


    except Exception, e:
        print str(e)

    try:
        driver.execute_script(FeaturesHook)
    except Exception, e:
        print str(e)

    try:
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    except Exception, e:
        print str(e)

    try:
        BeautifulSource = BeautifulSoup(PageSource, 'html.parser')
        StrSource = BeautifulSource.prettify()
        StrSource = StrSource.replace(" = ", "=")
        StrSource = StrSource.replace("= ", "=")
        StrSource = StrSource.replace(" =", "=")
    except Exception, e:
        print str(e)

    onLoad(StrSource.encode('utf-8').strip())
    Onchange(StrSource.encode('utf-8').strip())
    onClick(StrSource.encode('utf-8').strip())
    onMouseOver(StrSource.encode('utf-8').strip())
    onMouseOut(StrSource.encode('utf-8').strip())
    onKeydown(StrSource.encode('utf-8').strip())
    onSubmit(StrSource.encode('utf-8').strip())


    ## Functions Which try to force fingerprinting scripts to show up

    EventExecutor(driver)
    Eventscr[:] = []
    ClickonButtons(driver)
    bodyloadExecutor(driver)

    try:

        Results = driver.execute_script(GetResults)

        FinalResult[PageAddress]["plugins"] = Results["plugins"]
        FinalResult[PageAddress]["useragent"] = Results["useragent"]
        FinalResult[PageAddress]["languages"] = Results["languages"]
        FinalResult[PageAddress]["language"] = Results["language"]
        FinalResult[PageAddress]["cpuclass"] = Results["cpuclass"]
        FinalResult[PageAddress]["platform"] = Results["platform"]
        FinalResult[PageAddress]["DNT"] = Results["DNT"]
        FinalResult[PageAddress]["appname"] = Results["appname"]
        FinalResult[PageAddress]["colorDepth"] = Results["colorDepth"]
        FinalResult[PageAddress]["height"] = Results["height"]
        FinalResult[PageAddress]["width"] = Results["width"]
        FinalResult[PageAddress]["localstorage"] = Results["localstorage"]
        FinalResult[PageAddress]["sessionstorage"] = Results["sessionstorage"]
        FinalResult[PageAddress]["indexdb"] = Results["indexdb"]
        FinalResult[PageAddress]["connection"] = Results["connection"]
        FinalResult[PageAddress]["rtc"] = Results["rtc"]

        audstate = Results["audstate"]
        audioFunc = Results["aud"]
        samplerate = Results["sample"]
        if audioFunc > 0 and samplerate > 0 and audstate > 0:
            FinalResult[PageAddress]["aud"] = 1
        else:
            FinalResult[PageAddress]["aud"] = 0

        FinalResult[PageAddress]["memory"] = Results["memory"]
        FinalResult[PageAddress]["concurrency"] = Results["concurrency"]
        FinalResult[PageAddress]["geolocation"] = Results["geolocation"]
        tourl = Results["tourl"]
        filltext = Results["filltext"]
        stroketext = Results["stroketext"]
        getimagedata = Results["getimagedata"]
        if (tourl > 0 and stroketext > 0) or (getimagedata > 0 and stroketext > 0) or (tourl > 0 and filltext > 0) or (
                        getimagedata > 0 and filltext > 0):
            FinalResult[PageAddress]["canvas"] = 1
        else:
            FinalResult[PageAddress]["canvas"] = 0
        debugelem = Results["getdebuginfo"]
        drawarray = Results["drawarray"]
        glextensions = Results["getextension"]
        debugcount = 0
        if debugelem != None:
            for i in range(0, len(debugelem)):
                if debugelem[i][0] == "WEBGL_debug_renderer_info":
                    debugcount += 1
        if (drawarray > 0 and glextensions > 0 and debugcount > 0 and tourl > 0):
            FinalResult[PageAddress]["webgl"] = 1
        else:
            FinalResult[PageAddress]["webgl"] = 0
    except Exception, e:
        pass

    if args.e:
        hrefExtract(driver)
        Linklist = list(set(Linklist))
        RemoveDuplicates()
        print str(len(Linklist)) + " Links have been found"
        surfer(driver)

    IndexToDatabase()

    print "\n"
    print "-------------------------"
    print "Results: "

    for val in FinalResult:
        print "\n"
        print "The address accessed following browser objects to gather unique information on you: "
        print " "
        sentinel = 1
        for elem in FinalResult[val]:
            if FinalResult[val][elem] > 0:
                print str(sentinel) + "- " + elem
                sentinel += 1
    print "Test is Finished. you can also review results in " + args.output + ".db"

    driver.close()

elif args.i != None and args.a == None:

    f = open(str(args.i), "r")
    contents = f.readlines()
    for val in contents:
        temp = val.split(',')
        if temp[1].startswith("http"):
            PageAddress = temp[1]
        else:
            PageAddress = "http://" + temp[1]
        print "Working on " + PageAddress
        PageSource = SourceRetriever(PageAddress)
        try:
            options = webdriver.ChromeOptions()
            options.add_argument('--ignore-certificate-errors')
            driver = webdriver.Chrome(chrome_options=options)
            driver.get(PageAddress)

        except Exception, e:
            print str(e)

        try:
            driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")

        except Exception, e:
            pass

        try:
            BeautifulSource = BeautifulSoup(PageSource, 'html.parser')
            StrSource = BeautifulSource.prettify()
            StrSource = StrSource.replace(" = ", "=")
            StrSource = StrSource.replace("= ", "=")
            StrSource = StrSource.replace(" =", "=")
        except Exception, e:
            print str(e)

        onLoad(StrSource.encode('utf-8').strip())
        Onchange(StrSource.encode('utf-8').strip())
        onClick(StrSource.encode('utf-8').strip())
        onMouseOver(StrSource.encode('utf-8').strip())
        onMouseOut(StrSource.encode('utf-8').strip())
        onKeydown(StrSource.encode('utf-8').strip())
        onSubmit(StrSource.encode('utf-8').strip())

        try:
            driver.execute_script(FeaturesHook)
            driver.implicitly_wait(3)
        except Exception, e:
            pass

        ## Functions Which try to force fingerprinting scripts to show up

        EventExecutor(driver)
        Eventscr[:] = []
        ClickonButtons(driver)
        bodyloadExecutor(driver)

        try:

            Results = driver.execute_script(GetResults)

            FinalResult[PageAddress]["plugins"] = Results["plugins"]
            FinalResult[PageAddress]["useragent"] = Results["useragent"]
            FinalResult[PageAddress]["languages"] = Results["languages"]
            FinalResult[PageAddress]["language"] = Results["language"]
            FinalResult[PageAddress]["cpuclass"] = Results["cpuclass"]
            FinalResult[PageAddress]["platform"] = Results["platform"]
            FinalResult[PageAddress]["DNT"] = Results["DNT"]
            FinalResult[PageAddress]["appname"] = Results["appname"]
            FinalResult[PageAddress]["colorDepth"] = Results["colorDepth"]
            FinalResult[PageAddress]["height"] = Results["height"]
            FinalResult[PageAddress]["width"] = Results["width"]
            FinalResult[PageAddress]["localstorage"] = Results["localstorage"]
            FinalResult[PageAddress]["sessionstorage"] = Results["sessionstorage"]
            FinalResult[PageAddress]["indexdb"] = Results["indexdb"]
            FinalResult[PageAddress]["connection"] = Results["connection"]
            FinalResult[PageAddress]["rtc"] = Results["rtc"]

            audstate = Results["audstate"]
            audioFunc = Results["aud"]
            samplerate = Results["sample"]
            if audioFunc > 0 and samplerate > 0 and audstate > 0:
                FinalResult[PageAddress]["aud"] = 1
            else:
                FinalResult[PageAddress]["aud"] = 0

            FinalResult[PageAddress]["memory"] = Results["memory"]
            FinalResult[PageAddress]["concurrency"] = Results["concurrency"]
            FinalResult[PageAddress]["geolocation"] = Results["geolocation"]
            tourl = Results["tourl"]
            filltext = Results["filltext"]
            stroketext = Results["stroketext"]
            getimagedata = Results["getimagedata"]
            if (tourl > 0 and stroketext > 0) or (getimagedata > 0 and stroketext > 0) or (
                    tourl > 0 and filltext > 0) or (
                            getimagedata > 0 and filltext > 0):
                FinalResult[PageAddress]["canvas"] = 1
            else:
                FinalResult[PageAddress]["canvas"] = 0
            debugelem = Results["getdebuginfo"]
            drawarray = Results["drawarray"]
            glextensions = Results["getextension"]
            debugcount = 0
            if debugelem != None:
                for i in range(0, len(debugelem)):
                    if debugelem[i][0] == "WEBGL_debug_renderer_info":
                        debugcount += 1
            if (drawarray > 0 and glextensions > 0 and debugcount > 0 and tourl > 0):
                FinalResult[PageAddress]["webgl"] = 1
            else:
                FinalResult[PageAddress]["webgl"] = 0
        except Exception, e:
            pass

        if args.e:
            hrefExtract(driver)
            Linklist = list(set(Linklist))
            RemoveDuplicates()
            print str(len(Linklist)) + " Links have been found"
            surfer(driver)

        IndexToDatabase()
        driver.close()




