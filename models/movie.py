from dataclasses import dataclass

@dataclass
class Movie():
  title: str
  year: int
  actors: str

  id: int = None

  def valid(self):
    return True
