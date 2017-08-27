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

YTstats = youtube.getStats(YTuser)

print YTstats
