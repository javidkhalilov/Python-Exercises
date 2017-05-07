import sys
from PyQt4 import QtGui,QtCore


#!/usr/bin/python
# -*- coding: utf-8 -*-

"""
ZetCode PyQt4 tutorial 

In this example, we create a simple
window in PyQt4.

author: Jan Bodnar
website: zetcode.com 
last edited: October 2011
"""



def main():
    
    app = QtGui.QApplication(sys.argv)
    
    c=QtGui.QWidget()
    w = QtGui.QWidget()
    w.resize(450, 450)
    w.move(300, 300)
    w.setWindowTitle('Simple')
    w.show()


    sys.exit(app.exec_())


if __name__ == '__main__':
    main()

