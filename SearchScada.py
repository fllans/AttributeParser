import glob
import re
from xml.dom.minidom import Document
import psutil
import subprocess


diskList = psutil.disk_partitions()
for i in range (len(diskList)):
    diskList[i] = str(diskList[i]).split(", ")
    while len(diskList[i]) != 1:
        diskList[i].pop()
    diskList[i] = diskList[i][0].replace("sdiskpart(device='", "").replace("\\'", "")
# print(diskList)

listOfScada = [0]*len(diskList)
for i in range(len(diskList)):
    listOfScada[i] = glob.glob(f'{diskList[i]}*/Scada*Client*')
    listOfScada[i] = listOfScada[i]
# print(listOfScada)

scadaList = []
for i in range(len(listOfScada)):
    scadaList = scadaList+listOfScada[i]
# print(scadaList)

for i in range(len(scadaList)):
    scadaList[i] = scadaList[i].replace("Scada.Client", "")
print(scadaList)