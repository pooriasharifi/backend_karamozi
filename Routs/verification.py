import sys
sys.path.append('../')
from flask import Blueprint,make_response
from model.user import Users
from model.ostad import Ostad
from helper.res_struct import res_str
from mongoengine import *


verification=Blueprint('verification',__name__)

@verification.route('/verification/<username>',methods=['GET'])
def verification_get(username):
    try:
        if not username:
            make_response({"message":"id is null","status":400},400)
        else:
            ostad_obj=Ostad.objects(username=username).first()
            ostad_send=list()
            print(ostad_obj.name)
            print(ostad_obj.sign)
            if not ostad_obj:
                return make_response({"message":"ostad not found","status":404},404)
            else:
                user_obj=Users.objects(sign=ostad_obj.sign, verify=False)
                # print(user_obj.username)
                if not user_obj:
                    return make_response({"message":"user not found","status":404},404)
                for item in user_obj:
                    print(item.username)
                #     if iteme.verify==True:
                #         if item.sign==ostad_obj.sign:
                    ostad_send.append(dict(
                        name=item.name,
                        username=item.username,
                    ))
                # print(ostad_send)
                return make_response(res_str('wait',ostad_send),200)
        return make_response('id is null',504)
    except OSError as err:
        return make_response(err,500)

    









    #     user_ostad=Ostad.objects(username=username).first()
    #     user_list=Users.objects()
    #     res_data=list()
    #     for item in user_list:
    #         if item.verify==True:
    #             if item.sign==user_ostad.sign:

    #                print(item.sign)
    #                list_temp=dict(
    #                name=item.name,
    #                username=item.username,
    #             )
    #             res_data.append(list_temp)
    #     return make_response(res_str('wait',res_data),200)
    # except OSError as err:
    #     return make_response('internal server error',400)


















# import sys
#
# from model.ostad import Ostad
# sys.path.append('../')
# from flask import Blueprint,make_response
# from model.user import *
# from model.ostad import *
# from helper.res_struct import res_str
#
# verification=Blueprint('verification',__name__)
#
# @verification.route('/verification/<username>',methods=['GET'])
# def verification_get(username):
#     try:
#         if not username:
#             make_response({"message":"id is null","status":400},400)
#         else:
#             ostad_obj=Ostad.objects(username=username).first()
#             ostad_send=list()
#             # print(ostad_obj.name)
#             if not ostad_obj:
#                 return make_response({"message":"ostad not found","status":404},404)
#             else:
#                 user_obj=Users.objects(sign=ostad_obj.sign, verify=False)
#                 if not user_obj:
#                     return make_response({"message":"user not found","status":404},404)
#                 for item in user_obj:
#                 #     if iteme.verify==True:
#                 #         if item.sign==ostad_obj.sign:
#                     ostad_send.append(dict(
#                         name=item.name,
#                         username=item.username,
#                     ))
#                 # print(ostad_send)
#                 return make_response(res_str('wait',ostad_send),200)
#         return make_response('id is null',504)
#     except OSError as err:
#         return make_response(err,500)