#!/usr/bin/python
# -*- coding: utf-8 -*-
#test ospath to import sometemplate

import os.path

#
import textwrap

import tornado.httpserver
import tornado.ioloop
import tornado.options
import tornado.web
#define parameter
from tornado.options import define, options
define("port", default=8111, help="run on the given port", type=int)

class IndexHandler(tornado.web.RequestHandler):
    def get(self):
      #greeting = self.get_argument('greeting', 'Hello')
      #self.write(greeting + ', friendly user!')
      
      #test index.html
      self.render('index.html')

class AllMsgHandler(tornado.web.RequestHandler):
    def get(self):
        #main
        pass

    def post(self):
        pass

    def head(self):
        pass

class UserAuth(tornado.web.RequestHandler):
    def post(self):
        pass

class SingleGoodMsgHandler(tornado.web.RequestHandler):
    def get(self):
if __name__ == "__main__":
    tornado.options.parse_command_line()
    app = tornado.web.Application(handlers=[(r"/", IndexHandler),
                                            (r"/fridge/current",AllMessageHandler),(r"/fridge/SngMsg")])
    http_server = tornado.httpserver.HTTPServer(app)
    http_server.listen(options.port)
    tornado.ioloop.IOLoop.instance().start()
