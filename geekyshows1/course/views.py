from django.shortcuts import render
from django.http import HttpResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status as stus
from .serializers import *
from .queries import *
from rest_framework.decorators import api_view , permission_classes , authentication_classes
import MySQLdb

def learn_django(request):
    return HttpResponse('<h1>Hello Django</h1>')

def learn_python(request):
    return HttpResponse('<h1>Hello Python Learners</h1>')

@api_view(['GET','POST'])
def index_f(request):
    courses={
        'course' : 'python',
        'learn' : ['flask','django','python'],
        'course_provider' : 'scalar'
    }
    if request.method == 'GET':
        print('You hit a get method')
        return Response(courses)
    elif request.method == 'POST':
        print("you hit a POST method")
        return Response(courses)

@api_view(['POST'])
def teste_f(request):
    testing = {
        'tester' : 'kushagra',
        'perforance' : 'robust',
        'skillset' : 'excellent'
    }
    return Response(testing)

@api_view(['POST'])
def abc(request):
    serializer = EmployeeDetails(data=request.data)
    if serializer.is_valid():
        ep_id = serializer.data["ep_id"]
        emp_designation = serializer.data["emp_designation"]
        e_age = serializer.data["e_age"]
        e_skills = serializer.data["e_skills"]
        e_softskills = serializer.data["e_softskills"]
        insert = insert_q(ep_id,emp_designation,e_age,e_skills,e_softskills)
        if insert:
            json_response = {
            "status_code":200,
            "status":"SUCCESS",
            "data":"",
            "message":"DATA INSERTED"
            }
            return Response(json_response,status=stus.HTTP_200_OK)
        else:
            json_response = {
            "status_code":400,
            "status":"FAILED",
            "data":"",
            "message":"DATA NOT INSERTED"
            }
            return Response(json_response,status=stus.HTTP_400_BAD_REQUEST)
    else:
        json_data = {
                'status_code': 300,
                'status': 'Fail',
                'Reason': serializer.errors,
                'Remark': 'Send valid data'
            }
        return Response(json_data)
    
@api_view(['POST'])
def kush(request):
    serializer = Kushdetails(data=request.data)
    if serializer.is_valid():
        kush_id = serializer.data["kush_id"]
        kush_name = serializer.data["kush_name"]
        kush_designation = serializer.data["kush_designation"]
        kush_mob = serializer.data["kush_mob"]
        insert1 = insert_q1(kush_id,kush_name,kush_designation,kush_mob)
        if insert1:
            json_response = {
            "status_code":200,
            "status":"SUCCESS",
            "data":"",
            "message":"DATA INSERTED"
            }
            return Response(json_response,status=stus.HTTP_200_OK)
        else:
            json_response = {
            "status_code":400,
            "status":"FAILED",
            "data":"",
            "message":"DATA NOT INSERTED"
            }
            return Response(json_response,status=stus.HTTP_400_BAD_REQUEST)
    else:
        json_data = {
                'status_code': 300,
                'status': 'Fail',
                'Reason': serializer.errors,
                'Remark': 'Send valid data'
            }
        return Response(json_data)
    
@api_view(['POST'])
def shiva(request):
    serializer = shivadetails(data=request.data)
    if serializer.is_valid():
        shiva_name = serializer.data["shiva_name"]
        shiva_designation = serializer.data["shiva_designation"]
        insert2 = insert_q2(shiva_name,shiva_designation)
        if insert2:
            json_response = {
            "status_code":200,
            "status":"SUCCESS",
            "data":"",
            "message":"DATA INSERTED"
            }
            return Response(json_response,status=stus.HTTP_200_OK)
        else:
            json_response = {
            "status_code":400,
            "status":"FAILED",
            "data":"",
            "message":"DATA NOT INSERTED"
            }
            return Response(json_response,status=stus.HTTP_400_BAD_REQUEST)
    else:
        json_data = {
                'status_code': 300,
                'status': 'Fail',
                'Reason': serializer.errors,
                'Remark': 'Send valid data'
            }
        return Response(json_data)
          
        

