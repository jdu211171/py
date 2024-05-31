# soat,minut,soniya
# 1:1:1
# 2:2:2
# print(abs((1 * 60 * 60 + 1 * 60 + 1) - (2 * 60 * 60 + 2 * 60 + 2)))
# vaqt1 = [int(x) for x in input('birinchi soatni kiriting:\n').split(':')]
# vaqt2 = [int(y) for y in input('ikkinchi soatni kiriting:\n').split(':')]
# farq = abs((vaqt1[0] * 60 * 60 + vaqt1[1] * 60 + vaqt1[2]) - (vaqt2[0] * 60 * 60 + vaqt2[1] * 60 + vaqt2[2]))
# print(farq)
# --------------------------------------------
# K = tovaga qo'yish mumkin bo'lgan kotlet soni, M = daqiqa, N = istalgancha kotletlar soni
# quyidagi formula yordamida ishlaymiz:
# bitta kotlet 1 * M * 2 vaqtda pishadi
# K ta kotlet K * M * 2 vaqtda pishadi
# N ta kotlet (M * 2) * (N // K) + (M * 2 * N % K)
# malumot = [x for x in input().split(' ')]
# malumot[0] K
# malumot[1] M
# malumot[2] N
# for i in range(len(malumot)):
#     malumot[i] = malumot[i].split('=')[-1]
#     malumot[i] = int(malumot[i])
#
# qoldiq_son = malumot[2] % malumot[0]
# natija = (malumot[1] * 2) * (malumot[2] // malumot[0]) + (malumot[1] * 2 * qoldiq_son)
# print(natija)
# --------------------------------------------
# sentence = input('gapni kiriting:\n')
# gap = sentence[:]
#
# birinchi_h_indeksi = gap.lower().find('h')
# oxirgi_h_indeksi = gap.lower().rfind('h')
# gap_boshi = gap[0:birinchi_h_indeksi]
# gap_oxiri = gap[oxirgi_h_indeksi:]
# gap_ortasi = gap[birinchi_h_indeksi:oxirgi_h_indeksi]
# takrorlanadigan_gap = gap_ortasi[1:]
# natija = gap_boshi + gap_ortasi + takrorlanadigan_gap + gap_oxiri
# print(natija)
# --------------------------------------------
# class Product:
#     def __init__(self, name, price, year):
#         self.name = name
#         self.price = price
#         self.year = year
#
#
# class Farm(Product):
#     def __init__(self, name, price, year, date):
#         super().__init__(name, price, year)
#         self.date = date
#
#     def passed_time(self):
#         date = self.year
#         date2 = self.date
#         time = [int(x) for x in date.split('/')]
#         time2 = [int(x) for x in date2.split('/')]
#         time[1] = time[1]
#         time2[1] = time2[1]
#         vaqt = [abs(time[0] - time2[0]), abs(time[1] - time2[1]), abs((time[2] - time2[2]) // 12)]
#         kun_to_vaqt = vaqt[0] // 30
#         natija = sum([kun_to_vaqt, vaqt[1], vaqt[2]])
#         return natija
#
#
# my_obj1 = Farm('Kolbasa', '12000', '01/01/2024', '04/02/2024')
# my_obj2 = Farm('Sosiska', '14000', '01/01/2024', '31/03/2024')
# my_obj3 = Farm('Uzum', '15000', '01/01/2024', '01/02/2024')
# my_obj4 = Farm('Banan', '16000', '01/01/2024', '03/02/2024')
# my_obj5 = Farm('Kiwi', '17000', '01/01/2024', '31/03/2024')
# print(my_obj2.passed_time())
# --------------------------------------------
# import sqlite3
#
# conn = sqlite3.connect('university.db')
#
# cursor = conn.cursor()
#
# cursor.execute('''CREATE TABLE student (
#                     id INTEGER PRIMARY KEY AUTOINCREMENT,
#                     name TEXT,
#                     department TEXT,
#                     date_beg TEXT,
#                     date_end TEXT,
#                     GPA INTEGER,
#                     count INTEGER,
#                     scholarship REAL
#                 )''')
#
# cursor.execute("INSERT INTO student (name, department, date_beg, date_end, GPA, count, scholarship) VALUES ('Anvar', 'Foundation', '10.10.2020', '04.05.2021', 250, 5, 50000)")
# cursor.execute("INSERT INTO student (name, department, date_beg, date_end, GPA, count, scholarship) VALUES ('Sardor', 'SMM', '11.11.2022', '20.02.2023', 350, 15, 150000)")
# cursor.execute("INSERT INTO student (name, department, date_beg, date_end, GPA, count, scholarship) VALUES ('Davron', 'ReactJS', '01.12.2023', '04.05.2024', 300, 3, 100000)")
# cursor.execute("INSERT INTO student (name, department, date_beg, date_end, GPA, count, scholarship) VALUES ('Kamola', '.NET', '05.01.2021', '25.10.2021', 200, 2, 200000)")
# cursor.execute("INSERT INTO student (name, department, date_beg, date_end, GPA, count, scholarship) VALUES ('Lola', 'AI', '09.05.2022', '20.05.2023', 240, 8, 250000)")
# cursor.execute("INSERT INTO student (name, department, date_beg, date_end, GPA, count, scholarship) VALUES ('Farangiz', 'Golang', '10.02.2023', '10.10.2023', 400, 12, 400000)")
# cursor.execute("INSERT INTO student (name, department, date_beg, date_end, GPA, count, scholarship) VALUES ('Baxtiyor', 'Java', '15.07.2020', '01.08.2021', 370, 10, 180000)")
# cursor.execute("INSERT INTO student (name, department, date_beg, date_end, GPA, count, scholarship) VALUES ('Komil', 'FullStack', '18.08.2022', '20.09.2023', 320, 6, 240000)")
# cursor.execute("INSERT INTO student (name, department, date_beg, date_end, GPA, count, scholarship) VALUES ('Malika', 'Python', '01.09.2021', '10.01.2022', 280, 3, 350000)")
# cursor.execute("INSERT INTO student (name, department, date_beg, date_end, GPA, count, scholarship) VALUES ('Sharof', 'Design', '18.03.2023', '20.12.2023', 290, 1, 320000)")
#
# cursor.execute("""
#     SELECT name
#     FROM student
#     WHERE LENGTH(name) = (SELECT LENGTH(name) FROM student WHERE name = 'Anvar');
# """)
#
# # ism_uzunligi = int(input('ism uzunligini kiriting:\n'))
# # cursor.execute("""
# #     SELECT name
# #     FROM student
# #     WHERE LENGTH(name) = ?;
# # """, (ism_uzunligi,))
#
# cursor.execute("""
#     SELECT name, date_beg, date_end
#     FROM student
#     ORDER BY GPA DESC
#     LIMIT 3
# """)
#
# natijalar = cursor.fetchall()
#
# for natija in natijalar:
#     print(natija)
#
# conn.commit()
#
# conn.close()
# print('success!')

