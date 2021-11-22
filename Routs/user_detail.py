from os import name
import sys
from model.ostad import Ostad
sys.path.append('../')
from model.user import Users
from flask import Blueprint,request,make_response
from helper.res_struct import res_str

detail = Blueprint('detail',__name__)

@detail.route('/detail/<username>',methods=['GET'])
def get_detail(username):
    print(username)
    try:
        if not username:
            return make_response('id is null',400)
        else:
            user = Users.objects(username=username).first()
            print(user.name)
            if not user:
                return make_response('internal server error',400)
            else:
                info=dict(
                kar_location=user.kar_location,
                name=user.name,
                sarparast=user.sarparast,
                ostad=user.ostad,
                verify=user.verify,
                )
                return make_response(res_str('wait',info),200)
        return make_response('id ',400)
    except OSError as err:
        return make_response('internal server error',400)