@api_view(['POST'])
def testupdatefunction(request):
    serializer = updateserializer(data = request.data)
    if serializer.is_valid():
        id = serializer.data["kush_id"]
        OldData = testFetch(id)
        print(id)
        print(OldData)
       
        data = {
            "kush_name": serializer.data['kush_name'] if serializer.data['kush_name'] else OldData['kush_name'],
            "kush_designation": serializer.data['kush_designation'] if serializer.data['kush_designation'] else OldData['kush_designation'],
            "kush_mob": serializer.data['kush_mob'] if serializer.data['kush_mob'] else OldData['kush_mob'],
            'id': serializer.data['kush_id']
            }
        updateddata = updatetest(data.values())
        if updateddata:
            json_data = {
                    'status_code': 200,
                    'status': 'Success',
                    'data': '',
                    'message': 'Data updated successfully'
                }
            return Response(json_data, status=stus.HTTP_200_OK)
        else:
            json_data = {
                    'status_code': 200,
                    'status': 'Success',
                    'data': '',
                    'message': 'data not updated'
                }
        return Response(json_data, status=stus.HTTP_200_OK)
    else:
        json_data = {
                'status_code': 300,
                'status': 'Fail',
                'Reason': serializer.errors,
                'Remark': 'Send valid data'
            }
        return Response(json_data, status=stus.HTTP_300_MULTIPLE_CHOICES)
    
@api_view(['POST'])
def practiseupdatefunc(request):
    serializer = funcserializer(data = request.data)
    if serializer.is_valid():
        id = serializer.data["fun_id"]
        OldData = funcfetch(id)
        #print(OldData)

        data = {
            "fun_name": serializer.data['fun_name'] if serializer.data['fun_name'] else OldData['fun_name'],
            "fun_work": serializer.data['fun_work'] if serializer.data['fun_work'] else OldData['fun_work'],
            'id': serializer.data['fun_id']
            }
        updateddata = updatetest1(data.values())
        if updateddata:
            json_data = {
                    'status_code': 200,
                    'status': 'Success',
                    'data': '',
                    'message': 'Data updated successfully'
                }
            return Response(json_data, status=stus.HTTP_200_OK)
        else:
            json_data = {
                    'status_code': 200,
                    'status': 'Success',
                    'data': '',
                    'message': 'data not updated'
                }
        return Response(json_data, status=stus.HTTP_200_OK)
    else:
        json_data = {
                'status_code': 300,
                'status': 'Fail',
                'Reason': serializer.errors,
                'Remark': 'Send valid data'
            }
        return Response(json_data, status=stus.HTTP_300_MULTIPLE_CHOICES)
    
@api_view(['POST'])
def kushagrainsert(request):
    serializer = insertkushagra(data=request.data)
    if serializer.is_valid():
        sun_id = serializer.data["sun_id"]
        sun_name = serializer.data["sun_name"]
        sun_designation = serializer.data["sun_designation"]
        sun_mob = serializer.data["sun_mob"]
        insertkush = insert_kush(sun_id,sun_name,sun_designation,sun_mob)
        if insertkush:
            json_response = {
            "status_code":200,
            "status":"SUCCESS",
            "data":"",
            "message":"DATA INSERTED"
            }
            return Response(json_response,status=stus.HTTP_200_OK)
        else:
            json_response = {
            "status_code":400,
            "status":"FAILED",
            "data":"",
            "message":"DATA NOT INSERTED"
            }
            return Response(json_response,status=stus.HTTP_400_BAD_REQUEST)
    else:
        json_data = {
                'status_code': 300,
                'status': 'Fail',
                'Reason': serializer.errors,
                'Remark': 'Send valid data'
            }
        return Response(json_data)
    
@api_view(['POST'])
def abcinsert(request):
    serializer = abcserializer(data=request.data)
    if serializer.is_valid():
       
        murari_id = serializer.data["murari_id"]
        murari_name = serializer.data["murari_name"]
        murari_designation = serializer.data["murari_designation"]

        list=[murari_id,murari_name,murari_designation]
        
        insertmurari = insert_murari(list)
        
        if insertmurari:
            json_response = {
            "status_code":200,
            "status":"SUCCESS",
            "data":"",
            "message":"DATA INSERTED"
            }
            return Response(json_response,status=stus.HTTP_200_OK)
        else:
            json_response = {
            "status_code":400,
            "status":"FAILED",
            "data":"",
            "message":"DATA NOT INSERTED"
            }
            return Response(json_response,status=stus.HTTP_400_BAD_REQUEST)
    else:
        json_data = {
                'status_code': 300,
                'status': 'Fail',
                'Reason': serializer.errors,
                'Remark': 'Send valid data'
            }
        return Response(json_data)
    
