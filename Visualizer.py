import sqlite3
import argparse
import collections
import plotly
import plotly.graph_objs as go


count = 0
Res = collections.defaultdict(dict)
x = []
plugins = []
useragent = []
language = []
languages = []
concurrency = []
cpuclass = []
platform = []
DNT = []
appname = []
colorDepth = []
height = []
width = []
localstorage = []
sessionstorage = []
indexdb = []
connection = []
rtc = []
aud = []
memory = []
geolocation = []
canvas = []
webgl = []
###



parser = argparse.ArgumentParser("Visualizer.py")
parser.add_argument("input" , type = str , help = "Address to file to read input from")
parser.add_argument("-s" , help = "Display Data on a bar chart individually", action="store_true")
parser.add_argument("-m" , help = "Display aggregate Result for Available Data ", action="store_true")
args = parser.parse_args()

def Getdata():
    try:
        db = sqlite3.connect(str(args.input))
        cursor = db.cursor()
        cursor.execute('''
            SELECT * FROM IndexPage WHERE plugins IS NOT NULL 
            ''')
        rows = cursor.fetchall()
        db.commit()
        cursor.execute('''
                    SELECT COUNT(*) FROM IndexPage WHERE plugins IS NOT NULL
                    ''')
        cnt = cursor.fetchone()
        db.commit()
        if args.s:
            ParseIndData(rows)
        elif args.m:
            ParseAggData(rows,cnt[0])




    except Exception as e:
        print str(e)
        db.rollback()

    finally:
        db.close()
def ParseIndData(rows):
    for val in rows:
        x.append(val[1])
        plugins.append(val[2])
        useragent.append(val[3])
        language.append(val[4])
        languages.append(val[5])
        concurrency.append(val[6])
        cpuclass.append(val[7])
        platform.append(val[8])
        DNT.append(val[9])
        appname.append(val[10])
        colorDepth.append(val[11])
        height.append(val[12])
        width.append(val[13])
        localstorage.append(val[14])
        sessionstorage.append(val[15])
        indexdb.append(val[16])
        connection.append(val[17])
        rtc.append(val[18])
        aud.append(val[19])
        memory.append(val[20])
        geolocation.append(val[21])
        canvas.append(val[22])
        webgl.append(val[23])
