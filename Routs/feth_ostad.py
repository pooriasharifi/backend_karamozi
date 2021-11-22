from os import name
import re
import sys
sys.path.append('../')
from flask import Blueprint,make_response,request
from model.user import Users
from model.ostad import Ostad
from helper.res_struct import res_str

fetchOstad=Blueprint('fetchOstad',__name__)


@fetchOstad.route('/fetchOstad/<username>',methods=['GET'])
def fetch_ostad(username):
    try:
        if not username:
            make_response({'message':'id is null','status':404})
        else:
            user=Users.objects(username=username).first()
            data_send=list()
            if not user:
                return make_response({'message':'user not found','status':400})
            ostad_obj=Ostad.objects()
            for item in ostad_obj:
                data_send.append(dict(
                    name=item.name,
                    sign=item.sign,
                ))
            return make_response(res_str('wait',data_send),200)
        return make_response('id is null',505)
    except OSError as e:
        return make_response(e,504)
        