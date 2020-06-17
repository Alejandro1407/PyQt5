from PyQt5.QtWidgets import QMessageBox, QApplication
from ..objects.usuario import usuario

class session(object):

    __instance = None # Instance of the session; just can exists one on all the app

    def __new__(cls,*args,**kwargs ):        
        if cls.__instance is None :
            cls.__instance =  object.__new__(cls)
            super(session,cls.__instance).__init__()
            cls.__sessionObject = args[0]
        return cls.__instance

    def __init__(self,*args):
        if not self.isValid():
            QMessageBox.warning(None,"¡Error!","Session invalida o inexistente\nCerrado Aplicacion...")
            QApplication.exit(0)

    @property
    def access_token(self):
        return self.__sessionObject.access_token

    def isValid(self): # just validate that an user object exits, if access_token is invalid o doesnt exist API will deny access
        return True if isinstance(self.__sessionObject,usuario) else False
