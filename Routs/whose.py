from datetime import date
import sys
import pandas as pd
from model.user import Users, Comment
sys.path.append('../')
from flask import Flask,blueprints,request,make_response
from model.whose import whose_ostad
from helper.res_struct import res_str
from mongoengine import *


whose = blueprints.Blueprint('whose',__name__)


@whose.route('/whose/<username>',methods=['POST'])
def get_whose(username):
    print(username)
    try:
        content=request.json
        print(content)
        if not username:
            return make_response('id is null',404)
        else:
            user=Users.objects(username=username).first()
            print(user.name)
            if not user:
                return make_response('user not found',400)
            else:
                user_obj=Comment(
                    comment=content['comment'],
                    date=content['date'],
                    timer=content['timer']
                    
                )
                user.comments.append(user_obj)
                user.save()

                for item in user.comments:
                    print(item.comment)
                return make_response({"status":200,"message":"success"})




    except Exception as e:
        return make_response(print(e),400)
