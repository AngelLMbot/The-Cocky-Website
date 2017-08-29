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
IGuser = 'angel_lm_'                                    # Instagram username. https://www.instagram.


try:
    IGstats = instagram.getStats(IGuser)
except Exception as ige:
    dateError=datetime.now()
    dateErrorStr =  dateError.strftime('%Y-%m-%d %H:%M:%S')
    print "[Instagram exception] - " + dateNowStr + " - " + str(ige)
