class WeatherStation:
  def __init__(self):
    self.subscribers = []  # List to store subscribing devices
    self.temperature = None

  def subscribe(self, device):
    self.subscribers.append(device)

  def unsubscribe(self, device):
    if device in self.subscribers:
      self.subscribers.remove(device)
      print(f"Device '{device}' unsubscribed successfully.")
    else:
      print(f"Device '{device}' is not subscribed.")

  def set_temperature(self, new_temperature):
    self.temperature = new_temperature
    self.notify()

  def notify(self):
    for device in self.subscribers:
      device.update(self.temperature)

class DisplayDevice:
  def __init__(self, name, offset=0):
    self.name = name
    self.offset = offset  # Temperature offset for this device

  def update(self, temperature):
    adjusted_temp = temperature + self.offset
    print(f"Temperature update for {self.name}: {adjusted_temp} degrees Celsius")

  def __str__(self):
    return f"Display Device: {self.name}"  # Informative string representation

# Usage
weather_station = WeatherStation()

display1 = DisplayDevice("Display 1")
display2 = DisplayDevice("Display 2", offset=5)  # Add an offset of 5 degrees for display2
display3 = DisplayDevice("Display 3 (Living Room)")

weather_station.subscribe(display1)
weather_station.subscribe(display2)
weather_station.subscribe(display3)

# Set temperature (all devices will receive the same update but process it differently)
weather_station.set_temperature(25)
