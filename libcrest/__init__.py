
class Crest:
  def __init__(self, url, accept='application/json', headers=None, data=None):
    self.accept = accept
    self.base_url = url
    self.default_headers = headers if headers else []
    self.default_data = data if data else {}

