from django.db import connection , connections
from .helper import dictfetchone, dictfetchall


def insert_q(ep_id,emp_designation,e_age,e_skills,e_softskills):
    with connections["default"].cursor() as cursor:
        resp = cursor.execute("""INSERT into kushagra (ep_id,emp_designation,e_age,e_skills,e_softskills)
        values (%s,%s,%s,%s,%s)""",[ep_id,emp_designation,e_age,e_skills,e_softskills])
    return resp

def insert_q1(kush_id,kush_name,kush_designation,kush_mob):
    with connections["default"].cursor() as cursor:
        resp = cursor.execute("""INSERT into test (kush_id,kush_name,kush_designation,kush_mob)
        values (%s,%s,%s,%s)""",[kush_id,kush_name,kush_designation,kush_mob])
    return resp

def insert_q2(shiva_name,shiva_designation):
    with connections["default"].cursor() as cursor:
        resp = cursor.execute("""INSERT into shivaay (shiva_name,shiva_designation)
        values (%s,%s)""",[shiva_name,shiva_designation])
    return resp

def updatetest(data):
    with connections['default'].cursor() as cursor:
        resp = cursor.execute("""update test
        set  kush_name = %s, kush_designation = %s, kush_mob = %s
        where kush_id = %s ;""", data)
    return resp

def testFetch(id):
    with connections['default'].cursor() as cursor:
        resp = cursor.execute(f""" SELECT kush_name,kush_designation,kush_mob FROM test where kush_id='{id}'
       """)
        if resp and cursor.rowcount:
            resp = dictfetchone(cursor)
        else:
            resp = None
    return resp

def funcfetch(id):
    with connections['default'].cursor() as cursor:
        resp = cursor.execute(f""" SELECT fun_name,fun_work FROM func_2 where fun_id='{id}'
       """)
        if resp and cursor.rowcount:
            resp = dictfetchone(cursor)
        else:
            resp = None
    return resp

def updatetest1(data):
    with connections['default'].cursor() as cursor:
        resp = cursor.execute("""update func_2
        set  fun_name = %s, fun_work = %s where fun_id = %s""", data)
    return resp

def insert_kush(sun_id,sun_name,sun_designation,sun_mob):
    with connections["default"].cursor() as cursor:
        resp = cursor.execute("""INSERT into kushagra (sun_id,sun_name,sun_designation,sun_mob)
        values (%s,%s,%s,%s)""",[sun_id,sun_name,sun_designation,sun_mob])
    return resp

def insert_murari(list):
    with connections["default"].cursor() as cursor:
        resp = cursor.execute("""INSERT into murari (murari_id,murari_name,murari_designation)
        values (%s,%s,%s)""",list)
    return resp


def functfetch(id):
    with connections['default'].cursor() as cursor:
        resp = cursor.execute(f""" SELECT up_id,up_name,up_designation FROM up where up_id='{id}'
       """)
        if resp and cursor.rowcount:
            resp = dictfetchone(cursor)
        else:
            resp = None
    return resp

def updatetest2(data):
    with connections['default'].cursor() as cursor:
        resp = cursor.execute("""update up
        set  up_name = %s, up_designation = %s where up_id = %s""", data)
    return resp

def datalist_q():
    with connections["default"].cursor() as cursor:
        resp = cursor.execute(f"""SELECT id,name,designation,skills FROM xyz order by id desc;""")
        if resp and cursor.rowcount:
            # resp = dictfetchall(cursor) // for get all table
            resp = dictfetchall(cursor)
        else: 
            resp = None
    return resp

def yashlist_q():
    with connections["default"].cursor() as cursor:
        resp = cursor.execute(f"""SELECT joy_id,joy_name,joy_designation FROM joy order by joy_id desc;""")
        if resp and cursor.rowcount:
            # resp = dictfetchall(cursor) // for get all table
            resp = dictfetchall(cursor)
        else: 
            resp = None
    return resp

def samlist_q():
    with connections["default"].cursor() as cursor:
        resp = cursor.execute(f"""SELECT sam_id,sam_name,sam_designation,sam_school FROM sam order by sam_id desc;""")
        if resp and cursor.rowcount:
            # resp = dictfetchall(cursor) // for get all table
            resp = dictfetchall(cursor)
        else: 
            resp = None
    return resp

def tomlist_q():
    with connections["default"].cursor() as cursor:
        resp = cursor.execute(f"""SELECT tom_id,tom_name,tom_designation,tom_doc FROM tom order by tom_id desc;""")
        if resp and cursor.rowcount:
            # resp = dictfetchall(cursor) // for get all table
            resp = dictfetchone(cursor)
        else: 
            resp = None
    return resp

def rajquery_q():
    with connections["default"].cursor() as cursor:
        resp = cursor.execute(f"""SELECT raj_id,raj_name,raj_work FROM raj order by raj_id desc;""")
        if resp and cursor.rowcount:
            # resp = dictfetchall(cursor) // for get all table
            resp = dictfetchall(cursor)
        else: 
            resp = None
    return resp

       






    