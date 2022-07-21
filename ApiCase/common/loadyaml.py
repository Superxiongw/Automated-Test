# -*- coding: utf-8 -*-
import logging
import os.path
import traceback
import yaml,sys,pytest
from yamlinclude import YamlIncludeConstructor
# yaml_path = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))),"yaml_file/data.yaml")
# basePath = 'E:\Program Files\Sendi_Project\ApiCase\yaml_file'
def read_yaml(yaml_path):
    with open('E:/Program Files/Sendi_Project/ApiCase/yaml_file' + yaml_path,'r', encoding='gbk') as f:
        data=yaml.load(stream=f,Loader=yaml.FullLoader)
        return data
        # print(data)
def read_includeyaml(roofile,basePath):
    YamlIncludeConstructor.add_to_loader_class(loader_class=yaml.FullLoader, base_dir=basePath)
    with open(roofile) as f:
        data = yaml.load(f,Loader=yaml.FullLoader)
    return data
# class Loader(yaml.Loader):
#     def __init__(self, stream):
#         self._root = os.path.split(stream.name)[0]
#         super(Loader, self).__init__(stream)
#     def include(self, node):
#         filename = os.path.join(self._root, self.construct_scalar(node))
#         with open(filename, 'r') as f:
#             return yaml.load(f, Loader)
# Loader.add_constructor('!include', Loader.include)
#
# if __name__ == '__main__':
#     with open('E:\Program Files\Sendi_Project\ApiCase\yaml_file\System_Company\Company_GetAgreementList.yaml', 'r',encoding='gbk') as f:
#         result = yaml.load(f, Loader)
#         print(result)
if __name__ == '__main__':
    re = read_includeyaml('E:\Program Files\Sendi_Project\ApiCase\yaml_file\System_Company\Company_GetAgreementList.yaml',
                          '../System_Company')
    print(re)

