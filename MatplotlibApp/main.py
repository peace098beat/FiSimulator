#! coding:utf-8
"""
main.py

Created by 0160929 on 2016/02/05 11:35
"""
from Algorithm.algorithm_manager import AlgorithmManager

__version__ = '0.0'

import os
import sys
import logging
# format = '> %(asctime)-s - %(filename)-s - %(funcName)-s - >> %(message)-s'
# logging.basicConfig(filename='./log/MatplotlibApp.log', filemode='w', level=logging.NOTSET, format=format)


from MatplotlibApp.Plotter import Plotter

if __name__ == '__main__':

    logging.info('Run main')

    # 計算パラメータ
    import numpy as np
    Fs = 48000
    time = np.linspace(start=0, stop=1, num=Fs)
    signal = np.random.rand(len(time)) + np.cos(2 * np.pi * 1000 * time) + np.cos(2 * np.pi * 10000 * time)

    # 解析
    # -----------------------------------
    params = {'Fs': Fs, 'x': signal}
    alg_mgr = AlgorithmManager()
    alg_mgr.set_params(params=params)
    alg_mgr.calculation()
    result_datasets = alg_mgr.get_results()

    # Matlab関数
    plotter = Plotter(result_datasets)
    plotter.plot()
    plotter.save_fig('./result/result.png')
