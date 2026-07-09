try:
    num = int(input("Type a number: "))
except ValueError:
    print("Please only numbers are allowed.")

try:
    num2 = int(input("Type a new number: "))

except ZeroDivisionError:
    print("Number cannot be zero.")
print(num / num2)

def safe_divide(a, b):
    assert b != 0, "b can't be zero"
    return a / b



sentence = input("Write a sentence: ")
print(sentence.upper())
print(sentence.lower())
print(len(sentence.split()))

with open("output.txt", "w") as file:
    file.write(sentence)

with open("output.txt", "r") as file:
    content = file.read()
    print(content)

sentence_2 = input("Input sentence: ")

with open("output.txt", "a") as file:
    file.write("\n")
    file.write(sentence_2)
try:

    with open("output.txt", "r") as file:
        content_2 = file.read()
        print(content_2)
except FileNotFoundError:
    print("file does not exist")