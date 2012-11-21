import unittest
from subprocess import Popen, PIPE
from server import Server as TestServer

class CrestTestHelper(unittest.TestCase):
  def curl(self, curl_str):
    command = 'curl ' + curl_str
    print 'executing command:'
    print command
    output = Popen(command, stdout=PIPE, shell=True).communicate()[0]
    return output

#  def setUp(self):
#   # start server
#   if not hasattr(self,'server'):
#     self.server = TestServer()

#   self.server.start()

# def tearDown(self):
#   self.server.stop()
