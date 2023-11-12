import csv

# sorted with movie year in ascending order
with open('./file_operations/kino.file_operations', newline='\r\n') as f:
    movies = f.read().split('\r\n')
    movie = csv.reader(movies)
    movie = sorted(movie, key=lambda info: int(info[2]))
    print(list(movie))

# all movies that production year is above 2000
with open('./file_operations/kino.file_operations', newline='\r\n') as f:
    movies = f.read().split('\r\n')
    movie = csv.reader(movies)
    movie = sorted(movie, key=lambda info: int(info[2]))
    result = [i for i in movie if int(i[2]) >= 2000]
    print(list(result))
