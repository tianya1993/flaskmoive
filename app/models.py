# coding:utf8


from datetime import datetime
from  app import  db


# 会员信息
class User(db.Model):
	__tablename__ = "user"
	id = db.Column(db.Integer, primary_key=True)  # 编号
	name = db.Column(db.String(100), unique=True)  # 昵称
	#login_name = db.Column(db.String(100), unique=True) #登录名
	#status =db.Boolean
	pwd = db.Column(db.String(100))  # 密码
	email = db.Column(db.String(100), unique=True)  # 邮箱
	phone = db.Column(db.String(11), unique=True)  # 手机号码
	info = db.Column(db.Text)  # 简介
	face = db.Column(db.String(255), unique=True)  # 头像
	addtime = db.Column(db.DateTime, index=True, default=datetime.now)  # 注册时间
	uuid = db.Column(db.String(255), unique=True)  # 唯一标识
	userlogs = db.relationship('Userlog', backref='user')  # 会员日志外键关系关联
	comments = db.relationship('Comment', backref='user')  # 评论外键关系关联
	moviecols = db.relationship('Moviecol', backref='user')  # 电影收藏信息
	
	def __repr__(self):
		return "<User %r>" % self.name
	def check_pwd(self,pwd):
		from  werkzeug.security import  check_password_hash
		return check_password_hash(self.pwd,pwd)


# 会员登录日志
class Userlog(db.Model):
	__tablename__ = "userlog"
	id = db.Column(db.Integer, primary_key=True)  # 编号
	user_id = db.Column(db.Integer, db.ForeignKey('user.id'))  # 所属会员
	ip = db.Column(db.String(100))  # IP
	addtime = db.Column(db.DateTime, index=True, default=datetime.now)  # 注册时间
	
	def __repr__(self):
		return "<Userlog %r>" % self.id


# 定义标签
class Tag(db.Model):
	__tablename__ = "tag"
	id = db.Column(db.Integer, primary_key=True)  # 编号
	name = db.Column(db.String(100), unique=True)
	addtime = db.Column(db.DateTime, index=True, default=datetime.now)  # 注册时间
	movies = db.relationship("Moive", backref='tag')  # 电影外键关联
	
	def __repr__(self):
		return "<Tag %r>" % self.name


class Moive(db.Model):
	__tablename__ = "moive"
	id = db.Column(db.Integer, primary_key=True)  # 编号
	title = db.Column(db.String(255), unique=True)  # 标题
	url = db.Column(db.String(255), unique=True)  # 地址
	info = db.Column(db.Text)  # 简介
	logo = db.Column(db.String(255), unique=True)  # 封面
	start = db.Column(db.SmallInteger)  # 星级
	playnum = db.Column(db.BigInteger)  # 播放数量
	commentnum = db.Column(db.BigInteger)
	tag_id = db.Column(db.Integer, db.ForeignKey('tag.id'))
	area = db.Column(db.String(255))
	release_time = db.Column(db.Date)
	length = db.Column(db.String(100))
	addtime = db.Column(db.DateTime, index=True, default=datetime.now)  # 添加时间
	comment = db.relationship("Comment", backref='moive')  # 电影评论外键关联
	moviecols = db.relationship('Moviecol', backref='moive')  # 电影收藏信息
	
	def __repr__(self):
		return "<Moive %r>" % self.title


# 上映预告模型
class Perview(db.Model):
	__tablename__ = "perview"
	id = db.Column(db.Integer, primary_key=True)  # 编号
	title = db.Column(db.String(255), unique=True)  # 标题
	logo = db.Column(db.String(255), unique=True)  # 封面
	addtime = db.Column(db.DateTime, index=True, default=datetime.now)  # 添加时间
	
	def __repr__(self):
		return "<Perview %r>" % self.title


class Comment(db.Model):
	__tablename__ = "comment"
	id = db.Column(db.Integer, primary_key=True)  # 编号
	content = db.Column(db.Text)  # 评论
	movie_id = db.Column(db.Integer, db.ForeignKey('moive.id'))
	user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
	addtime = db.Column(db.DateTime, index=True, default=datetime.now)  # 添加时间
	
	def __repr__(self):
		return "<omment %r>" % self.id


