#from moviepy import *
import requests, json, re, os, shutil
from downloader.getWbi import GetWbi

class VideoDownloader():

    def __init__(self):
        self.outPath = ''
        self.tempPath = ''
        self.urlDecoder = ''
        self.title = ''
        self.video = False
        self.audio = False

        #头文件
        self.headers = {
        "User-Agent" : "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36",
        "Referer" : "https://www.bilibili.com/",
        }

    #合并视频和音频
    def writeVideo(self, adPath, vdPath):
        putOutPath = f"{self.outPath}\\{self.title}.mp4"


        if(self.video == False or self.audio == False):
            shutil.copy(vdPath, putOutPath)

        if os.path.exists(putOutPath): return putOutPath
        self.selfPath = os.path.dirname(os.path.abspath(__file__))
        
        # #判断是否使用ffmpeg
        # if self.urlDecoder == "ffmpeg":
        #     os.system(f"{self.selfPath}\\ffmpeg\\bin\\ffmpeg.exe -i {vdPath} -i {adPath} -c:v copy -c:a copy -bsf:a aac_adtstoasc {putOutPath}")
        # else:
        #     os.system(f"{self.selfPath}\\moviepy\\moviepyDownload.exe --vdPath={vdPath} --adPath={adPath} --outPath={putOutPath}")


    def getVideo(self, url, path, title):
        videoContent = requests.get(headers=self.headers, url=url).content
        with open(f"{path}\\{title}.mp4", 'wb') as v:
            v.write(videoContent)
        
    def getAudio(self, url, path, title):
        audioContent = requests.get(headers=self.headers, url=url).content
        with open(f"{path}\\{title}.mp3", 'wb') as a:
            a.write(audioContent)

    def getInfo(self, sessdata, bvid):
        api = "https://api.bilibili.com/x/web-interface/view"
        params = {
            'bvid': bvid
        }

        cookies = {"SESSDATA":sessdata}

        res = requests.get(url=api, headers=self.headers, params=params, cookies=cookies).json()

        cid = res['data']['cid']
        title = res['data']['title']
        return cid, title


    #获取视频 
    def getPage(self, url, cookie, outPath, urlDecoder, tempPath):
        
        self.tempPath = tempPath
        self.outPath = outPath
        self.urlDecoder = urlDecoder
        bvid = re.findall("https://www.bilibili.com/video/(.*?)/\?.*?", url)[0]
        sessdata = re.findall("SESSDATA=(.*?);", cookie)[0]
        sessdata_cookie = {"SESSDATA":sessdata}
        #获取cid和标题
        cid, self.title = self.getInfo(bvid=bvid, sessdata=sessdata)

        params = {
            'bvid': bvid,
            'qn':'80',
            'fnval':'1',
            'cid': cid,
        }


        # 获取视频信息
        getwbi = GetWbi()
        paramUrl = getwbi.getWbi(params=params,sessdata=sessdata)
        playUrl = "https://api.bilibili.com/x/player/wbi/playurl?" + paramUrl
        resp = requests.get(url=playUrl, headers=self.headers, cookies=sessdata_cookie).json()
        videoUrl = resp['data']['durl'][0]['url']

        #获取视频
        if os.path.exists(f"{self.tempPath}\\{self.title}.mp4") == False:
            self.getVideo(url=videoUrl, path=self.tempPath, title=self.title)
            self.video = True

        self.writeVideo(adPath = f"{self.tempPath}\\{self.title}.mp3", vdPath = f"{self.tempPath}\\{self.title}.mp4")
        return self.title
    

