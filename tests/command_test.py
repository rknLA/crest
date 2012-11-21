from test_helper import CrestTestHelper
from subprocess import Popen, PIPE
from libcrest.Session import CrestSession

class TestCrestCommands(CrestTestHelper):

  def test_get_root(self):
    expected = self.curl('-v http://localhost:3334/')
    print "expected:"
    print expected
    self.crest.send('GET /')
    self.assertEqual(self.crest.history[-1]['raw'], expected)