# --------------------------------------------
# def can_place_knight(board, row, col):
#     # Check for knights in the 'L' shape positions
#     moves = [(2, 1), (1, 2), (-1, 2), (-2, 1), (-2, -1), (-1, -2), (1, -2), (2, -1)]
#     for move in moves:
#         r, c = row + move[0], col + move[1]
#         if 0 <= r < 8 and 0 <= c < 8 and (board[r][c] == 'knight' or board[r][c] == 'rook'):
#             return False
#
#     # Check for rook in the same row or column
#     for i in range(8):
#         if board[i][col] == 'rook' or board[row][i] == 'rook':
#             return False
#
#     return True
#
#
# def place_knights(board):
#     count = 0
#     for i in range(8):
#         for j in range(8):
#             if board[i][j] != 'knight' and board[i][j] != 'rook' and can_place_knight(board, i, j):
#                 board[i][j] = 'knight'
#                 count += 1
#     return count, board
#
#
# chessboard = [['a8', 'b8', 'c8', 'd8', 'e8', 'f8', 'g8', 'h8'],
#               ['a7', 'b7', 'c7', 'd7', 'e7', 'f7', 'g7', 'h7'],
#               ['a6', 'b6', 'c6', 'd6', 'e6', 'f6', 'g6', 'h6'],
#               ['a5', 'b5', 'c5', 'rook', 'e5', 'f5', 'g5', 'h5'],
#               ['a4', 'b4', 'c4', 'd4', 'e4', 'f4', 'g4', 'h4'],
#               ['a3', 'b3', 'c3', 'd3', 'e3', 'f3', 'g3', 'h3'],
#               ['a2', 'knight', 'c2', 'd2', 'e2', 'f2', 'g2', 'h2'],
#               ['a1', 'b1', 'c1', 'd1', 'e1', 'f1', 'g1', 'h1']]
#
# knight_count, updated_chessboard = place_knights(chessboard)
#
# print(f"Knight Count: {knight_count}")
# for row in updated_chessboard:
#     print(row)

