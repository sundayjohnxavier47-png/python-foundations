
# list 
favorite_food = ["Rice", "Garri", "Goat meat", "Chicken", "Beef"]
print(favorite_food[0])
print(favorite_food[-1])
# how to add to list
favorite_food.append("Pineapple")
# to loop in list
for food in favorite_food:
    print(food)

# dictionary loop with .items
person = {
    "name": "Mono",
    "age": 32,
    "city": "Japan"
}

for key, value in person.items():
    print(key, value)
# index used if you want a part
print(favorite_food[1:3])


# list []
# tuple ()
# set {}
# Methods: .append(), .remove(), len()
#Dictionary {"key": value} accessed by key, not position. Loop with .items()
# to get both key and value together.
#Slicing — list[start:stop] extracts a sub-section (stop index not included).