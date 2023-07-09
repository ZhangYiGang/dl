import codecs
import logging
import time

from googletrans import Translator
from multiprocessing.dummy import Pool as ThreadPool
pool = ThreadPool(8)

def request(text):
    lang = "zh-cn"
    t = Translator(timeout=50)
    translate_text = t.translate(text.strip(), src='ja', dest=lang)
    return translate_text

class MyTranslator:
    def __init__(self):
        self._translator = Translator(proxies={'https': '127.0.0.1:7890'})

    def translate(self, sentence):
        """
        :param sentence: 返回一句话
        :return:
        """
        translation = self._translator.translate(sentence, src='ja', dest="zh-cn")
        # translation = self._translator.translate(translation.text, lang_src='ja', dest='zh')
        print(translation)
        return translation

    def translateTexts(self, textlist):
        time1 = time.time()
        with codecs.open("./test.txt", 'r', encoding='utf-8') as f_p:
           texts = f_p.readlines()
        try:
            results = pool.map(request, texts)
        except Exception as e:
            raise e
        pool.close()
        pool.join()
        time2 = time.time()
        logging.info("Translating %s sentences, a total of %s s" % (len(textlist), time2 - time1))


    def translateExcel(self, csv_file):
        # self.csv =
        pass



