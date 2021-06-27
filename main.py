import PySide2
from PySide2 import QtCore, QtWidgets
from PySide2.QtWidgets import QApplication, QWidget, QMainWindow, QPushButton,QLabel
from PySide2.QtGui import QWindow, QIcon
from PySide2.QtCore import QSize
import os
import sys

class ui(QMainWindow):
	def __init__(self):
		super().__init__()
		self.setWindowTitle("Game Booster")
		self.setGeometry(0,0,400,200)
		self.setStyleSheet("Background:#000000;Border-color:000000;")
		self.setMaximumHeight(200)
		self.setMinimumHeight(200)
		self.setMaximumWidth(400)
		self.setMinimumWidth(400)

		self.enable = QPushButton("Enable", self)
		self.enable.setGeometry(50,50,100,50)
		self.enable.setStyleSheet("Color:white")
		self.enable.clicked.connect(enable)

		self.disable = QPushButton("Disable", self)
		self.disable.setGeometry(230,50,100,50)
		self.disable.setStyleSheet("Color:white")
		self.disable.clicked.connect(disable)



def enable():
	os.system("notify-send -u critical 'Game Booster On'")
	os.system("(xfwm4 --compositor=off --replace)&")
	os.system("bash ~/LinuxGameBooster/src/governor/init_performance.sh")

def disable():
	os.system("notify-send -u critical 'Game Booster Off'")
	os.system("bash ~/LinuxGameBooster/src/governor/init_ondemand.sh")

app = QApplication(sys.argv)
canvas = ui()
canvas.show()
app.exec_()
sys.exit()
