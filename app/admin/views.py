# coding:utf8
from . import admin
from flask import render_template, redirect, url_for,flash,session,request,abort
from  app.admin.forms import  LoginForm,TagForm,MoiveForm,PreviewForm,ChangepwdView,AuthForm,RoleForm,AddadminForm
from  app.models import   Admin,Tag,Moive,Perview,Comment,User,Moviecol,Adminlog,Oplog,Userlog,Auth,Role
from  functools import  wraps
from  app import  db,app
from werkzeug.utils import  secure_filename
import   os
import   uuid
from datetime import datetime

#上下文应用处理器
@admin.context_processor
def tpl_extra():
	data = dict(
		online_time =datetime.now().strftime("%Y-%m-%d %H:%M:%S")
	)
	return   data




#登录装饰器
def admin_login_req(f):
	@wraps(f)
	def decorated_function(*args,**kwargs):
		if "admin" not in  session:
			return  redirect(url_for("admin.login",next=request.url))
		return  f(*args,**kwargs)
		
	return  decorated_function

#权限装饰器
def  admin_auth(f):
	@wraps(f)
	def decorated_function(*args,**kwargs):
		admin =Admin.query.join(
			Role
		).filter(
			Role.id == Admin.role_id,
			Admin.id ==session['admin_id']
			
		).first()
		auths = admin.role.auths
		auths = list(map(lambda v:int(v),auths.split(",")))
		auth_list = Auth.query.all()
		print(auth_list)
		urls = [v.url for v  in auth_list for val in auths if val == v.id]
		rule = request.url_rule
		print(urls,rule)
		if  str(rule)  not in urls:
			abort(404)
		
		
		return f(*args, **kwargs)
		
	return decorated_function


#更改文件名称
def change_filename(filename):
    fileinfo = os.path.splitext(filename)
    filename = datetime.now().strftime("%Y%m%d%H%M%S") + str(uuid.uuid4().hex) + fileinfo[-1]
    return filename




"""
#更改文件名称
def change_filename(filename):
	fileinfo = os.path.splitext(filename)
	filename = datetime.datetime.now().strftime("%Y%m%d%H%M%S")+str(uuid.uuid4().hex)+fileinfo[-1]
	return  filename
"""
@admin.route("/")
@admin_login_req

def index():
	return render_template("admin/index.html")


@admin.route("/login/",methods=["GET","POST"])

def login():
	form = LoginForm()
	if  form.validate_on_submit():
		data = form.data #获取表单数据
		admin = Admin.query.filter_by(name=data["account"]).first()
		if not  admin.check_pwd(data['pwd']):
			flash('密码错误！','err')
			return redirect(url_for("admin.login"))
		session["admin"]= data["account"]
		session['admin_id']= admin.id
		adminlog = Adminlog(
			admin_id = admin.id,
			ip = request.remote_addr
		)
		db.session.add(adminlog)
		db.session.commit()
		return  redirect(request.args.get("next")  or url_for("admin.index"))
	return render_template('admin/login.html',form=form)


@admin.route("/logout/")
@admin_login_req
def logout():
	session.pop("account",None) #删除session信息
	session.pop("admin_id",None)#删除管理员ID
	return redirect(url_for('admin.login'))  # 退出页面


@admin.route("/pwd/",methods=["POST","GET"])
@admin_login_req
def pwd():
	form = ChangepwdView()
	if form.validate_on_submit():
		data =form.data
		admin= Admin.query.filter_by(name=session['admin']).first()
		from  werkzeug.security import  generate_password_hash
		admin.pwd =generate_password_hash(data['new_pass'])
		db.session.add(admin)
		db.session.commit()
		flash("修改密码成功，请重新登录！","ok")
		oplog = Oplog(
			admin_id=session['admin_id'],
			ip=request.remote_addr,
			reason="%s用户修改密码成功！" % admin.name
		
		)
		db.session.add(oplog)
		db.session.commit()
		return  redirect(url_for("admin.login"))
		
	
	return render_template('admin/pwd.html',form=form)  # 修改密码页面


@admin.route("/userlist/<int:page>/")
@admin_login_req
@admin_auth
def userlist(page=None):
	if page is None:
		page = 1
	page_data = User.query.order_by(
		User.addtime.desc()
	).paginate(page=page, per_page=10)
	return render_template('admin/user_list.html',page_data=page_data)  # 用户列表页




#查看会员-列表页
@admin.route("/userview/<int:id>/")
@admin_login_req
@admin_auth
def userview(id=None):
	user= User.query.filter_by(id=id).first_or_404()
	
	
	return render_template('admin/user_view.html',user=user )


