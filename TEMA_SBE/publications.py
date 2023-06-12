#clasa de publicatii
import random

class Publication:
  #constrangerile pentru obiectele de tip publicatie
  publication_structure = {
    "stationid": (int, (0, 100)),
    "city": (str, ["Pascani", "Brasov", "Cluj"]),
    "temp": (int, (-10, 40)),
    "rain": (float, (0.0, 1.0)),
    "wind": (int, (0, 30)),
    "direction": (str, ["N", "S", "E", "W", "NE", "NW", "SE", "SW"]),
    "date": (str, ["1.01.2023", "2.01.2023", "3.01.2023", "4.01.2023"])
  }

  def generate_publications(self, n):
    objects = []
    for i in range(n):
      object = {}
      for key, value in self.publication_structure.items():
        type_, choices = value
        if type_ == int:
          object[key] = random.randint(*choices)
        elif type_ == float:
          object[key] = round(random.uniform(*choices), 2)
        elif type_ == str:
          object[key] = random.choice(choices)
        else:
          raise ValueError(f"Unsupported type {type_}")
      objects.append(object)
    return objects

  def __str__(self):
    return f"({self.stationid}, {self.city}, {self.temp}, {self.rain}, {self.wind}, {self.direction}, {self.date})"