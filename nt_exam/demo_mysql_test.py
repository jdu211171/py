import mysql.connector

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="root",
    database="py"
)

mycursor = mydb.cursor()

mycursor.execute("CREATE TABLE IF NOT EXISTS airplane ("
                 "id INT AUTO_INCREMENT,"
                 "type VARCHAR(17),"
                 "trip INT,"
                 "town_from VARCHAR(30),"
                 "town_to VARCHAR(30),"
                 "time VARCHAR(8),"
                 "PRIMARY KEY (id)"
                 ")"
                 )

mycursor.execute("INSERT INTO airplane (type, trip, town_from, town_to, time)"
                 "VALUES"
                 "('Boeing 737', 101, 'New York', 'London', '07:30:00'),"
                 "('Airbus A320', 102, 'Paris', 'Berlin', '01:15:00'),"
                 "('Boeing 747', 103, 'Tokyo', 'Sydney', '09:45:00'),"
                 "('Airbus A380', 104, 'Dubai', 'Toronto', '13:20:00'),"
                 "('Boeing 777', 105, 'Singapore', 'San Francisco', '14:55:00'),"
                 "('Airbus A330', 106, 'Amsterdam', 'Shanghai', '11:40:00'),"
                 "('Boeing 787', 107, 'Los Angeles', 'Rome', '12:35:00'),"
                 "('Airbus A350', 108, 'Madrid', 'Mumbai', '09:50:00'),"
                 "('Boeing 767', 109, 'Beijing', 'Buenos Aires', '20:00:00'),"
                 "('Airbus A340', 110, 'Cairo', 'Chicago', '12:25:00');")

mycursor.execute("SELECT * FROM airplane ORDER BY time ASC LIMIT 1;")
result = mycursor.fetchall()
mydb.commit()
print(result)

mycursor.execute("SELECT town_to, COUNT(*) as flight_count FROM airplane GROUP BY town_to ORDER BY flight_count DESC "
                 "LIMIT 1;")
result = mycursor.fetchall()
mydb.commit()
print(result)

mydb.close()
