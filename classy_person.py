'''
Starter code!
don't forget the use of 'self' and to have the methods:
1. __init__
2. increase_age
3. say_greeting
4. count_to_age
'''

class Person:
    age = 0 
    name = ""
    def __init__(self, age, name): 
        self.name = name
        self.age = age
        

    def say_greeting(self):
        print(f"Hello world! My name is {self.name}!")
    
    def increase_age(self):
        self.age = self.age + 1
        print(self.age)


    def count_to_age(self):
        for n in range(self.age):
            print (n+1)








nathan = Person(32, "Nathan")
print(nathan.age)
nathan.say_greeting()
nathan.increase_age()
nathan.count_to_age()





# You won't need to call anything here.
