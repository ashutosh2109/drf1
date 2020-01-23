from django.shortcuts import render
from django.http import HttpResponse

def emp_data_view(request):
    emp_data={ 'eno':100,
               'ename':'ashu',
               'esal':1000}
    resp ='<h1>employee no:{}employee name:{} ' \
          'employee salary:{}</h1>'.format(emp_data['eno'],emp_data['ename'],emp_data['esal'])
    return HttpResponse(resp)


import json
def emp_data_jsonview(request):
    emp_data={ 'eno':200,
               'ename':'ashutosh',
               'esal':1000}

    json_data=json.dumps(emp_data)
    return HttpResponse(json_data,content_type='application/json')

from django.http import JsonResponse
def emp_data_jsonview2(request):
    emp_data={ 'eno':300,
               'ename':'ash',
               'esal':1000}

    return JsonResponse (emp_data)

#function based view...above 3 ways of json format
###################################################################################################################
# class based view
# from django.views.generic import View
# class jsoncbv(View):
#     def get(self,request,*args,**kwrgs):
#         emp_data={'eno':501,'ename':'ashutosh','esal':57000}
#         return JsonResponse(emp_data,content_type='application/json')

from django.views.generic import View
from app1.mixin import HttpResponseMixin
class jsoncbv(HttpResponseMixin,View):        #2 parent class
    def get(self,request,*args,**kwrgs):
        json_data=json.dumps({'msg':'this is from get method'})
        return self.render_to_http_response(json_data)   #this is for mixin

    def post(self,request,*args,**kwrgs):
        json_data=json.dumps({'msg':'this is from post method'})
        return self.render_to_http_response(json_data)

    def put(self,request,*args,**kwrgs):
        json_data=json.dumps({'msg':'this is from put method'})
        return HttpResponse(json_data,content_type='application/json')

    def delete(self,request,*args,**kwrgs):
        json_data=json.dumps({'msg':'this is from delete method'})
        return HttpResponse(json_data,content_type='application/json')



















