import sys
sys.path.append("functions")
import thingiverse
import github
import hackaday
import youtube
import twitter
import googlegroups
import instagram

import re
from subprocess import call
from time import time, gmtime, strftime
from datetime import date, timedelta, datetime
import glob
import os, errno

TVuser = 'AngelLM'                                      # Thingiverse username. https://www.thingiverse.com/USERNAME/
GHuser = 'AngelLM'                                      # GitHub username. https://github.com/USERNAME
HDuser = 'AngelLM'                                      # Hackaday username. https://hackaday.io/USERNAME
YTuser = 'AngelLM'                                      # Youtube username. https://www.youtube.com/USERNAME
TWuser = '_AngelLM'                                     # Twitter username. https://twitter.com/USERNAME
GGname = 'thor-opensource-3d-printable-robotic-arm'     # Google Group name. https://groups.google.com/forum/#!forum/GROUPNAME
IGuser = 'angel_lm_'                                    # Instagram username. https://www.instagram.com/

separator=''

Fbase = open("indexbase.txt", "r")
Textbase = Fbase.read()
Fbase.close()

Fsplitted = Textbase.split("!!!")

try:
    YTstats = youtube.getStats(YTuser)
except Exception as yte:
    dateError=datetime.now()
    dateErrorStr =  dateError.strftime('%Y-%m-%d %H:%M:%S')
    print "[Youtube exception] - " + dateErrorStr + " - " + str(yte)

try:
    IGstats = instagram.getStats(IGuser)
except Exception as ige:
    dateError=datetime.now()
    dateErrorStr =  dateError.strftime('%Y-%m-%d %H:%M:%S')
    print "[Instagram exception] - " + dateErrorStr + " - " + str(ige)

try:
    GHstats = github.getStats(GHuser)
except Exception as ghe:
    dateError=datetime.now()
    dateErrorStr =  dateError.strftime('%Y-%m-%d %H:%M:%S')
    print "[GitHub exception] - " + dateErrorStr + " - " + str(ghe)

try:
    GGstats = googlegroups.getStats(GGname)
except Exception as gge:
    dateError=datetime.now()
    dateErrorStr =  dateError.strftime('%Y-%m-%d %H:%M:%S')
    print "[Google Groups exception] - " + dateErrorStr + " - " + str(gge)

try:
    TWstats = twitter.getStats(TWuser)
except Exception as twe:
    dateError=datetime.now()
    dateErrorStr =  dateError.strftime('%Y-%m-%d %H:%M:%S')
    print "[Twitter exception] - " + dateErrorStr + " - " + str(twe)

try:
    TVstats = thingiverse.getStats(TVuser)
except Exception as tve:
    dateError=datetime.now()
    dateErrorStr =  dateError.strftime('%Y-%m-%d %H:%M:%S')
    print "[Thingiverse exception] - " + dateErrorStr + " - " + str(tve)

try:
    HDstats = hackaday.getStats(HDuser)
except Exception as hde:
    dateError=datetime.now()
    dateErrorStr =  dateError.strftime('%Y-%m-%d %H:%M:%S')
    print "[Hackaday exception] - " + dateErrorStr + " - " + str(hde)


dateNow=datetime.now()
dateNowStr =  dateNow.strftime('%Y-%m-%d %H:%M:%S')

StatsData = [GHstats[0], GHstats[1], GHstats[2], GHstats[3], GHstats[4], TVstats[0], TVstats[1], TVstats[2], TVstats[3], TVstats[4], TVstats[5], TVstats[6], YTstats[0], YTstats[1], YTstats[2], YTstats[3], HDstats[0], HDstats[1], HDstats[2], HDstats[3], HDstats[4], TWstats[0], TWstats[1], TWstats[2], TWstats[3], GGstats[0], GGstats[1], IGstats[0], IGstats[1], IGstats[2], IGstats[3]]


yesterdayDate = date.today()-timedelta(days=1)
yearYesterday = yesterdayDate.strftime("%Y")
monthYesterday = yesterdayDate.strftime("%m")
dayYesterday = yesterdayDate.strftime("%d")

pathYesterday = 'logs/' + yearYesterday + '/' + monthYesterday + '/' + dayYesterday + '/' + '*.txt'
filesPath = glob.glob(pathYesterday)
filesPath.sort()

Fyesterday = open(filesPath[len(filesPath)-1], "r")

statsYesterday = re.findall(r'\d+', Fyesterday.read())

for k in range(len(statsYesterday)):
    statsYesterday[k] = int(statsYesterday[k])

statsDiffYesterday = []

for t in range(len(StatsData)):
    statsDiffYesterday.append(StatsData[t]-statsYesterday[t])

diffYestCounter = []

for diff in statsDiffYesterday:
    if diff > 0:
        diffYestCounter.append('<sup class="diffpos"> +'+str(diff)+'</sup>')
    elif diff < 0:
        diffYestCounter.append('<sup class="diffneg"> '+str(diff)+'</sup>')
    else:
        diffYestCounter.append(' ')

for s in range(len(Fsplitted)-2):
    Fsplitted[s]=Fsplitted[s]+str(StatsData[s])+diffYestCounter[s]+'</p>'

Fsplitted[len(Fsplitted)-2]=Fsplitted[len(Fsplitted)-2]+dateNowStr+ ' (GMT+1)' + '</p>'

Fjoined = separator.join(Fsplitted)


Ffinal = open("index.html", "w")
Ffinal.write(Fjoined)
Ffinal.close()



Flogbase = open("logs/logbase.txt", "r")
Logbase = Flogbase.read()
Flogbase.close()
LogbaseSplitted = Logbase.split("!")

for w in range(len(LogbaseSplitted)-1):
    LogbaseSplitted[w]=LogbaseSplitted[w]+str(StatsData[w])
Logbasejoined = separator.join(LogbaseSplitted)

yearNow = dateNow.strftime("%Y")
monthNow = dateNow.strftime("%m")
dayNow = dateNow.strftime("%d")
FullDateNow = dateNow.strftime('%Y-%m-%d_%H-%M-%S')

PathFolder = 'logs/' + yearNow + '/' + monthNow + '/' + dayNow
PathNow = PathFolder + '/' + FullDateNow + '.txt'

try:
    os.makedirs(PathFolder)
except OSError as e:
    if e.errno != errno.EEXIST:
        raise

Flog = open(PathNow, "w+")
Flog.write(Logbasejoined)
Flog.close()

call(["git", "add", "./"])
call(["git", "commit", "-m", "Automatic commit "+dateNowStr])
call(["git", "push", "origin", "master"])
