from moviepy.editor import *
import tempfile, requests, json, re, os

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

        #判断是否使用ffmpeg
        if self.urlDecoder == "ffmpeg":
            os.system(f"start ffmpeg -i {vdPath} -i {adPath} -c:v copy -c:a copy -bsf:a aac_adtstoasc {putOutPath}")
            # ffmpeg.concat(ffmpeg.input(vdPath), ffmpeg.input(adPath), v=1, a=1).output(putOutPath).run()
        else:
            os.system(f".\\bilibili_downloader\\downloader\\moviepyDownload.exe --vdPath={vdPath} --adPath={adPath} --outPath={putOutPath}")
        return putOutPath


    #获取视频 
    def getVideo(self, url, cookie, outPath, urlDecoder, index, tempPath):
        
        self.tempPath = tempPath
        self.outPath = outPath
        self.urlDecoder = urlDecoder



        #头文件
        headers = {
        "User-Agent" : "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36",
        "Referer" : url,
        "cookie" : cookie
        }

        #访问主页面
        resPage = requests.get(url=url, headers=headers).text



        #获取标题
        self.title = ("视频标题：" + re.findall('title="(.*?)"', resPage)[0])

        #获取音频和视频信息
        videoInfo = re.findall('window.__playinfo__=(.*?)</script>',resPage)[0]
        jsonData = json.loads(videoInfo)
        videoUrl = jsonData['data']['dash']['video'][0]['baseUrl']  #视频链接所在位置
        audioUrl = jsonData['data']['dash']['audio'][0]['baseUrl']  #音频链接所在位置

        #获取视频和音频
        if os.path.exists(f"{self.tempPath}\\{self.title}.mp4") == False:
            videoContent = requests.get(headers=headers, url=videoUrl).content
            with open(f"{self.tempPath}\\{self.title}.mp4", 'wb') as v:
                v.write(videoContent)
        
        if os.path.exists(f"{self.tempPath}\\{self.title}.mp3") == False:
            audioContent = requests.get(headers=headers, url=audioUrl).content
            with open(f"{self.tempPath}\\{self.title}.mp3", 'wb') as a:
                a.write(audioContent)
       
        # 合并视频
        result = self.writeVideo(adPath = f"{self.tempPath}\\{self.title}.mp3", vdPath = f"{self.tempPath}\\{self.title}.mp4")
        checkDownload = [os.path.exists(result), index]
        return checkDownload