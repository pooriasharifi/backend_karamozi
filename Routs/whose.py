from datetime import date
import sys
# from model.comment import Comment
import pandas as pd
from model.user import Users, Comment
sys.path.append('../')
from flask import Flask,blueprints,request,make_response
# from model.user import User
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
                # print(content['comment'])
                user_obj=Comment(
                    comment=content['comment'],
                    date=content['date'],
                    timer=content['timer']
                    
                )
                user.comments.append(user_obj)
                user.save()

                for item in user.comments:
                    print(item.comment)
                # user.comments.append(
                #         comment=content['comment'],
                #         date=content['date']
                # )
                # user.save()
                return make_response({"status":200,"message":"success"})
        # whosing=whose_ostad(
        #     sign=content['sign'],
        #     username=content['username'],
        # )
        # whosing.save()



        # user id fetch
        # by username fetch user
        # in user.comment append comment
        #user.save

    except Exception as e:
        return make_response(print(e),400)