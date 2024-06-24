#linhas 4, 16-26, 35-39
import sys
from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5.QtWidgets import QPushButton, QToolTip #segunda mudar as imagens

class Janela(QMainWindow):
    def __init__(self): 
            super().__init__()

            self.esquerda = 100 
            self.topo = 100 
            self.largura = 800
            self.altura = 600
            self.titulo = "Executor Roblox"
#precisamos criar os botões antes da opção CarregarJanela, pois se a criação for feita depois dele a janela sera carregada sem os elementos
            botao1 = QPushButton('Botão 1', self)
            botao1.move(100,100)
            botao1.resize(150,50)
            botao1.setStyleSheet('QPushButton {background-color:#2DC12B}')
            botao1.clicked.connect(self.botao1_click)
            
            botao2 = QPushButton('Botão 2',self)
            botao2.move(260, 100)
            botao2.resize(150,50)
            botao2.setStyleSheet('QPushButton {background-color:#2DC12B}')
            botao2.clicked.connect(self.botao2_click)

            self.CarregarJanela()

    def CarregarJanela(self):
        self.setGeometry(self.esquerda,self.topo,self.largura,self.altura)
        self.setWindowTitle(self.titulo)
        self.show()

    def botao1_click(self):
        print('botão 1 foi clicado!')

    def botao2_click(self):
        print('botão 2 foi clicado!')


aplicacao = QApplication(sys.argv) 
j = Janela() 
sys.exit(aplicacao.exec_())



