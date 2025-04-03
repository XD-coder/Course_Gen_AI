# #class for password saving !!!

# class Client:
#     name = "default"
#     phone = "(123)456-7890"
#     email = "foo@bar.com"
#     purchases = 0

# def main():
#     firstClient = Client()
#     firstClient.name = "James Tam"
#     firstClient.email = "tam@ucalgary.ca"

#     print(firstClient.name)
#     print(firstClient.phone)
#     print(firstClient.email)
#     print(firstClient.purchases)

# main()

#person class 
# class Person:
#     name = "I have no name :("

#     def sayName(self):
#         print("My name is...", self.name)

# def main():
#     aPerson = Person()
#     aPerson.sayName()
#     aPerson.name = "Big Smiley :D"
#     aPerson.sayName()

# main()

# #person class experiment 2
# class Person:
#     name = "I have no name :("

#     def sayName(self):
#         print("My name is...", self.name)

# def main():
#     lisa = Person()
#     lisa.name = "Lisa Simpson, pleased to meet you."
#     bart = Person()
#     bart.name = "I'm Bart Simpson, who the hek are you???!!!"

#     lisa.sayName()
#     bart.sayName()

# main()


# #reference example
# class Person:
#     age = 0
#     name = "none"

#     def __init__(self, newAge, newName):
#         self.age = newAge
#         self.name = newName

# def displayAge (aPerson):
#     print("%s age %d" % (aPerson.name, aPerson.age))

# def start():
#     # Part 1
#     person1 = Person (13, "Person2")
#     person2 = person1
#     displayAge (person1)
#     displayAge (person2)
#     print()

#     # Part 2
#     person1 = Person (888, "Person1")
#     displayAge (person1)
#     displayAge (person2)

# start()

# #init method

# class Person:
#     name = ""

#     def __init__(self, name = "I have no name"):
#         self.name = name

# def main():
#     smiley = Person()
#     print("My name is...", smiley.name)

#     jt = Person("James")
#     print("My name is...", jt.name)

# main()


# class Person:
#     age = 0
#     name = "none"
#     def __init__(self,newAge,newName):
#         self.age = newAge
#         self.name = newName
#     def displayAge(aPerson):
#         print("%s age %d" %(aPerson.name,aPerson.age))



