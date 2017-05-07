
import sys
from PyQt4 import QtGui,QtCore

class Window(QtGui.QMainWindow):
    
    def __init__(self):
        super(Window,self).__init__()
        self.setGeometry(50,50,500,300)
        self.setWindowTitle("PyQT")
        self.setWindowIcon(QtGui.QIcon('pythonlogo.png'))

        extractAction=QtGui.QAction("& get to the choppah",self)
        extractAction.setShortcut("Ctrl+Q")
        extractAction.setStatusTip("leave the app")
        extractAction.triggered.connect(self.close_application)
        
        openEditor=QtGui.QAction("&Editor", self)
        openEditor.setShortcut("Ctrl+E")
        openEditor.setStatusTip('Open Editor')
        openEditor.triggered.connect(self.editor)
        
        openFile=QtGui.QAction("&Open File", self)
        openFile.setShortcut("Ctrl+O")
        openFile.setStatusTip('Open File')
        openFile.triggered.connect(self.file_open)
        
        saveFile=QtGui.QAction("&Save File", self)
        saveFile.setShortcut("Ctrl+S")
        saveFile.setStatusTip('Save File')
        saveFile.triggered.connect(self.file_save)

        self.statusBar()

        mainMenu=self.menuBar()
        fileMenu=mainMenu.addMenu('&File')
        fileMenu.addAction(extractAction)
        fileMenu.addAction(openFile)
        fileMenu.addAction(saveFile)
        
        editorMenu=mainMenu.addMenu('&Editor')
        editorMenu.addAction(openEditor)

        self.home()
    
    def home(self):
        btn=QtGui.QPushButton("Quit",self)
        btn.clicked.connect(self.close_application)   
        btn.resize(btn.minimumSizeHint())
        btn.move(100,100)

        extractAction=QtGui.QAction(QtGui.QIcon('pythonlogo.png'),'flee the scene',self)
        extractAction.triggered.connect(self.close_application)
        self.toolbar=self.addToolBar("Extraction")
        self.toolbar.addAction(extractAction)

        fontChoice=QtGui.QAction('Font',self)
        fontChoice.triggered.connect(self.font_choice)
        self.toolbar=self.addToolBar("Font Choice")
        self.toolbar.addAction(fontChoice)

        color=QtGui.QColor(0,0,0)

        fontColor=QtGui.QAction('Font bg color',self)
        fontColor.triggered.connect(self.color_picker)

        self.toolbar.addAction(fontColor)





        checkBox=QtGui.QCheckBox('Enlarge window',self)
        checkBox.move(300,25)
        checkBox.toggle()
        checkBox.stateChanged.connect(self.enlarge_window)

        self.progress=QtGui.QProgressBar(self)
        self.progress.setGeometry(200,80,250,20)
        

        self.btn=QtGui.QPushButton("Dowload",self)
        self.btn.move(200,120)
        self.btn.clicked.connect(self.download)

        print(self.style().objectName())
        self.styleChoice=QtGui.QLabel("Windows 8.1",self)

        comboBox=QtGui.QComboBox(self)
        comboBox.addItem("motif")
        comboBox.addItem("Windows")
        comboBox.addItem("cde")
        comboBox.addItem("Plastique")
        comboBox.addItem("Cleanlooks")
        comboBox.addItem("windowsvista")

        comboBox.move(50,250)
        self.styleChoice.move(50,150)
        comboBox.activated[str].connect(self.style_choice)

        cal=QtGui.QCalendarWidget(self)
        cal.move(500,200)
        cal.resize(200,200)

        self.show()

    def color_picker(self):
        color=QtGui.QColorDialog.getColor()
        self.styleChoice.setStyleSheet("QWidget {background-color: %s}"%color.name())
        
    def file_open(self):
        name=QtGui.QFileDialog.getOpenFileName(self, 'Open File')
        file=open(name, 'r')
        self.editor()
        with file:
            text=file.read()
            self.textEdit.setText(text)

    def file_save(self):
        name=QtGui.QFileDialog.getSaveFileName(self,'Save File')
        file=open(name,'w')
        text=self.textEdit.toPlainText()
        file.write(text)
        file.close()
        
        
    def editor(self):
        self.textEdit= QtGui.QTextEdit()
        self.setCentralWidget(self.textEdit)    
        
    def font_choice(self):

        font, valid=QtGui.QFontDialog.getFont()
        if valid:
            self.styleChoice.setFont(font)

    def style_choice(self,text):
        self.styleChoice.setText(text)
        QtGui.QApplication.setStyle(QtGui.QStyleFactory.create(text))

    def download(self):
        self.completed=0

        while self.completed<100:
            self.completed+=0.0001
            self.progress.setValue(self.completed)


        
        
        

    def enlarge_window(self,state):
        if state==QtCore.Qt.Checked:
            self.setGeometry(50,50,1000,600)
        else:
            self.setGeometry(50,50,500,300)

        
    def close_application(self):
        #print("whoaaa")
        #self.setWindowTitle("Hele Hele")
        #sys.exit()

        choice=QtGui.QMessageBox.question(self,'Extract',"Do you wanna close ?",
                                        QtGui.QMessageBox.Yes | QtGui.QMessageBox.No)

        if choice==QtGui.QMessageBox.Yes:
            print("hell yeahh")
            sys.exit()
        else:
            pass

    
def run():
    app=QtGui.QApplication(sys.argv)
    GUI=Window()
    sys.exit(app.exec_())

run()
