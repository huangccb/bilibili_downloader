from PyQt6.QtWidgets import *
from threading import Thread
from PyQt6.QtCore import pyqtSignal
import traceback
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


    #清除日志
    def clearText(self):
        self.ui.outBrowser.clear()

    def handleCalc(self):

        # #获取变量并执行下载任务
        url = self.ui.urlEdit.text()
        cookie = self.ui.cookieEdit.text()
        urlDecoder = self.ui.comboBox.currentText()
        outPath = self.ui.outPath.text()

        thread = Thread(target=self.download,
                        args=(url, cookie, urlDecoder, outPath)

        )

        thread.start()

        self.ui.outBrowser.append('---------开始下载---------')
        self.ui.outBrowser.ensureCursorVisible()


    def download(self, url, cookie, urlDecoder, outPath):
        try:
            videoDownloader = VideoDownloader()
            path = videoDownloader.getVideo(url, cookie, outPath, urlDecoder)
            if path != '':
                self.ms.text_print.emit(f"文件已保存在{path}")
                self.ms.text_print.emit("---------下载成功---------")


        except Exception as e:
            self.ms.text_print.emit("---------下载失败---------")                
            self.ms.text_print.emit(traceback.format_exc()) 




if __name__ == '__main__':
    app = QApplication([])
    donloader = Downloader()
    donloader.show()
    app.exec()    

        