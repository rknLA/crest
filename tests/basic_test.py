import unittest
from libcrest.Session import CrestSession

class TestCrestInitialization(unittest.TestCase):

  def test_initialization_with_url_only(self):
    instance = CrestSession('api.github.com')
    self.assertEqual(instance.base_url, 'api.github.com')

  def test_initialization_without_url(self):
    with self.assertRaises(TypeError):
      instance = CrestSession() # this should fail.
