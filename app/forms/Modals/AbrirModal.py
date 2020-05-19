from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets  import QGraphicsDropShadowEffect
from resources.resources import *
from classes.Modal import Modal

class UIAbrir(Modal):
    
    def __init__(self,MainWindow):
        super(UIAbrir,self).__init__(MainWindow)
        self.setupUI()

    def setupUI(self):
        Login = self
        Login.setObjectName("Login")
        Login.setWindowModality(QtCore.Qt.WindowModal)
        Login.resize(480, 640)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(Login.sizePolicy().hasHeightForWidth())
        Login.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Noto Serif")
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        Login.setFont(font)
        Login.setContextMenuPolicy(QtCore.Qt.NoContextMenu)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("../../../../../.designer/if_16_1751363.ico"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        Login.setWindowIcon(icon)
        Login.setStyleSheet("background-color: rgb(255, 255, 255);")
        Login.setInputMethodHints(QtCore.Qt.ImhSensitiveData)
        self.MainFrame = QtWidgets.QFrame(Login)
        self.MainFrame.setGeometry(QtCore.QRect(10, 10, 461, 621))
        self.MainFrame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.MainFrame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.MainFrame.setObjectName("MainFrame")
        self.shadow = QGraphicsDropShadowEffect()
        self.shadow.setBlurRadius(4)
        self.shadow.setOffset(2)
        self.MainFrame.setGraphicsEffect(self.shadow)
        self.label_3 = QtWidgets.QLabel(self.MainFrame)
        self.label_3.setGeometry(QtCore.QRect(360, 20, 71, 71))
        self.label_3.setStyleSheet("background-color: rgb(65, 105, 225);")
        self.label_3.setText("")
        self.label_3.setPixmap(QtGui.QPixmap(":/source/img/iiie.png"))
        self.label_3.setObjectName("label_3")
        self.label = QtWidgets.QLabel(self.MainFrame)
        self.label.setGeometry(QtCore.QRect(10, 5, 81, 101))
        self.label.setStyleSheet("background-color: rgb(65, 105, 225);")
        self.label.setText("")
        self.label.setPixmap(QtGui.QPixmap(":/source/img/logo.png"))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.MainFrame)
        self.label_2.setGeometry(QtCore.QRect(90, 40, 111, 31))
        font = QtGui.QFont()
        font.setPointSize(21)
        font.setBold(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setAutoFillBackground(False)
        self.label_2.setStyleSheet("color: rgb(255, 255, 0);background-color: rgb(65, 105, 225);")
        self.label_2.setObjectName("label_2")
        self.btnExit = QtWidgets.QPushButton(self.MainFrame)
        self.btnExit.setGeometry(QtCore.QRect(435, 2, 24, 24))
        self.btnExit.setText("")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(":/source/img/Cancelar.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btnExit.setIcon(icon1)
        self.btnExit.setIconSize(QtCore.QSize(24, 24))
        self.btnExit.setFlat(True)
        self.btnExit.setObjectName("btnExit")
        self.graphicsView = QtWidgets.QGraphicsView(self.MainFrame)
        self.graphicsView.setGeometry(QtCore.QRect(0, 0, 461, 116))
        self.graphicsView.setAutoFillBackground(True)
        self.graphicsView.setStyleSheet("background-color: rgb(65, 105, 225);")
        self.graphicsView.setObjectName("graphicsView")
        self.graphicsView.raise_()
        self.label.raise_()
        self.label_2.raise_()
        self.label_3.raise_()
        self.btnExit.raise_()

        self.retranslateUi(Login)
        QtCore.QMetaObject.connectSlotsByName(Login)

        #Listener
        self.btnExit.clicked.connect(self.exit)

    def retranslateUi(self, Login):
        _translate = QtCore.QCoreApplication.translate
        Login.setWindowTitle(_translate("Login", "Sistema SCADA"))
        self.label_2.setText(_translate("Login", "SCADA"))
