import sys
sys.path.append('../')
from flask import Blueprint,make_response,request
from model.user import Users
from helper.password import check_encrypted_password




signin = Blueprint('signin',__name__)

@signin.route('/signin',methods=['POST'])
def user_signin():
    try:
        content=request.json
        user=Users.objects(username=content['username']).first()
        if user:
            if user.password==content['password']:
                return make_response({"status":200,"message":"success",'username':user.username})
        return make_response({"status":400,"message":"نام کاربری یا رمز عبور اشتباه است"})
    except OSError as err:
        return make_response({"status":504,"message":'internal server error',"data":{}})