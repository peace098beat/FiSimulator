#! coding:utf-8
"""
BaseClass.py

Created by 0160929 on 2016/02/05 11:39
"""
__version__ = '0.0'

# *******************************************************
#
#   FiSimulator module
#
# *******************************************************
class AlgorithmManagerBaseClass():
    def __init__(self, params=None):
        self.set_params(params)
        pass

    def set_params(self, params):
        self.__params = params

    def calculation(self):
        pass


class ResultDatasetBaseClass():
    def __init__(self):
        self.name = None
        self.x = None
        self.y = None
        self.title = None
        self.xlabel = None
        self.ylabel = None
        self.xlim = None
        self.ylim = None
        pass
