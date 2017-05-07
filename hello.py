import sys
from PyQt4 import QtGui,QtCore


#!/usr/bin/python
# -*- coding: utf-8 -*-




def main():
    
    app = QtGui.QApplication(sys.argv)
    
    c=QtGui.QWidget()
    w = QtGui.QWidget()
    w.resize(450, 450)
    w.move(300, 300)
    w.setWindowTitle('Simple HELLO')
    w.show()


    sys.exit(app.exec_())


if __name__ == '__main__':
    main()