def ParseAggData(rows, count):
    for val in rows:
        if val[2] > 0:
            Res[val[1]]["plugins"] = 1
        else:
            Res[val[1]]["plugins"] = 0
        if val[3] > 0:
            Res[val[1]]["useragent"] = 1
        else:
            Res[val[1]]["useragent"] = 0
        if val[4] > 0:
            Res[val[1]]["language"] = 1
        else:
            Res[val[1]]["language"] = 0
        if val[5] > 0:
            Res[val[1]]["languages"] = 1
        else:
            Res[val[1]]["languages"] = 0
        if val[6] > 0:
            Res[val[1]]["concurrency"] = 1
        else:
            Res[val[1]]["concurrency"] = 0
        if val[7] > 0:
            Res[val[1]]["cpuclass"] = 1
        else:
            Res[val[1]]["cpuclass"] = 0
        if val[8] > 0:
            Res[val[1]]["platform"] = 1
        else:
            Res[val[1]]["platform"] = 0
        if val[9] > 0:
            Res[val[1]]["DNT"] = 1
        else:
            Res[val[1]]["DNT"] = 0
        if val[10] > 0:
            Res[val[1]]["appname"] = 1
        else:
            Res[val[1]]["appname"] = 0
        if val[11] > 0:
            Res[val[1]]["colorDepth"] = 1
        else:
            Res[val[1]]["colorDepth"] = 0
        if val[12] > 0:
            Res[val[1]]["height"] = 1
        else:
            Res[val[1]]["height"] = 0
        if val[13] > 0:
            Res[val[1]]["width"] = 1
        else:
            Res[val[1]]["width"] = 0
        if val[14] > 0:
            Res[val[1]]["localstorage"] = 1
        else:
            Res[val[1]]["localstorage"] = 0
        if val[15] > 0:
            Res[val[1]]["sessionstorage"] = 1
        else:
            Res[val[1]]["sessionstorage"] = 0
        if val[16] > 0:
            Res[val[1]]["indexdb"] = 1
        else:
            Res[val[1]]["indexdb"] = 0
        if val[17] > 0:
            Res[val[1]]["connection"] = 1
        else:
            Res[val[1]]["connection"] = 0
        if val[18] > 0:
            Res[val[1]]["rtc"] = 1
        else:
            Res[val[1]]["rtc"] = 0
        if val[19] > 0:
            Res[val[1]]["aud"] = 1
        else:
            Res[val[1]]["aud"] = 0
        if val[20] > 0:
            Res[val[1]]["memory"] = 1
        else:
            Res[val[1]]["memory"] = 0
        if val[21] > 0:
            Res[val[1]]["geolocation"] = 1
        else:
            Res[val[1]]["geolocation"] = 0
        if val[22] > 0:
            Res[val[1]]["canvas"] = 1
        else:
            Res[val[1]]["canvas"] = 0
        if val[23] > 0:
            Res[val[1]]["webgl"] = 1
        else:
            Res[val[1]]["webgl"] = 0
    SumPlugins = 0
    SumUseragent = 0
    SumLanguage = 0
    SumLanguages = 0
    SumConcurrency = 0
    SumCpuclass = 0
    SumPlatform = 0
    SumDNT = 0
    SumAppname = 0
    SumColorDepth = 0
    SumHeight = 0
    SumWidth = 0
    SumLocalstorage = 0
    SumSessionstorage = 0
    SumIndexdb = 0
    Sumconnection = 0
    SumRTC = 0
    SumAUD = 0
    SumMemory = 0
    SumGeolocation = 0
    SumCanvas = 0
    SumWebgl = 0

    for val in Res:
        SumPlugins = SumPlugins + Res[val]["plugins"]
        SumUseragent = SumUseragent + Res[val]["useragent"]
        SumLanguage = SumLanguage + Res[val]["language"]
        SumLanguages = SumLanguages + Res[val]["languages"]
        SumConcurrency = SumConcurrency + Res[val]["concurrency"]
        SumCpuclass = SumCpuclass + Res[val]["cpuclass"]
        SumPlatform = SumPlatform + Res[val]["platform"]
        SumDNT = SumDNT + Res[val]["DNT"]
        SumAppname = SumAppname + Res[val]["appname"]
        SumColorDepth = SumColorDepth + Res[val]["colorDepth"]
        SumHeight = SumHeight + Res[val]["height"]
        SumWidth = SumWidth + Res[val]["width"]
        SumLocalstorage = SumLocalstorage + Res[val]["localstorage"]
        SumSessionstorage = SumSessionstorage + Res[val]["sessionstorage"]
        SumIndexdb = SumIndexdb + Res[val]["indexdb"]
        Sumconnection = Sumconnection + Res[val]["connection"]
        SumRTC = SumRTC + Res[val]["rtc"]
        SumAUD = SumAUD + Res[val]["aud"]
        SumMemory = SumMemory + Res[val]["memory"]
        SumGeolocation = SumGeolocation + Res[val]["geolocation"]
        SumCanvas = SumCanvas + Res[val]["canvas"]
        SumWebgl = SumWebgl + Res[val]["webgl"]

    SumPlugins = float(SumPlugins)/count * 100
    SumUseragent = float(SumUseragent) / count * 100
    SumLanguage = float(SumLanguage) / count * 100
    SumConcurrency = float(SumConcurrency) / count * 100
    SumCpuclass = float(SumCpuclass) / count * 100
    SumPlatform = float(SumPlatform) / count * 100
    SumDNT = float(SumDNT) / count * 100
    SumAppname = float(SumAppname) / count * 100
    SumColorDepth = float(SumColorDepth) / count * 100
    SumHeight = float(SumHeight) / count * 100
    SumWidth = float(SumWidth) / count * 100
    SumLocalstorage = float(SumLocalstorage) / count * 100
    SumSessionstorage = float(SumSessionstorage) / count * 100
    SumIndexdb = float(SumIndexdb) / count * 100
    Sumconnection = float(Sumconnection) / count * 100
    SumRTC = float(SumRTC) / count * 100
    SumAUD = float(SumAUD) / count * 100
    SumMemory = float(SumMemory) / count * 100
    SumGeolocation = float(SumGeolocation) / count * 100
    SumCanvas = float(SumCanvas) / count * 100
    SumWebgl = float(SumWebgl) / count * 100
    DrawAggChart(SumPlugins,SumUseragent,SumLanguage,SumLanguages,SumConcurrency,
                 SumCpuclass,SumPlatform,SumDNT,SumAppname,SumColorDepth,
                 SumHeight,SumWidth,SumLocalstorage,SumSessionstorage,SumIndexdb,
                 Sumconnection,SumRTC,SumAUD,SumMemory,SumGeolocation,SumCanvas,SumWebgl,count)






