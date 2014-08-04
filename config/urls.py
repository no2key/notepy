from handler import base, index, post


urls = [
    (r"/", index.MainHandler),
    (r"/index/page", index.MainHandler),
    (r"/index/page/([0-9]+)", index.MainHandler),

    (r"/login", index.LoginHandler),
    (r"/logout", index.LogoutHandler),

    (r"/reg", index.RegHandler),

    (r"/post/add", post.AddHandler),
    (r"/post/id/([0-9]+)", post.IndexHandler),

    (r"/post/delete/([0-9]+)", post.DeleteHandler),
    (r"/post/delete", post.DeleteHandler),

    (r"/post/edit/([0-9]+)", post.UpdateHandler),
    (r"/post/update", post.UpdateHandler),

    (r"/tag/(.*)/page/([0-9]+)", post.TagHandler),
    (r"/tag/(.*)", post.TagHandler),

    (r"/post/search", post.SearchHandler),
    (r"/post/search/(.*)/page/([0-9]+)", post.SearchHandler),

    #用于捕获未定义url（404）
    (r".*", base.BaseHandler),
]