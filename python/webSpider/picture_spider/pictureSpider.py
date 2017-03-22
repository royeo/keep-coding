import urllib.request
import socket
import re
import sys
import os

targetDir = r"/home/ljn/WorkSpace/WebSpider/load"

# 设置保存地址
def destFile(path):
    if not os.path.isdir(targetDir):
        os.mkdir(targetDir)
    pos = path.rindex('/')
    t = os.path.join(targetDir, path[pos+1:])
    return t

# 保持爬取回来的报文
def saveFile(data):
    save_path = r"/home/ljn/WorkSpace/WebSpider/content.html"
    f_obj = open(save_path, 'wb')
    f_obj.write(data)
    f_obj.close()

if __name__ == "__main__":
    webUrl = 'http://www.douban.com'

    # 最简单的获取页面
    data = urllib.request.urlopen(webUrl).read()

    # 设置http请求的头
    webheaders = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:23.0) Gecko/20100101 Firefox/23.0'}
    webReq = urllib.request.Request(url=webUrl, headers=webheaders)
    webPage = urllib.request.urlopen(webReq)
    data = webPage.read()

    # 保持爬取的页面
    saveFile(data)

    for link, t in set(re.findall(r'(https:[^\s]*?(jpg|png|gif))', str(data))):
        print(link)
        try:
            urllib.request.urlretrieve(link, destFile(link))
        except:
            print('失败')


    # print(data)
    # print(type(webPage))
    # print(webPage.geturl())
    # print(webPage.info())
    # print(webPage.getcode())
