import sys
sys.path.append('../')
from flask import Blueprint,make_response,request
from model.user import *
from helper.res_struct import res_str

remove=Blueprint('remove',__name__)


@remove.route('/remove/<username>',methods=['POST'])
def remove_post(username):
    try:
        content=request.json
        user=Users.objects(username=username).update(
            set__verify=content['verify'],
            set__sign=content['sign'],
            set__ostad=content['ostad'],
        )
        # print(user.name)
        return make_response({'status':200,'message':'success'})
    except OSError as err:
        return make_response({'status':400,'message':err})
# from os import remove
# import sys
# sys.path.append('../')
# from flask import Blueprint,make_response,request
# from model.user import *
# from helper.res_struct import res_str

# remove=Blueprint('remove',__name__)


# @remove.route('/remove/<username>',methods=['POST'])
# def remove_post(username):
#     try:
#         content=request.json
#         user=Users.objects(username=username).update(
#             set__verify=content['verify']
#         )
#         # print(user.name)
#         return make_response({'status':200,'message':'success'})
#     except OSError as err:
#         return make_response({'status':400,'message':err})
