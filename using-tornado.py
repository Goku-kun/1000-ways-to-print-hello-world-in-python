import tornado.ioloop
import tornado.web
import datetime

class MainHandler(tornado.web.RequestHandler):
    def get(self):
        self.write("Hello world")

def make_app():
    return tornado.web.Application([
        (r"/", MainHandler),
    ])
    
def startTornado(*args, **kwargs):
    app = make_app()
    server = app.listen(8888)
    print("Running Hello World on localhost:8888")
    return server

def stopTornado():
    tornado.ioloop.IOLoop.instance().stop()

if __name__ == "__main__":
    server = startTornado()
    print("Hello World")
    print("The server will exit after 30 seconds")
    tornado.ioloop.IOLoop.current().add_timeout(
        datetime.timedelta(seconds=30),
        stopTornado)
    tornado.ioloop.IOLoop.current().start()
    print("Server exit")
    server.stop()
