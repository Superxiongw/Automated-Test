# -*- coding: utf-8 -*-
import os,yaml,pytest


class YamlUtil:

    # 读取extract.yaml文件
    def read_extract_yaml(self, Token):
        if Token is not None:
            with open(os.getcwd() + "/extract.yml", mode='r', encoding='gbk') as f:
                data = yaml.load(stream=f, Loader=yaml.FullLoader)
                return data[Token]
                # print(data)
        else:
            print("Token未获取")

    # 写入xtract.yaml文件
    def write_extract_yaml(self,data):
        with open(os.getcwd()+"/extract.yml", mode='a', encoding='gbk') as f:
            yaml.dump(data=data,stream=f, allow_unicode=True)

    # 清除xtract.yaml文件
    def clear_extract_yaml(self):
        with open(os.getcwd()+"/extract.yml", mode='w', encoding='gbk') as f:
            f.truncate()

    # # 直接读取extract.yaml文件
    # def read_extract_yamls(self):
    #     with open(os.getcwd() + "/extract.yml", mode='r', encoding='gbk') as f:
    #         value = yaml.load(stream=f, Loader=yaml.FullLoader)
    #         return value