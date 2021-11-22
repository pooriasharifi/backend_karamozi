import sys
import mongoengine
sys.path.append('../')
from model.user import Users, Comment
# from model.comment import Comment
from flask import Blueprint, request, Flask,make_response
from helper.res_struct import res_str


comment = Blueprint('comment', __name__)

@comment.route('/comment/<username>', methods=['GET'])
def get_userComment(username):
    print(username)
    try:
        if not username:
            return make_response({"status":205,"message":"user id is null"})
        else:
            user=Users.objects(username=username).first()
            res_data=list()
            print(user.name)
            if not user:
                return make_response({"status":207,"message":"user not found"})
            else:
                res_data.append(dict(
                        sign=user.sign,
                        verify=user.verify
                    ))
                for item in user.comments:
                    # print(item.comment)
                    info=dict(
                        comment=item.comment,
                        date=item.date,
                        timer=item.timer,
                    )
                    # {'sign':user.sign,'verify':user.verify}
                    res_data.append(info)
                    
                    print(info)
                return make_response(res_str('wait',res_data),200)
        return make_response('id ',400)
    except OSError as err:
        return make_response('internal server error',504)