# 会员删除页面
@admin.route("/userdel/<int:id>/")
@admin_login_req
@admin_auth
def userdel(id=None):
	user = User.query.filter_by(id=id).first_or_404()
	db.session.delete(user)
	db.session.commit()
	flash("删除会员成功！", "ok")
	oplog = Oplog(
		admin_id=session['admin_id'],
		ip=request.remote_addr,
		reason="删除会员成功!%s" % user.name
	
	)
	db.session.add(oplog)
	db.session.commit()
	
	return redirect(url_for('admin.userlist',page=1))

# 添加标签页面
@admin.route("/addtag/",methods=["POST","GET"])
@admin_login_req
@admin_auth
def addtag():
	form   = TagForm()
	if  form.validate_on_submit():
		data = form.data
		tag = Tag.query.filter_by(name=data["name"]).count()
		if tag == 1:
			flash("标签已经存在",'err')
			return  redirect(url_for('admin.addtag'))
		tag = Tag(
			name=data['name']
		)
		db.session.add(tag)
		db.session.commit()
		flash("标签添加成功","ok")
		oplog =Oplog(
			admin_id = session['admin_id'],
			ip = request.remote_addr,
			reason = "添加标签%s" % data["name"]
			
		)
		db.session.add(oplog)
		db.session.commit()
		redirect(url_for("admin.addtag"))
		
		
	return render_template('admin/tag_add.html',form=form)


# 标签列表页面
@admin.route("/taglist/<int:page>/",methods=["GET"])
@admin_login_req
@admin_auth
def taglist(page=None):
	if page  is None:
		page = 1
	page_data = Tag.query.order_by(
		Tag.addtime.desc()
	).paginate(page=page,per_page=10)
	
	return render_template('admin/tag_list.html',page_data=page_data)

#标签删除
@admin.route("/tag/del/<int:id>/",methods=["GET"])
@admin_login_req
@admin_auth
def tag_del(id=None):
	tag = Tag.query.filter_by(id=id).first_or_404()
	db.session.delete(tag) #删除
	db.session.commit()
	flash("删除标签成功！", "ok")
	oplog = Oplog(
		admin_id=session['admin_id'],
		ip=request.remote_addr,
		reason="删除标签成功%s" % tag.name
	
	)
	db.session.add(oplog)
	db.session.commit()
	return  redirect(url_for("admin.taglist",page=1))
	
#编辑标签

@admin.route("/tag/edit/<int:id>/",methods=["GET","POST"])
@admin_login_req
@admin_auth
def tag_edit(id=None):
	form = TagForm()
	tag = Tag.query.get_or_404(id)
	if form.validate_on_submit():
		data =form.data
		tag_count = Tag.query.filter_by(name=data["name"]).count()
		if tag.name != data['name']  and   tag_count == 1:
			flash("标签已经存在", 'err')
			return redirect(url_for('admin.tag_edit',id=id))
		tag.name = data['name']
		db.session.add(tag)
		db.session.commit()
		flash("编辑标签成功！", "ok")
		oplog = Oplog(
			admin_id=session['admin_id'],
			ip=request.remote_addr,
			reason="编辑标签成功%s" % data['name']
		
		)
		db.session.add(oplog)
		db.session.commit()
		
		redirect(url_for('admin.tag_edit',id=id))
	return  render_template("admin/tag_edit.html",form=form,tag=tag)



# 添加电影页面
@admin.route("/addmovie/",methods=["GET","POST"])
@admin_login_req
@admin_auth
def movieadd():
	form = MoiveForm()
	if form.validate_on_submit():
		data = form.data
		#格式化文件名
		file_url = secure_filename(form.url.data.filename)
		file_logo = secure_filename(form.logo.data.filename)
		
		
		if not os.path.exists(app.config["UP_DIR"]):  # 判断目录是否存在
			os.makedirs(app.config["UP_DIR"])
			os.chmod(app.config["UP_DIR"], "rw")
		url = change_filename(file_url)
		logo = change_filename(file_logo)
	
		form.url.data.save(app.config["UP_DIR"] + url)
		form.logo.data.save(app.config["UP_DIR"] + logo)
			
		moive = Moive(
				title=data["title"],
				url=url,
				info=data["info"],
				logo=logo,
				start=int(data["start"]),
				tag_id=int(data["tag_id"]),
				playnum=0,
				commentnum=0,
				area=data["area"],
				length=data["length"],
				release_time=data["release_time"]
			)
		db.session.add(moive)
		db.session.commit()
		flash("电影添加成功!", "ok")
		oplog = Oplog(
			admin_id=session['admin_id'],
			ip=request.remote_addr,
			reason="添加电影成功%s" % data['title']
		
		)
		db.session.add(oplog)
		db.session.commit()
		
		return redirect(url_for("admin.movieadd"))
	
	return render_template('admin/movie_add.html', form=form)
	



