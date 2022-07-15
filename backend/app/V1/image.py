from flask.views import MethodView
from . import b_image

class ImageView(MethodView):
    # 获取图片信息,返回图片缩略图和图片名称
    def get(self):
        pass
    
    # 下载图片接口
    def post(self):
        pass

    def put(self):
        pass

b_image.add_url_rule('img/',view_func=ImageView.as_view('img'))