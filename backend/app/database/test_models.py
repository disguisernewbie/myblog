from app import db
from datetime import datetime

class BaseModel(object):
    """
    模型基类，为每个模型补充创建时间与更新时间
    """
    id = db.Column(db.Integer, primary_key=True)  # 主键id
    # 记录创建时间
    create_time = db.Column(db.DateTime, default=datetime.now)
    # 记录更新时间
    update_time = db.Column(db.DateTime, default=datetime.now, onupdate=datetime.now)

class User(db.Model, BaseModel):
    __tablename__ = "users"
    accounts = db.Column(db.String(20), unique=True, nullable=False)  # 账户
    password = db.Column(db.String(120), nullable=False)  # 密码
    name = db.Column(db.String(20), unique=True)  # 名称
    weight = db.Column(db.Integer, default=0)  # 权限

    # department_id = db.Column(db.Integer, db.ForeignKey('department.id'), nullable=False)  # 所属部门id
    # company_id = db.Column(db.Integer, db.ForeignKey('company.id'), nullable=False)  # 所属公司id
    #
    # orders = db.relationship('Orders', backref='users')  # 关联orders表
    # usersorders = db.relationship('UsersOrders', backref='users')  # 关联usersorders表