#Create a class Person with atributes Name, age, salalry and a method display() for showing the details. Create two instances of the class and call the method for each instance 
class Person:

  def __init__(self,name,age,salary):
    self.name=name
    self.age=age
    self.salary=salary

  def display(self):
    print("Person Details:-")
    print("Name:",self.name)
    print("Age:",self.age)
    print("Salary:",self.salary)
    

p1=Person("Micheal",24,254000)
p1.display()

p2=Person("Samuel",30,558000)
print("\n")
p2.display()