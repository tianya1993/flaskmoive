#coding:utf8
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, FileField, TextAreaField, SelectField,SelectMultipleField
from wtforms.validators import DataRequired, ValidationError,EqualTo,Regexp,Email
from  app.models import   User
class RegisterviewForm(FlaskForm):
	name = StringField(
		label='昵称',
		validators = [
		             DataRequired("请输入昵称！")
	             ],
	  description = "昵称",
	 render_kw = {
		"class": "form-control",
		"placeholder": "请输入昵称！",
		#"required": "required"
	}
	)
	email = StringField(
		label='邮箱',
		validators=[
			DataRequired("请输入邮箱！"),
			Email("邮箱格式不正确！")
		],
		description="邮箱",
		render_kw={
			"class": "form-control",
			"placeholder": "请输入邮箱！",
		
		}
	
	)
	
	phone = StringField(
		label='手机',
		validators=[
			DataRequired("请输入手机！"),
			Regexp("1[ 34578]\\d[9]",message="号码格式不正确！")
		],
		description="手机",
		render_kw={
			"class": "form-control",
			"placeholder": "请输入手机！",
			#"required": "required"
		}
	
	)
	pwd = PasswordField(
		label='管理员密码',
		validators=[
			DataRequired("请输入管理员密码！")
		],
		description="管理员密码",
		render_kw={
			"class": "form-control",
			"placeholder": "请输入管理员密码！"
		}
	)
	repwd = PasswordField(
		label='确认管理员密码',
		validators=[
			DataRequired("请确认管理员密码！"),
			EqualTo('pwd', message="两次密码不一致！")
		],
		description="确认管理员密码",
		render_kw={
			"class": "form-control",
		
			"placeholder": "请输入确认管理员密码！",
			
		}
	)
	
	
	submit = SubmitField(
		"注册",
		render_kw={
			"class": "btn btn-primary",
		}
	
	)


class LoginForm(FlaskForm):
	"""登录表单"""
	name = StringField(
		label="账号",
		validators=[
			DataRequired("请输入账号！")
		],
		description="账号",
		render_kw={
			"class": "form-control",
			"placeholder": "请输入账号！",
			#"required": "required"
		}
	
	)
	pwd = PasswordField(
		label="密码",
		validators=[
			DataRequired("请输入密码！")
		],
		description="密码",
		render_kw={
			"class": "form-control",
			"placeholder": "请输入密码！",
			# "required": "required"
		}
	
	)
	submit = SubmitField(
		"登录",
		render_kw={
			"class": "btn btn-primary btn-block btn-flat",
		}
	
	)
class UserinfoView(FlaskForm):
	"""会员中心"""
	name = StringField(
		label='昵称',
		validators=[
			DataRequired("请输入昵称！")
		],
		description="昵称",
		render_kw={
			"class": "form-control",
			"placeholder": "请输入昵称！",
			# "required": "required"
		}
	)
	email = StringField(
		label='邮箱',
		validators=[
			DataRequired("请输入邮箱！"),
			Email("邮箱格式不正确！")
		],
		description="邮箱",
		render_kw={
			"class": "form-control",
			"placeholder": "请输入邮箱！",
			
		}
	
	)
	
	phone = StringField(
		label='手机',
		validators=[
			DataRequired("请输入手机！"),
			Regexp("1[ 34578]\\d[9]", message="号码格式不正确！")
		],
		description="手机",
		render_kw={
			"class": "form-control",
			"placeholder": "请输入手机！",
			# "required": "required"
		}
	
	)
	face = FileField(
		label='头像',
		
		validators=[
			DataRequired("请上传用户头像")
		],
		description="用户图片",
	
	)
	info = TextAreaField(
		label='简介',
		validators=[
			DataRequired("请输入会员简介！")
		],
		description="会员简介",
		render_kw={
			"class": "form-control",
			"id": "input_info",
			"rows": 10
		}
	)
	submit = SubmitField(
		"保存修改",
		render_kw={
			"class": "btn btn-success",
		}
	
	)
class  UserpwdView(FlaskForm):
	old_pass = PasswordField(
		label='旧密码',
		validators=[
			DataRequired("请输入旧密码")
		],
		description="旧密码",
		render_kw={
			"class": "form-control",
			"id": "input_title",
			"placeholder": "请输入旧密码！"
		}
	)
	new_pass = PasswordField(
		label='新密码',
		validators=[
			DataRequired("请输入新密码")
		],
		description="新密码",
		render_kw={
			"class": "form-control",
			"id": "input_title",
			"placeholder": "请输入新密码！"
		}
	)
	submit = SubmitField(
		"修改",
		render_kw={
			"class": "btn btn-primary",
		}
	
	)
	"""
	def  validate_old_pass(self,field):
		from  flask import   session
		pwd = field.data
		name = session["admin"]
		admin = Admin.query.filter_by(
			name=name
		).first()
		if not admin.check_pwd(pwd):
			raise  ValidationError("旧密码错误！")
	"""
	
	def validate_old_pass(self, field):
		from flask import session
		pwd = field.data
		name = session["user"]
		user= User.query.filter_by(
			name=name
		).first()
		if not user.check_pwd(pwd):
			raise ValidationError("旧密码错误！")
		
class  CommentForm(FlaskForm):
	content = TextAreaField(
		label='评论内容',
		validators=[
			DataRequired("请输评论内容")
		],
		description="请输入内容！",
		render_kw={
			"id": "input_content"
		}
	)
	submit = SubmitField(
		"提交",
		render_kw={
			"class": "btn btn-success",
			'id':'btn-sub'
		}
	
	)