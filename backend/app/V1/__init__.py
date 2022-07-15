from flask import Blueprint

b_user = Blueprint('user', __name__)
b_image = Blueprint('image', __name__)
b_video = Blueprint('video', __name__)

from . import user, image, video