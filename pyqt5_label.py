#linhas 4, 28-31 41,42,45,46
import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton, QToolTip
from PyQt5.QtWidgets import QLabel

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
            botao2.setStyleSheet('QPushButton {background-color:#add8e6}')
            botao2.clicked.connect(self.botao2_click)

            self.label1 = QLabel(self)
            self.label1.setText("Clique em um botão")
            self.label1.move(200,200)
            self.label1.resize(200,25)

            self.CarregarJanela()

    def CarregarJanela(self):
        self.setGeometry(self.esquerda,self.topo,self.largura,self.altura)
        self.setWindowTitle(self.titulo)
        self.show()

    def botao1_click(self):
        self.label1.setText("Você clicou no botão 1")
        self.label1.setStyleSheet('QLabel {font:bold; color:#2DC12B}')

    def botao2_click(self):
        self.label1.setText("Você clicou no botão 2")
        self.label1.setStyleSheet('QLabel {font:bold; color:#add8e6}')


aplicacao = QApplication(sys.argv) 
j = Janela() 
sys.exit(aplicacao.exec_())
