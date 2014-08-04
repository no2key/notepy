"""
使用peewee自动创建数据库表，每个模型对应一个数据库表
在开始之前需要建立相应数据库，并在 config/config中配置
文档：http://peewee.readthedocs.org/en/latest/
"""


from datetime import datetime
from peewee import *
from config.config import database as dbconfig


db = MySQLDatabase(dbconfig['database'], user=dbconfig['user'], passwd=dbconfig['password'])


class BaseModel(Model):
    class Meta:
        database = db


class User(BaseModel):
    username = CharField(unique=True, max_length=20)
    email = CharField(unique=True)
    password = CharField()
    reg_date = DateTimeField(default=datetime.now())

    class Meta:
        table_alias = 'user'


class Post(BaseModel):
    title = CharField(max_length=50)
    content = TextField()
    user = ForeignKeyField(User, related_name='posts')
    pub_date = DateTimeField(default=datetime.now())

    class Meta:
        order_by = ('-pub_date',)
        indexes = (
            (('title',), False),
        )


class Tag(BaseModel):
    tag = CharField(unique=True, max_length=25)

    class Meta:
        pass


class PostTag(BaseModel):
    post = ForeignKeyField(Post, related_name='posts')
    tag = ForeignKeyField(Tag, related_name='tags')

    class Meta:
        db_table = 'post_tag'


if __name__ == '__main__':
    #创建数据表
    User.create_table()
    Post.create_table()
    Tag.create_table()
    PostTag.create_table()