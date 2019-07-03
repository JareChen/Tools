# 批量修改压缩包内文件名，处理游戏rom文件名编码格式不对导致乱码
import subprocess
import os
import zipfile

def ReName(filePath):
    # # 默认模式r,读
    azip = zipfile.ZipFile(filePath)  # ['bb/', 'bb/aa.txt']
    # # 返回所有文件夹和文件
    fileNames = azip.namelist()
    if len(fileNames) == 1:
        fileName = fileNames[0]
        print(fileName)
        fileName = fileName.encode("cp437","ignore").decode("GBK", "ignore")
        print(fileName)
        azip.close()
        cmdstr = "WinRAR.exe rn \"%s\" *.* \"%s\"" % (filePath, fileName)
        print(cmdstr)
        print(subprocess.call(cmdstr))
        
i = 0
os.chdir(r'C:\Program Files\WinRAR')
path = r'E:\SFC中文游戏全集\\'
for fileName in os.listdir(path):
    filePath = path + fileName
    if os.path.isfile(filePath):
        i = i + 1
        ReName(filePath)
    else:
        for fileName1 in os.listdir(filePath + "\\"):
            filePath1 = filePath + "\\" + fileName1
            i = i + 1
            ReName(filePath1)