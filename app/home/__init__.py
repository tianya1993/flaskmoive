#coding:utf8
from  flask  import  Blueprint
home  =Blueprint("home",__name__,template_folder='templates')
import   app.home.views #导入视图