# 电影收藏
class Moviecol(db.Model):
	__tablename__ = "moviecol"
	id = db.Column(db.Integer, primary_key=True)  # 编号
	#content = db.Column(db.Text)  # 内容
	movie_id = db.Column(db.Integer, db.ForeignKey('moive.id'))
	user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
	addtime = db.Column(db.DateTime, index=True, default=datetime.now)  # 添加时间
	
	def __repr__(self):
		return "<Moviecol %r>" % self.id


# 权限
class Auth(db.Model):
	__tablename__ = "auth"
	id = db.Column(db.Integer, primary_key=True)  # 编号
	name = db.Column(db.String(100), unique=True)  # 名称
	url = db.Column(db.String(255), unique=True)  # 标题
	addtime = db.Column(db.DateTime, index=True, default=datetime.now)  # 添加时间
	
	def __repr__(self):
		return "<Auth %r>" % self.name


# 角色
class Role(db.Model):
	__tablename__ = "role"
	id = db.Column(db.Integer, primary_key=True)  # 编号
	name = db.Column(db.String(100), unique=True)  # 名称
	auths = db.Column(db.String(600), unique=True)  # 权限
	addtime = db.Column(db.DateTime, index=True, default=datetime.now)  # 添加时间
	admins = db.relationship("Admin", backref='role')  # 管理员外键关系关联
	
	def __repr__(self):
		return "<Role %r>" % self.name


# 管理员
class Admin(db.Model):
	__tablename__ = "admin"
	id = db.Column(db.Integer, primary_key=True)  # 编号
	name = db.Column(db.String(100), unique=True)  # 管理员账号
	pwd = db.Column(db.String(100))  # 管理员密码
	is_super = db.Column(db.SmallInteger)  # 是否为超级管理员，0 为超级管理员
	role_id = db.Column(db.Integer, db.ForeignKey('role.id'))
	addtime = db.Column(db.DateTime, index=True, default=datetime.now)  # 添加时间
	adminlogs = db.relationship('Adminlog', backref='admin')  # 管理员登录日志关联关系
	oplogs = db.relationship('Oplog', backref='admin')  # 管理员操作日志关联关系
	
	def __repr__(self):
		return "<Admin %r>" % self.name
	
	#定义密码验证
	def check_pwd(self,pwd):
		from  werkzeug.security import  check_password_hash
		return check_password_hash(self.pwd,pwd)



# 登录日志


class Adminlog(db.Model):
	__tablename__ = "adminlog"
	id = db.Column(db.Integer, primary_key=True)  # 编号
	admin_id = db.Column(db.Integer, db.ForeignKey('admin.id'))  # 所属会员
	ip = db.Column(db.String(100))  # IP
	addtime = db.Column(db.DateTime, index=True, default=datetime.now)  # 注册时间
	
	def __repr__(self):
		return "<Adminlog %r>" % self.id


# 操作日志
class Oplog(db.Model):
	__tablename__ = "oplog"
	id = db.Column(db.Integer, primary_key=True)  # 编号
	admin_id = db.Column(db.Integer, db.ForeignKey('admin.id'))  # 所属管理员
	ip = db.Column(db.String(100))  # 登录IP
	reason = db.Column(db.String(600))  # 操作原因
	addtime = db.Column(db.DateTime, index=True, default=datetime.now)  # 注册时间
	
	def __repr__(self):
		return "<Oplog %r>" % self.id


if __name__ == "__main__":
	#db.create_all()
	
	"""
	#初始化管理员
	role =Role(
		name="普通管理员",
		auths=""
	)
	db.session.add(role)
	db.session.commit()
	"""
	"""
	from werkzeug.security import generate_password_hash
	
	admin = Admin(
		name="admin",
		pwd=generate_password_hash("admin"),
		is_super=0,
		role_id=1
	
	)
	db.session.add(admin)
	db.session.commit()
"""
	"""
	from werkzeug.security import generate_password_hash
	userinfo = User(
		name='userinfo2',
		pwd =generate_password_hash('userinfo'),
		email='146153506@qq.com',
		phone='18393358060',
		info="非常喜欢编程语言11",
		face="201805060201143c410569ac9d428f999e3a0730cb4201.png",
		
	)
	db.session.add(userinfo)
	db.session.commit()
	"""