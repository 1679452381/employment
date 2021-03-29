#-*- codeing = utf-8 -*-
#@Time : 2021/3/7 19:11
#@Author:zxc
#@File : serializers.py
#@Software : PyCharm
# import time
# from utils import serializers
# from accounts import token_set
#
#
# class UserSerializer(serializers.BaseSerializer):
#     '''用户信息'''
#
#     def to_dict(self):
#         user = self.object
#         header = {
#             'username': user.username,
#             'type': 'jwt',
#             'time':time.time()
#         }
#         mytoken = token_set.set_token(header)
#         data = {
#             'id':user.id,
#             'rid': user.rid,
#             'username':user.username,
#             'stuNum':user.stuNum,
#             'token':mytoken
#         }
#         return data