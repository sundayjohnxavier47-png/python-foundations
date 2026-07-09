
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

with open("output.txt", "r") as file:
    content_2 = file.read()
    print(content_2)