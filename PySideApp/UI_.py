# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'UI_.ui'
#
# Created: Fri Feb 05 17:27:40 2016
#      by: pyside-uic 0.2.15 running on PySide 1.2.4
#
# WARNING! All changes made in this file will be lost!

from PySide import QtCore, QtGui

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.horizontalLayout = QtGui.QHBoxLayout(self.centralwidget)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.verticalLayout_2 = QtGui.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.Plotter1 = Plotter(self.centralwidget)
        self.Plotter1.setObjectName("Plotter1")
        self.verticalLayout_2.addWidget(self.Plotter1)
        self.line = QtGui.QFrame(self.centralwidget)
        self.line.setFrameShape(QtGui.QFrame.HLine)
        self.line.setFrameShadow(QtGui.QFrame.Sunken)
        self.line.setObjectName("line")
        self.verticalLayout_2.addWidget(self.line)
        self.Plotter2 = Plotter(self.centralwidget)
        self.Plotter2.setObjectName("Plotter2")
        self.verticalLayout_2.addWidget(self.Plotter2)
        self.horizontalLayout.addLayout(self.verticalLayout_2)
        self.formLayout = QtGui.QFormLayout()
        self.formLayout.setObjectName("formLayout")
        self.label = QtGui.QLabel(self.centralwidget)
        self.label.setObjectName("label")
        self.formLayout.setWidget(0, QtGui.QFormLayout.LabelRole, self.label)
        self.doubleSpinBox = QtGui.QDoubleSpinBox(self.centralwidget)
        self.doubleSpinBox.setObjectName("doubleSpinBox")
        self.formLayout.setWidget(0, QtGui.QFormLayout.FieldRole, self.doubleSpinBox)
        self.label_2 = QtGui.QLabel(self.centralwidget)
        self.label_2.setObjectName("label_2")
        self.formLayout.setWidget(1, QtGui.QFormLayout.LabelRole, self.label_2)
        self.doubleSpinBox_2 = QtGui.QDoubleSpinBox(self.centralwidget)
        self.doubleSpinBox_2.setObjectName("doubleSpinBox_2")
        self.formLayout.setWidget(1, QtGui.QFormLayout.FieldRole, self.doubleSpinBox_2)
        self.label_3 = QtGui.QLabel(self.centralwidget)
        self.label_3.setObjectName("label_3")
        self.formLayout.setWidget(2, QtGui.QFormLayout.LabelRole, self.label_3)
        self.doubleSpinBox_3 = QtGui.QDoubleSpinBox(self.centralwidget)
        self.doubleSpinBox_3.setObjectName("doubleSpinBox_3")
        self.formLayout.setWidget(2, QtGui.QFormLayout.FieldRole, self.doubleSpinBox_3)
        self.label_4 = QtGui.QLabel(self.centralwidget)
        self.label_4.setObjectName("label_4")
        self.formLayout.setWidget(3, QtGui.QFormLayout.LabelRole, self.label_4)
        self.doubleSpinBox_4 = QtGui.QDoubleSpinBox(self.centralwidget)
        self.doubleSpinBox_4.setObjectName("doubleSpinBox_4")
        self.formLayout.setWidget(3, QtGui.QFormLayout.FieldRole, self.doubleSpinBox_4)
        self.horizontalLayout.addLayout(self.formLayout)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 17))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QObject.connect(self.doubleSpinBox, QtCore.SIGNAL("valueChanged(double)"), MainWindow.set_f1)
        QtCore.QObject.connect(self.doubleSpinBox_2, QtCore.SIGNAL("valueChanged(double)"), MainWindow.set_f2)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QtGui.QApplication.translate("MainWindow", "MainWindow", None, QtGui.QApplication.UnicodeUTF8))
        self.label.setText(QtGui.QApplication.translate("MainWindow", "f1", None, QtGui.QApplication.UnicodeUTF8))
        self.label_2.setText(QtGui.QApplication.translate("MainWindow", "f2", None, QtGui.QApplication.UnicodeUTF8))
        self.label_3.setText(QtGui.QApplication.translate("MainWindow", "L", None, QtGui.QApplication.UnicodeUTF8))
        self.label_4.setText(QtGui.QApplication.translate("MainWindow", "Sigma", None, QtGui.QApplication.UnicodeUTF8))

from PySideApp.Plotter import Plotter
