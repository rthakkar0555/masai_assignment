class Device:
  def __init__(self,name,type,deviceid):
    self.name=name
    self.type=type
    self.deviceid=deviceid
  def deviceinfo(self):
    print(f"name:{self.name} type:{self.type} id:{self.deviceid}")

class Flyer:
  def fly(self):
    print("dron is now flying")

class Drone(Flyer,Device):
  def __init__(self,name,type,id):
    super().__init__(name,type,id)
  def cupture_image(self):
    print("image has been captured")

d=Drone("dron1","type1","d1")
d.deviceinfo()
d.fly()
d.cupture_image()