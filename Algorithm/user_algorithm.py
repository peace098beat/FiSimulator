#! coding:utf-8
"""
user_algorithm.py

Created by 0160929 on 2016/02/05 11:42
"""
__version__ = '0.0'

import numpy as np

def fft(X, Fs):
    # FFT
    Y = np.fft.fft(X)
    freq = np.fft.fftfreq(X.size, d=1. / Fs)

    return Y, freq

