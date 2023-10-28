# Form implementation generated from reading ui file 'untitled.ui'
#
# Created by: PyQt6 UI code generator 6.5.0
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(801, 599)
        self.centralwidget = QtWidgets.QWidget(parent=MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.btnGenerate = QtWidgets.QPushButton(parent=self.centralwidget)
        self.btnGenerate.setGeometry(QtCore.QRect(670, 510, 131, 41))
        self.btnGenerate.setObjectName("btnGenerate")
        self.progressBar = QtWidgets.QProgressBar(parent=self.centralwidget)
        self.progressBar.setGeometry(QtCore.QRect(0, 530, 661, 23))
        self.progressBar.setProperty("value", 0)
        self.progressBar.setObjectName("progressBar")
        self.threads_slider = QtWidgets.QSlider(parent=self.centralwidget)
        self.threads_slider.setGeometry(QtCore.QRect(10, 500, 211, 21))
        self.threads_slider.setMinimum(1)
        self.threads_slider.setMaximum(200)
        self.threads_slider.setSliderPosition(30)
        self.threads_slider.setOrientation(QtCore.Qt.Orientation.Horizontal)
        self.threads_slider.setObjectName("threads_slider")
        self.label = QtWidgets.QLabel(parent=self.centralwidget)
        self.label.setGeometry(QtCore.QRect(10, 480, 111, 16))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(parent=self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(10, 10, 61, 16))
        self.label_2.setObjectName("label_2")
        self.edNickname = QtWidgets.QLineEdit(parent=self.centralwidget)
        self.edNickname.setGeometry(QtCore.QRect(10, 30, 113, 20))
        self.edNickname.setObjectName("edNickname")
        self.verticalLayoutWidget = QtWidgets.QWidget(parent=self.centralwidget)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(660, 350, 111, 41))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.rbReqGenres = QtWidgets.QRadioButton(parent=self.verticalLayoutWidget)
        self.rbReqGenres.setChecked(True)
        self.rbReqGenres.setObjectName("rbReqGenres")
        self.verticalLayout.addWidget(self.rbReqGenres)
        self.rbIncludedGenres = QtWidgets.QRadioButton(parent=self.verticalLayoutWidget)
        self.rbIncludedGenres.setChecked(False)
        self.rbIncludedGenres.setObjectName("rbIncludedGenres")
        self.verticalLayout.addWidget(self.rbIncludedGenres)
        self.verticalLayoutWidget_2 = QtWidgets.QWidget(parent=self.centralwidget)
        self.verticalLayoutWidget_2.setGeometry(QtCore.QRect(10, 180, 81, 41))
        self.verticalLayoutWidget_2.setObjectName("verticalLayoutWidget_2")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_2)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.label_3 = QtWidgets.QLabel(parent=self.verticalLayoutWidget_2)
        self.label_3.setObjectName("label_3")
        self.verticalLayout_2.addWidget(self.label_3)
        self.edGettingNum = QtWidgets.QLineEdit(parent=self.verticalLayoutWidget_2)
        self.edGettingNum.setObjectName("edGettingNum")
        self.verticalLayout_2.addWidget(self.edGettingNum)
        self.verticalLayoutWidget_3 = QtWidgets.QWidget(parent=self.centralwidget)
        self.verticalLayoutWidget_3.setGeometry(QtCore.QRect(10, 230, 81, 41))
        self.verticalLayoutWidget_3.setObjectName("verticalLayoutWidget_3")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_3)
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.label_4 = QtWidgets.QLabel(parent=self.verticalLayoutWidget_3)
        self.label_4.setObjectName("label_4")
        self.verticalLayout_3.addWidget(self.label_4)
        self.edTotalNum = QtWidgets.QLineEdit(parent=self.verticalLayoutWidget_3)
        self.edTotalNum.setObjectName("edTotalNum")
        self.verticalLayout_3.addWidget(self.edTotalNum)
        self.verticalLayoutWidget_4 = QtWidgets.QWidget(parent=self.centralwidget)
        self.verticalLayoutWidget_4.setGeometry(QtCore.QRect(550, 0, 61, 92))
        self.verticalLayoutWidget_4.setObjectName("verticalLayoutWidget_4")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_4)
        self.verticalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.cbONA = QtWidgets.QCheckBox(parent=self.verticalLayoutWidget_4)
        self.cbONA.setChecked(True)
        self.cbONA.setObjectName("cbONA")
        self.verticalLayout_4.addWidget(self.cbONA)
        self.cbOVA = QtWidgets.QCheckBox(parent=self.verticalLayoutWidget_4)
        self.cbOVA.setObjectName("cbOVA")
        self.verticalLayout_4.addWidget(self.cbOVA)
        self.cbMovie = QtWidgets.QCheckBox(parent=self.verticalLayoutWidget_4)
        self.cbMovie.setChecked(True)
        self.cbMovie.setObjectName("cbMovie")
        self.verticalLayout_4.addWidget(self.cbMovie)
        self.cbSpecials = QtWidgets.QCheckBox(parent=self.verticalLayoutWidget_4)
        self.cbSpecials.setObjectName("cbSpecials")
        self.verticalLayout_4.addWidget(self.cbSpecials)
        self.verticalLayoutWidget_5 = QtWidgets.QWidget(parent=self.centralwidget)
        self.verticalLayoutWidget_5.setGeometry(QtCore.QRect(10, 330, 119, 92))
        self.verticalLayoutWidget_5.setObjectName("verticalLayoutWidget_5")
        self.verticalLayout_5 = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_5)
        self.verticalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.cbScrRound = QtWidgets.QCheckBox(parent=self.verticalLayoutWidget_5)
        self.cbScrRound.setChecked(True)
        self.cbScrRound.setObjectName("cbScrRound")
        self.verticalLayout_5.addWidget(self.cbScrRound)
        self.cbOPRound = QtWidgets.QCheckBox(parent=self.verticalLayoutWidget_5)
        self.cbOPRound.setChecked(True)
        self.cbOPRound.setObjectName("cbOPRound")
        self.verticalLayout_5.addWidget(self.cbOPRound)
        self.cbDescRound = QtWidgets.QCheckBox(parent=self.verticalLayoutWidget_5)
        self.cbDescRound.setChecked(False)
        self.cbDescRound.setObjectName("cbDescRound")
        self.verticalLayout_5.addWidget(self.cbDescRound)
        self.cbChatGPTRound = QtWidgets.QCheckBox(parent=self.verticalLayoutWidget_5)
        self.cbChatGPTRound.setObjectName("cbChatGPTRound")
        self.verticalLayout_5.addWidget(self.cbChatGPTRound)
        self.cbDownloadToHost = QtWidgets.QCheckBox(parent=self.centralwidget)
        self.cbDownloadToHost.setGeometry(QtCore.QRect(620, 480, 171, 18))
        self.cbDownloadToHost.setObjectName("cbDownloadToHost")
        self.verticalLayoutWidget_6 = QtWidgets.QWidget(parent=self.centralwidget)
        self.verticalLayoutWidget_6.setGeometry(QtCore.QRect(10, 280, 89, 41))
        self.verticalLayoutWidget_6.setObjectName("verticalLayoutWidget_6")
        self.verticalLayout_6 = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_6)
        self.verticalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.label_5 = QtWidgets.QLabel(parent=self.verticalLayoutWidget_6)
        self.label_5.setObjectName("label_5")
        self.verticalLayout_6.addWidget(self.label_5)
        self.edOPDuration = QtWidgets.QLineEdit(parent=self.verticalLayoutWidget_6)
        self.edOPDuration.setObjectName("edOPDuration")
        self.verticalLayout_6.addWidget(self.edOPDuration)
        self.verticalLayoutWidget_7 = QtWidgets.QWidget(parent=self.centralwidget)
        self.verticalLayoutWidget_7.setGeometry(QtCore.QRect(10, 70, 191, 91))
        self.verticalLayoutWidget_7.setObjectName("verticalLayoutWidget_7")
        self.verticalLayout_7 = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_7)
        self.verticalLayout_7.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_7.setObjectName("verticalLayout_7")
        self.cbRemoveDuplicates = QtWidgets.QCheckBox(parent=self.verticalLayoutWidget_7)
        self.cbRemoveDuplicates.setChecked(True)
        self.cbRemoveDuplicates.setObjectName("cbRemoveDuplicates")
        self.verticalLayout_7.addWidget(self.cbRemoveDuplicates)
        self.cbShuffleLines = QtWidgets.QCheckBox(parent=self.verticalLayoutWidget_7)
        self.cbShuffleLines.setObjectName("cbShuffleLines")
        self.verticalLayout_7.addWidget(self.cbShuffleLines)
        self.cbShuffleQuestions = QtWidgets.QCheckBox(parent=self.verticalLayoutWidget_7)
        self.cbShuffleQuestions.setObjectName("cbShuffleQuestions")
        self.verticalLayout_7.addWidget(self.cbShuffleQuestions)
        self.cbLimitToOne = QtWidgets.QCheckBox(parent=self.verticalLayoutWidget_7)
        self.cbLimitToOne.setObjectName("cbLimitToOne")
        self.verticalLayout_7.addWidget(self.cbLimitToOne)
        self.cbUseMoreScr = QtWidgets.QCheckBox(parent=self.verticalLayoutWidget_7)
        self.cbUseMoreScr.setObjectName("cbUseMoreScr")
        self.verticalLayout_7.addWidget(self.cbUseMoreScr)
        self.cbHostingStatus = QtWidgets.QLabel(parent=self.centralwidget)
        self.cbHostingStatus.setGeometry(QtCore.QRect(700, 450, 81, 16))
        self.cbHostingStatus.setObjectName("cbHostingStatus")
        self.checkBox_15 = QtWidgets.QCheckBox(parent=self.centralwidget)
        self.checkBox_15.setGeometry(QtCore.QRect(780, 450, 16, 18))
        self.checkBox_15.setText("")
        self.checkBox_15.setObjectName("checkBox_15")
        self.listGenres = QtWidgets.QListWidget(parent=self.centralwidget)
        self.listGenres.setGeometry(QtCore.QRect(620, 0, 181, 341))
        self.listGenres.setSelectionMode(QtWidgets.QAbstractItemView.SelectionMode.MultiSelection)
        self.listGenres.setObjectName("listGenres")
        self.lbl_slider_value = QtWidgets.QLabel(parent=self.centralwidget)
        self.lbl_slider_value.setGeometry(QtCore.QRect(230, 500, 47, 14))
        self.lbl_slider_value.setObjectName("lbl_slider_value")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(parent=MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 801, 22))
        self.menubar.setObjectName("menubar")
        self.menuFile = QtWidgets.QMenu(parent=self.menubar)
        self.menuFile.setObjectName("menuFile")
        self.menuAbout = QtWidgets.QMenu(parent=self.menubar)
        self.menuAbout.setObjectName("menuAbout")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(parent=MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.actionSettings = QtGui.QAction(parent=MainWindow)
        self.actionSettings.setObjectName("actionSettings")
        self.menuFile.addAction(self.actionSettings)
        self.menubar.addAction(self.menuFile.menuAction())
        self.menubar.addAction(self.menuAbout.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.btnGenerate.setText(_translate("MainWindow", "Generate!"))
        self.label.setText(_translate("MainWindow", "DownloadingThreads :"))
        self.label_2.setText(_translate("MainWindow", "Nickname:"))
        self.edNickname.setText(_translate("MainWindow", "lonsdale228"))
        self.rbReqGenres.setText(_translate("MainWindow", "Required Genres"))
        self.rbIncludedGenres.setText(_translate("MainWindow", "Included genres"))
        self.label_3.setText(_translate("MainWindow", "Num of getting:"))
        self.edGettingNum.setText(_translate("MainWindow", "150"))
        self.label_4.setText(_translate("MainWindow", "Num of total:"))
        self.edTotalNum.setText(_translate("MainWindow", "50"))
        self.cbONA.setText(_translate("MainWindow", "ONA"))
        self.cbOVA.setText(_translate("MainWindow", "OVA"))
        self.cbMovie.setText(_translate("MainWindow", "Movie"))
        self.cbSpecials.setText(_translate("MainWindow", "Special"))
        self.cbScrRound.setText(_translate("MainWindow", "Screenshots round"))
        self.cbOPRound.setText(_translate("MainWindow", "OP round"))
        self.cbDescRound.setText(_translate("MainWindow", "Description round"))
        self.cbChatGPTRound.setText(_translate("MainWindow", "ChatGPT Questions"))
        self.cbDownloadToHost.setText(_translate("MainWindow", "Download to custom hosting"))
        self.label_5.setText(_translate("MainWindow", "OP Duration(sec):"))
        self.edOPDuration.setText(_translate("MainWindow", "30"))
        self.cbRemoveDuplicates.setText(_translate("MainWindow", "Remove Duplicates"))
        self.cbShuffleLines.setText(_translate("MainWindow", "Shuffle lines between rounds"))
        self.cbShuffleQuestions.setText(_translate("MainWindow", "Shuffle questions between lines"))
        self.cbLimitToOne.setText(_translate("MainWindow", "Limit each theme to one round"))
        self.cbUseMoreScr.setText(_translate("MainWindow", "Use more screenshots (slower)"))
        self.cbHostingStatus.setText(_translate("MainWindow", "Hosting status:"))
        self.lbl_slider_value.setText(_translate("MainWindow", "TextLabel"))
        self.menuFile.setTitle(_translate("MainWindow", "File"))
        self.menuAbout.setTitle(_translate("MainWindow", "About"))
        self.actionSettings.setText(_translate("MainWindow", "Settings"))
