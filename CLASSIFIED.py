import sys
from PyQt5.QtWidgets import  QLabel,QFileDialog,QMainWindow, QApplication, QWidget, QPushButton, QAction, QLineEdit, QMessageBox,QHBoxLayout, QGroupBox, QDialog, QVBoxLayout
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import pyqtSlot,Qt
import ctypes
import subprocess
import test
import imutils
import cv2
from imutils.video import FileVideoStream,FPS
class App(QWidget):
    def __init__(self):
        super().__init__()
        self.title = 'C.L.A.S.S.I.F.I.E.D.'
        self.left = 750
        self.top = 300
        self.width = 300
        self.height = 500
        self.initUI()
        
    def initUI(self):
        #Main Window
        self.setWindowTitle(self.title)
        self.setGeometry(self.left, self.top, self.width, self.height)
        #video select Hbox
        self.horizontalGroupBox = QGroupBox("Open a video to Classify")
        layout = QVBoxLayout()
        #Video Selection Box
        self.textbox = QLineEdit(self)
        self.textbox.move(20, 20)
        self.textbox.resize(300,30)
        #Video Select Button
        button = QPushButton('Select Video', self)
        button.setToolTip('Open Video')
        button.move(640,20)
        button.resize(90,50)
        button.clicked.connect(self.select_video)
        layout.addWidget(self.textbox)
        layout.addWidget(button)
        self.horizontalGroupBox.setLayout(layout)
        #URL Load Button
        self.loadbutton = QPushButton('Load URL', self)
        self.loadbutton.setToolTip('paste video URL in the box')
        self.loadbutton.move(640,20)
        self.loadbutton.resize(90,50)
        self.loadbutton.clicked.connect(self.select_url)
        layout.addWidget(self.loadbutton)
        self.horizontalGroupBox.setLayout(layout)
        #Classify Group Box
        self.ClassifyGroupBox = QGroupBox("")
        classifylayout = QHBoxLayout()
        #Classify button
        classifybutton = QPushButton('Classify!', self)
        classifybutton.setToolTip('Classify the selected video')
        classifybutton.move(325,400)
        classifybutton.resize(75,50)
        classifybutton.clicked.connect(self.classify)
        classifylayout.addWidget(classifybutton)
        self.ClassifyGroupBox.setLayout(classifylayout)
        #Final Result Box
        self.ResultGroupBox = QGroupBox("Result!")
        Resultlayout = QHBoxLayout()
        #Final Result Label
        self.ResultLabel = QLabel()
        self.ResultLabel.resize(300,50)
        self.ResultLabel.setAlignment(Qt.AlignCenter)
        self.ResultLabel.setText("Hit Classify!")
        Resultlayout.addWidget(self.ResultLabel)
        self.ResultGroupBox.setLayout(Resultlayout)
        #Final Window Layout
        windowLayout = QVBoxLayout()
        windowLayout.addWidget(self.horizontalGroupBox)
        windowLayout.addWidget(self.ClassifyGroupBox)
        windowLayout.addWidget(self.ResultGroupBox)
        self.setLayout(windowLayout)
        self.show()
    @pyqtSlot()
    def select_video(self):
        print('opened video explorer')
        self.file_path = QFileDialog.getOpenFileName(self, 'Select Video','C:\\',"Video files (*.mp4 *.avi)")
        if self.file_path[0] : 
            self.loadbutton.hide()  
            print(self.file_path[0])
            self.textbox.setText(self.file_path[0])
    def select_url(self):
        print('decoding url')
        self.file_path = self.textbox.text()
        if self.file_path[0] :   
            print(self.file_path)
            self.textbox.setText(self.file_path)
    def classify(self):
        if self.file_path[0:4]!='http' : 
            print('started classifying video')
            subprocess.Popen("python test.py --graph=./inception/retrained_graph.pb --labels=./inception/retrained_labels.txt --input_layer=Placeholder --output_layer=final_result --video="+str(self.file_path[0]))
        else :
            print('started classifying video')
            subprocess.Popen("python test.py --graph=./inception/retrained_graph.pb --labels=./inception/retrained_labels.txt --input_layer=Placeholder --output_layer=final_result --video="+str(self.file_path))
    def set_Result(self,prediction):
        self.ResultLabel.setText(prediction)
    
if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = App()
    sys.exit(app.exec_())
