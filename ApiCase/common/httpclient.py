# -*- coding: utf-8 -*-
import requests

class HttpClient:
    # 只要用到这个类，就会进入到init这个函数里面
    def __init__(self):
        self.session=requests.session()

    # 注意：**kwargs 代表不确定的请求值
    # 封装请求 get/post/delete/put
    def send_request(self,method,url,param_type,data,**kwargs):
        # 设置请求方式转换成大写
        method=method.upper()
        # 设置参数类型转换成大写
        param_type=param_type.upper()
        # 判断请求方式是get/post/delete/put
        if 'GET'==method:
            response=self.session.request(method=method,url=url,params=data,**kwargs)
        elif 'POST'==method:
            # 判断参数类型是json/data提交
            if 'FROM'==param_type:
                response=self.session.request(method=method, url=url, data=data,**kwargs)
            else:
                response=self.session.request(method=method, url=url, json=data,**kwargs)
        elif 'DELETE'==method:
            # 判断参数类型是json/data提交
            if 'FROM' == param_type:
                response=self.session.request(method=method, url=url, data=data, **kwargs)
            else:
                response=self.session.request(method=method, url=url, json=data, **kwargs)
        elif 'PUT'==method:
            # 判断参数类型是json/data提交
            if 'FROM' == param_type:
                response=self.session.request(method=method, url=url, data=data, **kwargs)
            else:
                response=self.session.request(method=method, url=url, json=data, **kwargs)
        else:
            raise ValueError

        return response

    def close_session(self):
        self.session.close()

