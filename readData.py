import logging

import pandas as pd
from logger import log


from mytaranslate import MyTranslator
from config import getReplaceWord, getKeyWordPain,gettenPainWord
from util import isTextHasAllThingsInlist

def filter(text):
	replaceWords = getReplaceWord()
	for word in replaceWords.keys():
		if word in text:
			text = text.replace(word,replaceWords[word])
	return text
class MyExcel:
	def __init__(self, csvPath):
		self.readCsvPath = csvPath
		self.currentCol =1
		self._info = None
		self._translateInfo = None
		self._resultList = []

	@property
	def resultList(self):
	     return self._resultList;


	@property
	def translateInfo(self):
		return self._translateInfo



	def read_excel(self,isTranslate):

		df = pd.read_excel(self.readCsvPath)
		test = df.columns
		if df.columns.size == 1:
			self.currentCol = 0
		if df.columns.size >2:
			logging.error("这个excel文件提供的列数大于2，请再做检查")
			return False
		self._info = list(df.iloc[:, self.currentCol])
		if isTranslate:
			self.my_translate()
		else:
			self._translateInfo = self._info
		self._translateInfo = [filter(item) for item in self._translateInfo]
		needList = self.splitQuestion()
		needPainList = self.splitTenPain(needList)
		self._resultList = self.splitTenPain(needPainList)

	def splitQuestion(self):
		keyWordPain = getKeyWordPain()
		if len(keyWordPain) == 0:
			logging.error("请注意配置文件，缺少两个问题的关键词，主要是变量keyWordPain")

		needList = []
		isNeed = False
		for text in self._translateInfo:
			if keyWordPain[0] in text or keyWordPain[1] in text:
				isNeed = not isNeed
			if isNeed:
					needList.append(text)
		return needList

	def splitTenPain(self, needWorkList):
		tenPainWord = gettenPainWord()
		nowIndex = 0
		resultList = []

		start = 0
		end = 0
		for i in range(len(needWorkList)):
			if nowIndex == 10:
				break
			nowText = needWorkList[i]
			if isTextHasAllThingsInlist(nowText, tenPainWord[nowIndex]):
				end = i
				nowIndex = nowIndex+1
				resultList.append(needWorkList[start:end])
				start = i
		if start < len(needWorkList):
			resultList.append(needWorkList[start:])
		return resultList

	def my_translate(self):
		myTranslator = MyTranslator()
		for item in self._info:
			myTranslator.translate(item)
		self._translateInfo = [myTranslator.translate(i) for i in self._info]




