from flask.views import MethodView
from flask import request
from flask import jsonify
from app.utils.tools import jwt_auth
from . import b_user
from app.database.models import *

class UserView(MethodView):
    """用户视图"""
    @jwt_auth
    def get(self):
        print('xxxxxxxxx')
        account = request.args.get('account', None)
        password = request.args.get('password', None)
        level = request.args.get('level', None)
        print('???????', request.args)
        users = User.query.all()
        data = {
            'account': account+'ssssssssssss',
            'password': password,
            'level': level
        }
        return jsonify({'code': 200, 'msg': '登录接口', 'data': data, 'args': request.args})
    
    def post(self):
        pass

    def put(self):
        pass

    def delete(self):
        pass

b_user.add_url_rule('guest/', view_func=UserView.as_view('guest'))
