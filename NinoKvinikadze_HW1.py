
# 1

name = input("write your name: ")
surname = input("write your surname: ")
print(name, surname)

# 2
a = float(input("write first number: "))
b = float(input("write second number: "))
print(a ** b)

# 3
# დაწერე პროგრამა რომელიც გეკითხება სახელს, გვარს, ასაკს და ქალაქს და ბეჭდავს ინფორმაციას
name = input("write your name: ")
surname = input("write your surname: ")
age = input("write your age: ")
city = input("write the city where you live: ")
text = f""" Name: {name}
Surname: {surname}
Age: {age}
City: {city}"""
print(text)

# 4
# დაწერე პროგრამა, რომელიც გთხოვს შეიყვანო ნებისმიერი სამი სხვადასხვა ხილის
# დასახელება ცალცალკე. რეზულტატი კი იბეჭდება შემდეგი სახით: Apple//Peach%%Orange

a = input("Name the fruit: ")
b = input("Another fruit: ")
c = input("One more please: ")
text = f"""{a}//{b}%%{c}"""
print(text)

# 5
# დაწერე პროგრამა,რომელიც გთხოვს, შეიყვანო ტექსტი, დათვლის მასში არსებული
# სიმბოლოების რაოდენობას და გამოიტანს შედეგს შემდეგნაირად: Number of symbols: 50

a = input("Write the text, please: ")
length = len(a)
text = f"""Number of symbols: {length}"""
print(text)
