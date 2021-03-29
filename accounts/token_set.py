# #-*- codeing = utf-8 -*-
# #@Time : 2021/3/12 20:25
# #@Author:zxc
# #@File : token_set.py
# #@Software : PyCharm
#
# # import jwt
# #
# # header = {
# #     'name':'zxc',
# #     'type':'jwt'
# # }
# # encode_jwt = jwt.encode(header,'zxc',algorithm='HS256')
# # decode_jwt = jwt.decode(encode_jwt,'zxc',algorithm='HS256')
# # print(encode_jwt)
# # print(decode_jwt)
# # print(decode_jwt['name'])
# import jwt
#
# def set_token(header):
#     mytoken = jwt.encode(header,'991213',algorithm='HS256')
#     mytoken = str(mytoken, 'utf-8')
#     return mytoken
# def detoken(token):
#     mytoken = jwt.decode(token,'991213',algorithm='HS256')
#     data = mytoken['name']
#     return data
