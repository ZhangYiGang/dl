import logging
from logging.handlers import TimedRotatingFileHandler

log = None

def config_log(file_path,logLevel,  is_debug=False, when="D"):
    """
    日志方法
    :param file_path: 日志路径及文件
    :param is_debug: 级别
    :param when: 按照规则切分
    """
    if is_debug:
        fmt = '[%(asctime)s]-%(filename)s-%(lineno)d-%(threadName)s-%(message)s'
    else:
        fmt = '[%(asctime)s]-%(filename)s-%(lineno)d-%(threadName)s-%(message)s'
    log = logging.getLogger('')
    fileTimeHandler = TimedRotatingFileHandler(file_path, when, 1, 3, encoding='utf-8')
    fileTimeHandler.suffix = "%Y%m%d"
    fileTimeHandler.setFormatter(logging.Formatter(fmt))
    logging.basicConfig(level=logLevel, format=fmt)
    log.addHandler(fileTimeHandler)


