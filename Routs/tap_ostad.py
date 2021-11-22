import sys
sys.path.append('../')
from flask import Blueprint,make_response,request
from model.user import *
from helper.res_struct import res_str

ostadTap=Blueprint('ostadTap',__name__)


@ostadTap.route('/ostadTap/<username>',methods=['POST'])
def ostadTap_post(username):
    try:
        content=request.json
        user=Users.objects(username=username).update(
            set__verify=content['verify']
        )
        # print(user.name)
        return make_response({'status':200,'message':'success'})
    except OSError as err:
        return make_response({'status':400,'message':err})
