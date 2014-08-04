import random
import tornado.web
from config.config import conf


class RecentPost(tornado.web.UIModule):
    """随机文章

    用于侧边栏显示
    """
    def render(self, post, show=conf['RECENT_POST_NUM']):
        if show:
            return self.render_string("uimodule/recent-post.html", post=post)
        else:
            #返回空，否则会显示NaN,下同
            return ''


class RandomPost(tornado.web.UIModule):
    """随机文章

    用于侧边栏显示
    """
    def render(self, post, show=conf['RANDOM_POST_NUM']):
        if show:
            return self.render_string("uimodule/random-post.html", post=post)
        else:
            #返回空，否则会显示NaN,下同
            return ''


class TodayTip(tornado.web.UIModule):
    from config.config import tips
    tips = tips

    def render(self, show=False):
        tip = self.tips[random.randint(0, len(self.tips)-1)]
        if show:
            return self.render_string("uimodule/today-tip.html", tip=tip)
        else:
            return ''


class Tag(tornado.web.UIModule):
    """获取所有标签"""
    def render(self, tags, show=conf['TAG_NUM']):
        if show:
            return self.render_string("uimodule/tag.html", tags=tags)
        else:
            return ''


class PageNav(tornado.web.UIModule):
    """分页导航
    只有一页时不显示分页
    当分页过多时应该只显示部分，但似乎这不是问题，是我多虑了，哈哈！
    """
    def render(self, nav, show=False):
        if show:
            if nav['num'] % conf['POST_NUM'] != 0:
                nav['num'] = nav['num'] // conf['POST_NUM'] + 1
            else:
                nav['num'] = nav['num'] // conf['POST_NUM']
            if nav['num'] != 1:
                return self.render_string("uimodule/page-nav.html", nav=nav)
            else:
                return ''