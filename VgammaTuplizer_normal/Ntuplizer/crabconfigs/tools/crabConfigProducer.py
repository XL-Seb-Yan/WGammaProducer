import os
import string

f = open('SMbkgs.txt', "r")
lines = f.readlines()
outDir = "VgammaTuplizer/Ntuplizer/crabconfigs"


configTemplateFile = open("crabTemplate.py","r")
templateLines = configTemplateFile.readlines()

for bkgDir in lines:
  splitOnSlash = bkgDir.split("/")
  splitOnUnderscore = splitOnSlash[1].split("_")
  bkgName = "%s_%s"%(splitOnUnderscore[0],splitOnUnderscore[1])


  configFileName = "crab_MC2017%s.py"%bkgName
  fullconfigPath = "%s/%s"%(outDir,configFileName)
  print("building config for background %s in file %s"%(bkgName,fullconfigPath))
  if os.path.exists(fullconfigPath):  
    os.remove(fullconfigPath)
  configFile = open(fullconfigPath,"w+")
  

  for line in templateLines:
    retLine = string.replace(string.replace(line,"@BKGNAME@",bkgName),"@DATASET@",bkgDir[:-1])
    configFile.write(retLine)
  configFile.close()
