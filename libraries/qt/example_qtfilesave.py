import sys
from PyQt5 import QtGui, QtCore, QtWidgets

app = QtWidgets.QApplication(sys.argv)
mainwindow = QtWidgets.QMainWindow()
path = QtWidgets.QFileDialog.getSaveFileName(None, "Save Node Layout", "./", "JSON Files (*.json)")[0]
print(path)