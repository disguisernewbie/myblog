from flask.views import MethodView
from . import b_video

# 视频视图
class VideoView(MethodView):

    def get(self):
        pass

    def post(self):
        pass

b_video.add_url_rule('video/', view_func=VideoView.as_view('video'))
