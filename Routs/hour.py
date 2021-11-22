import sys
sys.path.append('../')
from flask import make_response,Blueprint,request
from model.user import  Users

hour=Blueprint('hour',__name__)


@hour.route('/hour/<username>',methods=['POST'])
def hour_post(username):
    try:
        content=request.json
        user=Users.objects(username=username).first()
        print(user.hour)
        return make_response({'status':'success','message':200},200)
    except OSError as err:
        return make_response({'status':'failed','message':err},400)