import tornado.web
import model
from datetime import datetime
from handler import base
from model.model import Post, Tag, PostTag
from config.config import conf
from peewee import DatabaseError, DoesNotExist


class IndexHandler(base.BaseHandler):
    def get(self, pid):
        try:
            post = Post.get(id=pid)
            post.tags = Tag.select().join(PostTag).join(Post).where(Post.id == pid)
            self.render('post/index.html', post=post, side=self.get_side(), title=post.title)
        except DoesNotExist:
            self.send_error(404)


class AddHandler(base.BaseHandler):
    """文章添加操作
    """
    @tornado.web.authenticated
    def get(self):
        tags = model.get_tags_and_numbers()
        self.render('post/add.html', title='添加文章', side=self.get_side(), tags=tags)

    @tornado.web.authenticated
    def post(self):
        title = self.get_argument('title')
        content = self.get_argument("content")
        author_id = self.get_secure_cookie('uid')
        tags = model.get_tags(str(self.get_argument('tags')))

        try:
            post = Post.create(title=title, content=content, user=author_id, pub_date=datetime.now())
            model.tag_save(tags, post.id)
        except DatabaseError:
            self.write("<script>alert('文章添加失败');</script>")
        else:
            self.redirect('/post/edit/' + str(post.id))


class UpdateHandler(base.BaseHandler):
    """文章更新操作

    """
    @tornado.web.authenticated
    def get(self, pid):
        try:
            post = Post.get(id=pid)
            post.tags = Tag.select().join(PostTag).join(Post).where(Post.id == pid)
            self.render('post/edit.html', post=post, side=self.get_side(), title='编辑-' + post.title)
        except DoesNotExist:
            self.send_error(404)

    @tornado.web.authenticated
    def post(self):
        pid = int(self.get_argument("id"))
        post = Post.get(id=pid)
        post.title = self.get_argument('title')
        post.content = self.get_argument("content")

        tags = model.get_tags(str(self.get_argument('tags')))
        try:
            model.tag_save(tags, post.id)
            post.save()
            self.success('文章更新成功')
        except DatabaseError:
            self.error('文章更新失败')


class DeleteHandler(base.BaseHandler):
    """文章删除操作

    """
    @tornado.web.authenticated
    def get(self, pid):
        self.render('post/delete.html', id=pid)

    @tornado.web.authenticated
    def post(self):
        pid = self.get_argument('id')
        try:
            try:
                post_tag = PostTag.delete().where(PostTag.post == pid)
                post_tag.execute()
            except DoesNotExist:
                pass
            post = Post.get(Post.id == pid)
            post.delete_instance()
            self.success('删除成功')
        except DoesNotExist:
            pass
        except DatabaseError:
            self.failure('删除失败')


class SearchHandler(base.BaseHandler):
    """搜索功能

    仅搜索标题
    """
    def get(self, q='', page=0):
        if not q:
            q = '%' + self.get_argument('q') + '%'
        try:
            post = Post.select().where(Post.title ** q | Post.content ** q).paginate(int(page), conf['POST_NUM'])
            nav = {
                'model': 'post/search/'+q,
                'num': Post.select().where(Post.title ** q | Post.content ** q).count()
            }
            self.render('post/search.html', post=post, side=self.get_side(), title=q, nav=nav)
        except DatabaseError:
            self.success('搜索失败')


class TagHandler(base.BaseHandler):
    def get(self, tag, page=1):
        p = Post.select(Post).join(PostTag).join(Tag).where(Tag.tag == tag).\
            paginate(int(page), conf['POST_NUM'])
        nav = {
            'model': 'tag/' + tag,
            'num': Post.select(Post).join(PostTag).join(Tag).where(Tag.tag == tag).count(),
        }
        self.render("tag/index.html", post=p, title=tag, side=self.get_side(), nav=nav)