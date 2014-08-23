NotePy
=====

a very simple blog.



## 说明

notepy是一个非常简单的博客系统，采用 tornado 框架开发，支持文章的增删改查，支持文章标签，notepy 文章发布支持 markdown 语法。
如果你厌倦了那些功能复杂的博客，只想安心写点东西，或许notepy就是你要的！


## 项目依赖(Python3)

所有依赖项目只在最新版下做过测试

* tornado 3.2
* Markdown 2.4
* peewee 2.2.1
* PyMySQL 0.6.1



## 安装配置

1. 在MySql数据库中新建一个数据库，可命名为notepy，并将notepy.sql导入，
配置数据库，修改config/config.py中数据库配置部分。（也可用/model/model.py自动创建数据库表）

2. 在 config/config.py 开启注册功能（将is_reg设置为True),

3. 运行 note.py，默认监听10000端口（可在note.py 中修改，也可在运行时添加 port参数指定端口）。

4. 登陆localhost:10000/reg,注册新用户，注册完毕后返回配置文件关闭注册功能。


## TODO

添加代码语法高亮
