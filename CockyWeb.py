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
from time import gmtime, strftime

# Users & Names variables. Fill them with your usernames if you want the stats of that platform. Leave it blank if you don't want the stats.

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

Fsplitted = Textbase.split(":")

GHstats = github.getStats(GHuser)
TVstats = thingiverse.getStats(TVuser)
YTstats = youtube.getStats(YTuser)
HDstats = hackaday.getStats(HDuser)
TWstats = twitter.getStats(TWuser)
GGstats = googlegroups.getStats(GGname)
IGstats = instagram.getStats(IGuser)

dateNow = strftime("%Y-%m-%d %H:%M:%S", gmtime())
StatsData = [GHstats[0], GHstats[1], GHstats[2], GHstats[3], GHstats[4], TVstats[0], TVstats[1], TVstats[2], TVstats[3], TVstats[4], TVstats[5], TVstats[6], YTstats[0], YTstats[1], YTstats[2], YTstats[3], HDstats[0], HDstats[1], HDstats[2], HDstats[3], HDstats[4], TWstats, GGstats[0], GGstats[1], IGstats[0], IGstats[1], IGstats[2], IGstats[3]]

for s in range(len(Fsplitted)-2):
    Fsplitted[s]=Fsplitted[s]+': '+str(StatsData[s])+'</p>'
Fsplitted[len(Fsplitted)-1]=Fsplitted[len(Fsplitted)-1]+dateNow+'</p>'

Fjoined = separator.join(Fsplitted)


Ffinal = open("index.html", "w")
Ffinal.write(Fjoined)
Ffinal.close()

call(["git", "add", "./"])
call(["git", "commit", "-m", "Automatic commit"])
call(["git", "push", "origin", "master"])
