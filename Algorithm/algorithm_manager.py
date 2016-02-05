#! coding:utf-8
"""
algorithm_manager.py

Created by 0160929 on 2016/02/05 11:43
"""
from Algorithm.BaseClass import AlgorithmManagerBaseClass, ResultDatasetBaseClass
from user_algorithm import fft

__version__ = '0.0'
import logging
# format = '> %(asctime)-s - %(filename)-s - %(funcName)-s - >> %(message)-s'
# logging.basicConfig(filename='./log/algorithm_manager.log', filemode='w', level=logging.NOTSET, format=format)


import numpy as np

class AlgorithmManager(AlgorithmManagerBaseClass):
    """ 解析結果のデータセットを渡す
    """

    def __init__(self, params=None):
        logging.info('DummyAlgorithmManager Create')
        AlgorithmManagerBaseClass.__init__(self)
        self.__result_datasets = []
        self.set_params(params)

    def set_params(self, params):
        self.__params = params

    def calculation(self):
        """パラメータの整理と計算の実行"""
        Fs = self.__params['Fs']
        X = self.__params['x']
        # FFT
        Y, freq = fft(X, Fs)

        dataset_amplitude = ResultDatasetBaseClass()
        dataset_amplitude.x = freq
        dataset_amplitude.y = 20 * np.log10(np.abs(Y))
        dataset_amplitude.name = 'Amplitude'
        dataset_amplitude.title = ''
        dataset_amplitude.ylabel = 'Amplitude [db]'
        dataset_amplitude.xlabel = 'Frequency [Hz]'
        dataset_amplitude.xlim = [min(freq), max(freq)]
        dataset_amplitude.ylim = [min(dataset_amplitude.y) - 10., max(dataset_amplitude.y) + 10]

        self.__result_datasets.append(dataset_amplitude)

        dataset_phase = ResultDatasetBaseClass()
        dataset_phase.x = freq
        dataset_phase.y = np.angle(Y)
        dataset_phase.name = 'phase'
        dataset_phase.title = ''
        dataset_phase.ylabel = 'Phase [rad]'
        dataset_phase.xlabel = 'Frequency [Hz]'
        dataset_phase.xlim = [min(freq), max(freq)]
        dataset_phase.ylim = [min(dataset_phase.y) - 10., max(dataset_phase.y) + 10]

        self.__result_datasets.append(dataset_phase)

    def get_results(self):
        result_datasets = []
        return self.__result_datasets
