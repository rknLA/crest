import unittest

class TestCrestInitialization(unittest.TestCase):

  def setUp(self):
    print "just settin' up"

  def test_fail(self):
    self.assertTrue(False)
