"""所有配置项可以在这里修改

"""

#注册功能，默认关闭，请在安装并注册首个管理员账户后关闭
is_reg = False

#显示设置
app = {
    #应用名称
    'name': 'NotePy',
    #应用附加信息(简短的说明)
    'title': 'a simple blog',
    #联系邮箱
    'email': 'imaguowei@gmail.com',
}

#数据库配置
database = {
    'host': 'localhost',
    'database': 'notepy',
    'user': 'root',
    'password': 'root',
    'autocommit': True,
    'buffered': True,
}

#参数配置项
#如果设置为0则不现实，此处的更改为全局设置，但仍然可以单独设置某处的显示选项
conf = {
    #主页显示的文章数目
    'POST_NUM': 5,
    #近期文章数目
    'RECENT_POST_NUM': 10,
    #随机文章数目
    'RANDOM_POST_NUM': 6,
    #标签云中显示的标签数目
    'TAG_NUM': 100,
}

settings = {
    "app": app,
    "template_path": "template",
    "static_path": "static",
    "cookie_secret": "entercookiesecret",
    "login_url": "/login",
    "xsrf_cookies": True,
    "debug": False,
}

"""日志设置
开启多个实例时请使用 -log_file_prefix='log@8000.txt' 命令参数，
每个端口需要单独定义。
此时该设置将无任何作用
"""
#开启日志文件记录，默认为 False
log = False
#日志记录位置
log_file = 'log/log.txt'


"""每日警句
"""
tips = [
    ("Fear not that the life shall come to an end, but rather fear that it shall never have a beginning.",
     "J.H. Newman"),
    ("Gods determine what you're going to be.", "Julius Erving"),
    ("An aim in life is the only fortune worth finding.", "Robert Louis Stevenson"),
    ("A man can fail many times, but he isn't a failure until he begins to blame somebody else.", "J. Burroughs"),
    ("Man errs as long as he strives.", "Goethe"),
    ("Cease to struggle and you cease to live.", "Thomas Carlyle"),
]