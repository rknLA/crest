from BaseHTTPServer import BaseHTTPRequestHandler, HTTPServer

class EchoTestHandler(BaseHTTPRequestHandler):
  def handle(self):
    print "handling request in EchoTestHandler"
    print self


class Server:
  def _should_run(self):
    return self.running

  def start(self):
    print "starting test server"
    self.running = True
    self.server = HTTPServer(('', 3334), EchoTestHandler)
    while self._should_run():
      self.server.handle_request()

  def stop(self):
    self.running = False
    print "stopped test server"
