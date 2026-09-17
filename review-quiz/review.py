# Section A
#name = "Xavier"
#age = 42
#print(f"My name is {name} and my dog is {age} years old")
#num1 = int(input("choose a number: "))
#num2 = int(input("choose a number: "))
#add = num1 + num2
#diff = num1 - num2
#div = num1 // num2
#print(add)
#print(diff)
#print(div)
#print(num1 % 2 == 0)

# Section B

#for i in range(1, 20+1):
 #   if i % 4 == 0:
  #      continue
   # print(i)



#word = input("what is the password? ")
#while word != "secret":
 #   word = input("what is the password? ")

    
# Section C

#package = ["cook", "sweep", "clean", "wipe"]
#print(package[1])
#print(package[-1])

#expense = {
  #  "description": "what",
 #   "amount" : 90,
#    "category": "type"
#}

#for key, value in expense.items():
 #   print(key, value)

#nums = [10, 20, 30, 40, 50]
#print(nums[1:-1])

# Section D

#def calculate_total(amounts):
   # return sum(amounts)

#def format_task(title, priority="Medium"):
  #  return f"{title}, {priority}"

#print(calculate_total([100, 200, 300]))
#print(format_task("Write report"))
#print(format_task("Write report", "High"))


# Section E

#word = input("input word(s):  ")
#print(word.title())
'''
with open("file.txt", "w") as fi:
    fi.write(input("input: ") + "\n")
    fi.write(input("input: ") + "\n")
    fi.write(input("input: ") + "\n")

with open("file.txt", "r") as fi:
    content = fi.read()
    print(content)




def safe_add(a, b):
    try:
        return a + b
    except TypeError:
        return "use numbers only"


class Car:
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year

    def describe(self):
        print(f"This is a {self.make} {self.model} model of {self.year}")

class ElectricCar(Car):
    def __init__(self, make, model, year, battery_range):
        super().__init__(make, model, year)
        self.battery_range = battery_range
    
    def describe(self):
        print(f"A {self.make} {self.model} of {self.year} with battery range of {self.battery_range}")

my_car = Car("Toyota", "Corolla", 2020)
my_car.describe()

my_ecar = ElectricCar("Tesla", "Model 3", 2023, 350)
my_ecar.describe()
'''
