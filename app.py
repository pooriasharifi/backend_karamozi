# # from model.user import Users, Comment
from flask import Flask
from flask.helpers import make_response
from os import name
from mongoengine import connect

# from model.ostad import Ostad



from Routs.signin import signin
from Routs.user_detail import detail
from Routs.comment import comment
from Routs.ostad import ostad
from Routs.whose import whose
from Routs.ostadlist import asami
from Routs.verification import verification
from Routs.tap_ostad import ostadTap
from Routs.remove import remove
from Routs.second_req import secondreq
from Routs.feth_ostad import fetchOstad
from Routs.signup import signup
from Routs.hour import hour


DB_URI ="mongodb+srv://<>username:<password>@cluster0.t0eso.mongodb.net/myFirstDatabase?retryWrites=true&w=majority"



app = Flask(__name__)

connect(host=DB_URI)


app.register_blueprint(signin)
app.register_blueprint(detail)
app.register_blueprint(comment)
app.register_blueprint(ostad)
app.register_blueprint(whose)
app.register_blueprint(asami)
app.register_blueprint(verification)
app.register_blueprint(ostadTap)
app.register_blueprint(remove)
app.register_blueprint(secondreq)
app.register_blueprint(fetchOstad)
app.register_blueprint(signup)
app.register_blueprint(hour)

from model.user import Users




@app.route("/")
def home():
    return make_response('server is ready',200)


# ostad_obj=Ostad(
#     name='استاد مختاری',
#     username= 12345673,
#     password='1234567',
#     sign=10,
# ).save()






if __name__ == "__main__":
    app.run(host='0.0.0.0',port=5000, debug=True)

