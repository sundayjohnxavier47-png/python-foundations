

favorite_food = ["Rice", "Garri", "Goat meat", "Chicken", "Beef"]
print(favorite_food[0])
print(favorite_food[-1])

favorite_food.append("Pineapple")

for food in favorite_food:
    print(food)


person = {
    "name": "Mono",
    "age": 32,
    "city": "Japan"
}

for key, value in person.items():
    print(key, value)

print(favorite_food[1:3])