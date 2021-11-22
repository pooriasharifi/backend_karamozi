import sys

from flask.blueprints import Blueprint
sys.path.append('../')
from flask import Flask, make_response,request,Blueprint
from model.user import Users
from model.ostad import Ostad


secondreq=Blueprint('secondreq',__name__)



@secondreq.route('/secondreq/<username>',methods=['POST'])
def second_req(username):
    try:
        content=request.json
        user=Users.objects(username=username).update(
            set__verify=False,
            set__sign=content['sign'],
            set__ostad=content['ostad']
        )
        return make_response({'status':200,'message':'success'})
    except OSError as err:
        return make_response({'status':504,'message':err})