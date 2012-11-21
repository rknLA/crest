import unittest
from libcrest.Session import CrestSession

class TestCrestInitialization(unittest.TestCase):

  def test_initialization_with_url_only(self):
    instance = CrestSession('api.github.com')
    self.assertEqual(instance.base_url, 'api.github.com')
    # test defaults
    self.assertEqual(instance.default['accept'], 'application/json')
    self.assertEqual(instance.default['headers'], [])
    self.assertEqual(instance.default['data'], {})

  def test_initialization_without_url(self):
    with self.assertRaises(TypeError):
      instance = CrestSession()

  def test_initialize_with_accept(self):
    instance = CrestSession('api.github.com', 'application/xml')
    self.assertEqual(instance.default['accept'], 'application/xml')

  def test_initialize_with_headers_string(self):
    instance = CrestSession('api.github.com',
                            headers="Content-Type: application/json")
    self.assertListEqual(instance.default['headers'],
                         [ "Content-Type: application/json" ])

  def test_initialize_with_headers_array(self):
    instance = CrestSession('api.github.com',
        headers = [ 'Content-Type: application/json',
                    'X-Auth-Key: 1234' ])
    self.assertListEqual(instance.default['headers'],
                         [ 'Content-Type: application/json',
                           'X-Auth-Key: 1234' ])

  def test_history_after_initialization(self):
    instance = CrestSession('api.github.com')
    self.assertEqual(instance.history, [])
