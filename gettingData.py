import re
from time import time, gmtime, strftime
from datetime import date, timedelta, datetime
import glob
import os, errno

def getStatsFromFile(filePath):
    returnMessage = []
    F = open(filePath, 'r')
    Flines = F.read().split('\n')
    F.close()
    while '' in Flines: Flines.remove('')
    while '----------' in Flines: Flines.remove('----------')
    whereIam = ''
    for line in Flines:
        if line == 'Github':
            whereIam = 'Github'
        elif line == 'Thingiverse':
            whereIam = 'Thingiverse'
        elif line == 'Youtube':
            whereIam = 'Youtube'
        elif line == 'Hackaday':
            whereIam = 'Hackaday'
        elif line == 'Twitter':
            whereIam = 'Twitter'
        elif line == 'Google Groups':
            whereIam = 'Google Groups'
        elif line == 'Instagram':
            whereIam = 'Instagram'
        else:
            partlines = line.split(': ')
            returnMessage.append(whereIam + '-' + partlines[0] + '-' + partlines[1])
    return (returnMessage)


dateNow = datetime.now()
yearNow = dateNow.strftime('%Y')
monthNow = dateNow.strftime('%m')
dayNow = dateNow.strftime('%d')

Fdaily = open('js/logs/daily.txt', 'w+')
pathDaily = 'logs/' + yearNow + '/' + monthNow + '/' + dayNow+ '/' + '*.txt'
filesPathDaily = glob.glob(pathDaily)
filesPathDaily.sort()
for filePath in filesPathDaily:
    hourFile =filePath.split('/')[4].split('_')[1].split('.')[0].split('-')[0]
    minuteFile =filePath.split('/')[4].split('_')[1].split('.')[0].split('-')[1]
    statsFromFile = getStatsFromFile(filePath)
    for k in range (len(statsFromFile)-1):
        Fdaily.write(statsFromFile[k]+ '-' + hourFile + ':' + minuteFile + '\n')
Fdaily.close()

Fweekly = open('js/logs/weekly.txt', 'w+')
for i in range(6, -1, -1):
    prevDate = dateNow-timedelta(days=i)
    prevYear = prevDate.strftime('%Y')
    prevMonth = prevDate.strftime('%m')
    prevDay = prevDate.strftime('%d')
    pathWeekly = 'logs/' + prevYear + '/' + prevMonth + '/' + prevDay+ '/' + '*.txt'
    filesPathWeekly = glob.glob(pathWeekly)
    filesPathWeekly.sort()
    lastFilePath = filesPathWeekly[len(filesPathWeekly)-1]
    yearFile = lastFilePath.split('/')[1]
    monthFile = lastFilePath.split('/')[2]
    dayFile = lastFilePath.split('/')[3]
    statsFromFile = getStatsFromFile(lastFilePath)
    for k in range (len(statsFromFile)-1):
        Fweekly.write(statsFromFile[k]+'-'+dayFile+'/'+monthFile+'/'+yearFile+'\n')
Fweekly.close()

Fmonthly = open('js/logs/monthly.txt', 'w+')
for i in range(29, -1, -1):
    try:
        prevDate = dateNow-timedelta(days=i)
        prevYear = prevDate.strftime('%Y')
        prevMonth = prevDate.strftime('%m')
        prevDay = prevDate.strftime('%d')
        pathMonthly = 'logs/' + prevYear + '/' + prevMonth + '/' + prevDay+ '/' + '*.txt'
        filesPathMonthly = glob.glob(pathMonthly)
        filesPathMonthly.sort()
        lastFilePath = filesPathMonthly[len(filesPathMonthly)-1]
        yearFile = lastFilePath.split('/')[1]
        monthFile = lastFilePath.split('/')[2]
        dayFile = lastFilePath.split('/')[3]
        statsFromFile = getStatsFromFile(lastFilePath)
        for k in range (len(statsFromFile)-1):
            Fmonthly.write(statsFromFile[k]+'-'+dayFile+'/'+monthFile+'/'+yearFile+'\n')
    except:
        continue
Fmonthly.close()
