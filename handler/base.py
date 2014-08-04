import markdown
from peewee import DoesNotExist, fn
import tornado.web
from model.model import Post, User, Tag, PostTag
from config.config import conf
from util.gravatar import Gravatar


class BaseHandler(tornado.web.RequestHandler):
    """基础 Handler

    所有Handler都要继承此类以获取必要的应用内通用方法和数据
    """

    @property
    def gravatar(self):
        return Gravatar

    @property
    def markdown(self):
        return markdown.markdown

    def get(self):
        """捕获404"""
        self.send_error(404)

    def get_current_user(self):
        """用户验证

        如果存在 cookie 则根据用户 cookie 获取用户信息并返回，
        否则返回 None
        """
        uid = self.get_secure_cookie('uid')
        if not uid:
            return None
        else:
            user = ''
            try:
                user = User.get(User.id == uid)
            except DoesNotExist:
                self.clear_cookie('uid')
            return user

    def write_error(self, status_code, **kwargs):
        """重写404错误页
        """
        if status_code == 404:
            self.render('public/404.html')
        elif status_code == 500:
            self.render('public/500.html')
        else:
            self.write('error:' + str(status_code))

    @staticmethod
    def get_side():
        """获取侧边栏内容

        通用侧边栏数据
        """
        side = {
            'recent_post': Post.select().limit(conf['RECENT_POST_NUM']),
            'random_post': Post.select().order_by(fn.Rand()).limit(conf['RANDOM_POST_NUM']),
            'tags': Tag.select(Tag, fn.Count(Post.id).alias('count')).join(PostTag).join(Post).group_by(Tag),
        }
        return side

    def success(self, message='操作成功', url=''):
        """操作成功提示
        """
        self.render('message/success.html', message=message, url=url)

    def failure(self, message="操作失败", url=''):
        self.render('message/failure.html', message=message, url=url)

    def error(self, message="出现错误了", url=''):
        """操作失败提示
        """
        self.render('message/error.html', message=message, url=url)