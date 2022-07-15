#测试传统路由
from flask import app
from flask.globals import request
from flask.json import jsonify


# 测试路由
@app.route('/test', methods=['GET, POST'])
def test():
    if request.method == 'POST':
        data = request.get_data()
        print('post参数为：', data)

        return jsonify({'code': 200, 'data': data})
    if request.method == 'GET':
        data = request.url.get('data')
        print('url参数为：', data)

        return jsonify({'code': 200, 'data': data})