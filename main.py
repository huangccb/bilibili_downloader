from PyQt6.QtWidgets import *
from threading import Thread
from PyQt6.QtCore import pyqtSignal
import traceback, re, os
from multiprocessing import Pool
from  guiFiles.main_ui import Ui_Form
from videoDownloader import VideoDownloader



#自定义信号
class FinishSignals(QWidget):
    text_print = pyqtSignal(str)

#加载UILoader
# uiloader = QUiLoader()

class Downloader(QWidget, Ui_Form):
    
    def __init__(self):
        
        #加载ui文件
        super().__init__()
        self.ui = Ui_Form()
        self.ui.setupUi(self)

        #设置cookie链接按钮
        self.ui.linkButton.setUrl("https://blog.csdn.net/qq_28821897/article/details/132002110")
        

        # self.ui = uiloader.load('.\GUI-Files\main.ui')

        #自定义信号的处理参数
        self.ms = FinishSignals()
        self.ms.text_print.connect(self.printToGui)

        #处理下载按钮
        self.ui.pushButton.clicked.connect(self.handleCalc)

        #处理点击按钮
        self.ui.clearButton.clicked.connect(self.clearText)

    #打印信号处理
    def printToGui(self, text):
        self.ui.outBrowser.append(str(text))
        self.ui.outBrowser.ensureCursorVisible()


    #清除日志
    def clearText(self):
        self.ui.outBrowser.clear()

    #处理下载
    def handleCalc(self):

        # #获取变量并执行下载任务
        urlText = re.split(' |\n',self.ui.urlEdit.toPlainText())
        cookie = self.ui.cookieEdit.text()
        urlDecoder = self.ui.comboBox.currentText()
        outPath = self.ui.outPath.text()
        if outPath == '':
            outPath = os.path.expanduser('~') + '\\Videos'  #设置默认文件夹为视频文件夹

        thread = Thread(target=self.download,
                        args=(urlText, cookie, urlDecoder, outPath), daemon=True

        )
        thread.start()
            
        

        


    def download(self,urls, cookie, urlDecoder, outPath):
        threadList = []
        pool = Pool(2)
        self.ms.text_print.emit(f"视频开始下载，保存路径：{outPath}")
        downloadNum = 0
        #多线程执行，利用线程池
        try:
            videoDownloader = VideoDownloader()
            for url in urls:
                downloadNum += 1

                threadList.append(pool.apply_async(videoDownloader.getVideo, (url, cookie, outPath, urlDecoder, downloadNum, )))
                
            pool.close()
            pool.join()
            # allTask = [executor.submit(VideoDownloader.getVideo,  (url, cookie, outPath, urlDecoder, downloadNum)) for url in]

            #获取输出
            # for t in pool(threadList):
                # checkDownload = t.get()
                # if checkDownload[0] == True:
                #     self.ms.text_print.emit(f"链接{checkDownload[1]}已完成下载")
                # else:
                #     self.ms.text_print.emit(f"链接{checkDownload[1]}下载失败")
            self.ms.text_print.emit("所有视频已完成下载")


        # videoDownloader = VideoDownloader()
        # try:
        #     path = videoDownloader.getVideo(urlText, cookie, outPath, urlDecoder)
        #     if path == '':
        #         self.ms.text_print.emit(f"视频下载失败")
        #         return
        #     self.ms.text_print.emit(f"视频下载成功")

        except Exception as e:
            pool.terminate()
            self.ms.text_print.emit(f"视频下载失败")                
            self.ms.text_print.emit(traceback.format_exc()) 




if __name__ == '__main__':
    app = QApplication([])
    donloader = Downloader()
    donloader.show()
    app.exec()    

        