import os
import shutil
import urllib.request

# 爬虫
file_dir = "G:\\RetroArch\\info"
a = "https://buildbot.libretro.com/nightly/windows/x86_64/latest/"
b = ".dll.zip"
array = []
for root, dirs, files in os.walk(file_dir):
    for file in files:  
        if os.path.splitext(file)[1] == '.info':
            file = file.replace('.info', b)
            array.append(file)

for index in range(len(array)):
    print (array[index])

# print(os.path.join(a, file))
# 要输出到的文件目录

pathsss = "O:\Jare\Downloads\T\\"
dir_down = ""
for count in range(len(array)):
    file_path = pathsss + array[count]
    c = os.path.join(a, array[count])
    if os.path.exists(file_path) != True:
        print(c, file_path)
        try:
            urllib.request.urlretrieve(c, file_path)  # 下载
        except:
            continue


