import sys
from PyQt5.QtWidgets import *
from PyQt5 import QtCore
from PyQt5 import uic
import re
import datetime
import os
from lib.ViewerLayout import Ui_YoutubeDownload

# form_class = uic.loadUiType('C:\\Users\\User\\workspace\\study-python\\section6\\ui\\youtube_viewer_v1.0.ui')[0]

class Main(QMainWindow, Ui_YoutubeDownload):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    viewer = Main()
    viewer.show()
    app.exec_()
