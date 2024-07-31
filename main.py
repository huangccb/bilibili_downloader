from PyQt6.QtWidgets import *
from threading import Thread
from PyQt6.QtCore import pyqtSignal
import traceback, re, time
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
        self.threads = []    #管理线程

        thread = Thread(target=self.download,
                        args=(urlText, cookie, urlDecoder, outPath), daemon=True

        )
        thread.start()
        self.threads.append(thread)

        self.ms.text_print.emit("视频开始下载")
            
        

        


    def download(self,urlText, cookie, urlDecoder, outPath):

        videoDownloader = VideoDownloader()
        try:
            path = videoDownloader.getVideo(urlText, cookie, outPath, urlDecoder)
            if path == '':
                self.ms.text_print.emit(f"视频下载失败")
                return
            self.ms.text_print.emit(f"视频下载成功")

        except Exception as e:
            self.ms.text_print.emit(f"视频下载失败")                
            self.ms.text_print.emit(traceback.format_exc()) 




if __name__ == '__main__':
    app = QApplication([])
    donloader = Downloader()
    donloader.show()
    app.exec()    

        