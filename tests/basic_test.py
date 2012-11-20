import unittest
from libcrest import Crest

class TestCrestInitialization(unittest.TestCase):

  def test_initialization_with_url_only(self):
    instance = Crest('api.github.com')
    self.assertEqual(instance.base_url, 'api.github.com')

  def test_initialization_without_url(self):
    instance = Crest() # this should fail.
    self.assertTrue(False)
