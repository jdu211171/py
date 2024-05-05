import sqlite3

# Create a connection to the database
conn = sqlite3.connect('sportswear.db')

# Create a cursor object
cursor = conn.cursor()

# Create the color table
# cursor.execute('''CREATE TABLE color (
#                     id INTEGER PRIMARY KEY AUTOINCREMENT,
#                     name TEXT NOT NULL UNIQUE,
#                     extra_fee REAL
#                 )''')
#
# Create the customer table
# cursor.execute('''CREATE TABLE customer (
#                     id INTEGER PRIMARY KEY AUTOINCREMENT,
#                     first_name TEXT NOT NULL,
#                     last_name TEXT NOT NULL,
#                     favorite_color_id INTEGER REFERENCES color(id)
#                 )''')
#
# Create the category table
# cursor.execute('''CREATE TABLE category (
#                     id INTEGER PRIMARY KEY AUTOINCREMENT,
#                     name TEXT NOT NULL UNIQUE,
#                     parent_id INTEGER REFERENCES category(id)
#                 )''')
#
# Create the clothing table
# cursor.execute('''CREATE TABLE clothing (
#                     id INTEGER PRIMARY KEY AUTOINCREMENT,
#                     name TEXT NOT NULL UNIQUE,
#                     size TEXT NOT NULL CHECK(size IN ('S', 'M', 'L', 'XL', '2XL', '3XL')),
#                     price REAL NOT NULL,
#                     color_id INTEGER REFERENCES color(id),
#                     category_id INTEGER REFERENCES category(id)
#                 )''')
#
# Create the clothing_order table
# cursor.execute('''CREATE TABLE clothing_order (
#                     id INTEGER PRIMARY KEY AUTOINCREMENT,
#                     customer_id INTEGER REFERENCES customer(id),
#                     clothing_id INTEGER REFERENCES clothing(id),
#                     items INTEGER NOT NULL,
#                     order_date DATE NOT NULL
#                 )''')

# Insert data into the color table
# cursor.execute("INSERT INTO color (name, extra_fee) VALUES (?, ?)", ('Red', 10.0))
# cursor.execute("INSERT INTO color (name, extra_fee) VALUES (?, ?)", ('Blue', 15.0))

# Insert data into the customer table
# cursor.execute("INSERT INTO customer (first_name, last_name, favorite_color_id) VALUES (?, ?, ?)", ('John', 'Doe', 1))
# cursor.execute("INSERT INTO customer (first_name, last_name, favorite_color_id) VALUES (?, ?, ?)", ('Jane', 'Doe', 2))

# Insert data into the category table
# cursor.execute("INSERT INTO category (name, parent_id) VALUES (?, ?)", ('Shirts', None))
# cursor.execute("INSERT INTO category (name, parent_id) VALUES (?, ?)", ('T-Shirts', 1))

# Insert data into the clothing table
# cursor.execute("INSERT INTO clothing (name, size, price, color_id, category_id) VALUES (?, ?, ?, ?, ?)", ('T-Shirt', 'M', 20.0, 1, 2))
# cursor.execute("INSERT INTO clothing (name, size, price, color_id, category_id) VALUES (?, ?, ?, ?, ?)", ('Shirt', 'L', 30.0, 2, 1))

# Insert data into the clothing_order table
# cursor.execute("INSERT INTO clothing_order (customer_id, clothing_id, items, order_date) VALUES (?, ?, ?, ?)", (1, 1, 2, '2022-01-01'))
# cursor.execute("INSERT INTO clothing_order (customer_id, clothing_id, items, order_date) VALUES (?, ?, ?, ?)", (2, 2, 1, '2022-01-02'))

# ----------------- SELECT -----------------
"""Display the name of clothing items (name the column clothes), their color (name the column color), and the last 
name and first name of the customer(s) who bought this apparel in their favorite color. Sort rows according to color, 
in ascending order."""
# cursor.execute("""
#     SELECT clothing.name AS clothes, color.name AS color, customer.last_name, customer.first_name
#     FROM clothing_order
#     JOIN customer ON clothing_order.customer_id = customer.id
#     JOIN clothing ON clothing_order.clothing_id = clothing.id
#     JOIN color ON clothing.color_id = color.id
#     WHERE color.id = customer.favorite_color_id
#     ORDER BY color.name ASC
# """)
#
# # Fetch all the rows
# rows = cursor.fetchall()
#
# # Print the rows
# for row in rows:
#     print(row)
"""Select the last name and first name of customers and the name of their favorite color for customers with no 
purchases."""
# cursor.execute("""
#     SELECT customer.last_name, customer.first_name, color.name AS favorite_color
#     FROM customer
#     LEFT JOIN color ON customer.favorite_color_id = color.id
#     LEFT JOIN clothing_order ON customer.id = clothing_order.customer_id
#     WHERE clothing_order.customer_id IS NULL
# """)
#
# # Fetch all the rows
# rows = cursor.fetchall()
#
# # Print the rows
# for row in rows:
#     print(row)

"""Select the name of the main categories (which have a NULL in the parent_id column) and the name of their direct 
subcategory (if one exists). Name the first column category and the second column subcategory."""
# cursor.execute("""
#     SELECT main_category.name AS category, sub_category.name AS subcategory
#     FROM category AS main_category
#     LEFT JOIN category AS sub_category ON main_category.id = sub_category.parent_id
#     WHERE main_category.parent_id IS NULL
# """)
#
# # Fetch all the rows
# rows = cursor.fetchall()
#
# # Print the rows
# for row in rows:
#     print(row)



# Save the changes
conn.commit()

# Close the connection
conn.close()

# print("Database and tables created successfully!")
# print("Data inserted successfully!")