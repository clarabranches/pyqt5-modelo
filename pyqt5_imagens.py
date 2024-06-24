#linhas 4, 33-36, 48, 53
import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton, QToolTip, QLabel
from PyQt5 import QtGui

class Janela(QMainWindow):
    def __init__(self): 
            super().__init__()

            self.esquerda = 100 
            self.topo = 100 
            self.largura = 800
            self.altura = 600
            self.titulo = "Executor Roblox"

            botao1 = QPushButton('Onix', self)
            botao1.move(100,100)
            botao1.resize(150,50)
            botao1.setStyleSheet('QPushButton {background-color:#2DC12B}')
            botao1.clicked.connect(self.botao1_click)
            
            botao2 = QPushButton('Trator',self)
            botao2.move(260, 100)
            botao2.resize(150,50)
            botao2.setStyleSheet('QPushButton {background-color:#add8e6}')
            botao2.clicked.connect(self.botao2_click)

            self.label1 = QLabel(self)
            self.label1.setText("Clique em um botão")
            self.label1.move(200,200)
            self.label1.resize(200,25)

            self.carro = QLabel(self)
            self.carro.move(40, 280)
            self.carro.setPixmap(QtGui.QPixmap(''))
            self.carro.resize(500,200)

            self.CarregarJanela()

    def CarregarJanela(self):
        self.setGeometry(self.esquerda,self.topo,self.largura,self.altura)
        self.setWindowTitle(self.titulo)
        self.show()

    def botao1_click(self):
        self.label1.setText("Você selecionou o Onix")
        self.label1.setStyleSheet('QLabel {font:bold; color:#2DC12B}')
        self.carro.setPixmap(QtGui.QPixmap('carro1.png'))

    def botao2_click(self):
        self.label1.setText("Você selecionou o trator")
        self.label1.setStyleSheet('QLabel {font:bold; color:#add8e6}')
        self.carro.setPixmap(QtGui.QPixmap('carro2.png'))


aplicacao = QApplication(sys.argv) 
j = Janela() 
sys.exit(aplicacao.exec_())
