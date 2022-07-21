# -*- coding: utf-8 -*-
import logging
# 创建日志对象
logger = logging.getLogger("cnodeweb")
# 控制台等级
logger.setLevel(logging.DEBUG)

format = logging.Formatter('[%(asctime)s] [%(levelname)s] [%(funcName)s] [%(message)s')

fl = logging.FileHandler(filename='E:/Program Files/Sendi_Project/ApiCase/logs/cnode.log',
                         mode='a',encoding='utf-8')
fl.setFormatter(format)

#创建控制台处理器
sl = logging.StreamHandler()
sl.setFormatter(format)
# 日志器添加控制台处理器
logger.addHandler(fl)
logger.addHandler(sl)