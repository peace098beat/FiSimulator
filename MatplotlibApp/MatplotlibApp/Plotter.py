#! coding:utf-8
"""
Plotter.py
計算結果データセットをプロットするクラス

result_datasetsフォーマット
    result_datasets.x
    result_datasets.y
    result_datasets.title
    result_datasets.xlabel
    result_datasets.ylabel
    result_datasets.xlim
    result_datasets.ylim

使い方
plotter = Plotter()
plotter.set_result_datasets(result_datasets)
plotter.plot()
plotter.save_fig('figure1.jpg')

Created by 0160929 on 2016/02/05 11:31
"""
__version__ = '0.0'

import matplotlib.pyplot as plt


class Plotter():
    def __init__(self, result_datasets=None):
        self.set_result_datasets(result_datasets)

    def set_result_datasets(self, result_datasets):
        self._result_datasets = result_datasets

    def plot(self):
        result_datasets = self._result_datasets
        fig = plt.figure(1)
        for i, result in enumerate(result_datasets):
            ax = fig.add_subplot(len(result_datasets), 1, i + 1)
            x = result.x
            y = result.y
            plt.plot(x, y)
            plt.title(result.title)
            plt.xlabel(result.xlabel)
            plt.ylabel(result.ylabel)
            plt.xlim(result.xlim)
            plt.ylim(result.ylim)

            ax.grid(True)
        plt.show()
        self.fig = fig

        return self.fig

    def save_fig(self, figname):
        self.fig.savefig(figname)
