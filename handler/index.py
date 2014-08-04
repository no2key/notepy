from datetime import datetime
from peewee import DoesNotExist
import tornado.web
from handler import base
from model.model import Post, User
from config.config import conf, is_reg
from util.util import get_password


class MainHandler(base.BaseHandler):
    """主页面

    """
    def get(self, page=1):
        post = Post.select().paginate(int(page), conf['POST_NUM'])
        nav = {
            'model': 'index',
            'num': Post.select().count(),
        }
        self.render('index/index.html', title="首页", post=post, side=self.get_side(), nav=nav)


class LoginHandler(base.BaseHandler):
    """登录
    登陆成功后返回登陆前的页面
    """
    def get(self):
        come_url = self.get_argument('next', '/')
        self.render('index/login.html', title="登陆", next=come_url)

    def post(self, *args, **kwargs):
        username = self.get_argument('username', '')
        password = self.get_argument('password', '')
        #用户和名密码不可为空
        if (not username) or (not password):
            self.write("<script>alert('用户名或者密码不能为空');history.back();</script>")
        else:
            try:
                t_user = User.get(username=username)
                if get_password(password) == t_user.password:
                    self.set_secure_cookie('uid', str(t_user.id))
                    self.redirect(self.get_argument('next', '/'))
                else:
                    self.write("<script>alert('用户名或密码错误');history.back();</script>")
            except DoesNotExist:
                self.write("<script>alert('您输入的用户名不存在');history.back();</script>")


class LogoutHandler(base.BaseHandler):
    """退出登录

    只有登录用户才可以执行退出动作
    """
    @tornado.web.authenticated
    def get(self):
        self.clear_cookie('uid')
        self.redirect(self.get_argument("next", "/"))


class RegHandler(base.BaseHandler):
    """用户注册
    目前仅支持单用户，在第一次注册之后请关闭注册功能
    """
    def get(self):
        self.render('index/reg.html', title='注册')

    def post(self):
        if is_reg:
            username = self.get_argument('username')
            email = self.get_argument('email')
            password = self.get_argument('password')
            re_password = self.get_argument('re_password')
            if re_password == password:
                #简单加密
                password = get_password(password)
                User.create(username=username, email=email, password=password, reg_data=datetime.now())
                self.redirect(self.get_login_url())
            else:
                self.write("<script>alert('两次输入的密码不一致');history.back();</script>")
        else:
            self.write("<script>alert('注册功能暂时不对外开放');history.back();</script>")