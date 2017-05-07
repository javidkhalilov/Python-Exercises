#!/usr/bin/python
# -*- coding: utf-8 -*-


import sys
from PyQt4 import QtGui


def main():
    
    app = QtGui.QApplication(sys.argv)
    
    c=QtGui.QWidget()
    w = QtGui.QWidget()
    w.resize(250, 250)
    w.move(300, 300)
    w.setWindowTitle('Simple')
    w.show()
    
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()
