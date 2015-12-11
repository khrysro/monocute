# - coding: utf-8 -
#
# portado por KhrysRo
#
# This file is part of the Monocute Connection Manager
#
# Monocute Connection Manager is free software: you can redistribute
# it and/or modify it under the terms of the GNU General Public License
# as published by the Free Software Foundation, either version 2 of the
# License, or (at your option) any later version.
#
# Monocute Connection Manager is distributed in the hope that it will
# be useful, but WITHOUT ANY WARRANTY; without even the implied warranty
# of MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License along
# with the Monocute Connection Manager. If not, see
# <http://www.gnu.org/licenses/>.
#

import threading
import BaseHTTPServer
import SimpleHTTPServer
import os

class MccmHttpServerThread(threading.Thread):
    def __init__(self, path, port=8000):
        threading.Thread.__init__(self)
        self.path = path
        self.port = port
        self.running = False

    def run(self):
        self.running = True
        server_class = BaseHTTPServer.HTTPServer
        handler_class = SimpleHTTPServer.SimpleHTTPRequestHandler
        server_address = ('0.0.0.0', self.port)
        httpd = server_class(server_address, handler_class)
        os.chdir(self.path)
        while self.running:
            httpd.handle_request()

    def stop(self):
        self.running = False

if __name__ == '__main__':
    import time
    x = MccmHttpServerThread("/tmp")
    x.start()
    i = 0
    while i < 10:
<<<<<<< HEAD
        print ("Hola")
=======
        print "Hola"
>>>>>>> 8b5052b832fed10909b9901bacee0d407e16cf84
        time.sleep(2)
        i += 1
    x.stop()
