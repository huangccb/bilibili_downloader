import logging
class Log():
    def __init__(self):
        self.logger = logging.getLogger('download_logger')
        self.logger.setLevel(logging.DEBUG)

        #设置输出格式和文件
        file_handler = logging.FileHandler('app.log')
        formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
        file_handler.setFormatter(formatter)

        #将文件处理器添加到日志记录器
        self.logger.addHandler(file_handler)

    def errorLog(self, text):
        self.logger.error(text)

    def debugLog(self, text):
        self.logger.debug(text)
        
    def infoLog(self, text):
        self.logger.info(text)

    def warnLog(self, text):
        self.logger.warning(text)