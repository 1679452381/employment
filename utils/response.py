#-*- codeing = utf-8 -*-
#@Time : 2021/3/7 21:22
#@Author:zxc
#@File : response.py
#@Software : PyCharm
from  django.http import JsonResponse



# class SucceedJsonResponse(JsonResponse):
#     ''' 200 '''
#     status_code = 200
#     def __init__(self,*args,**kwargs):
#         data = {
#             'err_code':200,
#             'err-msg':'登录成功'
#         }
#         super().__init__(data,*args,**kwargs)

class NotFoundJsonResponse(JsonResponse):
    ''' 404 '''
    status_code = 404
    def __init__(self,*args,**kwargs):
        data = {
            'err_code':404,
            'err-msg':'访问内容不存在或被删除'
        }
        super().__init__(data,*args,**kwargs)

class BadRequestJsonResponse(JsonResponse):
    ''' 表单验证未通过 '''
    status_code = 405
    def __init__(self,err_list=[],*args,**kwargs):
        data = {
            'err_code':'405',
            'err-msg':'表单验证未通过',
            'err_list':err_list
        }
        super().__init__(data,*args,**kwargs)

class MethodNotAllowJsonResponse(JsonResponse):
    ''' 请求方式不被允许 '''
    status_code = 400
    def __init__(self,*args,**kwargs):
        data = {
            'err_code':'400',
            'err-msg':'请求方式不被允许',
        }
        super().__init__(data,*args,**kwargs)