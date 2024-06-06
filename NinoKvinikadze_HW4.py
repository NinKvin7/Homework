# 1. ციკლის მეშვეობით 3 მომხმარებელს შეაყვანინე ინფორმაცია საკუთარი სახელის, გვარის და ასაკის
# შესახებ. თითოეული მომხმარებლის ინფორმაცია შეინახე ინდივიდუალურ სიაში. შემდეგ კი სამივე სია
# დაამატე საერთო ცალრიელ სიას სახელად consumer_info. Input_ის მეშვეობით მომხმარებლის ინდექსის შეყვანის
# შემთხვევაში პროგრამამ უნდა დაბრუნოს არჩეულ მომხმარებელზე ინფორმაცია შემდეგნაირად:
# Name: Elene
# Lastname: Khardava
# Age: 21

# consumer_info = []
#
# while len(consumer_info) < 3:
#     n = input("შემოიყვანეთ თქვენი სახელი: ")
#     ln = input("შემოიყვანეთ თქვენი გვარი: ")
#     while True:
#         try:
#             Age = int(input("შემოიყვანეთ თქვენი ასაკი: "))
#             break
#         except ValueError:
#             print("შემოიყვანეთ ასაკი!")
#     l = ["Name: " + n, "LastName: " + ln, "Age: " + str(Age)]
#     consumer_info.append(l)
#
#
# while True:
#     try:
#         m = int(input("რომელი ინდექსის მქონე მონაცემი დავბეჭდო? (0-2): "))
#         if 0 <= m < 3:
#             break
#         else:
#             print("ასეთი ინდექსი სიაში არაა, სხვა სცადე")
#     except ValueError:
#         print("შემოიყვანეთ რიცხვი!")
#
#
# for item in consumer_info[m]:
#     print(item)


# 2. შექმენი ჩაშენებული სია, რომელშიც იქნება შენახული ცნობილი მსახიობების შესახებ ინფორმაცია.
# მომხმარებელს შემოჰყავს მსახიობის სახელი ან გვარი. თუ სიაში მოიძებნა მსახიობი, დაბეჭდe მის შესახებ
# არსებული ინფორმაცია რეზუმის სახით.

# Actors = [['Tom', 'Hanks', 67, 1.83],
#           ['Leonardo', 'Dicaprio', 49, 1.83],
#           ['Al', 'Pacino', 84, 1.68],
#           ['Tom', 'Hardy', 46, 1.75],
#           ['Tom', 'Cruise', 61, 1.70]]

# n = (input("შემოიყანეთ მსახიობის სახელი ან გვარი: ").lower()).capitalize()
#
# suffixes = ["name", "surname", "age", "height"]
#
# found = False
# for i, actor in enumerate(Actors):
#     if n in actor:
#         found = True
#         print(f"Actor {n} found at index {i}")
#         for suffix, item in zip(suffixes, actor):
#             print(f"{suffix}: {item}")
#         print()
# if not found:
#     print(f"Actor {n} not found")


# 3. შექმენი ფუნქცია რომელიც მიიღებს სიას და დააბრუნებს ასევე სიას, თუმცა უნიკალური
# ელემენტებით (გამოიყენე set მონაცემთა ტიპი).

# def unique_list():
#     sia = []
#     n = ""
#
#     while n.lower() != "stop":
#         n = input("Enter item (type 'stop' to end): ")
#         if n.lower() != "stop":
#             sia.append(n)
#
#     sia = list(set(sia))
#     sia.sort()
#
#     return sia
#
#
# print(unique_list())




# l = [1,4,4,4,6,5]
#
# def unique_list(x):
#     x = list(set(x))
#     return x
#
# print(unique_list(l))


# 4. შექმენი ფუნქცია რომელიც მიიღებს ორ set ტიპის მონაცემს, გააერთიანებს მათ, შემდეგ კი გადააქცევს
# tuple ტიპის მონაცემად და დააბრუნებს შედეგს.

# def set_to_Tuple():
#     set1 = set()
#     set2 = set()
#     n = ""
#     m = ""
#
#     while n.lower() != "stop":
#         n = input("Enter item for the first set (type 'stop' to end): ")
#         if n.lower() != "stop":
#             set1.add(n)
#
#     while m.lower() != "stop":
#         m = input("Enter item for the second set (type 'stop' to end): ")
#         if m.lower() != "stop":
#             set2.add(m)
#
#     Final = set1.union(set2)
#
#     return f"""{set1},
# {set2},
# {tuple(Final)}"""
#
# print(set_to_Tuple())





# set3 = {1, 3, 4, 4}
# set4 = {4, 3, 5, 8}
#
# def set_to_tuple(x, y):
#     u = x.union(y)
#     return tuple(u)
#
# print(set_to_tuple(set3, set4))


# 5. დაწერე პროგრამა, რომელიც შეამოწმებს გადაცემული ლექსიკონი არის თუ არა ცარიელი.

# d1 = {'ვაშლი': 2.89, 'მარწყვი': 5.84}
# d2 = {}
#
# def empty_or_not(d):
#     if len(d) > 0:
#         return f"{d} არ არის ცარიელი"
#     else:
#         return f"{d} ცარიელია"
#
# print(empty_or_not(d1))
# print(empty_or_not(d2))


# 6: დაწერე პროგრამა, რომელიც სტრიქონისგან ქმნის ლექსიკონს. დათვალე სტრიქონში კონკრეტული სიმბოლოს
# ოდენობა. მაგალითად პროგრამას გადავეცით სტრიქონი: "w3schools"
# უნდა დააბრუნოს ლექსიკონი: {'w':1, '3':1, 's':2, 'c':1, 'h':1,'o':2,'l':1}

