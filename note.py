import tornado
import tornado.ioloop
import tornado.web
import tornado.httpserver
import tornado.options
from tornado.options import options, define
from config.config import settings, log, log_file
from config.urls import urls as handlers
from handler.uimodules import uimodules


if log:
    options.log_file_prefix = log_file

define('port', default=10000, help='监听端口号', type=int)
settings['ui_modules'] = uimodules
handlers.append((r"(apple-touch-icon\.png)", tornado.web.StaticFileHandler, dict(path=settings['static_path'])))


class Application(tornado.web.Application):
    """应用
    """
    def __init__(self):
        tornado.web.Application.__init__(self, handlers, **settings)


if __name__ == "__main__":
    tornado.options.parse_command_line()
    http_server = tornado.httpserver.HTTPServer(Application())
    http_server.listen(options.port)
    tornado.ioloop.IOLoop.instance().start()
