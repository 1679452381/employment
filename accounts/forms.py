# #-*- codeing = utf-8 -*-
# #@Time : 2021/3/7 19:03
# #@Author:zxc
# #@File : forms.py
# #@Software : PyCharm
#
#
#
# from django import forms
# from django.contrib.auth import authenticate, login
#
# from accounts import token_set
#
#
# class LoginForm(forms.Form):
#     '''登陆表单'''
#     username = forms.CharField(label='用户名',
#                                max_length=100,
#                                required=False,
#                                help_text='使用帮助',
#                                initial='admin')
#     password = forms.CharField(label='密码', max_length=200, min_length=6,
#                                widget=forms.PasswordInput)
#     def __init__(self, *args, **kwargs):
#         super().__init__(*args, **kwargs)
#         # 当前登录的用户
#         self.user = None
#
#
#     def clean(self):
#         data = super().clean()
#         if self.errors:
#             return
#         username = data.get('username',None)
#         password = data.get('password',None)
#
#         user = authenticate(username=username,password=password)
#
#         if user is None:
#             raise forms.ValidationError('用户或密码不正确')
#         else:
#             if not user.is_active:
#                 raise forms.ValidationError('该用户已经禁用')
#         self.user = user
#         return data
#     def do_login(self,request):
#         '''执行登录'''
#         user = self.user
#         login(request,user)
#         #修该最后登录时间
#         return user
