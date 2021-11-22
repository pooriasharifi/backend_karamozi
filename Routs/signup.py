from os import name
import sys

from mongoengine import errors
sys.path.append('../')
from flask import Blueprint,make_response,request
from model.user import Users
from model.ostad import Ostad


signup=Blueprint('signup',__name__)



@signup.route('/signup',methods=['POST'])
def user_signup():
    try:
        content=request.json
        user=Users(
            sarparast=content['sarparast'],
            username=content['username'],
            password=content['password'],
            ostad='هنوز انتخاب نکرده اید',
            kar_location=content['kar_location'],
            name=content['name'],
            verify=False,
            sign=1
            
        )
        user.save()
        return make_response({'message':'ثبت نام موفقیت آمیز','status':200})
    except errors.ValidationError as err:
        return make_response(err,504)
