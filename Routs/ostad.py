import sys
sys.path.append('../')
from helper.res_struct import res_str
from flask.helpers import make_response
sys.path.append('../')
from flask import Flask,blueprints,request
from mongoengine import *
from model.ostad import Ostad

ostad = blueprints.Blueprint('ostad',__name__)

@ostad.route('/ostad',methods=['POST'])
def get_ostad():
    try:
        content=request.json
        user=Ostad.objects(username=content['username']).first()
        if user:
            if user.password==content['password']:
                return make_response({"status":200,"message":"success",'username':user.username,'sign':user.sign})
        return make_response(res_str(0,'نام کاربری یا رمز عبور اشتباه است'),200)
    except OSError as err:
        return make_response(res_str(0,str(err)),200)