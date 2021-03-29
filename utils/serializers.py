#-*- codeing = utf-8 -*-
#@Time : 2021/3/7 19:11
#@Author:zxc
#@File : serializers.py
#@Software : PyCharm

class BaseSerializer(object):
    def __init__(self,obj):
        self.object = obj
    def to_dict(self):
        return {}
