# coding:utf8
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, FileField, TextAreaField, SelectField,SelectMultipleField
from wtforms.validators import DataRequired, ValidationError,EqualTo
from app.models import Admin, Moive,Tag,Auth,Role
tags = Tag.query.all()
auths_list= Auth.query.all()
roles =Role.query.all()

class LoginForm(FlaskForm):
	"""管理员登录表单"""
	account = StringField(
		label="账号",
		validators=[
			DataRequired("请输入账号！")
		],
		description="账号",
		render_kw={
			"class": "form-control",
			"placeholder": "请输入账号！",
			 "required":"required"
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
	
	def validate_account(self, field):
		account = field.data
		admin = Admin.query.filter_by(name=account).count()
		if admin == 0:
			raise ValidationError("账号不存在")


class TagForm(FlaskForm):
	name = StringField(
		label="名称",
		validators=[
			DataRequired("请输入标签！")
		],
		description="标签",
		render_kw={
			"class": "form-control",
			"id": "input_name",
			"placeholder": "请输入标签名称！"
		}
	)
	submit = SubmitField(
		"添加",
		render_kw={
			"class": "btn btn-primary",
		}
	
	)


class MoiveForm(FlaskForm):
	title = StringField(
		label='片名',
	validators = [
		DataRequired("请输入片名！")
	     ],
	 description = "电影片名",
	render_kw = {
		"class": "form-control",
		"id": "input_title",
		"placeholder": "请输入片名！"
	}
	)
	url = FileField(
		label='文件',
	validators = [
		DataRequired("请上传文件")
	    ],
	description = "文件",
	
	)
	info = TextAreaField(
		label='简介',
	validators = [
		DataRequired("请输入简介！")
	    ],
	description = "简介",
	render_kw = {
		"class": "form-control",
		"id": "input_info",
		"rows": 10
	}
	
	)
	
	
	logo = FileField(
		label='封面',
	validators = [
		DataRequired("请上传封面图片")
	    ],
	description = "封面图片",
	
	)
	start = SelectField(
		label='星级',
	validators = [
		DataRequired("请选择星级")
	    ],
	coerce = int,
	choices = [(1, "1星"), (2, "2星"), (3, "3星"), (4, "4星"), (5, "5星")],
	description = "星级",
	render_kw = {
		"class": "form-control",
	}
	
	)
	
	tag_id =SelectField(
		label='标签',
	validators = [
		DataRequired("请选择标签")
	    ],
	coerce = int,
	choices = [(v.id,v.name) for v in tags],
	description = "标签类别",
	render_kw = {
		"class": "form-control",
	}
	)
	
	area = StringField(
		label='地区',
		validators=[
			DataRequired("请输入地区！")
		],
		description="地区名",
		render_kw={
			"class": "form-control",
			"placeholder": "请输入地区名！"
		}
	)
	length = StringField(
		label='片长',
		validators=[
			DataRequired("请输入片长！")
		],
		description="片长",
		render_kw={
			"class": "form-control",
			"placeholder": "请输入片长！"
		}
	)
	release_time = StringField(
		label='上映时间',
		validators=[
			DataRequired("请输入上映时间！")
		],
		description="上映时间",
		render_kw={
			"class": "form-control",
			'id':'input_release_time',
			"placeholder": "请选择上映时间！"
		}
	)
	submit = SubmitField(
		"添加",
		render_kw={
			"class": "btn btn-primary",
		}
	
	)
	
#添加预告
class  PreviewForm(FlaskForm):
	title=StringField(
		label='预告标题',
	validators = [
		DataRequired("请输入预告标题！")
	     ],
	 description = "预告标题",
	render_kw = {
		"class": "form-control",
		"id": "input_title",
		"placeholder": "请输入片名！"
	}
	)
	logo = FileField(
		label='预告封面',
		validators=[
			DataRequired("请上传封面图片")
		],
		description="预告封面图片"
		
	)
	submit = SubmitField(
		"添加",
		render_kw={
			"class": "btn btn-primary",
		}
	
	)
class ChangepwdView(FlaskForm):
	old_pass = PasswordField(
		label='旧密码',
	validators = [
		     DataRequired("请输入旧密码")
	             ],
	 description = "旧密码",
	render_kw = {
		"class": "form-control",
		"id": "input_title",
		"placeholder": "请输入旧密码！"
	}
	)
	new_pass = PasswordField(
		label='新密码',
	validators = [
		             DataRequired("请输入新密码")
	             ],
	description = "新密码",
	render_kw = {
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
		name = session["admin"]
		admin = Admin.query.filter_by(
				name=name
			).first()
		if not admin.check_pwd(pwd):
			raise ValidationError("旧密码错误！")
		
class AuthForm(FlaskForm):
	name = StringField(
		label='权限名称',
		validators=[
			DataRequired("请输入权限名称！")
		],
		description="权限名称",
		render_kw={
			"class": "form-control",
			"id": "input_title",
			"placeholder": "请输入权限名称！"
		}
	)
	url = StringField(
		label='权限地址',
		validators=[
			DataRequired("请输入权限地址！")
		],
		description="权限地址",
		render_kw={
			"class": "form-control",
			"id": "input_title",
			"placeholder": "请输入权限地址！"
		}
	)
	submit = SubmitField(
		"添加",
		render_kw={
			"class": "btn btn-primary",
		}
	
	)


class RoleForm(FlaskForm):
	name = StringField(
		label='角色名称',
		validators=[
			DataRequired("请输入角色名称！")
		],
		description="角色名称",
		render_kw={
			"class": "form-control",
			"id": "input_title",
			"placeholder": "请输入角色名称！"
		}
	)
	auths = SelectMultipleField(
		label='操作权限',
		validators=[
			DataRequired("请选择操作权限！")
		],
		coerce=int,
		
		choices=[(v.id, v.name) for v in auths_list],
		description="操作权限",
		render_kw={
			"class": "form-control",
		}
	)
	submit = SubmitField(
		"添加",
		render_kw={
			"class": "btn btn-primary",
		}
	
	)
class  AddadminForm(FlaskForm):
	name = StringField(
		label='管理员名称',
		validators=[
			DataRequired("请输入管理员名称！")
		],
		description="管理员名称",
		render_kw={
			"class": "form-control",
			"id": "input_title",
			"placeholder": "请输入管理员名称！"
		}
	)
	pwd =PasswordField(
	label='管理员密码',
	validators = [
		             DataRequired("请输入管理员密码！")
	             ],
	description = "管理员密码",
	render_kw = {
		"class": "form-control",
		"id": "input_title",
		"placeholder": "请输入管理员密码！"
	}
	)
	re_pwd = PasswordField(
		label='确认管理员密码',
		validators=[
			DataRequired("请确认管理员密码！"),
			EqualTo('pwd',message="两次密码不一致！")
		],
		description="确认管理员密码",
		render_kw={
			"class": "form-control",
			"id": "input_title",
			"placeholder": "请输入确认管理员密码！"
		}
	)
	
	role_id = SelectField(
		label='所属角色',
		validators=[
			DataRequired("---请选择所属角色!---")
		],
		coerce=int,
		choices=[(v.id, v.name) for v in roles],
		description="标签类别",
		render_kw={
			"class": "form-control",
		}
	)
	submit = SubmitField(
		"添加",
		render_kw={
			"class": "btn btn-primary",
		}
	
	)
