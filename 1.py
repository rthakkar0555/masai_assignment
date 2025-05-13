class Member:
  def __init__(self,name,membarshipid):
    self.name=name
    self.membarshipid=membarshipid
  def display_info(self):
    print(f"name:{self.name} membarship{self.membarshipid}")

class StudentMember(Member):
  def __init__(self,name,membarshipid):
    super().__init__(name,membarshipid)
    self.borrowCount=0
  def  borrow_book(self,name):
    print(f"book {name} borrowed")
    self.borrowCount+=1
  def return_book(self,name):
    print(f"returning book {name}")
    self.borrowCount-=1
  def borrowing_status(self):
    print(f"borrowd books number is {self.borrowCount}")
    
s1=StudentMember("rishi",100)
s1.display_info()
s1.borrow_book("phy")  # i am using book name just to print nothing esle
s1.return_book("phy")
s1.borrow_book("marvel")
s1.borrowing_status()