# 1. შექმენი ფუნქცია, რომელიც მომხმარებლისგან მიღებულ ინფორმაციას გაასამმაგებს და
# დაბეჭდავს შემდეგნაირად:     input: “word” Output: „Tripled: wordwordword“

# def Triple():
#     rep = input("შემოიყვანეთ სიტყვა: ")
#     print(f"Tripled: {rep * 3}")
#
# Triple()


# 2. შექმენი ფუნქცია, რომელიც მიიღებს მომხმარებლის წონას და დააბრუნებს მის წონას
# მთვარეზე. (მთვარის გრავიტაცია 6_ჯერ ნაკლებია დედამიწისაზე)

# def w():
#     weight = float(input("შემოიყვანეთ თქვენი წონა: "))
#     return weight / 6
#
# print(w())

# 3. შექმენი კალკულატორის ფუნქცია, რომელიც მიიღებს გამოსახულებას მომხმარებლისგან input()
# ფუნქციის დახმარებით (სამ მონაცემს: პირველ რიცხვს, მოქმედებას (+ - * / ^), მეორე რიცხვს)
# მაგ „2 * 6“, დათვლის და დააბრუნებს შედეგს. გაითვალისწინე, რომ რიცხვის შეყვანის მაგიერ
# სიმბოლოების შეყვანის შემთხვევაში უნდა დააბრუნოს ფუნქციამ შესაბამისი მესიჯი. ასევე ნულზე გაყოფა
# არ შეიძლება, ამ შემთხვევაშიც უნდა დააბრუნოს შესაბამისი მესიჯი

# def calculator():
#     operators = ['+', '-', '*', '**', '/']
#
#     while True:
#         try:
#             num1 = float(input("შემოიყვანეთ პირველი რიცხვი: "))
#             num2 = float(input("შემოიყვანეთ მეორე რიცხვი: "))
#             break
#         except ValueError:
#             print("გთხოვთ, შემოიყვანოთ რიცხვი!")
#
#     while True:
#         op = input("შემოიყვანეთ ოპერატორი (+, -, /, *, **): ")
#         if op in operators:
#             break
#         else:
#             print("თქვენს მიერ არჩეულ ოპერატორზე კალკულატორი არ მუშაობს!")
#
#     if op == "+":
#         result = num1 + num2
#     elif op == "-":
#         result = num1 - num2
#     elif op == "*":
#         result = num1 * num2
#     elif op == "**":
#         result = num1 ** num2
#     else:
#         if num2 == 0:
#             print("ნულზე გაყოფა არ შეიძლება!")
#         else:
#             result = num1 / num2
#
#     return f"{num1} {op} {num2} = {result}"
#
# print(calculator())