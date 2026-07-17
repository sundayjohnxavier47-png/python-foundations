

sentence = input("Write a sentence: ")
# string manipulation methods
print(sentence.upper())
print(sentence.lower())
print(len(sentence.split()))
# to write into file note the 'w'
with open("output.txt", "w") as file:
    file.write(sentence)
# to read a file and print note the 'r'
with open("output.txt", "r") as file:
    content = file.read()
    print(content)

sentence_2 = input("Input sentence: ")
# now with new line and adding note the 'a'
with open("output.txt", "a") as file:
    file.write("\n")
    file.write(sentence_2)

with open("output.txt", "r") as file:
    content_2 = file.read()
    print(content_2)


# .startswith(), .endswith(), and in to check for a substring.
# .split() turns a string into a list; .join() does the reverse,
# with open(...) as file: auto close when done
# Reading line by line — for line in file:
# .strip() to remove the trailing newline.