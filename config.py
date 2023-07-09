import  json
import os
from typing import Any
from logger import config_log
"""
mode: 1为单个文件
csvPath：csv文件目录
"""

currentPath = os.path.abspath(__file__).split(os.sep)
currentPath[-1] = 'config.json'

replaceWords = {}
keywordPain = {}
tenPainWord = []
scoreList = []
class ProInfo:
    def __init__(self):
        self._mode = 1
        self._csvPath = ""
        self._logLevel = 10
        self._logFilePath = "./"
        self._isTranslate = False



    @property
    def logFilePath(self):
        return self._logFilePath

    @logFilePath.setter
    def logFilePath(self, value):
        self._logFilePath = value

    @property
    def logLevel(self):
        return self._logLevel

    @logLevel.setter
    def logLevel(self, value):
        self._logLevel = value

    @property
    def csvPath(self):
        return self._csvPath

    @csvPath.setter
    def csvPath(self, value):
        self._csvPath = value

    @property
    def isTranslate(self):
        return self._isTranslate

    @isTranslate.setter
    def isTranslate(self, value):
        self._isTranslate = value

    # @property
    # def replaceWords(self):
    #     return self._replaceWords;



    def readConfig(self):
        global replaceWords
        global keywordPain
        global tenPainWord
        global scoreList
        with open(os.sep.join(currentPath), 'r', encoding='utf-8') as fp:
            # load()函数将fp(一个支持.read()的文件类对象，包含一个JSON文档)反序列化为一个Python对象
            data = json.load(fp)
            self._csvPath = data["single"]
            self._logLevel = data["logLevel"]
            self._logFilePath = data["logFilePath"]
            self._isTranslate = data["isTranslate"]
            replaceWords = data["replaceWords"]
            keywordPain = data["keywordPain"]
            tenPainWord = data["tenPainWord"]
            scoreList = data["score"]
        config_log(self._logFilePath, self._logLevel)
def getKeyWordPain():
    return keywordPain
def getReplaceWord():
    return  replaceWords

def gettenPainWord():
    return tenPainWord

def getScoreList():
    return scoreList






