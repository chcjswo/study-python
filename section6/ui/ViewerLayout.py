# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'youtube_viewer_v1.0.ui'
#
# Created by: PyQt5 UI code generator 5.10.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_YoutubeDownload(object):
    def setupUi(self, YoutubeDownload):
        YoutubeDownload.setObjectName("YoutubeDownload")
        YoutubeDownload.resize(980, 800)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(YoutubeDownload.sizePolicy().hasHeightForWidth())
        YoutubeDownload.setSizePolicy(sizePolicy)
        YoutubeDownload.setMinimumSize(QtCore.QSize(980, 800))
        YoutubeDownload.setMaximumSize(QtCore.QSize(980, 800))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("C:\\\\Users\\\\User\\\\workspace\\\\study-python\\\\section6/resource/title_ico.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        YoutubeDownload.setWindowIcon(icon)
        self.centralwidget = QtWidgets.QWidget(YoutubeDownload)
        self.centralwidget.setObjectName("centralwidget")
        self.groupBox = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox.setGeometry(QtCore.QRect(10, 10, 311, 441))
        self.groupBox.setObjectName("groupBox")
        self.label = QtWidgets.QLabel(self.groupBox)
        self.label.setGeometry(QtCore.QRect(60, 20, 191, 141))
        self.label.setText("")
        self.label.setPixmap(QtGui.QPixmap("C:\\\\Users\\\\User\\\\workspace\\\\study-python\\\\section6/resource/logo.png"))
        self.label.setObjectName("label")
        self.pushButton = QtWidgets.QPushButton(self.groupBox)
        self.pushButton.setGeometry(QtCore.QRect(10, 170, 281, 41))
        self.pushButton.setObjectName("pushButton")
        self.calendarWidget = QtWidgets.QCalendarWidget(self.groupBox)
        self.calendarWidget.setGeometry(QtCore.QRect(10, 220, 281, 211))
        self.calendarWidget.setObjectName("calendarWidget")
        self.groupBox_2 = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox_2.setGeometry(QtCore.QRect(330, 10, 641, 441))
        self.groupBox_2.setObjectName("groupBox_2")
        self.webView = QtWebEngineWidgets.QWebEngineView(self.groupBox_2)
        self.webView.setGeometry(QtCore.QRect(10, 10, 621, 421))
        self.webView.setUrl(QtCore.QUrl("about:blank"))
        self.webView.setObjectName("webView")
        self.line = QtWidgets.QFrame(self.centralwidget)
        self.line.setGeometry(QtCore.QRect(10, 453, 961, 16))
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.groupBox_3 = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox_3.setGeometry(QtCore.QRect(10, 470, 491, 241))
        self.groupBox_3.setObjectName("groupBox_3")
        self.label_4 = QtWidgets.QLabel(self.groupBox_3)
        self.label_4.setGeometry(QtCore.QRect(20, 40, 71, 16))
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(self.groupBox_3)
        self.label_5.setGeometry(QtCore.QRect(30, 90, 71, 16))
        self.label_5.setObjectName("label_5")
        self.label_6 = QtWidgets.QLabel(self.groupBox_3)
        self.label_6.setGeometry(QtCore.QRect(30, 130, 71, 16))
        self.label_6.setObjectName("label_6")
        self.lineEdit = QtWidgets.QLineEdit(self.groupBox_3)
        self.lineEdit.setGeometry(QtCore.QRect(90, 30, 321, 31))
        self.lineEdit.setObjectName("lineEdit")
        self.pushButton_2 = QtWidgets.QPushButton(self.groupBox_3)
        self.pushButton_2.setGeometry(QtCore.QRect(420, 30, 61, 31))
        self.pushButton_2.setObjectName("pushButton_2")
        self.lineEdit_2 = QtWidgets.QLineEdit(self.groupBox_3)
        self.lineEdit_2.setGeometry(QtCore.QRect(90, 80, 321, 31))
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.toolButton = QtWidgets.QToolButton(self.groupBox_3)
        self.toolButton.setGeometry(QtCore.QRect(420, 80, 61, 31))
        self.toolButton.setObjectName("toolButton")
        self.comboBox = QtWidgets.QComboBox(self.groupBox_3)
        self.comboBox.setGeometry(QtCore.QRect(90, 130, 391, 31))
        self.comboBox.setObjectName("comboBox")
        self.pushButton_3 = QtWidgets.QPushButton(self.groupBox_3)
        self.pushButton_3.setGeometry(QtCore.QRect(90, 170, 241, 51))
        self.pushButton_3.setObjectName("pushButton_3")
        self.pushButton_4 = QtWidgets.QPushButton(self.groupBox_3)
        self.pushButton_4.setGeometry(QtCore.QRect(334, 170, 151, 51))
        self.pushButton_4.setObjectName("pushButton_4")
        self.groupBox_4 = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox_4.setGeometry(QtCore.QRect(510, 470, 461, 241))
        self.groupBox_4.setObjectName("groupBox_4")
        self.plainTextEdit = QtWidgets.QPlainTextEdit(self.groupBox_4)
        self.plainTextEdit.setGeometry(QtCore.QRect(10, 20, 441, 211))
        self.plainTextEdit.setObjectName("plainTextEdit")
        self.line_2 = QtWidgets.QFrame(self.centralwidget)
        self.line_2.setGeometry(QtCore.QRect(10, 714, 961, 16))
        self.line_2.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_2.setObjectName("line_2")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(10, 734, 81, 21))
        self.label_2.setObjectName("label_2")
        self.line_3 = QtWidgets.QFrame(self.centralwidget)
        self.line_3.setGeometry(QtCore.QRect(90, 734, 20, 21))
        self.line_3.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_3.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_3.setObjectName("line_3")
        self.progressBar = QtWidgets.QProgressBar(self.centralwidget)
        self.progressBar.setGeometry(QtCore.QRect(110, 734, 391, 21))
        self.progressBar.setProperty("value", 0)
        self.progressBar.setObjectName("progressBar")
        self.progressBar_2 = QtWidgets.QProgressBar(self.centralwidget)
        self.progressBar_2.setGeometry(QtCore.QRect(620, 734, 351, 21))
        self.progressBar_2.setProperty("value", 0)
        self.progressBar_2.setObjectName("progressBar_2")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(514, 734, 81, 21))
        self.label_3.setObjectName("label_3")
        self.line_4 = QtWidgets.QFrame(self.centralwidget)
        self.line_4.setGeometry(QtCore.QRect(594, 734, 20, 21))
        self.line_4.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_4.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_4.setObjectName("line_4")
        YoutubeDownload.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(YoutubeDownload)
        self.statusbar.setObjectName("statusbar")
        YoutubeDownload.setStatusBar(self.statusbar)

        self.retranslateUi(YoutubeDownload)
        QtCore.QMetaObject.connectSlotsByName(YoutubeDownload)

    def retranslateUi(self, YoutubeDownload):
        _translate = QtCore.QCoreApplication.translate
        YoutubeDownload.setWindowTitle(_translate("YoutubeDownload", "MainWindow"))
        self.groupBox.setTitle(_translate("YoutubeDownload", "기본정보"))
        self.pushButton.setText(_translate("YoutubeDownload", "인증"))
        self.groupBox_2.setTitle(_translate("YoutubeDownload", "미리보기"))
        self.groupBox_3.setTitle(_translate("YoutubeDownload", "다운로드 URL 및 저장 위치 지정"))
        self.label_4.setText(_translate("YoutubeDownload", "Video URL:"))
        self.label_5.setText(_translate("YoutubeDownload", "Save To:"))
        self.label_6.setText(_translate("YoutubeDownload", "Stream:"))
        self.pushButton_2.setText(_translate("YoutubeDownload", "확인"))
        self.toolButton.setText(_translate("YoutubeDownload", "..."))
        self.pushButton_3.setText(_translate("YoutubeDownload", "시작"))
        self.pushButton_4.setText(_translate("YoutubeDownload", "종료"))
        self.groupBox_4.setTitle(_translate("YoutubeDownload", "로그"))
        self.label_2.setText(_translate("YoutubeDownload", "브라우저 로딩"))
        self.label_3.setText(_translate("YoutubeDownload", "다운로드 로딩"))

from PyQt5 import QtWebEngineWidgets

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    YoutubeDownload = QtWidgets.QMainWindow()
    ui = Ui_YoutubeDownload()
    ui.setupUi(YoutubeDownload)
    YoutubeDownload.show()
    sys.exit(app.exec_())