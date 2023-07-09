import json

import pytest    # 导入pytest包

from config import  ProInfo
from readData import MyExcel
from scoreByRule import getScore

def test_001():    # 函数以test_开头
    pro = ProInfo()
    pro.readConfig()
    myExcel = MyExcel(pro._csvPath)
    result = myExcel.read_excel(pro.isTranslate)
    resultList = myExcel.resultList
    scoredict = getScore(resultList)
    with open('test.json', 'w', encoding='utf8') as f2:
        # ensure_ascii=False才能输入中文，否则是Unicode字符
        # indent=2 JSON数据的缩进，美观
        json.dump(scoredict, f2, ensure_ascii=False, indent=2)