@api_view(['POST'])
def testupdate(request):
    serializer = upserializer(data=request.data)
    try:
        if serializer.is_valid():
            id = serializer.data["up_id"]
            OldData = functfetch(id)
            data = {
                "up_name": serializer.data['up_name'] if serializer.data['up_name'] else OldData['up_name'],
                "up_designation": serializer.data['up_designation'] if serializer.data['up_designation'] else OldData['up_designation'],
                'id': serializer.data['up_id']
                }
            print("data",data)
            updateddata = updatetest2(data.values())
            if updateddata:
                json_data = {
                        'status_code': 200,
                        'status': 'Success',
                        'data': '',
                        'message': 'Data updated successfully'
                    }
                return Response(json_data, status=stus.HTTP_200_OK)
            else:
                json_data = {
                        'status_code': 200,
                        'status': 'Success',
                        'data': '',
                        'message': 'data not updated'
                    }
            return Response(json_data, status=stus.HTTP_200_OK)
        else:
            json_data = {
                    'status_code': 300,
                    'status': 'Fail',
                    'Reason': serializer.errors,
                    'Remark': 'Send valid data'
                }
            return Response(json_data, status=stus.HTTP_300_MULTIPLE_CHOICES)


    except Exception as e:
        json_data = {
                    'status_code': 300,
                    'status': 'Fail',
                    'Reason': f"{e}",
                    'Remark': 'Send valid data'
                }
        return Response(json_data, status=stus.HTTP_300_MULTIPLE_CHOICES)
    
@api_view(['POST'])
def fetchall(request):
        userData = []
        userData = datalist_q()
        if userData:
            json_data = {
                    'status_code': 200,
                    'status': 'Success',
                    'data': userData,
                    'message': 'Data fetched successfully'
                }
            return Response(json_data, status=stus.HTTP_200_OK)
        else:
                json_data = {
                    'status_code': 200,
                    'status': 'Success',
                    'data': [],
                    'message': 'data not fetched'
                }
                return Response(json_data, status=stus.HTTP_200_OK)
        
@api_view(['POST'])
def yash(request):
       userData1 = []
       userData1 = yashlist_q()
       if userData1:
            json_data = {
                    'status_code': 200,
                    'status': 'Success',
                    'data': userData1,
                    'message': 'Data fetched successfully'
                }
            return Response(json_data, status=stus.HTTP_200_OK)
       else:
                json_data = {
                    'status_code': 200,
                    'status': 'Success',
                    'data': [],
                    'message': 'data not fetched'
                }
                return Response(json_data, status=stus.HTTP_200_OK)
       
@api_view(['POST'])
def sam(request):
    userData2 = []
    userData2 = samlist_q()
    if userData2:
        json_data = {
                    'status_code': 200,
                    'status': 'Success',
                    'data': userData2,
                    'message': 'Data fetched successfully'
                }
        return Response(json_data, status=stus.HTTP_200_OK)
    else:
                json_data = {
                    'status_code': 200,
                    'status': 'Success',
                    'data': [],
                    'message': 'data not fetched'
                }
                return Response(json_data, status=stus.HTTP_200_OK)
    
@api_view(['POST'])
def tom (request):
    userData3 = []
    userData3 = tomlist_q()
    if userData3:
        json_data = {
                    'status_code': 200,
                    'status': 'Success',
                    'data': userData3,
                    'message': 'Data fetched successfully'
                }
        return Response(json_data, status=stus.HTTP_200_OK)
    else:
                json_data = {
                    'status_code': 200,
                    'status': 'Success',
                    'data': [],
                    'message': 'data not fetched'
                }
                return Response(json_data, status=stus.HTTP_200_OK)

@api_view(['POST'])
def raj(request):
     userdata4 = []
     userdata4 = rajquery_q()
     if userdata4:
        json_data = {
                    'status_code': 200,
                    'status': 'Success',
                    'data': userdata4,
                    'message': 'Data fetched successfully'
                }
        return Response(json_data, status=stus.HTTP_200_OK)
     else:
                json_data = {
                    'status_code': 200,
                    'status': 'Success',
                    'data': [],
                    'message': 'data not fetched'
                }
                return Response(json_data, status=stus.HTTP_200_OK)









        









    
