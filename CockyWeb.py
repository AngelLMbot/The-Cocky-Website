import sys
import re
from subprocess import call
from time import time, gmtime, strftime
from datetime import date, timedelta, datetime
import glob
import os, errno
import time
sys.path.append("/home/angellm/repos/The-Cocky-Website/functions")
import thingiverse
import github
import hackaday
import youtube
import twitter
import googlegroups
import instagram

repopath = "/home/angellm/repos/The-Cocky-Website/"

tic=time.time()

TVuser = 'AngelLM'                                      # Thingiverse username. https://www.thingiverse.com/USERNAME/
GHuser = 'AngelLM'                                      # GitHub username. https://github.com/USERNAME
HDuser = 'AngelLM'                                      # Hackaday username. https://hackaday.io/USERNAME
YTuser = 'AngelLM'                                      # Youtube username. https://www.youtube.com/USERNAME
TWuser = '_AngelLM'                                     # Twitter username. https://twitter.com/USERNAME
GGname = 'thor-opensource-3d-printable-robotic-arm'     # Google Group name. https://groups.google.com/forum/#!forum/GROUPNAME
IGuser = 'angel_lm_'                                    # Instagram username. https://www.instagram.com/

separator=''

Fbase = open(repopath + "indexbase.txt", "r")
Textbase = Fbase.read()
Fbase.close()

Fsplitted = Textbase.split("!!!")
print "indexbase.html splitted at " + str(time.time()-tic) + "s"

YTstats = youtube.getStats(YTuser)
print "Youtube stats taken at " + str(time.time()-tic) + "s"
IGstats = instagram.getStats(IGuser)
print "Instagram stats taken at " + str(time.time()-tic) + "s"
GGstats = googlegroups.getStats(GGname)
print "Google Groups stats taken at " + str(time.time()-tic) + "s"
TWstats = twitter.getStats(TWuser)
print "Twitter stats taken at " + str(time.time()-tic) + "s"
GHstats = github.getStats(GHuser)
print "GitHub stats taken at " + str(time.time()-tic) + "s"
TVstats = thingiverse.getStats(TVuser)
print "Thingiverse stats taken at " + str(time.time()-tic) + "s"
HDstats = hackaday.getStats(HDuser)
print "Hackaday stats taken at " + str(time.time()-tic) + "s"
dateNow=datetime.now()
dateNowStr =  dateNow.strftime('%Y-%m-%d %H:%M:%S')

StatsData = [GHstats[0], GHstats[1], GHstats[2], GHstats[3], GHstats[4], TVstats[0], TVstats[1], TVstats[2], TVstats[3], TVstats[4], TVstats[5], TVstats[6], YTstats[0], YTstats[1], YTstats[2], YTstats[3], HDstats[0], HDstats[1], HDstats[2], HDstats[3], HDstats[4], TWstats[0], TWstats[1], TWstats[2], TWstats[3], GGstats[0], GGstats[1], IGstats[0], IGstats[1], IGstats[2], IGstats[3]]


yesterdayDate = date.today()-timedelta(days=1)
yearYesterday = yesterdayDate.strftime("%Y")
monthYesterday = yesterdayDate.strftime("%m")
dayYesterday = yesterdayDate.strftime("%d")

pathYesterday = repopath + 'logs/' + yearYesterday + '/' + monthYesterday + '/' + dayYesterday + '/' + '*.txt'
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


Ffinal = open(repopath + "index.html", "w")
Ffinal.write(Fjoined)
Ffinal.close()



Flogbase = open(repopath + "logs/logbase.txt", "r")
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

PathFolder = repopath + 'logs/' + yearNow + '/' + monthNow + '/' + dayNow
PathNow = PathFolder + '/' + FullDateNow + '.txt'

try:
    os.makedirs(PathFolder)
except OSError as e:
    if e.errno != errno.EEXIST:
        raise

Flog = open(PathNow, "w+")
Flog.write(Logbasejoined)
Flog.close()

print "antes del push"
os.chdir(repopath)
call(["git", "add", "./"])
call(["git", "commit", "-m", "Automatic commit "+dateNowStr])
#call(["git", "push", "origin", "master"])
print "despues del push"
toc = time.time()

print "Processing time (s): " + str(toc-tic)  