# --------------------------------------------
# N = int(input("Enter the number of stations: "))
# M = int(input("Enter the number of passengers: "))
#
# routes = [0] * (N + 1)
# print(routes)
# for _ in range(M):
#     name = input("Enter the passenger's name: ")
#     entry = int(input("Enter the entry station number: "))
#     exit = int(input("Enter the exit station number: "))
#
#     for i in range(entry, exit):
#         routes[i] += 1
#     print(routes)
#
# max_passengers = max(routes)
# print("Routes with the most passengers:")
# for i in range(1, N + 1):
#     if routes[i] == max_passengers:
#         print(f"{i}-{i + 1}")

# --------------------------------------------
# floors = [[] for _ in range(11)]
# print(floors)
# for i in range(10):
#     line = input("Enter the floors where the users go to: ")
#     if line != "-":
#         for floor in line.split(","):
#             floors[int(floor)].append(floor)
#     print(floors)
#
# print(floors)
# for i in range(10, -1, -1):
#     if floors[i]:
#         print(",".join(floors[i]))
#     else:
#         print("-")
#     print(floors)
# --------------------------------------------
import sqlite3

conn = sqlite3.connect('airplanes.db')

cursor = conn.cursor()

cursor.execute('''
    CREATE TABLE airplane (
        id INTEGER PRIMARY KEY AUTO_INCREMENT,
        type VARCHAR(17),
        trip INTEGER,
        town_from VARCHAR(30),
        town_to VARCHAR(30),
        time TIME
    )
''')

airplanes = [
    ('Boeing 747', 101, 'New York', 'London', '07:30:00'),
    ('Airbus A380', 102, 'Paris', 'Tokyo', '11:15:00'),
    ('Boeing 777', 103, 'Sydney', 'Los Angeles', '13:45:00'),
    ('Airbus A350', 104, 'Beijing', 'New York', '14:20:00'),
    ('Boeing 737', 105, 'London', 'Berlin', '01:30:00'),
    ('Airbus A320', 106, 'Madrid', 'Rome', '02:15:00'),
    ('Boeing 787', 107, 'Dubai', 'Paris', '06:45:00'),
    ('Airbus A330', 108, 'Tokyo', 'Sydney', '09:20:00'),
    ('Boeing 767', 109, 'Los Angeles', 'New York', '05:30:00'),
    ('Airbus A340', 110, 'Berlin', 'Madrid', '02:45:00')
]

cursor.executemany('''
    INSERT INTO airplane (type, trip, town_from, town_to, time)
    VALUES (?, ?, ?, ?, ?)
''', airplanes)

cursor.execute('''
    SELECT * FROM airplane
    WHERE time = (SELECT MIN(time) FROM airplane)
''')
print(cursor.fetchall())

cursor.execute('''
    SELECT town_to, COUNT(*) as flight_count
    FROM airplane
    GROUP BY town_to
    ORDER BY flight_count DESC
    LIMIT 3
''')

conn.commit()

conn.close()
