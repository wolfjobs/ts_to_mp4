import time
from urllib.request import urlretrieve
import ssl
import re
import os
import _thread

# 获取ts文件参数

hostname = 'https://zk.603ee.com/'
# date = time.strftime("%Y/%m/%d")
date = '2019/07/15'
secret = '/05HnRV0XKDcP4wye/'
tsParamUrl = hostname + date + secret + '023.ts'
tsPath = "./mp4/" + date.replace('/', '_') + secret

ssl._create_default_https_context = ssl._create_unverified_context


# tsParamData = urllib.request.urlopen(tsParamUrl).read().decode('utf-8', "ignore")

# print(tsParamData)

# pat = '/(.*?).ts'
# tsParamArr = re.compile(pat).findall(tsParamData)
# print(tsParamArr)

def aaa(s, e):
    # 爬取ts文件到本地
    for n in range(s, e):
        # strArr = tsParamArr[n].split('/')
        nn = ''
        if n < 10:
            nn = 'out00%d' % (n)
        elif n < 100:
            nn = 'out0%d' % (n)
        else:
            nn = 'out%d' % (n)
        localTSFileName = nn + '.ts'
        print(localTSFileName)
        tsLink = hostname + date + secret + nn + '.ts'
        if not os.path.isfile(os.path.join(tsPath, localTSFileName)):
            urlretrieve(tsLink, os.path.join(tsPath, localTSFileName))
            print(tsLink)


path_list = os.listdir(tsPath)
print(len(path_list))
if len(path_list) == 250:
    # 对文件进行排序并将排序后的ts文件路径放入列表中
    path_list.sort()
    li = [os.path.join(tsPath, filename) for filename in path_list]
    # 将ts路径并合成一个字符参数
    tsfiles = '|'.join(li)

    print(tsfiles)

    # 指定输出文件名称
    saveMp4file = tsPath + 'target.mp4'

    # 调取系统命令使用ffmpeg将ts合成mp4文件
    cmd = 'ffmpeg -i "concat:%s" -acodec copy -vcodec copy -bsf:v h264_mp4toannexb %s' % (tsfiles, saveMp4file)

    os.system(cmd)
    quit()

# 开启多线程进行数据爬取
try:
    # _thread.start_new_thread(aaa, (0, 25))
    # _thread.start_new_thread(aaa, (25, 50))
    # _thread.start_new_thread(aaa, (50, 75))
    # _thread.start_new_thread(aaa, (75, 100))
    # _thread.start_new_thread(aaa, (100, 130))
    # _thread.start_new_thread(aaa, (130, 140))
    # _thread.start_new_thread(aaa, (140, 150))
    # _thread.start_new_thread(aaa, (150, 180))
    # _thread.start_new_thread(aaa, (180, 200))
    _thread.start_new_thread(aaa, (0, 250))
except:
    print("Error: 无法启动线程")

while 1:
    pass
