class Appliance:
  def status(self):
    print("this is aplliance")

class AC(Appliance):
  def status(self):
    print("this is AC")

class Fan(Appliance):
  def status(self):
    print("this is FAN")

class Light(Appliance):
  def status(self):
    print("this is Light")

appliances=[Fan(),Light(),AC()]
for app in appliances:
  app.status()