class User:
  def __init__(self,name,email):
    self.name=name
    self.email=email
  def display_info(self):
    print(f"name:{self.name} email{self.email} ",end=" ")

class Instructor(User):
  def __init__(self,name,email,subExpertise):
    super().__init__(name,email)
    self.subExpertise=subExpertise
  def upload_content(self,content):
    print(f"Content {content} is uploded")
  def display_info(self):
    super().display_info()
    print(f"subExpertise is {self.subExpertise} ",end=" ")

class CourseCreater(Instructor):
   def __init__(self,name,email,subExpertise,coursename,modules):
     super().__init__(name,email,subExpertise)
     self.coursename=coursename
     self.modules=modules
   def display_info(self):
     print(f"course name : {self.coursename} course module{self.modules}")
    
user=User("rishi","rishi@gmail.com")
user.display_info()

inst=Instructor("rishi2","rishi2@gmail.com",["phy","DSA"])
inst.upload_content("file1")
inst.display_info()

coursereater=CourseCreater("rishi","rishi@gmail.com",["dsa","dev"],"ai ml",10)
coursereater.display_info()