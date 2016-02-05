#! coding:utf-8
"""
main.py

Created by 0160929 on 2016/02/05 16:23
"""
from UI_ import *
from Algorithm.algorithm_manager import AlgorithmManager

__version__ = '0.0'

import os
import sys
import math

from PySide.QtGui import *
from PySide.QtCore import *

import numpy as np


class MyWindow(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super(MyWindow, self).__init__()
        self.setupUi(self)
        self.setWindowTitle("main.py")
        # self.setWindowFlags(Qt.WindowStaysOnTopHint)
        self.resize(640, 480)

        # self.plotter1 = Plotter()
        # self.plotter2 = Plotter()
        # self.plotter3 = Plotter()
        #
        # QObject.connect(self.slider, SIGNAL("valueChanged(int)"), self.alg_update)
        self.f1 = 1
        self.f2 = 2.
        self.alg_mgr = AlgorithmManager()


    def set_f1(self, f1):
        self.f1 = f1
        self.alg_update(f1=self.f1, f2=self.f2)

    def set_f2(self, f2):
        self.f2 = f2
        self.alg_update(f1=self.f1, f2=self.f2)

    def alg_update(self, f1, f2):
        Fs = 48000
        time = np.linspace(start=0, stop=1, num=Fs)
        signal = np.random.rand(len(time)) + np.cos(2 * np.pi * f1 * time) + np.cos(2 * np.pi * f2 * time)

        # 解析
        # -----------------------------------
        params = {'Fs': Fs, 'x': signal}
        self.alg_mgr.set_params(params=params)
        self.alg_mgr.calculation()
        result_datasets = self.alg_mgr.get_results()

        result = result_datasets[0]
        x = result.x
        y = result.y
        self.Plotter1.setCurveData(id=1, x=x, y=y)
        self.Plotter1.set_xlim(result.xlim)
        self.Plotter1.set_ylim(result.ylim)
        self.Plotter1.plot()

        result = result_datasets[1]
        x = result.x
        y = result.y
        self.Plotter2.setCurveData(id=1, x=x, y=y)
        self.Plotter2.set_xlim(result.xlim)
        self.Plotter2.set_ylim(result.ylim)
        self.Plotter2.plot()


def main():
    app = QApplication(sys.argv)
    app.setStyle('plastique')
    win = MyWindow()

    win.show()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()
