import DataDissectorSettings as DDS
import tornado.web
import tornado.httpserver
import threading
import time

_VERSION = "alpa v0.1"
_EXITFLAG = False

class Application(tornado.web.Application):
    def __init__(self):
        handlers = [
            (r"/", IndexHandler),
            (r"/exit", ExitHandler),
        ]
        settings = {
            "template_path": DDS.TEMPLATE_PATH,
            "static_path": DDS.STATIC_PATH,
            "autoreload":True,
        }
        tornado.web.Application.__init__(self, handlers, **settings)

class IndexHandler(tornado.web.RequestHandler):
    def get(self):
        global _VERSION
        page_title = "Data Dissector " + _VERSION
        menu_title = "Main Menu"
        self.render("index.html", page_title=page_title, menu_title=menu_title)

class ExitHandler(tornado.web.RequestHandler):
    def get(self):
        global _EXITFLAG
        _EXITFLAG = True

#========================================
# Don't change anything below this line.
#========================================

def start_application():
    application = Application()
    http_server = tornado.httpserver.HTTPServer(application)
    http_server.listen(8888)

    print "Starting Data Dissector..."
    tornado.ioloop.IOLoop.instance().start()

def stop_application():
    ioloop = tornado.ioloop.IOLoop.instance()
    ioloop.add_callback(ioloop.stop)
    print "Stopping Data Dissector..."

def main():
    global _EXITFLAG

    t = threading.Thread(target=start_application)
    t.start()

    while _EXITFLAG is False:
        time.sleep(1)

    stop_application()
    t.join()


if __name__ == "__main__":
    main()
