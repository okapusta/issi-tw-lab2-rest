import requests

class Nominatim():
  def __init__(self, lat, lon):
    self.lat = lat
    self.lon = lon

  def call(self):
    resp = requests.get(
      f"https://nominatim.openstreetmap.org/reverse?lat={self.lat}&lon={self.lon}&format=json",
      headers={"User-Agent": "Mozilla/5.0"}
    )
    return resp.json()
