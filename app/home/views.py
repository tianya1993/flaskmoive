#coding:utf8
from  . import  home
from  flask  import  render_template,redirect,url_for,flash,session,request,Response
from  app.home.forms  import   RegisterviewForm,LoginForm,UserinfoView,UserpwdView,CommentForm
from  app.models import   User,Userlog,Perview,Moive,Tag,Comment,Moviecol
from  werkzeug.security import   generate_password_hash
from  werkzeug.utils import secure_filename
import   uuid
from  app  import  db,app,rd
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
	tags = Tag.query.all()[:-5]
	tid =  request.args.get("tid",0)
	page_data = Moive.query
	if int(tid) != 0:
		page_data = page_data.filter_by(tag_id=int(tid))
	
	start =  request.args.get("start",0)
	if int(start) != 0:
		page_data = page_data.filter_by(start=int(start))
	
	time = request.args.get("time", 0)
	if int(time) !=0:
		if int(time) == 1:
			page_data = page_data.order_by(
				Moive.addtime.desc()
			)
		else:
			page_data = page_data.order_by(
				Moive.addtime.asc()
			)
	pm = request.args.get("pm", 0)
	
	if  int(pm) != 0:
		if pm == 1:
			page_data = page_data.order_by(
				Moive.playnum.desc()
			)
		else:
			page_data = page_data.order_by(
				Moive.playnum.asc()
			)
		
	cm = request.args.get("cm", 0)
	if  int(cm) !=0:
		if int(cm)==1:
			page_data = page_data.order_by(
				Moive.commentnum.desc()
			)
		else:
			page_data = page_data.order_by(
				Moive.commentnum.asc()
			)
	page = request.args.get("page",1)
	page_data = page_data.paginate(page=int(page), per_page=4)
	p = dict(
		tid=tid,
		start=start,
		time=time,
		pm=pm,
		cm=cm
		
	)
	
	return render_template("home/index.html",tags=tags,p=p,page_data=page_data)
@home.route("/animation/")
#定义预告图片信息

def animation():
	perview = Perview.query.order_by(Perview.addtime.desc())[0:5]
	return render_template("home/animation.html",perview=perview)

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

@home.route("/comments/<int:page>/",methods=['POST',"GET"])
@user_login_req
def comments(page=None):
	if  page  is  None:
		page = 1
	page_data = Comment.query.join(Moive).join(
		User
	).filter(
		User.id == session['user_id']
	).order_by(
		Comment.addtime.desc()
	).paginate(page=page, per_page=10)
	

	return render_template("home/comments.html",page_data=page_data)
#添加电影收藏
@home.route("/moviecol/add/",methods=["GET"])
#@user_login_req
def moviecol_add():
	uid = request.args.get("uid", "")
	mid = request.args.get("mid", "")
	print(uid,mid)
	moviecol = Moviecol.query.filter_by(
		user_id=int(uid),
		movie_id=int(mid)
	).count()
	if  moviecol == 1 :
		data = dict(ok=0)
	else:
		moviecol =Moviecol(
			user_id=int(uid),
			movie_id=int(mid)
		)
		db.session.add(moviecol)
		db.session.commit()
		data = dict(ok=0)
	
	import   json
	return json.dumps(data)

#电影收藏
@home.route("/moviecol/<int:page>/",methods=["GET"])
@user_login_req
def moviecol(page=None):
	if page is None:
		page = 1
	page_data= Moviecol.query.join(
		Moive
	).join(
		User
	).filter(
		Moive.id == Moviecol.movie_id,
	    User.id == session['user_id']
	).order_by(
		Moviecol.addtime.desc()
	            ).paginate(page=page, per_page=10)
	
	
	return render_template("home/moviecol.html",page_data=page_data)

@home.route("/search/<int:page>/")
def search(page=None):
	if page is  None:
		page = 1
	key = request.args.get("key","")
	moive_count = Moive.query.filter(
		Moive.title.ilike('%' +key+ '%')
	).count()
	page_data=Moive.query.filter(
		Moive.title.ilike('%' +key+ '%')
	).order_by(
		Moive.addtime.desc()
	).paginate(page=page, per_page=10)
	
	
	return render_template("home/search.html",key=key,page_data=page_data,moive_count=moive_count)
