# # Create your views here.
# import json
#
# from django import http
#
# from accounts import serializers
# from accounts.forms import LoginForm
# from utils.response import BadRequestJsonResponse, MethodNotAllowJsonResponse
#
#
# def login_api(request):
#     '''用户登录接口——POST'''
#     # 获取输入内容
#     if request.method =='POST':
#         #表单验证
#         form = LoginForm(request.POST)
#         if form.is_valid():
#             # 通过 执行登录
#             # 返回信息
#             user = form.do_login(request)
#
#             data = {
#                 'data':serializers.UserSerializer(user).to_dict(),
#                 'meta':{
#                     'msg':'登陆成功',
#                     'status':'200',
#                 }
#             }
#             return http.JsonResponse(data)
#         else:
#             # 如果未通过 返回错误信息
#             err = json.loads(form.errors.as_json())
#             return BadRequestJsonResponse(err)
#     else:
#         #请求不被允许
#         return MethodNotAllowJsonResponse()
#
#
#
#
# def logout_api(request):
#          pass