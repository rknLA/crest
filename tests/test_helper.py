import unittest
from subprocess import Popen, PIPE
from libcrest.Session import CrestSession

class CrestTestHelper(unittest.TestCase):
  def curl(self, curl_str):
    command = 'curl -s ' + curl_str
    output = Popen(command, stdout=PIPE, stderr=PIPE, shell=True).communicate()
    return output[0]

  def setUp(self):
    self.crest = CrestSession('localhost:3334')