# 电影列表页面
@admin.route("/movie/list/<int:page>/",methods=["GET"])
@admin_login_req
@admin_auth
def movielist(page=None):
	if page is None:
		page = 1
	page_data = Moive.query.join(Tag).filter(
		Tag.id == Moive.tag_id
	).order_by(
		Moive.addtime.desc()
	).paginate(page=page, per_page=10)
	
	return render_template('admin/movie_list.html',page_data=page_data)

#删除电影
@admin.route("/movie/del/<int:id>/",methods=["GET"])
@admin_login_req
@admin_auth
def moive_del(id=None):
	moive = Moive.query.filter_by(id=id).first_or_404()
	db.session.delete(moive) #删除
	db.session.commit()
	flash("删除电影成功！", "ok")
	oplog = Oplog(
		admin_id=session['admin_id'],
		ip=request.remote_addr,
		reason="删除电影成功%s" % moive.title
	
	)
	db.session.add(oplog)
	db.session.commit()
	return  redirect(url_for("admin.movielist",page=1))

#编辑电影oive_edit
@admin.route("/moiveedit/<int:id>/",methods=["GET","POST"])
@admin_login_req
@admin_auth
def moive_edit(id=None):
	form = MoiveForm()
	form.url.validators = []
	form.logo.validators = []
	moive = Moive.query.get_or_404(int(id))
	if  request.method == "GET":
		form.info.data = moive.info
		form.start.data = moive.start
		form.tag_id.data = moive.tag_id
		
	if form.validate_on_submit():
		data = form.data
		moive_count = Moive.query.filter_by(title=data["title"]).count()
		if moive.title != data['title'] and moive_count == 1:
			flash("电影已经存在！", 'err')
			return redirect(url_for('admin.moive_edit', id=id))
		
		if not os.path.exists(app.config["UP_DIR"]):  # 判断目录是否存在
			os.makedirs(app.config["UP_DIR"])
			os.chmod(app.config["UP_DIR"], "rw")
		
		
		
		if form.url.data !="":
			file_url = secure_filename(form.url.data.filename)
			moive.url = change_filename(file_url)
			form.url.data.save(app.config["UP_DIR"] + moive.url)
			
		if form.logo.data != "":
			file_logo = secure_filename(form.logo.data.filename)
			moive.logo = change_filename(file_logo)
			form.logo.data.save(app.config["UP_DIR"] + moive.logo)
		
		moive.title = data['title']
		moive.info  = data['info']
		moive.start = int(data['start'])
		moive.area = data['area']
		moive.length = data['length']
		moive.release_time = data["release_time"]
		moive.tag_id = int(data["tag_id"])
		db.session.add(moive)  # 删除
		db.session.commit()

		flash("电影修改成功!", "ok")
		oplog = Oplog(
			admin_id=session['admin_id'],
			ip=request.remote_addr,
			reason="编辑电影成功%s" % data['title']
		
		)
		db.session.add(oplog)
		db.session.commit()
		return redirect(url_for('admin.moive_edit', id=id))
	
	return render_template('admin/movie_edit.html', form=form,moive=moive)


# 预告管理-添加预告
@admin.route("/addpreview/", methods=["GET","POST"])
@admin_login_req
@admin_auth
def addpreview():
	form = PreviewForm()
	if form.validate_on_submit():
		data = form.data
		# 格式化文件名
		file_logo = secure_filename(form.logo.data.filename)
		if not os.path.exists(app.config["UP_DIR"]):  # 判断目录是否存在
			os.makedirs(app.config["UP_DIR"])
			os.chmod(app.config["UP_DIR"], "rw")
		logo = change_filename(file_logo)
		form.logo.data.save(app.config["UP_DIR"] + logo)
		
		perview = Perview(
			title=data["title"],
			logo=logo )
		db.session.add(perview)
		db.session.commit()
		flash("预告添加成功!", "ok")
		oplog = Oplog(
			admin_id=session['admin_id'],
			ip=request.remote_addr,
			reason="添加预告成功%s" % data['title']
		
		)
		db.session.add(oplog)
		db.session.commit()
		return redirect(url_for("admin.addpreview"))
	return render_template('admin/preview_add.html', form=form)



