import os
playlistExt = ".lpl"
playlistFormat = """{
  "version": "1.0",
  "items": [%s
  ]
}"""

fileFormat = """
    {
      "path": "%s",
      "label": "%s",
      "core_path": "DETECT",
      "core_name": "DETECT",
      "crc32": "DETECT",
      "db_name": "%s"
    },"""
path = input("输入路径：")

playlistName = path.split("\\")[-1] + playlistExt

filelistStr = ""
def FindFile(path):
    global filelistStr
    for fileName in os.listdir(path):
        filePath = os.path.join(path, fileName)
        if os.path.isfile(filePath):
            oneFileStr = fileFormat % (filePath, path.split("\\")[-1], playlistName)
            filelistStr = filelistStr + oneFileStr
        else:
            FindFile(filePath)


FindFile(path)
plistListStr = (playlistFormat % (filelistStr[0:-1])).replace("\\", "/")
with open(os.path.join(path, playlistName), "w", newline='\n') as f:
    f.write(plistListStr)
    