# a = "w3schools"
# def symbol_quantity(str):
#     k = list(str)
#     v = [k.count(item) for item in k]
#
#     combined_dict = {i: j for i, j in zip(k, v)}
#
#     return combined_dict
#
# print(symbol_quantity(a))


# 7. შექმენი while ციკლი, რომელიც მომხმარებელს ხუთჯერ შემოატანინებს ინფორმაციას და
# ჩაამატებს ცარიელ სიაში. შედეგი დაბეჭდე. (append მეთოდი)

# l = list()
#
# i = 0
# while i < 5:
#     n = input("შემოიყვანეთ სიის წევრი: ")
#     l.append(n)
#     i += 1
#
# print(l)

# 8. მიღებული სიის პირველ და ბოლო ელემენტებს ადგილი შეუცვალე და დაბეჭდე შედეგი.
# წაშალე სიაში მომხმარებლის მიერ მოთხოვნილი ელემენტი. (remove მეთოდი)

# a = ['d',2,4,5,3]
# a.append(a[0])
# a[0] = a[-2]
# a.pop(-2)
# print(a)
#
# try:
#     k = int(input(f"რა ელემენტი წავშალო აქედან? {a} "))
# except ValueError:
#     k = input(f"რა ელემენტი წავშალო აქედან? {a} ")
#
# a.remove(k)
# print(a)

#ეს არ მომწონს მარა უკეთესი ვერ მოვიფიქრე


# 9. იპოვე სიის სიგრძე მინიმუმ ორი მეთოდით.
# l = [1,8,3,5,6,7]
# print(len(l))



# 10. ამობეჭდე სიის ყოველი ელემენტი მის ინდექსთან ერთად მინიმუმ ორი მეთოდით.

# u = [3,4,5,5,5]
# i = 0
# while i < len(u):
#     for item in u:
#         print(f"სიის წევრი {item}, მისი ინდექსია:{i}")
#         i += 1


# u = [3, 4, 5, 5, 5]
#
# for index, item in enumerate(u):
#     print(f"სიის წევრი {item}, მისი ინდექსია: {index}")

# 11. შეკრიბე ორი სია და დაბეჭდე შედეგი.

# a = [2, 1, 5]
# b = [0, 10, -8]
#
# sum = [i+j for i,j in zip(a,b)]
#
# print(sum)


# 12. შეასრულე იგივე ოპერაცია extend მეთოდის დახმარებით.
# a = [2, 1, 5]
# b = [0, 10, -8]
#
# result = []
# for i, j in zip(a, b):
#     result.extend([i + j])
#
# print(result)


# 13. გაამრავლე სია რიცხვზე და დაბეჭდე შედეგი.
# a = [1, 7, 4.5, 5.3]
# k = []
# for item in a:
#     i = 3 * item
#     k.append(i)
# print(a, k)


# # მეორე გზა
# a = [1, 7, 4.5, 5.3]
# k = [3 * item for item in a]
#
# print(a, k)


# 14. Slicing _ ის გამოყენებით შეაბრუნე სია და დაბეჭდე შედეგი.

# l = [1, 3, 7, 10, 11]
# reversed_list = l[::-1]
# print(reversed_list)


# 15. გააკეთე იგივე reverse მეთოდის გამოყენებით.

# l = [1,3,7,10,11]
# l.reverse()
# print(l)


# 16. მომხმარებელს შემოაყვანინე წინადადება და გადააქციე სიტყვების სიად.

# sentence = input("Enter a sentence: ")
# word_list = sentence.split()
#
# print(word_list)


# 18. მოცემულია სია: [“apple”, “orange”, “banana”, “strawberry”] მომხმარებელს შეაყვანინე
# სიტყვა, და თუ ეს სიტყვა მოიძებნა მოცემულ სიაში, ამობეჭდე მისი ინდექსი.

# r = ['apple', 'orange', 'banana', 'strawberry']
# w = input("შემოიყვანეთ ხილი: ")
# if w in r:
#     print(r.index(w))
# else:
#     print("ასეთი ხილი სიაში არ არის!")


# 19. შემთხვევითი რიცხვებით შექმენი სია, იპოვე მინიმალური და მაქსიმალური ელემენტი და დაბეჭდე (min max ფუნქციები)

# t = [9,2,3,5,7,8]
# print(min(t))
# print(max(t))

# 20. წაშალე სიის ბოლო ელემენტი, ამავე დროს ამოპრინტე წაშლილი ელემენტი და მიღებული სია.

# a = [2,3,4,4,5]
# print(a.pop())
# print(a)

# 21.დაითვალე სიაში არსებული კონკრეტული ერთნაირი
# ელემენტების რაოდენობა. (count მეთოდი)

# a = [3,2,3,2,2]
# print(a.count(2))

# 22. მომხმარებლის მიერ შემოყვანილი წინადადება გადააქციე სიად. შემდეგ ეს სია ელემენტებისგან
# გაასუფთავე და დაბეჭდე შედეგი. (clear მეთოდი)

# sentence = input("Enter a sentence: ")
# word_list = sentence.split()
# print(word_list)
# word_list.clear()
# print(word_list)

# 23. არსებულ სიაში ჩაამატე „third indexed“ ელემენტი მესამე
# ინდექსის ადგილას. (insert მეთოდი)

# a = [1,2,44,53,6,7]
# a.insert(3, "third indexed")
# print(a)