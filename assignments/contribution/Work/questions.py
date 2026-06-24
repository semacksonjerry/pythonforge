#!/usr/bin/python

# Question 1
text = "Computer Science"
print(text[0:8])                                        # Output: Computer
print(text[9:])                                         # Output: Science
print(text[-3:])                                        # Output: nce

# Question 2
word = "Programming"
print(word[1:6])                                        # Output: rogra
print(word[::-1])                                       # Output: gnimmargorP

# Question 3
fullname = "Cypher, Adjei"
names = fullname.split(", ")
print("First Name: ", names[0])                         # Output: Cypher
print("Last Name: ", names[1])                          # Output: Adjei

# Question 4
data = "HTML-CSS-JAVASCRIPT-PYTHON"
languages = data.split("-")
print("Languages: ", languages)                         # Output: ['HTML', 'CSS', 'JAVASCRIPT', 'PYTHON']
print("First Language: ", languages[0])                 # Output: HTML
print("Second Language: ", languages[1])                # Output: CSS
print("Third Language: ", languages[2])                 # Output: JAVASCRIPT
print("Fourth Language: ", languages[3])                # Output: PYTHON

# Question 5
sentence = "I love Java"
print(sentence.replace("Java", "Python"))               # Output: I love Python

# Question 6
text = "banana banana banana"
text = text.replace("banana", "mango", 2)
text = text.replace("mango", "banana", 1)
print(text)                                            # Output: banana mango banana

# Question 7
email = " student@gmail.com "
email = email.strip()
print(email)                                            # Output: student@gmail.com

# Question 8
name = " Cypher Adjei "
print(name.strip())                                     # Output: Cypher Adjei
print(name.upper())                                     # Output: CYPHER ADJEI

# Question 9
text = "python programming is fun"
print(text.upper())                                     # Output: PYTHON PROGRAMMING IS FUN
print(text.title())                                     # Output: Python Programming Is Fun

# Question 10
text = "DATA SCIENCE"
print(text.lower())                                     # Output: data science

# Question 11
text = "  cypher, adjei  "
cleaned_text = text.strip().title()
print(cleaned_text)                                     # Output: Cypher, Adjei
names = cleaned_text.split(", ")
print("First Name: ", names[0])                         # Output: Cypher
print("Last Name: ", names[1])                          # Output: Adjei

# Question 12
text = "Hello, Hello World!"
text = text.replace("Hello", "Mello", 2)
print(text)                                             # Output: Mello, Mello World!
text = text.replace("Mello", "Hello", 1)
print(text)                                             # Output: Hello, Mello World!


