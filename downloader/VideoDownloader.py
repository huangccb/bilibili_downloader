from moviepy.editor import *
import requests, json, re, os

class VideoDownloader():

    def __init__(self):
        self.outPath = ''
        self.tempPath = ''
        self.urlDecoder = ''
        self.title = ''


    #合并视频和音频
    def writeVideo(self, adPath, vdPath):
        
        putOutPath = f"{self.outPath}\\{self.title}.mp4"

        if os.path.exists(putOutPath): return putOutPath
        self.selfPath = os.path.dirname(os.path.abspath(__file__))
        
        #判断是否使用ffmpeg
        if self.urlDecoder == "ffmpeg":
            os.system(f"{self.selfPath}\\ffmpeg\\bin\\ffmpeg.exe -i {vdPath} -i {adPath} -c:v copy -c:a copy -bsf:a aac_adtstoasc {putOutPath}")
            print(self.selfPath)
        else:
            os.system(f"{self.selfPath}\\moviepy\\moviepyDownload.exe --vdPath={vdPath} --adPath={adPath} --outPath={putOutPath}")


    def getVideo(self, url, path, title):
        videoContent = requests.get(headers=self.headers, url=url).content
        with open(f"{path}\\{title}.mp4", 'wb') as v:
            v.write(videoContent)
        
    def getAudio(self, url, path, title):
        audioContent = requests.get(headers=self.headers, url=url).content
        with open(f"{path}\\{title}.mp3", 'wb') as a:
            a.write(audioContent)

    #获取视频 
    def getPage(self, url, cookie, outPath, urlDecoder, tempPath):
        
        self.tempPath = tempPath
        self.outPath = outPath
        self.urlDecoder = urlDecoder



        #头文件
        self.headers = {
        "User-Agent" : "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36",
        "Referer" : url,
        "cookie" : cookie
        }

        #访问主页面
        resPage = requests.get(url=url, headers=self.headers).text



        #获取标题
        self.title = re.findall('title="(.*?)"', resPage)[0]

        #获取音频和视频信息
        videoInfo = re.findall('window.__playinfo__=(.*?)</script>',resPage)[0]
        jsonData = json.loads(videoInfo)
        videoUrl = jsonData['data']['dash']['video'][0]['baseUrl']  #视频链接所在位置
        audioUrl = jsonData['data']['dash']['audio'][0]['baseUrl']  #音频链接所在位置

        #获取视频和音频
        if os.path.exists(f"{self.tempPath}\\{self.title}.mp4") == False:
            self.getVideo(url=videoUrl, path=self.tempPath, title=self.title)
        
        if os.path.exists(f"{self.tempPath}\\{self.title}.mp3") == False:
            self.getAudio(url=audioUrl, path=self.tempPath, title=self.title)
       
        # 合并视频
        self.writeVideo(adPath = f"{self.tempPath}\\{self.title}.mp3", vdPath = f"{self.tempPath}\\{self.title}.mp4")
        return self.title