from moviepy.editor import *
import tempfile, requests, json, re, os, ffmpeg
class VideoDownloader():
    
    def __init__(self):
    
        #文件默认路径
        self.roadPath = os.getcwd()  

        #获取缓存路径并添加文件夹
        self.tempPath = tempfile.gettempdir() + "\\bilibili_video"
        if os.path.exists(self.tempPath) == False:
            os.makedirs(self.tempPath)

    #合并视频和音频
    def writeVideo(self, adPath, vdPath, outPath, urlDecoder, title):
        
        putOutPath = f"{outPath}\\{title}.mp4"
        #判断是否使用ffmpeg
        if urlDecoder == "ffmpeg":
            # os.system(f"start cmd /k ffmpeg -i {vdPath} -i {adPath} -c:v copy -c:a copy -bsf:a aac_adtstoasc {putOutPath}")
            ffmpeg.concat(ffmpeg.input(vdPath), ffmpeg.input(adPath), v=1, a=1).output(putOutPath).run()
        else:

            #使用moviepy
            ad = AudioFileClip(adPath)
            vd = VideoFileClip(vdPath)

            vd2 = vd.set_audio(ad)
            vd2.write_videofile(outPath,threads = 32)


    #获取视频 
    def getVideo(self, urlText, cookie, outPath, urlDecoder):

        if outPath == '':
            outPath = os.path.expanduser('~') + '\\Videos'  #设置默认文件夹为视频文件夹

        for url in urlText:
            #头文件
            headers = {
            "User-Agent" : "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36",
            "Referer" : url,
            "cookie" : cookie
            }

            #访问主页面
            resPage = requests.get(url=url, headers=headers).text



            #获取标题
            title = ("视频标题：" + re.findall('title="(.*?)"', resPage)[0])

            #获取音频和视频信息
            videoInfo = re.findall('window.__playinfo__=(.*?)</script>',resPage)[0]
            jsonData = json.loads(videoInfo)
            videoUrl = jsonData['data']['dash']['video'][0]['baseUrl']  #视频链接所在位置
            audioUrl = jsonData['data']['dash']['audio'][0]['baseUrl']  #音频链接所在位置

            #获取视频和音频
            videoContent = requests.get(headers=headers, url=videoUrl).content
            audioContent = requests.get(headers=headers, url=audioUrl).content

            #将视频和音频写入缓存文件夹
            with open(f"{self.tempPath}\\{title}.mp4", 'wb') as v:
                v.write(videoContent)
            with open(f"{self.tempPath}\\{title}.mp3", 'wb') as a:
                a.write(audioContent)

            # 合并视频
            self.writeVideo(adPath = f"{self.tempPath}\\{title}.mp3", vdPath = f"{self.tempPath}\\{title}.mp4", outPath=outPath, urlDecoder=urlDecoder, title=title)
        return outPath