from django.http import HttpResponse
from django.shortcuts import render
import json
# Create your views here.
def index(request):
 return HttpResponse(u"你好")
#定义功能
def add_args(a,b):
    return a+b

#接口函数
def add(request):
    if request.method == 'POST':
        dic = {}
        #判断是否传参
        if request.POST:
            a = request.POST.get('a',0)
            b = request.POST.get('b',0)
            #判断参数中是否含有a和b
            if a and b :
                res =  add_args(a,b)
                dic['number'] = res
                dic = json.dumps(dic)
                return HttpResponse(dic)
            else:
                return HttpResponse('输入错误')
        else:
            return HttpResponse('输入为空')

    else:
        return HttpResponse('方法错误')
