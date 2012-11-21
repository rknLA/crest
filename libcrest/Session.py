from types import *

class CrestSession:
  def __init__(self, url, accept='application/json', headers=None, data=None):
    self.base_url = url
    self.default = { }
    self.default['accept'] = accept
    if type(headers) == StringType:
      self.default['headers'] = [headers]
    elif type(headers) == ListType:
      self.default['headers'] = headers
    else:
      self.default['headers'] = []
    self.default['data'] = data if data else {}

    self.history = []