# 预告管理-预告列表
@admin.route("/previewlist/<int:page>/",methods=["GET"])
@admin_login_req
@admin_auth
def previewlist(page=None):
	if page is None:
		page = 1
	page_data = Perview.query.order_by(
		Perview.addtime.desc()
	).paginate(page=page, per_page=5)

	return render_template('admin/preview_list.html',page_data=page_data)
# 预告管理-预告删除
@admin.route("/previedel/<int:id>/",methods=["GET"])
@admin_login_req
@admin_auth
def previedel(id=None):
	perview = Perview.query.filter_by(id=id).first_or_404()
	db.session.delete(perview) #删除
	db.session.commit()
	flash("删除预告成功！", "ok")
	oplog = Oplog(
		admin_id=session['admin_id'],
		ip=request.remote_addr,
		reason="删除预告成功%s" % perview.name
	
	)
	db.session.add(oplog)
	db.session.commit()
	return  redirect(url_for("admin.previewlist",page=1))

# 预告管理-编辑
@admin.route("/previeedit/<int:id>/", methods=["GET", "POST"])
@admin_login_req
@admin_auth
def previeedit(id=None):
	form = PreviewForm()
	form.logo.validators = []
	perview = Perview.query.get_or_404(int(id))
	
	if form.validate_on_submit():
		data = form.data
		perview_count = Perview.query.filter_by(title=data["title"]).count()
		if perview.title != data['title'] and perview_count == 1:
			flash("电影预告已经存在！", 'err')
			return redirect(url_for('admin.previeedit', id=id))
		
		if not os.path.exists(app.config["UP_DIR"]):  # 判断目录是否存在
			os.makedirs(app.config["UP_DIR"])
			os.chmod(app.config["UP_DIR"], "rw")
	
		
		if form.logo.data != "":
			file_logo = secure_filename(form.logo.data.filename)
			perview.logo = change_filename(file_logo)
			form.logo.data.save(app.config["UP_DIR"] + perview.logo)
			
		perview.title = data['title']
		db.session.add(perview)
		db.session.commit()
		
		flash("预告编辑成功!", "ok")
		#操作日志
		oplog = Oplog(
			admin_id=session['admin_id'],
			ip=request.remote_addr,
			reason="编辑预告成功%s" % data['title']
		)
		db.session.add(oplog)
		db.session.commit()
		return redirect(url_for('admin.previeedit', id=id))
	
	return render_template('admin/previe_edit.html', form=form, perview=perview)





# 收藏管理
@admin.route("/moviecollist/<int:page>/",methods=["GET", "POST"])
@admin_login_req
@admin_auth
def moviecollist(page=None):
	if page is None:
		page = 1
	page_data = Moviecol.query.order_by(
		Moviecol.addtime.desc()
	).paginate(page=page, per_page=10)
	return render_template('admin/moviecol_list.html',page_data=page_data)

# 收藏管理--删除
@admin.route("/moviecoldel/<int:id>/",methods=["GET", "POST"])
@admin_login_req
@admin_auth
def moviecoldel(id=None):
	moivecol= Moviecol.query.filter_by(id=id).first_or_404()
	db.session.delete(moivecol)
	db.session.commit()
	flash("删除收藏成功！", "ok")
	# 操作日志
	oplog = Oplog(
		admin_id=session['admin_id'],
		ip=request.remote_addr,
		reason="删除收藏成功ID编号为%s，收藏用户为%s" % (moivecol.movie_id,moivecol.user_id)
	)
	db.session.add(oplog)
	db.session.commit()
	
	return redirect(url_for("admin.moviecollist",page=1))
# 评论列表
@admin.route("/commentlist/<int:page>/",methods=["GET"])
@admin_login_req
@admin_auth
def commentlist(page=None):
	if page is None:
		page = 1
	page_data = Comment.query.order_by(
		Comment.addtime.desc()
	).paginate(page=page, per_page=10)
	
	return render_template('admin/comment_list.html',page_data=page_data)

# 评论列表-删除
@admin.route("/commendel/<int:id>/", methods=["GET","POST"])
@admin_login_req
@admin_auth
def commentdel(id=None):
	comment =Comment.query.filter_by(id=id).first_or_404()
	db.session.delete(comment)
	db.session.commit()
	flash("删除评论成功！", "ok")
	# 操作日志
	oplog = Oplog(
		admin_id=session['admin_id'],
		ip=request.remote_addr,
		reason="删除评论ID编号为%s，评论内容为%s" %(comment.id,comment.content)
	)
	db.session.add(oplog)
	db.session.commit()
	
	return redirect(url_for('admin.commentlist',page=1))





