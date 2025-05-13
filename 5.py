class ShapeCalculator:
  def area(self,arg1,arg2=None):
    if arg2 == None:
      return 3.14*2*arg1
    else: return arg1*arg2

obj=ShapeCalculator()
r=10
l=10
w=15
print(f"area of circal with radias {r} is {obj.area(r)}")
print(f"area of ractangle with l={l} and w={w} is {obj.area(l,w)}")