#linhas 5, 39-52, 71-74
import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton, QToolTip, QLabel
from PyQt5 import QtGui
from PyQt5.QtWidgets import QLineEdit

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

            self.caixa_texto = QLineEdit(self)
            self.caixa_texto.move(230,25)
            self.caixa_texto.resize(250,30)

            btn_caixa = QPushButton('Inserir texto',self)
            btn_caixa.move(450, 100)
            btn_caixa.resize(150,50)
            btn_caixa.setStyleSheet('QPushButton {background-color:white}')
            btn_caixa.clicked.connect(self.mostrar_texto)

            self.label2 = QLabel(self)
            self.label2.setText("Sem dono")
            self.label2.move(400,200)
            self.label2.resize(200,25)

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

    def mostrar_texto(self):
        # conteudo = self.caixa_texto.text()
        # self.label2.setText(conteudo)
        self.label2.setText("Dono: " + self.caixa_texto.text())


aplicacao = QApplication(sys.argv) 
j = Janela() 
sys.exit(aplicacao.exec_())