@home.route("/play/<int:id>/<int:page>/",methods=['POST',"GET"])
def play(id=None,page=None):
	moive = Moive.query.get_or_404(int(id))
	form = CommentForm()
	if page is  None:
		page =1
		
	commcount = Comment.query.filter_by(
		movie_id=moive.id
	).count()
	page_data =Comment.query.join(
		Moive
	).join(
		User
	).filter(
		Moive.id == moive.id,
		User.id ==  Comment.user_id
		
	).order_by(
		Comment.addtime.desc()
	).paginate(page=page, per_page=10)
	
	
	
	moive.playnum =moive.playnum +1
	
	
	if "user" in  session  and  form.validate_on_submit():
		data = form.data
		
		comments =Comment(
			content = data['content'],
			movie_id = moive.id,
		user_id = session['user_id'],
		
		
		)
		db.session.add(comments)
		db.session.commit()
		
		flash("评论成功！", 'ok')
		db.session.add(moive)
		db.session.commit()
		return  redirect(url_for('home.play',id=moive.id,page=1))
	moive.commentnum = moive.commentnum + 1
	db.session.add(moive)
	db.session.commit()
	
	
	return render_template("home/play.html",moive=moive,form=form,page_data=page_data,commcount=commcount)
#弹幕播放器
@home.route("/video/<int:id>/<int:page>/", methods=['POST', "GET"])
def video(id=None, page=None):
	moive = Moive.query.get_or_404(int(id))
	form = CommentForm()
	if page is None:
		page = 1
	
	commcount = Comment.query.filter_by(
		movie_id=moive.id
	).count()
	page_data = Comment.query.join(
		Moive
	).join(
		User
	).filter(
		Moive.id == moive.id,
		User.id == Comment.user_id
	
	).order_by(
		Comment.addtime.desc()
	).paginate(page=page, per_page=10)
	
	moive.playnum = moive.playnum + 1
	
	if "user" in session and form.validate_on_submit():
		data = form.data
		
		comments = Comment(
			content=data['content'],
			movie_id=moive.id,
			user_id=session['user_id'],
		
		)
		db.session.add(comments)
		db.session.commit()
		
		flash("评论成功！", 'ok')
		db.session.add(moive)
		db.session.commit()
		return redirect(url_for('home.video', id=moive.id, page=1))
	moive.commentnum = moive.commentnum + 1
	db.session.add(moive)
	db.session.commit()
	
	return render_template("home/video.html", moive=moive, form=form, page_data=page_data, commcount=commcount)
@home.route("/tm/", methods=["GET", "POST"])
def tm():
    """
    弹幕消息处理
    """
    import json
    if request.method == "GET":
        # 获取弹幕消息队列
        id = request.args.get('id')
        # 存放在redis队列中的键值
        key = "movie" + str(id)
        if rd.llen(key):
            msgs = rd.lrange(key, 0, 2999)
            res = {
                "code": 1,
                "danmaku": [json.loads(v) for v in msgs]
            }
        else:
            res = {
                "code": 1,
                "danmaku": []
            }
        resp = json.dumps(res)
    if request.method == "POST":
        # 添加弹幕
        data = json.loads(request.get_data())
        msg = {
            "__v": 0,
            "author": data["author"],
            "time": data["time"],
            "text": data["text"],
            "color": data["color"],
            "type": data['type'],
            "ip": request.remote_addr,
            "_id": datetime.now().strftime("%Y%m%d%H%M%S") + uuid.uuid4().hex,
            "player": [
                data["player"]
            ]
        }
        res = {
            "code": 1,
            "data": msg
        }
        resp = json.dumps(res)
        # 将添加的弹幕推入redis的队列中
        rd.lpush("movie" + str(data["player"]), json.dumps(msg))
    return Response(resp, mimetype='application/json')