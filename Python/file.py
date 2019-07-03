# 批量修改文件名并去重，处理游戏rom名称太复杂且重复
import shutil,os

path = r'E:\NDS中文游戏全集\\'
FTPath = path + "繁体\\"
CFPath = path + "重复\\"
ext = ".7z"
if not os.path.exists(FTPath):
   os.makedirs(FTPath)
if not os.path.exists(CFPath):
   os.makedirs(CFPath)

for fileName in os.listdir(path):
   sIndex1 = fileName.find("[")
   sIndex2 = fileName.find(" (")
   sIndex3 = fileName.find("(")

   sIndex = sIndex1

   if (sIndex > sIndex2 and sIndex2 != -1) or sIndex == -1:
      sIndex = sIndex2
   
   if (sIndex > sIndex3 and sIndex3 != -1) or sIndex == -1:
      sIndex = sIndex3

   print(sIndex, sIndex1, sIndex2, sIndex3)
   if fileName.find("繁体") != -1 or fileName.find("(繁")!= -1 or fileName.find("[繁")!= -1:
      oPath = path + fileName
      nPath =  FTPath + fileName
      if os.path.isfile(oPath):
         print(oPath, nPath)
         shutil.move(oPath, nPath)
   else:
      if sIndex != -1:
         oPath = path + fileName
         if os.path.isfile(oPath):
            nfileName = fileName[0:sIndex] + ext
            if os.path.exists(path + nfileName):
               shutil.move(path + fileName, CFPath + fileName)
               print(oPath, path + nfileName)
            else:
               shutil.move(path + fileName, path + nfileName)
               print(oPath, path + nfileName)
         


