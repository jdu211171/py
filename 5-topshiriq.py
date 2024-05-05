# K va N soni berilgan (N > 0). K sonini N marta print qiling.
# N = int(input('takrorlanish sonini kiriting:\n'))
# K = int(input('sonni kiriting:\n'))
# for i in range(0, N):
#     print(K)
# ----------------------------------------------------------------------------------------------------------------------
# 1 dan n gacha bo`lgan toq sonlar yig`indisini toping.
# n = int(input('oxirgi sonni kiriting:\n'))
# natija = 0
# for i in range(1, n+1, 2):
#     natija += i
# print(natija)
# ----------------------------------------------------------------------------------------------------------------------
# 1 dan n gacha bo`lgan 3 ga bo`linadigan lekin 9 ga bo`linmidigan sonlar yig`indisini toping.
# n = int(input('oxirgi sonni kiriting:\n'))
# sum = 0
# for i in range(1, n):
#     if i % 3 == 0 and not i % 9 == 0:
#         sum += i
# print(sum)
# ----------------------------------------------------------------------------------------------------------------------
# 1 dan n gacha bo`lgan sonlarni kvadratlari yig`indisini toping.
# n = int(input('oxirgi sonni kiriting:\n'))
# sum = 0
# for i in range(1, n):
#     sum += i ** 2
# print(sum)
# ----------------------------------------------------------------------------------------------------------------------
# Soz kiritaman. Undan keyin 1 dan – sozni uzunligigacha bolgan son kiritishimni sorasin. Kiritilgan sonni tartibidagi
# harifni soz da olib tashlasin.
# text = input("so'zni kiriting ustoz:\n")
# char_index = int(input(f"1 dan {len(text)} gacha bo'lgan musbat butun son kiriting:\n"))
# while 1 > char_index or char_index > len(text):
#     char_index = int(input(f"Iltimos! 1 dan {len(text)} gacha bo'lgan musbat butun son kiriting:\n"))
# print(text[:char_index-1] + text[char_index:])
# ----------------------------------------------------------------------------------------------------------------------
# agar online magazindan kiyim olsangiz va butun narx 100000 dan ko`p bo`lsa sizga 10% skidka qilib bersin . agar 50000
# dan ko`p bo`lsa sizga 5% skidka qilib bersin. agar undan kam bo`lsa o`zini narxida bersin.
# import os
#
#
# def clear_console():
#     os.system('cls' if os.name == 'nt' else 'clear')
#
#
# class ShoppingCart:
#     def __init__(self):
#         self.items = {}
#         self.total = 0
#
#     def add_item(self, item, price):
#         if item in self.items:
#             self.items[item]['qty'] += 1
#         else:
#             self.items[item] = {'price': price, 'qty': 1}
#         self.total += price
#         self.display_cart()
#
#     def display_cart(self):
#         print("Sizning hisobingizda:")
#         for item, details in self.items.items():
#             print(f"{item} - ${details['price']} x {details['qty']}")
#         print(f"Umumiy: ${self.total:.2f}\n")
#
#     def checkout(self):
#         if self.total >= 100000 and self.total > 50000:
#             sale_percentage = 0.1
#         elif self.total >= 50000:
#             sale_percentage = 0.05
#         else:
#             sale_percentage = 0
#         final_price = self.total * (1 - sale_percentage)
#         print(f"Umumiy summa: ${final_price:.2f}")
#         if sale_percentage != 0:
#             print(f"Siz uchun {int(sale_percentage * 100)}% skidka amal qiladi")
#         print("Bizdan xarid qilganingiz uchun raxmat!")
#
#
# def main():
#     cart = ShoppingCart()
#     products = {'Kostyum': 50000, 'Shim': 40000, 'Palto': 70000}
#
#     while True:
#         print("Mavjud mahsulotlar:")
#         for i, (product, price) in enumerate(products.items(), 1):
#             print(f"{i}. {product} - ${price}")
#
#         choice = input("Menudagi buyumlarning sonini tanlang va harid yakunlangach 'ok' deb yozing: ")
#         if choice.lower() == 'ok':
#             clear_console()
#             cart.checkout()
#             break
#         elif choice.isdigit() and int(choice) in range(1, len(products) + 1):
#             item = list(products.keys())[int(choice) - 1]
#             clear_console()
#             cart.add_item(item, products[item])
#         else:
#             print("Iltimos menudagi buyumlardan tanlang")
#
#
# if __name__ == "__main__":
#     main()
# ----------------------------------------------------------------------------------------------------------------------
# 7. Sonlar berilgan A va B (A < B). A va B oraligida joylashgan
# sonlarni kamayish tartibida print qilin (A va B) shu oraliqqa
# kirmasin. Shu sonlarni sonini (uzunligini) print qiling
# son1 = int(input('1-sonni kiriting:\n'))
# son2 = int(input('2-sonni kiriting:\n'))
# son_uzunligi = 0
# for i in range(son2, son1-1, -1):
#     print(i)
#     son_uzunligi += 1
# print(son_uzunligi)
# ----------------------------------------------------------------------------------------------------------------------
# 8. Son berilgan – u 1 kg konfetni narxi. 1, 2, ….. , 10 kg uchun narxni print qiling.
# narx = int(input('1 kg konfet narxini kiriting:\n'))
# for i in range(1, 11):
#     print(f"{i} kg = {narx * i}")
# ----------------------------------------------------------------------------------------------------------------------
# 9. Son berilgan – u 1 kg konfet narxi . 0.1, 0.2, …. , 1 kg uchun narxni print qiling.
# narx = int(input('1 kg konfet narxini kiriting:\n'))
# for i in range(1, 11):
#     print(f"{i / 10} kg = {narx * i / 10}")
# ----------------------------------------------------------------------------------------------------------------------
# 10. Butun sonlar berilgan A va B (A < B). A va B oralig’idagi butun sonlar kvadratini va ularning yig’indisini print
# qiling. A va B ham bu oraliqga kirsin. Masalan: 1, 2, 3 -> 1, 4, 9 -> 14
# A = int(input('1-sonni kiriting:\n'))
# B = int(input('2-sonni kiriting:\n'))
# sum = 0
# for i in range(A, B+1):
#     print(i ** 2)
#     sum += i ** 2
# print(sum)
# ----------------------------------------------------------------------------------------------------------------------
# 11. Butun son berilgan A va N (N > 0). Sikldan foydalangan holda A ni 1 – N bolgan darajasini print qililar
# A = int(input('1-sonni kiriting:\n'))
# N = int(input('2-sonni kiriting:\n'))
# for i in range(1, N+1):
#     print(A ** i)
# ----------------------------------------------------------------------------------------------------------------------
# 12. Butun son berilgan N (N > 0). 1 – N gacha bolgan sonlar kopaytmasini toping.
# N = int(input('sonni kiriting:\n'))
# sum = 1
# for i in range(1, N+1):
#     sum *= i
# print(sum)
# ----------------------------------------------------------------------------------------------------------------------
# 1. -Uzunligi teng bo'lgan ikkita so'z kiritilgan. Misol uchun A = "olma" B = "anor".
# Sikl oraqlik yangi so'z tuzing. Natija: C = "oalnmoar", yani A 1-si
# va B 1-si C boshiga qoshildi C = "oa. yani A 2-si va B 2-si C
# boshiga qoshildi C = "oaln. ....
# A = input('1-so\'zni kiriting:\n')
# B = input('2-so\'zni kiriting:\n')
# C = ''
# for i in range(len(A)):
#     C += A[i] + B[i]
# print(C)
# ----------------------------------------------------------------------------------------------------------------------
# 2. So'z berilgan "d!v!l@p!r" -> "developer" korinishiga o'tkazing.
# word = "d!v!l@p!r"
# clean_word = ""
#
# for char in word:
#     if char.isalpha():
#         clean_word += char
#     elif char == '!':
#         clean_word += 'e'
#     elif char == '@':
#         clean_word += 'o'
#
# print(clean_word)
# ----------------------------------------------------------------------------------------------------------------------
# 3. So'z kiritilgan, keyin esa harif kiritilgan, so'zda shu harifdan netcha borligni aniqlang.
# word = input('so\'zni kiriting:\n')
# letter = input('harfni kiriting:\n')
# count = 0
# for i in word:
#     if i == letter:
#         count += 1
# print(count)
# ----------------------------------------------------------------------------------------------------------------------
# 4. Katta va kichik hariflar bilan so'z kiritilgan. Katta hariflarni aloxida so'z qilib print qiling. Misol uchun:
# "TeLefOn". Natija: "TLO"
# word = input('so\'zni kiriting:\n')
# upper_case = ''
# for i in word:
#     if i.isupper():
#         upper_case += i
# print(upper_case)
# ----------------------------------------------------------------------------------------------------------------------
# 5. Katta va kichik hariflar bilan so'z kiritilgan. Kichik hariflarni aloxida so'z qilib print qiling. Misol uchun:
# "TeLefOn". Natija: "eefn"
# word = input('so\'zni kiriting:\n')
# lower_case = ''
# for i in word:
#     if i.islower():
#         lower_case += i
# print(lower_case)
# ----------------------------------------------------------------------------------------------------------------------
# 6. Katta va kichik hariflar bilan so'z kiritilgan. 4 va 5 vazifani birlashtirgan holda. Katta harifli so'zlarni
# boshiga kichik harifli so'zlarni oxiriga qoyib print qiling. Misol uchun: "TeLefOn".
# Natija: "TLOeefn".
# word = input('so\'zni kiriting:\n')
# upper_case = ''
# lower_case = ''
# for i in word:
#     if i.isupper():
#         upper_case += i
#     else:
#         lower_case += i
# print(upper_case + lower_case)
# ----------------------------------------------------------------------------------------------------------------------