# 日志管理-操作日志
@admin.route("/oplog/<int:page>/",methods=["GET"])
@admin_login_req
@admin_auth
def oplog(page=None):
	if page is None:
		page = 1
	page_data = Oplog.query.join(Admin).filter(
		Admin.id ==Oplog.admin_id,
	).order_by(
			Oplog.addtime.desc()
		).paginate(page=page, per_page=10)
	
	
	return render_template('admin/oplog_list.html',page_data=page_data)


# 日志管理-会员登录日志列表
@admin.route("/userloginlog/<int:page>/",methods=["GET"])
@admin_login_req
@admin_auth
def userloginlog(page=None):
	
	if page is None:
		page = 1
	page_data = Userlog.query.join(User).filter(
		User.id == Userlog.user_id
	).order_by(
			Userlog.addtime.desc()
		).paginate(page=page, per_page=10)
	
	return render_template('admin/userloginlog_list.html',page_data=page_data)


# 会员管理-管理员登录日志列表
@admin.route("/adminlog/<int:page>/",methods=['GET'])
@admin_login_req
@admin_auth
def adminlog(page=None):
	if page is  None:
		page=1
	page_data = Adminlog.query.order_by(
		Adminlog.addtime.desc()
	).paginate(page=page, per_page=10)
	
	return render_template('admin/adminloginlog_list.html',page_data=page_data)


# 权限管理-添加权限
@admin.route("/addauth/",methods=["GET","POST"])
@admin_login_req
#@admin_auth
def addauth():
	form = AuthForm()
	if form.validate_on_submit():
		data = form.data
		auth = Auth.query.filter_by(name=data["name"]).count()
		if auth == 1:
			flash("该权限已经存在", 'err')
			return redirect(url_for('admin.addauth'))
		auth = Auth(
			name=data['name'],
			url = data['url']
		)
		db.session.add(auth)
		db.session.commit()
		flash("权限添加成功", "ok")
		oplog = Oplog(
			admin_id=session['admin_id'],
			ip=request.remote_addr,
			reason="添加%s权限成功！" % data["name"]
		
		)
		db.session.add(oplog)
		db.session.commit()
		redirect(url_for("admin.addauth"))
	
	return render_template('admin/add_auth.html',form=form)


# 权限管理-权限列表
@admin.route("/authlist/<int:page>/")
@admin_login_req
#@admin_auth
def authlist(page=None):
	if page is None:
		page =1
	page_data = Auth.query.order_by(
		Auth.addtime.desc()
	).paginate(page=page, per_page=10)
	
	return render_template('admin/auth_list.html',page_data=page_data)


# 权限管理-删除权限
@admin.route("/authdel/<int:id>/")
@admin_login_req
#@admin_auth
def authdel(id=None):
	auth = Auth.query.filter_by(id=id).first_or_404()
	db.session.delete(auth)
	db.session.commit()
	flash("权限删除成功！", "ok")
	# 操作日志
	oplog = Oplog(
		admin_id=session['admin_id'],
		ip=request.remote_addr,
		reason="删除权限成功，权限名称为：%s，地址为:%s" % (auth.name, auth.url)
	)
	db.session.add(oplog)
	db.session.commit()
	
	return redirect(url_for('admin.authlist',page=1))

# 权限管理-编辑权限
@admin.route("/authedit/<int:id>/",methods=["GET","POST"])
@admin_login_req
#@admin_auth
def authedit(id=None):
	form = AuthForm()
	auth  = Auth.query.get_or_404(id)
	if form.validate_on_submit():
		data = form.data
		auth_count = Auth.query.filter_by(name=data["name"]).count()
		if auth.name != data['name'] and auth_count == 1:
			flash("该权限已经存在", 'err')
			return redirect(url_for('admin.authedit', id=id))
		auth.name = data['name']
		auth.url = data['url']
		db.session.add(auth)
		db.session.commit()
		flash("编辑权限成功！", "ok")
		oplog = Oplog(
			admin_id=session['admin_id'],
			ip=request.remote_addr,
			reason="编辑权限成功%s，地址为：%s" % (data['name'],data['url'])
		
		)
		db.session.add(oplog)
		db.session.commit()
		
		redirect(url_for('admin.authedit', id=id))
	return render_template("admin/auth_edit.html", form=form, auth=auth)