def DrawIndChart():
    trace1 = go.Bar(
        x=x,
        y=plugins,
        name='plugins',
        text=plugins,
        textposition='auto',
        marker=dict(
            color='rgb(215,214,125)',
            line=dict(
                color='rgb(8,48,107)',
                width=1.5),
        ),
        opacity=0.6
    )

    trace2 = go.Bar(
        x=x,
        y=useragent,
        name='useragent',
        text=useragent,
        textposition='auto',
        marker=dict(
            color='rgb(255,204,229)',
            line=dict(
                color='rgb(8,48,107)',
                width=1.5),
        ),
        opacity=0.6
    )

    trace3 = go.Bar(
        x=x,
        y=language,
        name='language',
        text=language,
        textposition='auto',
        marker=dict(
            color='rgb(229,204,255)',
            line=dict(
                color='rgb(229,204,255)',
                width=1.5),
        ),
        opacity=0.6
    )
    trace4 = go.Bar(
        x=x,
        y=languages,
        name='languages',
        text=languages,
        textposition='auto',
        marker=dict(
            color='rgb(204,229,255)',
            line=dict(
                color='rgb(8,48,107)',
                width=1.5),
        ),
        opacity=0.6
    )
    trace5 = go.Bar(
        x=x,
        y=concurrency,
        name='concurrency',
        text=concurrency,
        textposition='auto',
        marker=dict(
            color='rgb(204,255,204)',
            line=dict(
                color='rgb(8,48,107)',
                width=1.5),
        ),
        opacity=0.6
    )
    trace6 = go.Bar(
        x=x,
        y=cpuclass,
        name='cpuclass',
        text=cpuclass,
        textposition='auto',
        marker=dict(
            color='rgb(255,204,204)',
            line=dict(
                color='rgb(8,48,107)',
                width=1.5),
        ),
        opacity=0.6
    )
    trace7 = go.Bar(
        x=x,
        y=platform,
        name='platform',
        text=platform,
        textposition='auto',
        marker=dict(
            color='rgb(255,102,102)',
            line=dict(
                color='rgb(8,48,107)',
                width=1.5),
        ),
        opacity=0.6
    )
    trace8 = go.Bar(
        x=x,
        y=DNT,
        name='DNT',
        text=DNT,
        textposition='auto',
        marker=dict(
            color='rgb(204,02,5)',
            line=dict(
                color='rgb(8,48,107)',
                width=1.5),
        ),
        opacity=0.6
    )
    trace9 = go.Bar(
        x=x,
        y=appname,
        name='appname',
        text=appname,
        textposition='auto',
        marker=dict(
            color='rgb(153,153,0)',
            line=dict(
                color='rgb(8,48,107)',
                width=1.5),
        ),
        opacity=0.6
    )
    trace10 = go.Bar(
        x=x,
        y=colorDepth,
        name='colorDepth',
        text=colorDepth,
        textposition='auto',
        marker=dict(
            color='rgb(0,153,76)',
            line=dict(
                color='rgb(8,48,107)',
                width=1.5),
        ),
        opacity=0.6
    )
    trace11 = go.Bar(
        x=x,
        y=height,
        name='Height',
        text=height,
        textposition='auto',
        marker=dict(
            color='rgb(0,76,153)',
            line=dict(
                color='rgb(8,48,107)',
                width=1.5),
        ),
        opacity=0.6
    )
    trace12 = go.Bar(
        x=x,
        y=width,
        name='Width',
        text=width,
        textposition='auto',
        marker=dict(
            color='rgb(153,0,153)',
            line=dict(
                color='rgb(8,48,107)',
                width=1.5),
        ),
        opacity=0.6
    )
    trace13 = go.Bar(
        x=x,
        y=localstorage,
        name='Local Storage',
        text=localstorage,
        textposition='auto',
        marker=dict(
            color='rgb(255,0,255)',
            line=dict(
                color='rgb(8,48,107)',
                width=1.5),
        ),
        opacity=0.6
    )
    trace14 = go.Bar(
        x=x,
        y=sessionstorage,
        name='Session Storage',
        text=sessionstorage,
        textposition='auto',
        marker=dict(
            color='rgb(0,255,128)',
            line=dict(
                color='rgb(8,48,107)',
                width=1.5),
        ),
        opacity=0.6
    )
    trace15 = go.Bar(
        x=x,
        y=indexdb,
        name='indexedDB',
        text=indexdb,
        textposition='auto',
        marker=dict(
            color='rgb(160,160,160)',
            line=dict(
                color='rgb(8,48,107)',
                width=1.5),
        ),
        opacity=0.6
    )
    trace16 = go.Bar(
        x=x,
        y=connection,
        name='Connection',
        text=connection,
        textposition='auto',
        marker=dict(
            color='rgb(204,0,102)',
            line=dict(
                color='rgb(8,48,107)',
                width=1.5),
        ),
        opacity=0.6
    )
    trace17 = go.Bar(
        x=x,
        y=rtc,
        name='WebRTC',
        text=rtc,
        textposition='auto',
        marker=dict(
            color='rgb(0,128,255)',
            line=dict(
                color='rgb(8,48,107)',
                width=1.5),
        ),
        opacity=0.6
    )
    trace18 = go.Bar(
        x=x,
        y=aud,
        name='Audio Functions',
        text=aud,
        textposition='auto',
        marker=dict(
            color='rgb(0,102,51)',
            line=dict(
                color='rgb(8,48,107)',
                width=1.5),
        ),
        opacity=0.6
    )
    trace19 = go.Bar(
        x=x,
        y=memory,
        name='Memory',
        text=memory,
        textposition='auto',
        marker=dict(
            color='rgb(153,0,153)',
            line=dict(
                color='rgb(8,48,107)',
                width=1.5),
        ),
        opacity=0.6
    )
    trace20 = go.Bar(
        x=x,
        y=geolocation,
        name='Geolocation',
        text=geolocation,
        textposition='auto',
        marker=dict(
            color='rgb(51,255,153)',
            line=dict(
                color='rgb(8,48,107)',
                width=1.5),
        ),
        opacity=0.6
    )
    trace21 = go.Bar(
        x=x,
        y=canvas,
        name='Canvas Fingerprinting',
        text=canvas,
        textposition='auto',
        marker=dict(
            color='rgb(255,229,204)',
            line=dict(
                color='rgb(8,48,107)',
                width=1.5),
        ),
        opacity=0.6
    )
    trace22 = go.Bar(
        x=x,
        y=webgl,
        name='Webgl Fingerprinting',
        text=webgl,
        textposition='auto',
        marker=dict(
            color='rgb(255,128,0)',
            line=dict(
                color='rgb(8,48,107)',
                width=1.5),
        ),
        opacity=0.6

    )

    data = [trace1,trace2,trace3,trace4,trace5,trace6,trace7,trace8,trace9,
            trace10,trace11,trace12,trace13,trace14,trace15,trace16,trace17,
            trace18,trace19,trace20,trace21,trace22]

    layout = go.Layout(
        title='Detailed Report for Fingerprinting Prevalence', )
    plotly.offline.plot({
"data": data,
"layout":layout
})
def DrawAggChart(Plugins,Useragent,Language,Languages,Concurrency,
                 Cpuclass,Platform,DNT,Appname,ColorDepth,
                 Height,Width,Localstorage,Sessionstorage,Indexdb,
                 Connection,RTC,AUD,Memory,Geolocation,Canvas,Webgl,Count):


    data = [go.Bar(
        x=["Plugins", "Useragent", "Language", "Languages", "Concurrency", "Cpuclass", "Platform", "DNT", "Appname",
           "ColorDepth", "Height", "Width", "LocalStorage", "SessionStorage", "Indexeddb", "Connection", "WebRTC",
           "AuidoFunction",
           "Memory Access", "Geolocation", "Canvas Fingerprinting", "WebglFingerprinting"],
        y = [Plugins, Useragent, Language, Languages, Concurrency,
             Cpuclass, Platform, DNT, Appname, ColorDepth,
             Height, Width, Localstorage, Sessionstorage, Indexdb,
             Connection, RTC, AUD, Memory, Geolocation, Canvas, Webgl],
        marker=dict(
            color=['rgb(255,128,0)','255,229,204','rgb(51,255,153)','rgb(153,0,153)','rgb(0,102,51)','rgb(0,128,255)',
                   'rgb(0,128,255)','rgb(204,0,102)','rgb(160,160,160)','rgb(0,255,128)','rgb(255,0,255)','rgb(153,0,153)',
                   'rgb(0,76,153)','rgb(0,153,76)','rgb(153,153,0)','rgb(204,02,5)','rgb(255,102,102)','rgb(255,204,204)',
                   'rgb(204,255,204)','rgb(204,229,255)','rgb(229,204,255)','rgb(255,204,229)','rgb(215,214,125)']),
    )]
    layout = go.Layout(
        barmode='group',
        title='Prevalence of Fingerprinting between ' + str(Count) + " Top websites of Alexa in Percent" ,)
    plotly.offline.plot({
        "data": data,
        "layout": layout
    })



Getdata()
if args.s:
    DrawIndChart()

elif args.m:
    pass