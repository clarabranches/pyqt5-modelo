#python orientado a objeto
import sys
from PyQt5.QtWidgets import QApplication, QMainWindow

class Janela(QMainWindow):
    def __init__(self): #metodo contrutor
            super().__init__()

            self.esquerda = 100 # distancia que a janela vai ter do lado esquedo da tela em relação a tela do computador
            self.topo = 100 #altura que a janela vai aparecer na tela
            #tamanho
            self.largura = 800
            self.altura = 600
            self.titulo = "Executor Roblox"
            self.CarregarJanela()

    def CarregarJanela(self):
        self.setGeometry(self.esquerda,self.topo,self.largura,self.altura)
        self.setWindowTitle(self.titulo)
        self.show()

aplicacao = QApplication(sys.argv)  #usado para mexer nos parametros do sistema como fechar janela
j = Janela() # criação do objeto j que recebe funções de Janela
sys.exit(aplicacao.exec_())