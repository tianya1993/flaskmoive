#coding:utf8
from  . import  home
from  flask  import  render_template,redirect,url_for,flash,session,request
from  app.home.forms  import   RegisterviewForm,LoginForm,UserinfoView,UserpwdView
from  app.models import   User,Userlog
from  werkzeug.security import   generate_password_hash
from  werkzeug.utils import secure_filename
import   uuid
from  app  import  db,app
from  functools import  wraps
import   os
from datetime import datetime




# 登录装饰器
def user_login_req(f):
	@wraps(f)
	def decorated_function(*args, **kwargs):
		if "user" not in session:
			return redirect(url_for("home.login", next=request.url))
		return f(*args, **kwargs)
	
	return decorated_function

#更改文件名称
def change_filename(filename):
    fileinfo = os.path.splitext(filename)
    filename = datetime.now().strftime("%Y%m%d%H%M%S") + str(uuid.uuid4().hex) + fileinfo[-1]
    return filename

@home.route("/")
def index():
	return render_template("home/index.html")
@home.route("/animation/")
def animation():
	return render_template("home/animation.html")



@home.route("/login/",methods=['GET',"POST"])

def login():
	form = LoginForm()
	if  form.validate_on_submit():
		data = form.data
		user = User.query.filter_by(name=data["name"]).first()
		if not  user.check_pwd(data['pwd']):
			flash('密码错误！','err')
			return redirect(url_for("home.login"))
		session["user"] = user.name
		session["user_id"] = user.id
		userlog=Userlog(
			user_id= user.id,
			ip = request.remote_addr
		)
		db.session.add(userlog)
		db.session.commit()
		return  redirect(url_for('home.user'))

	return render_template("home/login.html",form=form) #登录页面

@home.route("/logout/")
def logout():
	session.pop("user", None)  # 删除session信息
	session.pop("user_id", None)  # 删除管理员ID
	return redirect(url_for("home.login"))  #重写退出页面跳转到登录页面

@home.route("/register/",methods=['GET',"POST"])
def register():
	form = RegisterviewForm()
	if  form.validate_on_submit():
		data = form.data
		name_count = User.query.filter_by(name=data["name"]).count()
		phone_count = User.query.filter_by( phone=data["phone"]).count()
		email_count = User.query.filter_by(email=data["email"]).count()
		if name_count == 1 :
			flash("该用户已经注册，请登录！",'err')
			return  redirect(url_for('home.login'))
		if phone_count == 1:
			flash("该手机已经注册，请登录！", 'err')
			return redirect(url_for('home.login'))
		
		if email_count == 1:
			flash("该邮箱已经注册，请登录！", 'err')
			return redirect(url_for('home.login'))
		user =User(
			name = data['name'],
			email = data['email'],
			phone = data['phone'],
			pwd = generate_password_hash(data['pwd']),
			uuid = uuid.uuid4().hex
			
		)
		db.session.add(user)
		db.session.commit()
		flash("注册成功！", "ok")
		
		
	
	return render_template("home/register.html",form=form)

@home.route("/user/",methods=["GET","POST"])
@user_login_req
def  user():
	form = UserinfoView()
	form.face.validators = []
	user = User.query.get(int(session["user_id"]))
	form.face.validators= []
	if request.method == "GET" :
		form.name.data = user.name
		form.email.data = user.email
		form.phone.data = user.phone
		form.info.data = user.info
		
	if form.validate_on_submit():
		
		data =form.data
		if form.face.data != "":
			file_face = secure_filename(form.face.data.filename)
			if not os.path.exists(app.config["UP_DIR"]):  # 判断目录是否存在
				os.makedirs(app.config["UP_DIR"])
				os.chmod(app.config["UP_DIR"], "rw")
			user.face = change_filename(file_face)
			form.face.data.save(app.config["UP_DIR"] +"user/" + user.face)
		
		name_count = User.query.filter_by(name=data["name"]).count()
		if data["name"] != user.name and name_count == 1:
			flash("昵称已经存在!", "err")
			return redirect(url_for("home.user"))
		
		email_count = User.query.filter_by(email=data["email"]).count()
		if data["email"] != user.email and email_count == 1:
			flash("邮箱已经存在!", "err")
			return redirect(url_for("home.user"))
		
		phone_count = User.query.filter_by(phone=data["phone"]).count()
		if data["phone"] != user.phone and phone_count == 1:
			flash("手机已经存在!", "err")
			return redirect(url_for("home.user"))
		user.name = data['name']
		user.email = data['email']
		user.phone = data['phone']
		user.info = data['info']
		#user.face= user_face
		db.session.add(user)
		db.session.commit()
		flash("编辑成功！", "ok")
		return  redirect(url_for("home.user"))
		
	return  render_template("home/user.html",form=form,user=user)


@home.route("/loginlog/<int:page>/")
@user_login_req
def loginlog(page=None):
	if page is None:
		page = 1
	page_data = Userlog.query.join(User).filter(
		Userlog.user_id == session['user_id']
	).order_by(
		Userlog.addtime.desc()
	).paginate(page=page, per_page=10)
	return render_template("home/loginlog.html",page_data=page_data)

@home.route("/pwd/",methods=["GET","POST"])
@user_login_req
def pwd():
	form = UserpwdView()
	if form.validate_on_submit():
		data = form.data
		user = User.query.filter_by(name=session['user']).first()
		from werkzeug.security import generate_password_hash
		user.pwd = generate_password_hash(data['new_pass'])
		db.session.add(user)
		db.session.commit()
		flash("修改密码成功，请重新登录！", "ok")
		
		return redirect(url_for("home.login"))
	return render_template("home/pwd.html",form=form)

@home.route("/comments/")
@user_login_req
def comments():
	return render_template("home/comments.html")
@home.route("/moviecol/")
@user_login_req
def moviecol():
	return render_template("home/moviecol.html")

@home.route("/search/")
def search():
	return render_template("home/search.html")
@home.route("/play/")
def play():
	return render_template("home/play.html")
