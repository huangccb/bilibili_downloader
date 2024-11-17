from PyQt6.QtWidgets import *
from threading import Thread
from PyQt6.QtCore import pyqtSignal
import traceback, re, os, tempfile
from videoDownloader import VideoDownloader
from guiFiles.main_ui import Ui_Form
from concurrent.futures import ThreadPoolExecutor


from qfluentwidgets import setTheme, Theme
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

        self.tempPath = ''
        
        #检查Temp文件夹
        self.ckeckTemp()

        #检查缓存中是否有cookie
        if os.path.exists(self.tempPath + '\\cookie.txt'):
            self.tempCookie = open(self.tempPath + '\\cookie.txt', 'r', encoding='utf-8').read()
            self.ui.cookieEdit.setText(self.tempCookie)


    

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
        self.urlText = re.split(' |\n',self.ui.urlEdit.toPlainText())
        self.cookie = self.ui.cookieEdit.text()
        self.urlDecoder = self.ui.comboBox.currentText()
        self.outPath = self.ui.outPath.text()
        if self.outPath == '':
            self.outPath = os.path.expanduser('~') + '\\Videos'  #设置默认文件夹为视频文件夹


        self.ms.text_print.emit(f"视频开始下载，保存路径：{self.outPath}")
        #多线程执行，利用线程池

        startThread = Thread(target=self.startDownload, daemon=True)
        startThread.start()        
        
    def startDownload(self):
        self.executor = ThreadPoolExecutor(max_workers=2)
        for url in self.urlText:
            self.executor.submit(self.download, url=url)        
        self.executor.shutdown(wait=True)
        self.ms.text_print.emit("所有视频已下载！！！")
        


    def download(self, url):

        #写入缓存文件
        if os.path.exists(self.tempPath + '\\cookie.txt') == False or self.cookie != self.tempCookie:
            with open(self.tempPath + '\\cookie.txt', 'w', encoding='utf-8') as f:
                f.write(self.cookie)


        #多线程执行，利用线程池
        try:
            videoDownloader = VideoDownloader()
            title = videoDownloader.getVideo(url, self.cookie, self.outPath, self.urlDecoder, self.tempPath)

            self.ms.text_print.emit(f"{title}：下载完成")

        except Exception:
            # self.pool.terminate()
            self.ms.text_print.emit(f"视频下载失败")                
            self.ms.text_print.emit(traceback.format_exc()) 
            self.executor.shutdown(now=True)

    #关闭窗口前退出进程池
    def closeEvent(self, event):
        self.executor.shutdown(now=True)
        event.accept()

    #处理Temp缓存文件夹
    def ckeckTemp(self):

        #将cookie写入缓存
        self.tempPath = tempfile.gettempdir() + "\\bilibili_video"
        if os.path.exists(self.tempPath) == False:
            os.makedirs(self.tempPath)

        num_files = 0
        for root, dirs, files in os.walk(self.tempPath):
            num_files += len(files)
        
        if num_files > 15:
            file_list = os.listdir(self.tempPath)
            for file in file_list:
                file_path = os.path.join(self.tempPath, file)
                if os.path.isfile(file_path) and file != 'cookie.txt':
                    os.remove(file_path)


if __name__ == '__main__':
    app = QApplication([])
    downloader = Downloader()
    setTheme(Theme.LIGHT)
    downloader.show()
    app.exec()    