# 角色管理-添加角色
@admin.route("/addrole/",methods=["GET","POST"])
@admin_login_req
#@admin_auth
def addrole():
	form = RoleForm()
	if form.validate_on_submit():
		data = form.data
		role = Role.query.filter_by(name=data["name"]).count()
		if role == 1:
			flash("该角色已经存在", 'err')
			return redirect(url_for('admin.addrole'))
		role = Role(
			name=data['name'],
			auths= ",".join(map(lambda v: str(v),data['auths']))
		)
		db.session.add(role)
		db.session.commit()
		flash("角色添加成功！", "ok")
		oplog = Oplog(
			admin_id=session['admin_id'],
			ip=request.remote_addr,
			reason="添加%s角色成功！" % data["name"]
		
		)
		db.session.add(oplog)
		db.session.commit()
		redirect(url_for("admin.addrole"))
	
	return render_template('admin/add_role.html', form=form)
	


# 角色管理-角色列表
@admin.route("/rolelist/<int:page>/",methods=["GET"])
@admin_login_req
#@admin_auth
def rolelist(page=None):
	if page  is  None:
		page =1
	page_data = Role.query.order_by(
		Role.addtime.desc()
	).paginate(page=page, per_page=10)
	return render_template('admin/role_list.html',page_data=page_data)


# 角色管理-删除权限
@admin.route("/roledel/<int:id>/" ,methods=["GET"])
@admin_login_req
@admin_auth
def roledel(id=None):
	role = Role.query.filter_by(id=id).first_or_404()
	db.session.delete(role)
	db.session.commit()
	flash("角色删除成功！", "ok")
	# 操作日志
	oplog = Oplog(
		admin_id=session['admin_id'],
		ip=request.remote_addr,
		reason="成功删除%s角色！" % role.name
	)
	db.session.add(oplog)
	db.session.commit()
	
	return redirect(url_for('admin.rolelist', page=1))

# 权限管理-编辑权限
@admin.route("/roleedit/<int:id>/", methods=["GET", "POST"])
@admin_login_req
#@admin_auth
def roleedit(id=None):
	form = RoleForm()
	role = Role.query.get_or_404(id)
	if  request.method =="GET":
		auths = role.auths
		form.auths.data = list(map(lambda v:int(v),auths.split(",")))
	
	if form.validate_on_submit():
		data = form.data
		
		role.name = data['name']
		role.auths = ",".join(map(lambda v: str(v),data['auths']))
		db.session.add(role)
		db.session.commit()
		flash("编辑角色成功！", "ok")
		oplog = Oplog(
			admin_id=session['admin_id'],
			ip=request.remote_addr,
			reason="编辑%s角色成功，" % data['name'],
		)
		db.session.add(oplog)
		db.session.commit()
		
		return redirect(url_for('admin.authedit', id=id))
	return render_template("admin/role_edit.html", form=form, role=role)


# 管理员管理-添加管理员
@admin.route("/addadmin/",methods=["POST","GET"])
@admin_login_req
@admin_auth
def addadmin():
	from  werkzeug.security import   generate_password_hash
	form = AddadminForm()
	if form.validate_on_submit():
		data = form.data
		admin = Admin.query.filter_by(name=data["name"]).count()
		if admin == 1:
			flash("该管理员用户已经存在！", 'err')
			return redirect(url_for('admin.addadmin'))
		admin = Admin(
			name=data['name'],
			pwd = generate_password_hash(data["pwd"]),
			role_id= data['role_id'],
			is_super = 1
		)
		db.session.add(admin)
		db.session.commit()
		flash("添加管理员成功！", "ok")
		oplog = Oplog(
			admin_id=session['admin_id'],
			ip=request.remote_addr,
			reason="添加%s管理员成功！" % data["name"]
		
		)
		db.session.add(oplog)
		db.session.commit()
		redirect(url_for("admin.addrole"))
	
	return render_template('admin/add_admin.html', form=form)
	
	


# 管理员-管理员列表
@admin.route("/adminlist/<int:page>/",methods=["POST","GET"])
@admin_login_req
@admin_auth
def adminlist(page=None):
	if page  is  None:
		page =1
	page_data = Admin.query.join(
		Role
	    ).filter(
		Role.id == Admin.role_id
	
	).order_by(
		Admin.addtime.desc()
	).paginate(page=page, per_page=10)
	
	return render_template('admin/admin_list.html',page_data=page_data)
