import sys
from PyQt5.QtWidgets import *
from PyQt5 import QtCore
from PyQt5.QtCore import pyqtSlot, pyqtSignal, QUrl
from PyQt5 import uic
import re
import datetime
import os
from lib.ViewerLayout import Ui_YoutubeDownload
from lib.AuthDialog import AuthDialog


# form_class = uic.loadUiType('C:\\Users\\User\\workspace\\study-python\\section6\\ui\\youtube_viewer_v1.0.ui')[0]

class Main(QMainWindow, Ui_YoutubeDownload):
    def __init__(self):
        super().__init__()
        # 초기화
        self.setupUi(self)
        # 초기 잠금
        self.initAuthLock()
        # 시그널 초기
        self.initSignal()
        # 로그인 관련 변
        self.user_id = 'test'
        self.user_pw = None
        # 재생 여부
        self.is_play = False

    # 기본 UI 비활성화
    def initAuthLock(self):
        self.previewButton.setEnabled(False)
        self.fileNavButton.setEnabled(False)
        self.streamCombobox.setEnabled(False)
        self.startButton.setEnabled(False)
        self.calendarWidget.setEnabled(False)
        self.urlTextEdit.setEnabled(False)
        self.pathTextEdit.setEnabled(False)
        # self.showStatusMsg('인증 안됨')

    # 기본 UI 활성화
    def initAuthActive(self):
        self.previewButton.setEnabled(True)
        self.fileNavButton.setEnabled(True)
        self.streamCombobox.setEnabled(True)
        self.calendarWidget.setEnabled(True)
        self.urlTextEdit.setEnabled(True)
        self.pathTextEdit.setEnabled(True)
        # self.showStatusMsg('인증 완료')

    def showStatusMsg(self, msg):
        self.statusBar.showMessage(msg)

    def initSignal(self):
        self.loginButton.clicked.connect(self.authCheck)
        self.previewButton.clicked.connect(self.load_url)
        self.exitButton.clicked.connect(QtCore.QCoreApplication.instance().quit)

    @pyqtSlot()
    def authCheck(self):
        # dlg = AuthDialog()
        # dlg.exec_()
        # self.user_id = dlg.user_id
        # self.user_pw = dlg.user_pw
        # print('id: %s password: %s' %(self.user_id, self.user_pw))

        if True:
            self.initAuthActive()
            self.loginButton.setText('인증완료')
            self.loginButton.setEnabled(False)
            self.urlTextEdit.setEnabled(True)
            self.append_log_msg('login success')
        else:
            QMessageBox(self, '인증오류', '아이디 또는 비밀번호 인증 오류')

    def load_url(self):
        url = self.urlTextEdit.text().strip()
        print(url)
        v = re.compile('^https://www.youtube.com/?')
        if self.is_play:
            pass
        else:
            if v.match(url) is not None:
                print('play~~~')
                self.append_log_msg('Play Click')
                self.webView.load(QUrl(url))
                # self.showStatusMsg(url + ' 재생중')
                self.previewButton.setText('중지')
                self.is_play = True
            else:
                print('asdfasdfasdasdsadfsaf')

    def append_log_msg(self, msg):
        now = datetime.datetime.now()
        nowDatatime = now.strftime('%Y-%m-%d %H:%M:%S')
        app_msg = self.user_id + ' : ' + msg + ' - (' + nowDatatime + ')'
        # print(app_msg)
        self.plainTextEdit.appendPlainText(app_msg)

        # 활동 로그 저장
        with open('C:\\Users\\User\\workspace\\study-python\\section6\\log\\log.txt', 'a') as f:
            f.write(app_msg + '\n')

if __name__ == '__main__':
    app = QApplication(sys.argv)
    viewer = Main()
    viewer.show()
    app.exec_()
