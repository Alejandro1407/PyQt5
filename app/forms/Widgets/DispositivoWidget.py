from PyQt5 import QtCore, QtGui, QtWidgets
from classes import widget,device,deviceSignals, Logica
from PyQt5.QtWidgets import QMessageBox

class UIDispositivoModalWidget(widget):

    def __init__(self, device:device):
        self.dispositivo = device
        super(UIDispositivoModalWidget,self).__init__()
        self.deviceSignals = deviceSignals()
        self.setupUi()

    def setupUi(self):
        DispositivoWidget = self
        DispositivoWidget.setObjectName("DispositivoWidget")
        DispositivoWidget.setWindowModality(QtCore.Qt.WindowModal)
        DispositivoWidget.resize(612, 186)
        DispositivoWidget.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.ProjectFrame = QtWidgets.QFrame(DispositivoWidget)
        self.ProjectFrame.setGeometry(QtCore.QRect(0, 0, 612, 182))
        self.ProjectFrame.setMinimumSize(QtCore.QSize(350, 182))
        self.ProjectFrame.setMaximumSize(QtCore.QSize(16777215, 200))
        self.ProjectFrame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.ProjectFrame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.ProjectFrame.setObjectName("ProjectFrame")
        self.lblImagen = QtWidgets.QLabel(self.ProjectFrame)
        self.lblImagen.setGeometry(QtCore.QRect(10, 15, 171, 151))
        self.lblImagen.setText("")
        self.lblImagen.setPixmap(QtGui.QPixmap(":/source/img/NoImage.png"))
        self.lblImagen.setScaledContents(True)
        self.lblImagen.setObjectName("lblImagen")
        self.InfoFrame = QtWidgets.QFrame(self.ProjectFrame)
        self.InfoFrame.setGeometry(QtCore.QRect(180, 10, 325, 165))
        self.InfoFrame.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.InfoFrame.setFrameShadow(QtWidgets.QFrame.Plain)
        self.InfoFrame.setLineWidth(0)
        self.InfoFrame.setObjectName("InfoFrame")
        self.lblNombre = QtWidgets.QLabel(self.InfoFrame)
        self.lblNombre.setGeometry(QtCore.QRect(5, 10, 85, 24))
        font = QtGui.QFont()
        font.setFamily("Roboto")
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.lblNombre.setFont(font)
        self.lblNombre.setLineWidth(0)
        self.lblNombre.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.lblNombre.setObjectName("lblNombre")
        self.lblID = QtWidgets.QLabel(self.InfoFrame)
        self.lblID.setGeometry(QtCore.QRect(5, 40, 85, 24))
        font = QtGui.QFont()
        font.setFamily("Roboto")
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.lblID.setFont(font)
        self.lblID.setLineWidth(0)
        self.lblID.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.lblID.setObjectName("lblID")
        self.lblToken = QtWidgets.QLabel(self.InfoFrame)
        self.lblToken.setGeometry(QtCore.QRect(5, 75, 85, 24))
        font = QtGui.QFont()
        font.setFamily("Roboto")
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.lblToken.setFont(font)
        self.lblToken.setLineWidth(0)
        self.lblToken.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.lblToken.setObjectName("lblToken")
        self.lblTiempo = QtWidgets.QLabel(self.InfoFrame)
        self.lblTiempo.setGeometry(QtCore.QRect(5, 115, 85, 24))
        font = QtGui.QFont()
        font.setFamily("Roboto")
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.lblTiempo.setFont(font)
        self.lblTiempo.setLineWidth(0)
        self.lblTiempo.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.lblTiempo.setObjectName("lblTiempo")
        self.lblVariables = QtWidgets.QLabel(self.InfoFrame)
        self.lblVariables.setGeometry(QtCore.QRect(5, 140, 85, 24))
        font = QtGui.QFont()
        font.setFamily("Roboto")
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.lblVariables.setFont(font)
        self.lblVariables.setLineWidth(0)
        self.lblVariables.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.lblVariables.setObjectName("lblVariables")
        self.ScrollNombre = QtWidgets.QScrollArea(self.InfoFrame)
        self.ScrollNombre.setGeometry(QtCore.QRect(100, 10, 200, 22))
        self.ScrollNombre.setMinimumSize(QtCore.QSize(110, 20))
        self.ScrollNombre.setMaximumSize(QtCore.QSize(200, 25))
        self.ScrollNombre.setFrameShape(QtWidgets.QFrame.Panel)
        self.ScrollNombre.setFrameShadow(QtWidgets.QFrame.Plain)
        self.ScrollNombre.setLineWidth(0)
        self.ScrollNombre.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAsNeeded)
        self.ScrollNombre.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.ScrollNombre.setWidgetResizable(True)
        self.ScrollNombre.setObjectName("ScrollNombre")
        self.NombreScrollLayout = QtWidgets.QWidget()
        self.NombreScrollLayout.setGeometry(QtCore.QRect(0, 0, 186, 36))
        self.NombreScrollLayout.setObjectName("NombreScrollLayout")
        self.vboxlayout = QtWidgets.QVBoxLayout(self.NombreScrollLayout)
        self.vboxlayout.setContentsMargins(0, 0, 0, 0)
        self.vboxlayout.setSpacing(0)
        self.vboxlayout.setObjectName("vboxlayout")
        self.txtNombre = QtWidgets.QLabel(self.NombreScrollLayout)
        self.txtNombre.setMaximumSize(QtCore.QSize(16666672, 16666672))
        font = QtGui.QFont()
        font.setFamily("Roboto")
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.txtNombre.setFont(font)
        self.txtNombre.setLineWidth(0)
        self.txtNombre.setTextFormat(QtCore.Qt.PlainText)
        self.txtNombre.setScaledContents(True)
        self.txtNombre.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.txtNombre.setWordWrap(True)
        self.txtNombre.setIndent(5)
        self.txtNombre.setObjectName("txtNombre")
        self.vboxlayout.addWidget(self.txtNombre)
        self.ScrollNombre.setWidget(self.NombreScrollLayout)
        self.ScrollID = QtWidgets.QScrollArea(self.InfoFrame)
        self.ScrollID.setGeometry(QtCore.QRect(100, 43, 210, 24))
        self.ScrollID.setMinimumSize(QtCore.QSize(110, 20))
        self.ScrollID.setMaximumSize(QtCore.QSize(215, 100))
        self.ScrollID.setFrameShape(QtWidgets.QFrame.Panel)
        self.ScrollID.setFrameShadow(QtWidgets.QFrame.Plain)
        self.ScrollID.setLineWidth(0)
        self.ScrollID.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.ScrollID.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAsNeeded)
        self.ScrollID.setSizeAdjustPolicy(QtWidgets.QAbstractScrollArea.AdjustIgnored)
        self.ScrollID.setWidgetResizable(False)
        self.ScrollID.setObjectName("ScrollID")
        self.IDScrollLayout = QtWidgets.QWidget()
        self.IDScrollLayout.setGeometry(QtCore.QRect(0, 0, 207, 18))
        self.IDScrollLayout.setObjectName("IDScrollLayout")
        self._2 = QtWidgets.QVBoxLayout(self.IDScrollLayout)
        self._2.setContentsMargins(0, 0, 0, 0)
        self._2.setSpacing(0)
        self._2.setObjectName("_2")
        self.txtID = QtWidgets.QLabel(self.IDScrollLayout)
        self.txtID.setMaximumSize(QtCore.QSize(16666672, 16666672))
        font = QtGui.QFont()
        font.setFamily("Roboto")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        font.setKerning(True)
        self.txtID.setFont(font)
        self.txtID.setLineWidth(0)
        self.txtID.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.txtID.setWordWrap(True)
        self.txtID.setIndent(-8)
        self.txtID.setObjectName("txtID")
        self._2.addWidget(self.txtID)
        self.ScrollID.setWidget(self.IDScrollLayout)
        self.ScrollToken = QtWidgets.QScrollArea(self.InfoFrame)
        self.ScrollToken.setGeometry(QtCore.QRect(100, 80, 190, 32))
        self.ScrollToken.setMinimumSize(QtCore.QSize(110, 20))
        self.ScrollToken.setMaximumSize(QtCore.QSize(225, 100))
        self.ScrollToken.setFrameShape(QtWidgets.QFrame.Panel)
        self.ScrollToken.setFrameShadow(QtWidgets.QFrame.Plain)
        self.ScrollToken.setLineWidth(0)
        self.ScrollToken.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.ScrollToken.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAsNeeded)
        self.ScrollToken.setSizeAdjustPolicy(QtWidgets.QAbstractScrollArea.AdjustToContents)
        self.ScrollToken.setWidgetResizable(False)
        self.ScrollToken.setObjectName("ScrollToken")
        self.TokencrollLayout = QtWidgets.QWidget()
        self.TokencrollLayout.setGeometry(QtCore.QRect(0, 0, 280, 18))
        self.TokencrollLayout.setObjectName("TokencrollLayout")
        self._3 = QtWidgets.QVBoxLayout(self.TokencrollLayout)
        self._3.setContentsMargins(0, 0, 0, 0)
        self._3.setSpacing(0)
        self._3.setObjectName("_3")
        self.txtToken = QtWidgets.QLabel(self.TokencrollLayout)
        self.txtToken.setMaximumSize(QtCore.QSize(16666672, 16666672))
        font = QtGui.QFont()
        font.setFamily("Roboto")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.txtToken.setFont(font)
        self.txtToken.setLineWidth(0)
        self.txtToken.setTextFormat(QtCore.Qt.RichText)
        self.txtToken.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.txtToken.setWordWrap(True)
        self.txtToken.setIndent(-8)
        self.txtToken.setObjectName("txtToken")
        self._3.addWidget(self.txtToken)
        self.ScrollToken.setWidget(self.TokencrollLayout)
        self.txtTiempo = QtWidgets.QLabel(self.InfoFrame)
        self.txtTiempo.setGeometry(QtCore.QRect(100, 115, 150, 24))
        font = QtGui.QFont()
        font.setFamily("Roboto")
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.txtTiempo.setFont(font)
        self.txtTiempo.setObjectName("txtTiempo")
        self.txtVariables = QtWidgets.QLabel(self.InfoFrame)
        self.txtVariables.setGeometry(QtCore.QRect(100, 140, 150, 24))
        font = QtGui.QFont()
        font.setFamily("Roboto")
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.txtVariables.setFont(font)
        self.txtVariables.setObjectName("txtVariables")
        self.utilsFrame = QtWidgets.QFrame(self.ProjectFrame)
        self.utilsFrame.setGeometry(QtCore.QRect(510, 10, 91, 165))
        self.utilsFrame.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.utilsFrame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.utilsFrame.setLineWidth(0)
        self.utilsFrame.setObjectName("utilsFrame")
        self.btnEditar = QtWidgets.QPushButton(self.utilsFrame)
        self.btnEditar.setGeometry(QtCore.QRect(10, 70, 38, 38))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btnEditar.sizePolicy().hasHeightForWidth())
        self.btnEditar.setSizePolicy(sizePolicy)
        self.btnEditar.setMinimumSize(QtCore.QSize(0, 0))
        self.btnEditar.setMaximumSize(QtCore.QSize(128, 48))
        font = QtGui.QFont()
        font.setFamily("Roboto")
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.btnEditar.setFont(font)
        self.btnEditar.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/source/img/Editar.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btnEditar.setIcon(icon)
        self.btnEditar.setIconSize(QtCore.QSize(24, 24))
        self.btnEditar.setShortcut("")
        self.btnEditar.setCheckable(False)
        self.btnEditar.setFlat(True)
        self.btnEditar.setObjectName("btnEditar")
        self.btnEliminar = QtWidgets.QPushButton(self.utilsFrame)
        self.btnEliminar.setGeometry(QtCore.QRect(50, 70, 38, 38))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btnEliminar.sizePolicy().hasHeightForWidth())
        self.btnEliminar.setSizePolicy(sizePolicy)
        self.btnEliminar.setMinimumSize(QtCore.QSize(0, 0))
        self.btnEliminar.setMaximumSize(QtCore.QSize(128, 48))
        font = QtGui.QFont()
        font.setFamily("Roboto")
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.btnEliminar.setFont(font)
        self.btnEliminar.setText("")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(":/source/img/Cancelar.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btnEliminar.setIcon(icon1)
        self.btnEliminar.setIconSize(QtCore.QSize(24, 24))
        self.btnEliminar.setShortcut("")
        self.btnEliminar.setCheckable(False)
        self.btnEliminar.setFlat(True)
        self.btnEliminar.setObjectName("btnEliminar")
        self.btnCopiar = QtWidgets.QPushButton(self.utilsFrame)
        self.btnCopiar.setGeometry(QtCore.QRect(60, 10, 24, 24))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btnCopiar.sizePolicy().hasHeightForWidth())
        self.btnCopiar.setSizePolicy(sizePolicy)
        self.btnCopiar.setMinimumSize(QtCore.QSize(0, 0))
        self.btnCopiar.setMaximumSize(QtCore.QSize(128, 48))
        font = QtGui.QFont()
        font.setFamily("Roboto")
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.btnCopiar.setFont(font)
        self.btnCopiar.setText("")
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(":/source/img/Copiar.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btnCopiar.setIcon(icon2)
        self.btnCopiar.setIconSize(QtCore.QSize(24, 24))
        self.btnCopiar.setShortcut("")
        self.btnCopiar.setCheckable(False)
        self.btnCopiar.setFlat(True)
        self.btnCopiar.setObjectName("btnCopiar")

        self.retranslateUi(DispositivoWidget)
        QtCore.QMetaObject.connectSlotsByName(DispositivoWidget)

        self.lblImagen.setPixmap(Logica.byteArrayToImage(self.dispositivo.image))
        #listener
        self.btnEditar.clicked.connect(self.btnEditar_Click)
        self.btnEliminar.clicked.connect(self.btnEliminar_Click)
        self.btnCopiar.clicked.connect(self.btnCopiar_Click)


    def btnEditar_Click(self):
        reply = self.prompt("Confirmación","¿Editar este Dispositivo?")
        if reply == QMessageBox.Yes:
            self.deviceSignals.edit.emit(self.dispositivo)

    def btnEliminar_Click(self):
        reply = self.prompt("Confirmación","¿Eliminar este Dispositivo?")
        if reply == QMessageBox.Yes:
            self.deviceSignals.delete.emit(self.dispositivo)

    def btnCopiar_Click(self):
        reply = self.prompt("Confirmación","¿Copiar este Dispositivo?")
        if reply == QMessageBox.Yes:
            self.deviceSignals.copy.emit(self.dispositivo)

    def prompt(self,title,msg):
        return QMessageBox.question(
            self,title,
            msg,
            QMessageBox.Yes | QMessageBox.No)

    def disconnectSignals(self):
        self.btnEditar.clicked.disconnect(self.btnEditar_Click)
        self.btnEliminar.clicked.disconnect(self.btnEliminar_Click)
        self.btnCopiar.clicked.disconnect(self.btnCopiar_Click)

    def sizeHint(self):
        return QtCore.QSize(612, 186)

    def retranslateUi(self, DispositivoWidget):
        _translate = QtCore.QCoreApplication.translate
        DispositivoWidget.setWindowTitle(_translate("DispositivoWidget", "Form"))
        self.lblNombre.setText(_translate("DispositivoWidget", "Nombre:"))
        self.lblID.setText(_translate("DispositivoWidget", "ID:"))
        self.lblToken.setText(_translate("DispositivoWidget", "Token:"))
        self.lblTiempo.setText(_translate("DispositivoWidget", "Tiempo:"))
        self.lblVariables.setText(_translate("DispositivoWidget", "# Variables:"))
        self.txtNombre.setText(_translate("DispositivoWidget", self.dispositivo.nombre))
        self.txtID.setText(_translate("DispositivoWidget", self.dispositivo.id))
        self.txtToken.setText(_translate("DispositivoWidget", self.dispositivo.token))
        self.txtTiempo.setText(_translate("DispositivoWidget", str(self.dispositivo.time)))
        self.txtVariables.setText(_translate("DispositivoWidget", str(len(self.dispositivo.variables))))
