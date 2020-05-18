from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMainWindow, QAction, QMenu
from PyQt5.QtCore import Qt
from resources.resources import *

class UIMainWindow(object):

    def setupUi(self,MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(820, 720)
        MainWindow.setMinimumSize(QtCore.QSize(820, 680))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/source/img/if_16_1751363.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        MainWindow.setWindowIcon(icon)
        MainWindow.setDockOptions(QtWidgets.QMainWindow.AllowTabbedDocks|QtWidgets.QMainWindow.AnimatedDocks)
        self.MainFrame = QtWidgets.QWidget(MainWindow)
        self.MainFrame.setStyleSheet("")
        self.MainFrame.setObjectName("MainFrame")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.MainFrame)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.frame = QtWidgets.QFrame(self.MainFrame)
        self.frame.setStyleSheet("background-color: rgb(255, 255, 255);\n"
        "")
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.frame)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setSpacing(0)
        self.gridLayout.setObjectName("gridLayout")
        self.label_5 = QtWidgets.QLabel(self.frame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_5.sizePolicy().hasHeightForWidth())
        self.label_5.setSizePolicy(sizePolicy)
        self.label_5.setMinimumSize(QtCore.QSize(0, 0))
        font = QtGui.QFont()
        font.setPointSize(21)
        font.setBold(True)
        font.setWeight(75)
        self.label_5.setFont(font)
        self.label_5.setAutoFillBackground(False)
        self.label_5.setStyleSheet("color: rgb(255, 255, 0);background-color: rgb(65, 105, 225);\n"
        "margin:0px;")
        self.label_5.setObjectName("label_5")
        self.gridLayout.addWidget(self.label_5, 0, 1, 1, 1)
        self.frame_2 = QtWidgets.QFrame(self.frame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame_2.sizePolicy().hasHeightForWidth())
        self.frame_2.setSizePolicy(sizePolicy)
        self.frame_2.setMinimumSize(QtCore.QSize(0, 81))
        self.frame_2.setStyleSheet("color: rgb(255, 255, 0);background-color: rgb(65, 105, 225);\n"
        "margin:0px;")
        self.frame_2.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.frame_2.setLineWidth(0)
        self.frame_2.setObjectName("frame_2")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.frame_2)
        self.verticalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_4.setSpacing(0)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.label = QtWidgets.QLabel(self.frame_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy)
        self.label.setStyleSheet("background-color: rgb(65, 105, 225);\n"
        "margin:0px;")
        self.label.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.label.setText("")
        self.label.setPixmap(QtGui.QPixmap(":/source/img/logo.png"))
        self.label.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label.setObjectName("label")
        self.verticalLayout_4.addWidget(self.label)
        self.gridLayout.addWidget(self.frame_2, 0, 2, 1, 1)
        self.label_3 = QtWidgets.QLabel(self.frame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_3.sizePolicy().hasHeightForWidth())
        self.label_3.setSizePolicy(sizePolicy)
        self.label_3.setStyleSheet("background-color: rgb(65, 105, 225);\n"
        "margin:0px;")
        self.label_3.setText("")
        self.label_3.setPixmap(QtGui.QPixmap(":/source/img/iiie.png"))
        self.label_3.setObjectName("label_3")
        self.gridLayout.addWidget(self.label_3, 0, 0, 1, 1)
        self.verticalLayout_2.addLayout(self.gridLayout)
        self.verticalLayout_3 = QtWidgets.QVBoxLayout()
        self.verticalLayout_3.setSpacing(0)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.frame_3 = QtWidgets.QFrame(self.frame)
        self.frame_3.setMinimumSize(QtCore.QSize(0, 24))
        self.frame_3.setStyleSheet("margin:0px;")
        self.frame_3.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.frame_3.setFrameShadow(QtWidgets.QFrame.Plain)
        self.frame_3.setLineWidth(0)
        self.frame_3.setObjectName("frame_3")
        self.MenuArchivo = QtWidgets.QToolButton(self.frame_3)
        self.MenuArchivo.setGeometry(QtCore.QRect(0, 0, 71, 24))
        self.MenuArchivo.setStyleSheet("margin:0px;")
        self.MenuArchivo.setPopupMode(QtWidgets.QToolButton.MenuButtonPopup)
        self.MenuArchivo.setToolButtonStyle(QtCore.Qt.ToolButtonTextBesideIcon)
        self.MenuArchivo.setAutoRaise(True)
        self.MenuArchivo.setArrowType(QtCore.Qt.NoArrow)
        self.MenuArchivo.setObjectName("MenuArchivo")
        self.MenuConfiguraciones = QtWidgets.QToolButton(self.frame_3)
        self.MenuConfiguraciones.setGeometry(QtCore.QRect(70, 0, 121, 24))
        self.MenuConfiguraciones.setStyleSheet("margin:0px;")
        self.MenuConfiguraciones.setPopupMode(QtWidgets.QToolButton.MenuButtonPopup)
        self.MenuConfiguraciones.setToolButtonStyle(QtCore.Qt.ToolButtonTextBesideIcon)
        self.MenuConfiguraciones.setAutoRaise(True)
        self.MenuConfiguraciones.setArrowType(QtCore.Qt.NoArrow)
        self.MenuConfiguraciones.setObjectName("MenuConfiguraciones")
        self.MenuReportes = QtWidgets.QToolButton(self.frame_3)
        self.MenuReportes.setGeometry(QtCore.QRect(190, 0, 91, 24))
        self.MenuReportes.setStyleSheet("margin:0px;")
        self.MenuReportes.setPopupMode(QtWidgets.QToolButton.MenuButtonPopup)
        self.MenuReportes.setToolButtonStyle(QtCore.Qt.ToolButtonTextBesideIcon)
        self.MenuReportes.setAutoRaise(True)
        self.MenuReportes.setArrowType(QtCore.Qt.NoArrow)
        self.MenuReportes.setObjectName("MenuReportes")
        self.verticalLayout_3.addWidget(self.frame_3)
        self.tabWidget = QtWidgets.QTabWidget(self.frame)
        self.tabWidget.setObjectName("tabWidget")
        self.tab = QtWidgets.QWidget()
        self.tab.setObjectName("tab")
        self.btnMax_2 = QtWidgets.QPushButton(self.tab)
        self.btnMax_2.setGeometry(QtCore.QRect(500, 120, 26, 18))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btnMax_2.sizePolicy().hasHeightForWidth())
        self.btnMax_2.setSizePolicy(sizePolicy)
        self.btnMax_2.setMinimumSize(QtCore.QSize(24, 12))
        self.btnMax_2.setMaximumSize(QtCore.QSize(64, 32))
        self.btnMax_2.setAutoFillBackground(False)
        self.btnMax_2.setStyleSheet("background-color: rgb(65, 105, 225);\n"
        "margin:0px;")
        self.btnMax_2.setText("")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(":/source/img/max.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btnMax_2.setIcon(icon1)
        self.btnMax_2.setIconSize(QtCore.QSize(16, 16))
        self.btnMax_2.setFlat(True)
        self.btnMax_2.setObjectName("btnMax_2")
        self.tabWidget.addTab(self.tab, "")
        self.tab_2 = QtWidgets.QWidget()
        self.tab_2.setObjectName("tab_2")
        self.tabWidget.addTab(self.tab_2, "")
        self.verticalLayout_3.addWidget(self.tabWidget)
        self.verticalLayout_2.addLayout(self.verticalLayout_3)
        self.frame_4 = QtWidgets.QFrame(self.frame)
        self.frame_4.setMinimumSize(QtCore.QSize(0, 24))
        self.frame_4.setStyleSheet("margin:0px;")
        self.frame_4.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.frame_4.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_4.setLineWidth(0)
        self.frame_4.setObjectName("frame_4")
        self.label_2 = QtWidgets.QLabel(self.frame_4)
        self.label_2.setGeometry(QtCore.QRect(5, 2, 54, 20))
        font = QtGui.QFont()
        font.setFamily("Roboto")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setLineWidth(0)
        self.label_2.setScaledContents(False)
        self.label_2.setObjectName("label_2")
        self.label_4 = QtWidgets.QLabel(self.frame_4)
        self.label_4.setGeometry(QtCore.QRect(50, 2, 54, 20))
        font = QtGui.QFont()
        font.setFamily("Roboto")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_4.setFont(font)
        self.label_4.setStyleSheet("color: rgb(0, 170, 127);")
        self.label_4.setLineWidth(0)
        self.label_4.setScaledContents(False)
        self.label_4.setAlignment(QtCore.Qt.AlignCenter)
        self.label_4.setObjectName("label_4")
        self.verticalLayout_2.addWidget(self.frame_4)
        self.verticalLayout.addWidget(self.frame)
        MainWindow.setCentralWidget(self.MainFrame)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        QMainWindow.setWindowFlags(MainWindow,Qt.WindowFlags() & ~Qt.FramelessWindowHint )
        QMainWindow.show(MainWindow)

        # Definicion de menus
        self.defineMenuArchivo()
        self.defineMenuConfiguraciones()
        self.defineMenuReportes()

        #action.setshorcut(Qkeysequence(Qt.Key_Ctrl + Qt.Key_A))
        #connect(nuevo,nuevo.triggered,nuevo_callback)

    def defineMenuArchivo(self):
        archivoMenu = QMenu()
        archivoMenu.addAction("{:13s} {:6s}".format("Nuevo","Ctrl+N"),self.new_Callback)
        archivoMenu.addAction("{:13s} {:6s}".format("Abrir","Ctrl+A"),self.open_Callback)
        archivoMenu.addAction("{:13s} {:6s}".format("Guardar","Ctrl+S"),self.save_Callback)
        archivoMenu.addAction("{:13s} {:6s}".format("Guardar Como","Ctrl+G"),self.saveAs_Callback)
        archivoMenu.addAction("{:13s} {:6s}".format("Cerrar","Ctrl+E"),self.close_Callback)
        archivoMenu.addAction("{:13s} {:6s}".format("Eliminar","Ctrl+Supr"), self.delete_Callback)
        archivoMenu.addAction("{:13s} {:6s}".format("Cerrar Sesiòn","Ctrl+X"),self.logout_CallbacK)
        archivoMenu.addAction("{:13s} {:6s}".format("Sair","Alt+f4"),self.exit_Callback)

        self.MenuArchivo.setMenu(archivoMenu)
        #self.MenuArchivo.setDefaultAction(QAction("Abrir",self))
        self.MenuArchivo.triggered.connect(self.archivoMenu_Default)

    def defineMenuConfiguraciones(self):
        configuracionesMenu = QMenu()
        configuracionesMenu.addAction("{:15s} {:6s}".format("Configuraciones","Ctrl+C"),self.settings_Callback)
        configuracionesMenu.addAction("{:15s} {:6s}".format("Dispostivos","Ctrl+D"),self.devices_Callback)
        configuracionesMenu.addAction("{:15s} {:6s}".format("API Local","Ctrl+H"),self.api_Callback)
        configuracionesMenu.addAction("{:15s} {:6s}".format("Usuarios","Ctrl+U"),self.users_Callback)
        configuracionesMenu.addAction("{:15s} {:6s}".format("Cuenta","Ctrl+P"),self.account_Callback)
        configuracionesMenu.addAction("{:15s} {:6s}".format("Acerca de",""), self.about_Callback)

        self.MenuConfiguraciones.setMenu(configuracionesMenu)
        #self.MenuArchivo.setDefaultAction(QAction("Abrir",self))
        self.MenuConfiguraciones.triggered.connect(self.configuracionesMenu_Default)

    def defineMenuReportes(self):
        ReportesMenu = QMenu()
        ReportesMenu.addAction("{:15s} {:6s}".format("Reportes","Ctrl+R"),self.settings_Callback)
        self.MenuReportes.setMenu(ReportesMenu)
        #self.MenuArchivo.setDefaultAction(QAction("Abrir",self))
        self.MenuReportes.triggered.connect(self.reports_Callback)

    # methods of reports:menu
    def reports_Callback(self):
            pass

    # methods of settings:menu
    def configuracionesMenu_Default(self):
            pass
    def settings_Callback(self):
            pass
    def devices_Callback(self):
            pass
    def api_Callback(self):
            pass
    def users_Callback(self):
            pass
    def account_Callback(self):
            pass
    def about_Callback(self):
            pass

    # methods of archive:menu
    def archivoMenu_Default(self):
            print("Default")
    def new_Callback(self):
            print("nuevo clicked")
    def open_Callback(self):
            pass
    def save_Callback(self):
            pass
    def saveAs_Callback(self):
            pass
    def close_Callback(self):
            pass
    def delete_Callback(self):
            pass
    def logout_CallbacK(self):
            pass
    def exit_Callback(self):
            pass

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Software SCADA"))
        self.label_5.setText(_translate("MainWindow", "SCADA"))
        self.MenuArchivo.setText(_translate("MainWindow", "Archivo"))
        self.MenuConfiguraciones.setText(_translate("MainWindow", "Configuraciones"))
        self.MenuReportes.setText(_translate("MainWindow", "Reportes"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _translate("MainWindow", "Tab 1"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), _translate("MainWindow", "Tab 2"))
        self.label_2.setText(_translate("MainWindow", "Estado:"))
        self.label_4.setText(_translate("MainWindow", "En linea"))